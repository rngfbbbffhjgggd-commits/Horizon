"""Content analysis using AI."""

import asyncio
import json
from typing import List, Optional
from pydantic import BaseModel, Field, ValidationError
from tenacity import retry, stop_after_attempt, wait_exponential
from rich.progress import Progress, SpinnerColumn, BarColumn, TextColumn, MofNCompleteColumn

from .client import AIClient
from .prompts import (
    BATCH_CONTENT_ANALYSIS_USER,
    CONTENT_ANALYSIS_SYSTEM,
    CONTENT_ANALYSIS_USER,
)
from .utils import parse_json_response
from ..models import ContentItem

DEFAULT_THROTTLE_SEC = 0.0

# Items analyzed in a single batched AI call. Larger batches amortize the
# (long) scoring-rules system prompt over more items but make reliable JSON
# array parsing harder.
BATCH_SIZE = 6

# Prompt payload truncation limits (characters) — keeps per-item input small.
CONTENT_LIMIT = 700
COMMENT_LIMIT = 800


class AnalysisResult(BaseModel):
    """Validated structured result returned by the analysis model."""

    score: float = Field(ge=0, le=10, allow_inf_nan=False)
    reason: str
    summary: str
    tags: list[str]


class ContentAnalyzer:
    """Analyzes content items using AI to determine importance."""

    def __init__(self, ai_client: AIClient):
        self.client = ai_client

    @staticmethod
    def _parse_json_response(response: str) -> Optional[dict]:
        """Try multiple strategies to extract a JSON object from an AI response."""
        return parse_json_response(response)

    @staticmethod
    def _parse_batch_response(response: str) -> Optional[List[dict]]:
        """Parse a JSON array of analysis results from a batched response.

        Tries direct parse, fenced code blocks, then the first balanced
        ``[...]`` region. Returns a list of dicts or None.
        """
        text = response.strip()
        try:
            data = json.loads(text)
            if isinstance(data, list):
                return data
        except (json.JSONDecodeError, ValueError):
            pass
        for marker in ("```json", "```"):
            if marker in text:
                try:
                    part = text.split(marker, 1)[1].split("```", 1)[0].strip()
                    data = json.loads(part)
                    if isinstance(data, list):
                        return data
                except (json.JSONDecodeError, ValueError, IndexError):
                    pass
        start = text.find("[")
        if start != -1:
            depth = 0
            for i in range(start, len(text)):
                if text[i] == "[":
                    depth += 1
                elif text[i] == "]":
                    depth -= 1
                    if depth == 0:
                        try:
                            data = json.loads(text[start : i + 1])
                            if isinstance(data, list):
                                return data
                        except (json.JSONDecodeError, ValueError):
                            break
        return None

    def _get_throttle_sec(self) -> float:
        """Return the configured inter-item throttle, clamped to zero or above."""
        config = getattr(self.client, "config", None)
        throttle_sec = getattr(config, "throttle_sec", DEFAULT_THROTTLE_SEC)
        return max(throttle_sec, 0.0)

    def _get_concurrency(self) -> int:
        """Return the configured analysis concurrency, clamped to 1 or above."""
        config = getattr(self.client, "config", None)
        concurrency = getattr(config, "analysis_concurrency", 1)
        return max(concurrency, 1)

    def _format_item_payload(self, index: int, item: ContentItem) -> str:
        """Format one item's (truncated) scoring input for the batch prompt."""
        content_section = ""
        if item.content:
            content_text = item.content
            if "--- Top Comments ---" in content_text:
                main, _comments = content_text.split("--- Top Comments ---", 1)
                content_section = f"Content: {main.strip()[:CONTENT_LIMIT]}"
            else:
                content_section = f"Content: {content_text[:CONTENT_LIMIT]}"

        discussion_parts = []
        if item.content and "--- Top Comments ---" in item.content:
            comments_part = item.content.split("--- Top Comments ---", 1)[1]
            discussion_parts.append(f"Community Comments:\n{comments_part[:COMMENT_LIMIT]}")

        meta = item.metadata or {}
        engagement_items = []
        if meta.get("score"):
            engagement_items.append(f"score: {meta['score']}")
        if meta.get("descendants"):
            engagement_items.append(f"{meta['descendants']} comments")
        if meta.get("favorite_count"):
            engagement_items.append(f"{meta['favorite_count']} likes")
        if meta.get("retweet_count"):
            engagement_items.append(f"{meta['retweet_count']} retweets")
        if meta.get("reply_count"):
            engagement_items.append(f"{meta['reply_count']} replies")
        if meta.get("views"):
            engagement_items.append(f"{meta['views']} views")
        if meta.get("bookmarks"):
            engagement_items.append(f"{meta['bookmarks']} bookmarks")
        if meta.get("upvote_ratio"):
            engagement_items.append(f"upvote ratio: {meta['upvote_ratio']:.0%}")
        if engagement_items:
            discussion_parts.append(f"Engagement: {', '.join(engagement_items)}")
        if meta.get("discussion_url"):
            discussion_parts.append(f"Discussion: {meta['discussion_url']}")
        if meta.get("community_note"):
            discussion_parts.append(f"Community Note: {meta['community_note']}")

        discussion_section = "\n".join(discussion_parts) if discussion_parts else ""

        return (
            f"Item {index}:\n"
            f"Title: {item.title}\n"
            f"Source: {item.source_type.value}\n"
            f"Author: {item.author or 'Unknown'}\n"
            f"URL: {item.url}\n"
            f"{content_section}\n"
            f"{discussion_section}"
        )

    @staticmethod
    def _apply_result(item: ContentItem, raw) -> None:
        """Validate one parsed dict and write it onto the item."""
        try:
            result = AnalysisResult.model_validate(raw)
        except (ValidationError, TypeError):
            item.ai_score = 0.0
            item.ai_reason = "Analysis response parse failed"
            item.ai_summary = item.title
            item.ai_tags = []
            return
        item.ai_score = result.score
        item.ai_reason = result.reason
        item.ai_summary = result.summary
        item.ai_tags = result.tags

    async def analyze_batch(self, items: List[ContentItem]) -> List[ContentItem]:
        """Analyze items with AI, batching several items per request to cut
        the repeated system-prompt overhead. Falls back to per-item calls
        when a batch cannot be parsed, so a bad response never drops items.
        """
        throttle_sec = self._get_throttle_sec()
        concurrency = self._get_concurrency()
        groups = [items[i : i + BATCH_SIZE] for i in range(0, len(items), BATCH_SIZE)]
        if not groups:
            return items
        semaphore = asyncio.Semaphore(max(1, min(concurrency, len(groups))))

        async def _process(group: List[ContentItem], index: int, progress_task):
            async with semaphore:
                await self._analyze_group(group)
                if throttle_sec > 0 and index < len(groups) - 1:
                    await asyncio.sleep(throttle_sec)
            progress.advance(progress_task, advance=len(group))
            return group

        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            BarColumn(),
            MofNCompleteColumn(),
            transient=True,
        ) as progress:
            task = progress.add_task("Analyzing", total=len(items))
            await asyncio.gather(
                *[_process(group, i, task) for i, group in enumerate(groups)]
            )
        return items

    async def _analyze_group(self, group: List[ContentItem]) -> None:
        """One batched AI call for a group; retry once, then fall back to
        per-item analysis so a bad response never drops the whole group."""
        payload = "\n\n".join(
            self._format_item_payload(i + 1, item) for i, item in enumerate(group)
        )
        user_prompt = BATCH_CONTENT_ANALYSIS_USER.format(items=payload)

        results = await self._try_batch_request(user_prompt)
        if results is not None and len(results) >= len(group):
            for i, item in enumerate(group):
                self._apply_result(item, results[i])
            return

        print(
            f"Warning: could not parse batch analysis response for {len(group)} items, "
            "falling back to per-item analysis"
        )
        for item in group:
            try:
                await self._analyze_item(item)
            except Exception as e:
                print(f"Error analyzing item {item.id}: {e}")
                item.ai_score = 0.0
                item.ai_reason = "Analysis failed"
                item.ai_summary = item.title

    async def _try_batch_request(self, user_prompt: str) -> Optional[List[dict]]:
        """Send the batched request; retry once on failure or unparsable output."""
        for _attempt in range(2):
            try:
                response = await self.client.complete(
                    system=CONTENT_ANALYSIS_SYSTEM,
                    user=user_prompt,
                    max_tokens=BATCH_SIZE * 350,
                )
            except Exception as e:
                print(f"Batch analysis call failed ({e}); retrying")
                continue
            results = self._parse_batch_response(response)
            if results is not None:
                return results
        return None

    @retry(
        stop=stop_after_attempt(3),
        wait=wait_exponential(min=2, max=10)
    )
    async def _analyze_item(self, item: ContentItem) -> None:
        """Analyze a single content item (per-item fallback path).

        Args:
            item: Content item to analyze (modified in-place)
        """
        # Prepare content section
        content_section = ""
        if item.content:
            # Split off comments if present
            content_text = item.content
            if "--- Top Comments ---" in content_text:
                main, comments_part = content_text.split("--- Top Comments ---", 1)
                content_section = f"Content: {main.strip()[:800]}"
            else:
                content_section = f"Content: {content_text[:1000]}"

        # Prepare discussion section (comments, engagement)
        discussion_parts = []
        if item.content and "--- Top Comments ---" in item.content:
            comments_part = item.content.split("--- Top Comments ---", 1)[1]
            discussion_parts.append(f"Community Comments:\n{comments_part[:1500]}")

        meta = item.metadata
        engagement_items = []
        if meta.get("score"):
            engagement_items.append(f"score: {meta['score']}")
        if meta.get("descendants"):
            engagement_items.append(f"{meta['descendants']} comments")
        if meta.get("favorite_count"):
            engagement_items.append(f"{meta['favorite_count']} likes")
        if meta.get("retweet_count"):
            engagement_items.append(f"{meta['retweet_count']} retweets")
        if meta.get("reply_count"):
            engagement_items.append(f"{meta['reply_count']} replies")
        if meta.get("views"):
            engagement_items.append(f"{meta['views']} views")
        if meta.get("bookmarks"):
            engagement_items.append(f"{meta['bookmarks']} bookmarks")
        if meta.get("upvote_ratio"):
            engagement_items.append(f"upvote ratio: {meta['upvote_ratio']:.0%}")
        if engagement_items:
            discussion_parts.append(f"Engagement: {', '.join(engagement_items)}")
        if meta.get("discussion_url"):
            discussion_parts.append(f"Discussion: {meta['discussion_url']}")
        if meta.get("community_note"):
            discussion_parts.append(f"Community Note: {meta['community_note']}")

        discussion_section = "\n".join(discussion_parts) if discussion_parts else ""

        # Generate user prompt
        user_prompt = CONTENT_ANALYSIS_USER.format(
            title=item.title,
            source=f"{item.source_type.value}",
            author=item.author or "Unknown",
            url=str(item.url),
            content_section=content_section,
            discussion_section=discussion_section
        )

        # Get AI completion
        response = await self.client.complete(
            system=CONTENT_ANALYSIS_SYSTEM,
            user=user_prompt,
        )

        # Parse JSON response with robust fallback
        parsed = self._parse_json_response(response)
        try:
            result = AnalysisResult.model_validate(parsed) if parsed is not None else None
        except ValidationError:
            result = None
        if result is None:
            print(f"Warning: could not parse analysis response for {item.id}, using defaults")
            item.ai_score = 0.0
            item.ai_reason = "Analysis response parse failed"
            item.ai_summary = item.title
            item.ai_tags = []
            return

        # Update item with analysis results
        item.ai_score = result.score
        item.ai_reason = result.reason
        item.ai_summary = result.summary
        item.ai_tags = result.tags
