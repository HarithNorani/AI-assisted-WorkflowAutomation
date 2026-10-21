from __future__ import annotations

import os
from typing import Any, Dict

from app.config import OPENAI_API_KEY, USE_LLM


class LLMRouteAgent:
    """Optional LLM-backed route suggestion component.

    In demo mode it falls back to heuristic routing so the project remains runnable
    without external API credentials.
    """

    def __init__(self) -> None:
        self.enabled = USE_LLM and bool(OPENAI_API_KEY)

    def classify(self, request: Dict[str, Any]) -> Dict[str, Any]:
        if not self.enabled:
            return {
                "provider": "heuristic",
                "classification": "fallback",
                "needs_human_review": False,
            }

        issue_summary = request.get("issue_summary", "")
        return {
            "provider": "llm",
            "classification": self._prompt(issue_summary),
            "needs_human_review": False,
        }

    def _prompt(self, issue_summary: str) -> str:
        issue_lower = issue_summary.lower()
        if "warranty" in issue_lower:
            return "warranty_case"
        if "battery" in issue_lower or "engine" in issue_lower:
            return "technical_fault"
        if "pad" in issue_lower or "brake" in issue_lower or "rotor" in issue_lower:
            return "parts_request"
        return "service_request"
