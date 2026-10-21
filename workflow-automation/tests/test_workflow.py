from app.workflow import WorkflowOrchestrator


def test_processes_policy_case(tmp_path):
    db_path = tmp_path / "service_cases.db"
    orchestrator = WorkflowOrchestrator(db_path=str(db_path))

    result = orchestrator.process_request({
        "organization_name": "Example Service Center",
        "requester_name": "Anna Schneider",
        "asset_name": "Example Asset A",
        "asset_id": "ASSET-001",
        "issue_summary": "A critical integration fails after an update. Policy coverage review requested.",
        "request_type": "service_request",
    })

    assert result["issue_category"] in {"technical_issue", "policy_case"}
    assert result["route_to"] in {"technical_support", "policy_team"}
    assert result["priority"] in {"high", "medium"}
    assert result["case_id"] is not None


def test_processes_inventory_request(tmp_path):
    db_path = tmp_path / "service_cases.db"
    orchestrator = WorkflowOrchestrator(db_path=str(db_path))

    result = orchestrator.process_request({
        "organization_name": "Example Service",
        "requester_name": "Lukas Weber",
        "asset_name": "Example Asset B",
        "asset_id": "ASSET-002",
        "issue_summary": "Customer needs a replacement component from current stock.",
        "request_type": "service_request",
    })

    assert result["issue_category"] == "inventory_request"
    assert result["route_to"] == "inventory_team"
    assert result["missing_fields"] == []
