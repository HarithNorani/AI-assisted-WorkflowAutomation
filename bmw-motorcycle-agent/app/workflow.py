from __future__ import annotations

from typing import Any, Dict, List

from app.ai_agent import IntakeAgent
from app.database import insert_case, list_cases
from app.llm_agent import LLMRouteAgent
from app.storage import StorageAdapter


class WorkflowOrchestrator:
    def __init__(self, db_path: str | None = None):
        self.db_path = db_path
        self.agent = IntakeAgent()
        self.llm_agent = LLMRouteAgent()
        self.storage = StorageAdapter()

    def process_request(self, request: Dict[str, Any]) -> Dict[str, Any]:
        normalized_request = {
            "dealer_name": str(request.get("dealer_name", "")).strip(),
            "customer_name": str(request.get("customer_name", "")).strip(),
            "vehicle_model": str(request.get("vehicle_model", "")).strip(),
            "vin": str(request.get("vin", "")).strip(),
            "issue_summary": str(request.get("issue_summary", "")).strip(),
            "request_type": str(request.get("request_type", "service_request")).strip() or "service_request",
        }

        analysis = self.agent.analyze(normalized_request)
        llm_result = self.llm_agent.classify(normalized_request)
        case_payload = {
            **normalized_request,
            "issue_category": analysis["issue_category"],
            "priority": analysis["priority"],
            "route_to": analysis["route_to"],
            "summary": analysis["summary"],
            "confidence": analysis["confidence"],
            "missing_fields": analysis["missing_fields"],
            "llm_provider": llm_result["provider"],
        }

        case_id = self.storage.save_case(case_payload) if self.db_path is None else insert_case(case_payload, self.db_path)
        result = {
            "case_id": case_id,
            **analysis,
            "llm_provider": llm_result["provider"],
            "dealer_name": normalized_request["dealer_name"],
            "customer_name": normalized_request["customer_name"],
            "vehicle_model": normalized_request["vehicle_model"],
            "vin": normalized_request["vin"],
            "issue_summary": normalized_request["issue_summary"],
            "request_type": normalized_request["request_type"],
        }
        return result

    def get_cases(self) -> List[Dict[str, Any]]:
        if self.db_path is not None:
            return list_cases(self.db_path)
        return self.storage.fetch_cases()
