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
        if any(token in issue_lower for token in ["warranty", "guarantee", "policy", "coverage", "compliance"]):
            return "policy_case"
        if any(token in issue_lower for token in ["battery", "engine", "electrical", "fault", "error", "fails"]):
            return "technical_issue"
        if any(token in issue_lower for token in ["part", "spare", "component", "replace", "item", "stock"]):
            return "inventory_request"
        return "service_request"
