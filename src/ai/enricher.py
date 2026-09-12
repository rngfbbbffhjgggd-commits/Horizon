"""Content enrichment using AI (second-pass analysis).

For items that pass the score threshold, this module:
1. Searches the web for relevant context (via DuckDuckGo)
2. Feeds search results + item content to AI to generate grounded background knowledge
"""

import asyncio
import json
import re
import sys
import os
from typing import List, Optional
from rich.progress import Progress, SpinnerColumn, BarColumn, TextColumn, MofNCompleteColumn
from ddgs import DDGS
from openai import BadRequestError

from .client import AIClient
from .prompts import (
    CONCEPT_EXTRACTION_SYSTEM, CONCEPT_EXTRACTION_USER,
    CONTENT_ENRICHMENT_SYSTEM, CONTENT_ENRICHMENT_USER,
)
from .utils import parse_json_response
from ..models import ContentItem


class ContentEnricher:
    """Enriches high-scoring content items with background knowledge."""

    def __init__(self, ai_client: AIClient):
        self.client = ai_client

    def _get_concurrency(self) -> int:
        """Return the configured enrichment concurrency, clamped to 1 or above."""
        config = getattr(self.client, "config", None)
        concurrency = getattr(config, "enrichment_concurrency", 1)
        return max(concurrency, 1)

    async def enrich_batch(self, items: List[ContentItem]) -> None:
        """Enrich items in-place with background knowledge.

        Args:
            items: Content items to enrich (modified in-place)
        """
        concurrency = self._get_concurrency()
        semaphore = asyncio.Semaphore(concurrency)

        async def _process(item: ContentItem, progress_task) -> None:
            async with semaphore:
                try:
                    await self._enrich_item(item)
                except Exception as e:
                    print(f"Error enriching item {item.id}: {e}, falling back to translation")
                    await self._translate_item(item)
            progress.advance(progress_task)

        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            BarColumn(),
            MofNCompleteColumn(),
            transient=True,
        ) as progress:
            task = progress.add_task("Enriching", total=len(items))
            coros = [
                _process(item, task) for item in items
            ]
            await asyncio.gather(*coros)

    async def _web_search(self, query: str, max_results: int = 5) -> list:
        """Search the web for context via DuckDuckGo.

        Raised 3 -> 5 results per concept on 2026-09-12: more grounding
        material gives the (small, free) writer model more concrete facts to
        draw on, which is the supply-side fix for thin one-paragraph items.

        Returns:
            List of dicts with keys: title, url, body
        """
        try:
            # Suppress primp "Impersonate ... does not exist" stderr warning
            stderr = sys.stderr
            sys.stderr = open(os.devnull, "w")
            try:
                ddgs = DDGS()
                results = await asyncio.to_thread(ddgs.text, query, max_results=max_results)
            finally:
                sys.stderr.close()
                sys.stderr = stderr
        except Exception:
            return []

        return [
            {"title": r.get("title", ""), "url": r.get("href", ""), "body": r.get("body", "")}
            for r in (results or [])
        ]

    @staticmethod
    def _parse_json_response(response: str) -> Optional[dict]:
        """Try multiple strategies to extract a JSON object from an AI response.

        Returns the parsed dict, or None if all strategies fail.
        """
        return parse_json_response(response)

    async def _extract_concepts(self, item: ContentItem, content_text: str) -> List[str]:
        """Ask AI to identify concepts that need explanation.

        Args:
            item: Content item
            content_text: Extracted content text

        Returns:
            List of search queries for concepts that need explanation
        """
        user_prompt = CONCEPT_EXTRACTION_USER.format(
            title=item.title,
            summary=item.ai_summary or item.title,
            tags=", ".join(item.ai_tags) if item.ai_tags else "",
            content=content_text[:1000],
        )

        try:
            response = await self.client.complete(
                system=CONCEPT_EXTRACTION_SYSTEM,
                user=user_prompt,
            )
            result = self._parse_json_response(response)
            if result is None:
                return []
            queries = result.get("queries", [])
            # 3 -> 4 concepts (2026-09-12): wider grounding coverage per item.
            return queries[:4]
        except Exception:
            return []

    async def _enrich_item(self, item: ContentItem) -> None:
        """Enrich a single item with background knowledge.

        Steps:
        1. Ask AI which concepts in the news need explanation
        2. Search the web for those concepts
        3. Ask AI to generate background based on search results

        Args:
            item: Content item to enrich (modified in-place via metadata)
        """
        # Extract content text and comments separately
        content_text = ""
        comments_text = ""
        if item.content:
            if "--- Top Comments ---" in item.content:
                main, comments_part = item.content.split("--- Top Comments ---", 1)
                content_text = main.strip()[:4000]
                comments_text = comments_part.strip()[:2000]
            else:
                content_text = item.content[:4000]

        # Step 1: AI identifies concepts to explain
        queries = await self._extract_concepts(item, content_text)

        # Step 2: Search web for each concept
        # Body snippets are capped so that the larger result count (5 per
        # concept x up to 4 concepts) does not bloat the prompt.
        all_results = []
        web_sections = []
        for query in queries:
            results = await self._web_search(query)
            all_results.extend(results)
            if results:
                lines = [
                    f"- [{r['title']}]({r['url']}): {str(r['body'])[:400]}"
                    for r in results
                ]
                web_sections.append(f"**{query}:**\n" + "\n".join(lines))
        web_context = "\n\n".join(web_sections) if web_sections else ""

        # Index of available URLs for citation validation
        available_urls = {r["url"]: r["title"] for r in all_results if r.get("url")}

        # Step 3: AI generates background grounded in search results
        user_prompt = CONTENT_ENRICHMENT_USER.format(
            title=item.title,
            url=str(item.url),
            summary=item.ai_summary or item.title,
            score=item.ai_score or 0,
            reason=item.ai_reason or "",
            tags=", ".join(item.ai_tags) if item.ai_tags else "",
            content=content_text,
            comments_section=f"\n**Community Comments:**\n{comments_text}" if comments_text else "",
            web_context=web_context or "No web search results available.",
        )

        # Request the AI to produce the enrichment, retrying once on transient
        # failures (e.g. truncated output) but NOT on BadRequestError, which is
        # a permanent problem with the request itself and would fail every retry.
        result = None
        for attempt in range(2):
            try:
                response = await self.client.complete(
                    system=CONTENT_ENRICHMENT_SYSTEM,
                    user=user_prompt,
                )
                result = self._parse_json_response(response)
                if result is not None:
                    break
                if attempt == 0:
                    print(
                        f"Warning: could not parse enrichment response for {item.id} "
                        f"(attempt 1/2), retrying"
                    )
            except BadRequestError:
                # Request is invalid; retrying is pointless. Fall back immediately.
                print(
                    f"Warning: enrichment request rejected for {item.id} "
                    f"(BadRequestError), falling back to translation"
                )
                await self._translate_item(item)
                return
            except Exception as e:
                if attempt == 0:
                    print(
                        f"Warning: enrichment call failed for {item.id} ({e}), retrying"
                    )
        if result is None:
            # Gracefully degrade: fall back to a lightweight translation
            # instead of dropping the item untranslated.
            print(f"Warning: could not parse enrichment response for {item.id}, falling back to translation")
            await self._translate_item(item)
            return

        # Combine structured sub-fields into per-language detailed_summary
        for lang in ("en", "zh"):
            if result.get(f"title_{lang}"):
                val = result[f"title_{lang}"]
                item.metadata[f"title_{lang}"] = val.get("text") or str(val) if isinstance(val, dict) else str(val)

            parts = []
            for field in ("whats_new", "why_it_matters", "key_details"):
                text = result.get(f"{field}_{lang}", "").strip()
                if text:
                    parts.append(text)
            if parts:
                item.metadata[f"detailed_summary_{lang}"] = " ".join(parts)

            if result.get(f"background_{lang}"):
                val = result[f"background_{lang}"]
                item.metadata[f"background_{lang}"] = val.get("text") or str(val) if isinstance(val, dict) else str(val)

            if result.get(f"community_discussion_{lang}"):
                val = result[f"community_discussion_{lang}"]
                item.metadata[f"community_discussion_{lang}"] = val.get("text") or str(val) if isinstance(val, dict) else str(val)

        # Store citation sources — only URLs that actually came from our search results
        if result.get("sources") and available_urls:
            valid = [
                {"url": u, "title": available_urls[u]}
                for u in result["sources"]
                if u in available_urls
            ]
            if valid:
                item.metadata["sources"] = valid

        # Backward-compatible fallback fields (English as default)
        item.metadata["detailed_summary"] = item.metadata.get("detailed_summary_en", "")
        item.metadata["background"] = item.metadata.get("background_en", "")
        item.metadata["community_discussion"] = item.metadata.get("community_discussion_en", "")

    async def _translate_item(self, item: ContentItem) -> None:
        """Lightweight translation fallback: when full enrichment fails, at least
        translate the title and summary to Chinese so the item is not dropped.

        Retries once on transient failures and — unlike the caller — keeps the
        translated Chinese even if the model restates the English source, so the
        summary survives for the ZH digest. Also logs instead of swallowing
        silently, so a provider content-filter rejection is visible.
        """
        last_error = None
        for attempt in range(2):
            try:
                response = await self.client.complete(
                    system="You are a translator. Translate only to Simplified Chinese. Do not reproduce English. Return only valid JSON, no other text.",
                    user=(
                        f'Title: {item.title}\n'
                        f'Summary: {item.ai_summary or item.title}\n\n'
                        'Return JSON:\n'
                        '{"title_zh": "<中文标题>", "summary_zh": "<用中文写1-2句摘要>"}'
                    ),
                )
                result = self._parse_json_response(response)
                if result:
                    saved = False
                    if result.get("title_zh"):
                        item.metadata["title_zh"] = result["title_zh"]
                        saved = True
                    if result.get("summary_zh"):
                        item.metadata["detailed_summary_zh"] = result["summary_zh"]
                        saved = True
                    if saved:
                        return
                    if attempt == 0:
                        print(
                            f"Warning: could not parse translation fallback for {item.id} "
                            f"(attempt 1/2), retrying"
                        )
                elif attempt == 0:
                    print(
                        f"Warning: could not parse translation fallback for {item.id} "
                        f"(attempt 1/2), retrying"
                    )
            except Exception as e:
                last_error = e
                if attempt == 0:
                    print(
                        f"Warning: translation fallback failed for {item.id} ({e}), retrying"
                    )
        if last_error is not None:
            print(
                f"Warning: translation fallback failed for {item.id} after retries "
                f"(provider rejection: {last_error}). Item left with original title."
            )


def _is_mostly_latin(text: str) -> bool:
    """Return True when a string has meaningful Latin/CJK mix that is mostly
    untranslated. Used to detect an item whose title/summary was left in
    English by the primary model (e.g. a content-filter rejection)."""
    if not text:
        return False
    letters = [c for c in text if c.isalpha()]
    if not letters:
        return False
    cjk = sum(1 for c in letters if "\u4e00" <= c <= "\u9fff")
    return cjk / len(letters) < 0.4


class TranslationFixer:
    """Thin post-enrichment pass that re-translates any item the primary model
    left in English.

    The primary model (e.g. Zhipu GLM) may occasionally reject a politically
    sensitive item via its content filter, leaving the title/summary in English.
    This pass uses a separate, content-filter-lenient model (e.g. DeepSeek) to
    review every item and fill in the Chinese title and summary when they are
    missing or still mostly Latin-script.
    """

    def __init__(self, ai_client: AIClient):
        self.client = ai_client

    def _get_concurrency(self) -> int:
        config = getattr(self.client, "config", None)
        concurrency = getattr(config, "enrichment_concurrency", 1)
        return max(concurrency, 1)

    @staticmethod
    def _needs_fix(item: ContentItem) -> bool:
        meta = item.metadata or {}
        title_zh = str(meta.get("title_zh") or "")
        summary_zh = str(meta.get("detailed_summary_zh") or "")
        # Needs a fix when the Chinese title is missing/empty/English, or the
        # Chinese summary is missing/empty/English.
        return (
            (not title_zh or _is_mostly_latin(title_zh))
            or (not summary_zh or _is_mostly_latin(summary_zh))
        )

    async def fix_batch(self, items: List[ContentItem]) -> None:
        """Review items in-place; re-translate any not yet in Chinese."""
        if not items:
            return
        to_fix = [it for it in items if self._needs_fix(it)]
        if not to_fix:
            return

        concurrency = self._get_concurrency()
        semaphore = asyncio.Semaphore(concurrency)

        async def _process(item: ContentItem) -> None:
            async with semaphore:
                try:
                    await self._fix_item(item)
                except Exception as e:
                    # Never let a correction failure break the digest.
                    print(f"TranslationFixer: item {item.id} fix failed ({e}), leaving as-is")

        await asyncio.gather(*(_process(it) for it in to_fix))

    async def _fix_item(self, item: ContentItem) -> None:
        """Re-translate a single item's title and summary to Simplified Chinese."""
        meta = item.metadata if item.metadata is not None else {}
        title_zh = str(meta.get("title_zh") or "")
        summary_zh = str(meta.get("detailed_summary_zh") or "")

        prompt_parts = ["Translate the following news into Simplified Chinese."]
        if title_zh and not _is_mostly_latin(title_zh):
            # Title already Chinese; only ask for a summary.
            prompt_parts.append(f"Title (keep as-is): {title_zh}")
        else:
            prompt_parts.append(f"Original title: {item.title}")
        if summary_zh and not _is_mostly_latin(summary_zh):
            prompt_parts.append(f"Summary (keep as-is): {summary_zh}")
        else:
            prompt_parts.append(
                f"Original summary: {item.ai_summary or item.title}"
            )
        prompt_parts.append(
            "Return valid JSON only:\n"
            '{"title_zh": "<中文标题>", "summary_zh": "<用中文写1-2句摘要>"}'
        )
        user = "\n".join(prompt_parts)

        response = await self.client.complete(
            system=(
                "You are a translator into Simplified Chinese. Translate only. "
                "Return only valid JSON, no other text."
            ),
            user=user,
        )
        result = parse_json_response(response)
        if not result:
            print(f"TranslationFixer: could not parse fix response for {item.id}")
            return

        new_title = result.get("title_zh") or title_zh
        new_summary = result.get("summary_zh") or summary_zh

        if new_title and not _is_mostly_latin(new_title):
            meta["title_zh"] = new_title
        if new_summary and not _is_mostly_latin(new_summary):
            meta["detailed_summary_zh"] = new_summary
        item.metadata = meta
