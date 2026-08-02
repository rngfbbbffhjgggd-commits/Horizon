"""Shared AI utility functions."""

import json
import re
from typing import Optional


def parse_json_response(response: str) -> Optional[dict]:
    """Try multiple strategies to extract a JSON object from an AI response.

    Returns the parsed dict, or None if all strategies fail.
    """
    text = response.strip()

    # Strategy 1: direct parse
    try:
        return json.loads(text)
    except (json.JSONDecodeError, ValueError):
        pass

    # Strategy 2: extract from ```json ... ``` code block
    if "```json" in text:
        try:
            json_str = text.split("```json")[1].split("```")[0].strip()
            return json.loads(json_str)
        except (json.JSONDecodeError, ValueError, IndexError):
            pass

    # Strategy 3: extract from ``` ... ``` code block
    if "```" in text:
        try:
            json_str = text.split("```")[1].split("```")[0].strip()
            return json.loads(json_str)
        except (json.JSONDecodeError, ValueError, IndexError):
            pass

    # Strategy 4: find the first { ... } block using brace matching
    start = text.find("{")
    if start != -1:
        depth = 0
        for i in range(start, len(text)):
            if text[i] == "{":
                depth += 1
            elif text[i] == "}":
                depth -= 1
                if depth == 0:
                    try:
                        return json.loads(text[start : i + 1])
                    except (json.JSONDecodeError, ValueError):
                        break

    # Strategy 5: regex extraction as last resort
    match = re.search(r"\{[\s\S]*\}", text)
    if match:
        try:
            return json.loads(match.group())
        except (json.JSONDecodeError, ValueError):
            pass

    # Strategy 6: attempt to repair a truncated JSON object (e.g. output hit
    # the token limit). Drop the trailing incomplete fragment and re-balance
    # brackets so the largest leading prefix that is valid JSON can parse.
    repaired = _repair_truncated_json(text)
    if repaired is not None:
        try:
            return json.loads(repaired)
        except (json.JSONDecodeError, ValueError):
            pass

    return None


def _repair_truncated_json(text: str):
    """Best-effort repair of a truncated JSON document.

    When the model's response is cut off (e.g. output hit the token limit),
    drop the trailing incomplete fragment and re-balance brackets so the
    largest leading prefix that is valid JSON can parse.
    """
    start = text.find("{")
    if start == -1:
        return None

    # Walk the JSON tracking bracket depth, skipping string literals.
    stack = []  # char at each open bracket
    i = start
    in_string = False
    escape = False
    last_complete = None  # last index+1 where brackets were balanced
    while i < len(text):
        ch = text[i]
        if in_string:
            if escape:
                escape = False
            elif ch == "\\":
                escape = True
            elif ch == '"':
                in_string = False
        else:
            if ch == '"':
                in_string = True
            elif ch in "{[":
                stack.append(ch)
            elif ch in "}]":
                if stack and ((ch == "}" and stack[-1] == "{") or (ch == "]" and stack[-1] == "[")):
                    stack.pop()
                    if not stack:
                        last_complete = i + 1
        i += 1

    if not stack and last_complete is not None:
        # Brackets balanced but JSON parse failed elsewhere: try the complete region.
        candidate = text[start:last_complete]
        try:
            obj = json.loads(candidate)
            if isinstance(obj, dict):
                return candidate
        except (json.JSONDecodeError, ValueError):
            pass

    if not stack:
        return None

    # There is an unclosed bracket at the end. Truncate at the last complete
    # closing of the outermost structure and re-close the open brackets.
    truncate_at = last_complete if last_complete is not None else len(text)
    prefix = text[start:truncate_at]
    if not prefix:
        return None

    # Re-open brackets still on the stack (only those opened within the prefix)
    closers = {"{": "}", "[": "]"}
    # Determine which openers from the stack fall within the kept prefix.
    stack2 = []
    j = start
    in_string = False
    escape = False
    while j < truncate_at:
        ch = text[j]
        if in_string:
            if escape:
                escape = False
            elif ch == "\\":
                escape = True
            elif ch == '"':
                in_string = False
        else:
            if ch == '"':
                in_string = True
            elif ch in "{[":
                stack2.append(ch)
            elif ch in "}]" and stack2:
                stack2.pop()
        j += 1

    tail = "".join(closers[ch] for ch in reversed(stack2))
    repaired = prefix + tail
    try:
        obj = json.loads(repaired)
        if isinstance(obj, dict):
            return repaired
    except (json.JSONDecodeError, ValueError):
        pass
    return None
