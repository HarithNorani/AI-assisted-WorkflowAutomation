from __future__ import annotations

from typing import List

from fastapi import FastAPI
from pydantic import BaseModel, Field

from app.workflow import WorkflowOrchestrator

app = FastAPI(title="Workflow Automation API")
workflow = WorkflowOrchestrator()


class ServiceRequestInput(BaseModel):
    organization_name: str = Field(..., min_length=2)
    requester_name: str = Field(..., min_length=2)
    asset_name: str = Field(..., min_length=2)
    asset_id: str = Field(..., min_length=5)
    issue_summary: str = Field(..., min_length=10)
    request_type: str = "service_request"


@app.get("/health")
def health() -> dict:
    return {"status": "ok", "service": "workflow-automation-service"}


@app.post("/api/v1/cases/submit")
def submit_case(payload: ServiceRequestInput) -> dict:
    result = workflow.process_request(payload.model_dump())
    return result


@app.get("/api/v1/cases")
def list_cases() -> List[dict]:
    return workflow.get_cases()
