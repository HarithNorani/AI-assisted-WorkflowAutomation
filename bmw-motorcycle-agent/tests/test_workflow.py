from app.workflow import WorkflowOrchestrator


def test_processes_warranty_case(tmp_path):
    db_path = tmp_path / "service_cases.db"
    orchestrator = WorkflowOrchestrator(db_path=str(db_path))

    result = orchestrator.process_request({
        "dealer_name": "Munich Motorrad Center",
        "customer_name": "Anna Schneider",
        "vehicle_model": "R 1250 GS",
        "vin": "WB10XXXX123456789",
        "issue_summary": "Battery keeps dying and engine fails to start in cold weather. Warranty claim requested.",
        "request_type": "service_request",
    })

    assert result["issue_category"] in {"technical_fault", "warranty_case"}
    assert result["route_to"] in {"technical_support", "warranty_team"}
    assert result["priority"] in {"high", "medium"}
    assert result["case_id"] is not None


def test_processes_parts_request(tmp_path):
    db_path = tmp_path / "service_cases.db"
    orchestrator = WorkflowOrchestrator(db_path=str(db_path))

    result = orchestrator.process_request({
        "dealer_name": "Berlin Motorrad",
        "customer_name": "Lukas Weber",
        "vehicle_model": "K 1600 GT",
        "vin": "WB11YYYY987654321",
        "issue_summary": "Customer needs replacement brake pad and rotor for front axle.",
        "request_type": "service_request",
    })

    assert result["issue_category"] == "parts_request"
    assert result["route_to"] == "parts_desk"
    assert result["missing_fields"] == []
