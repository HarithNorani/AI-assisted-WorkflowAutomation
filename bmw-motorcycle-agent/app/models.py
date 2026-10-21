from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Dict, List


@dataclass
class ServiceRequest:
    dealer_name: str
    customer_name: str
    vehicle_model: str
    vin: str
    issue_summary: str
    request_type: str = "service_request"


@dataclass
class CaseDecision:
    case_id: int | None = None
    request_type: str = "service_request"
    issue_category: str = "service_request"
    priority: str = "medium"
    route_to: str = "service_desk"
    summary: str = ""
    confidence: float = 0.0
    missing_fields: List[str] = field(default_factory=list)
    metadata: Dict[str, Any] = field(default_factory=dict)
