from __future__ import annotations

import re
from typing import Any, Dict, List


class IntakeAgent:
    """Lightweight heuristic triage layer for workflow automation demos."""

    def analyze(self, request: Dict[str, Any]) -> Dict[str, Any]:
        issue_text = (request.get("issue_summary") or "").lower()
        dealer_name = request.get("dealer_name", "Unknown dealer")
        customer_name = request.get("customer_name", "Unknown customer")
        vehicle_model = request.get("vehicle_model", "Unknown model")
        vin = request.get("vin", "")

        missing_fields: List[str] = []
        for field_name, value in {
            "dealer_name": dealer_name,
            "customer_name": customer_name,
            "vehicle_model": vehicle_model,
            "vin": vin,
            "issue_summary": request.get("issue_summary", ""),
        }.items():
            if not value or not str(value).strip():
                missing_fields.append(field_name)

        if "warranty" in issue_text or "guarantee" in issue_text:
            issue_category = "warranty_case"
            route_to = "warranty_team"
            priority = "high" if any(token in issue_text for token in ["fails", "critical", "not start", "unsafe"]) else "medium"
        elif any(token in issue_text for token in ["battery", "engine", "electrical", "start", "power", "fault", "fails", "error"]):
            issue_category = "technical_fault"
            route_to = "technical_support"
            priority = "high" if any(token in issue_text for token in ["fails", "critical", "safety", "not start"]) else "medium"
        elif any(token in issue_text for token in ["part", "spare", "brake", "rotor", "pad", "component", "replace"]):
            issue_category = "parts_request"
            route_to = "parts_desk"
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
        vehicle_model = request.get("vehicle_model", "unknown model")
        customer_name = request.get("customer_name", "customer")
        summary = (
            f"{customer_name}'s {vehicle_model} request was classified as '{issue_category}' with "
            f"priority '{priority}'. Recommended assignment: {route_to}."
        )
        return summary

    def _score_confidence(self, issue_text: str, category: str) -> float:
        keywords = {
            "technical_fault": ["battery", "engine", "electrical", "fails", "start", "fault"],
            "warranty_case": ["warranty", "guarantee", "replacement"],
            "parts_request": ["part", "spare", "rotor", "pad", "brake"],
            "service_request": ["service", "inspection", "check", "maintenance"],
        }
        matches = sum(1 for token in keywords.get(category, []) if token in issue_text)
        confidence = 0.55 + min(matches * 0.1, 0.35)
        return max(0.55, min(confidence, 0.97))
