from __future__ import annotations

import re
from typing import Any, Dict, List


class IntakeAgent:
    """Lightweight heuristic triage layer for workflow automation demos."""

    def analyze(self, request: Dict[str, Any]) -> Dict[str, Any]:
        issue_text = (request.get("issue_summary") or "").lower()
        organization_name = request.get("organization_name", "Unknown organization")
        requester_name = request.get("requester_name", "Unknown requester")
        asset_name = request.get("asset_name", "Unknown asset")
        asset_id = request.get("asset_id", "")

        missing_fields: List[str] = []
        for field_name, value in {
            "organization_name": organization_name,
            "requester_name": requester_name,
            "asset_name": asset_name,
            "asset_id": asset_id,
            "issue_summary": request.get("issue_summary", ""),
        }.items():
            if not value or not str(value).strip():
                missing_fields.append(field_name)

        if any(token in issue_text for token in ["warranty", "guarantee", "policy", "coverage", "compliance"]):
            issue_category = "policy_case"
            route_to = "policy_team"
            priority = "high" if any(token in issue_text for token in ["fails", "critical", "not start", "unsafe"]) else "medium"
        elif any(token in issue_text for token in ["battery", "engine", "electrical", "start", "power", "fault", "fails", "error"]):
            issue_category = "technical_issue"
            route_to = "technical_support"
            priority = "high" if any(token in issue_text for token in ["fails", "critical", "safety", "not start"]) else "medium"
        elif any(token in issue_text for token in ["part", "spare", "component", "replace", "item", "stock"]):
            issue_category = "inventory_request"
            route_to = "inventory_team"
            priority = "medium"
        elif "service" in issue_text or "inspection" in issue_text:
            issue_category = "service_request"
            route_to = "service_desk"
            priority = "medium"
        else:
            issue_category = "service_request"
            route_to = "service_desk"
            priority = "low"

        summary = self._build_summary(request, issue_category, route_to, priority)
        confidence = self._score_confidence(issue_text, issue_category)

        return {
            "issue_category": issue_category,
            "priority": priority,
            "route_to": route_to,
            "summary": summary,
            "confidence": round(confidence, 2),
            "missing_fields": missing_fields,
        }

    def _build_summary(self, request: Dict[str, Any], issue_category: str, route_to: str, priority: str) -> str:
        asset_name = request.get("asset_name", "unknown asset")
        requester_name = request.get("requester_name", "customer")
        summary = (
            f"{requester_name}'s {asset_name} request was classified as '{issue_category}' with "
            f"priority '{priority}'. Recommended assignment: {route_to}."
        )
        return summary

    def _score_confidence(self, issue_text: str, category: str) -> float:
        keywords = {
            "technical_issue": ["battery", "engine", "electrical", "fails", "start", "fault", "error"],
            "policy_case": ["warranty", "guarantee", "policy", "coverage", "compliance"],
            "inventory_request": ["part", "spare", "component", "replace", "item", "stock"],
            "service_request": ["service", "inspection", "check", "maintenance"],
        }
        matches = sum(1 for token in keywords.get(category, []) if token in issue_text)
        confidence = 0.55 + min(matches * 0.1, 0.35)
        return max(0.55, min(confidence, 0.97))
