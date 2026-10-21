from __future__ import annotations

from typing import List

from fastapi import FastAPI
from pydantic import BaseModel, Field

from app.workflow import WorkflowOrchestrator

app = FastAPI(title="BMW Motorrad Case Workflow API")
workflow = WorkflowOrchestrator()


class ServiceRequestInput(BaseModel):
    dealer_name: str = Field(..., min_length=2)
    customer_name: str = Field(..., min_length=2)
    vehicle_model: str = Field(..., min_length=2)
    vin: str = Field(..., min_length=5)
    issue_summary: str = Field(..., min_length=10)
    request_type: str = "service_request"


@app.get("/health")
def health() -> dict:
    return {"status": "ok", "service": "bmw-motorcycle-agent"}


@app.post("/api/v1/cases/submit")
def submit_case(payload: ServiceRequestInput) -> dict:
    result = workflow.process_request(payload.model_dump())
    return result


@app.get("/api/v1/cases")
def list_cases() -> List[dict]:
    return workflow.get_cases()
