# AI-assisted Workflow Automation

This project demonstrates a reusable AI-assisted workflow automation platform for service operations. It handles incoming requests, classifies them, identifies missing information, routes them to the correct team, and exposes operational insights through a dashboard.

## Problem

Service organizations often receive repeated requests from multiple channels such as email, spreadsheets, forms, and internal portals. These requests are often manually triaged, which leads to:

- slow processing times
- inconsistent routing
- delayed follow-up
- limited visibility into backlog and priority

## Solution

This project automates the triage and routing process with a layered architecture:

- workflow orchestration for intake and routing
- AI-inspired classification logic for service cases
- business rules and priority scoring
- storage for case history and operational reporting
- a dashboard for monitoring workflows and team assignments

## Tech stack

- Python: workflow orchestration, rules, AI-assisted classification
- FastAPI: REST API layer
- SQLite: local persistence
- Streamlit: operational dashboard
- Java / Spring Boot: enterprise-style routing service
- Docker Compose: optional PostgreSQL environment
- n8n: sample automation workflow orchestration example

## Current features

- request intake from a structured payload
- issue classification (technical issue, policy case, inventory request, service request)
- priority estimation
- team routing recommendation
- missing-field detection
- database-backed case storage
- dashboard view of recent cases and trends
- reusable dark operations view with clear routing signals and dense case evidence
- backend service using Spring Boot
- automated tests for core workflow logic

## Project structure

- `app/`: Python workflow, database, API, and AI logic
- `backend-java/`: Spring Boot service for enterprise routing
- `dashboard.py`: Streamlit dashboard for monitoring cases
- `n8n/`: example workflow definition for automation orchestration
- `data/`: SQLite database and schema files
- `tests/`: automated validation

## Quick start

1. Create and activate a virtual environment:

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Start the API:

   ```bash
   uvicorn app.api:app --reload
   ```

4. Submit a sample request:

   ```bash
   curl -X POST http://127.0.0.1:8000/api/v1/cases/submit \
     -H "Content-Type: application/json" \
     -d '{
       "organization_name": "Example Organization",
       "requester_name": "Anna Schneider",
       "asset_name": "Example Asset A",
       "asset_id": "ASSET-001",
       "issue_summary": "A critical integration fails after an update. Policy coverage review requested.",
       "request_type": "service_request"
     }'
   ```

5. List stored cases:

   ```bash
   curl http://127.0.0.1:8000/api/v1/cases
   ```

6. Start the dashboard:

   ```bash
   streamlit run dashboard.py
   ```

7. Optional: run the Java backend:

   ```bash
   cd backend-java/workflow-automation-java
   mvn spring-boot:run
   ```

## Example use case

A service team receives a request about a critical integration failure. The system classifies it, estimates urgency, recommends the appropriate team, identifies missing information, and stores the case for human review and monitoring.

## Future improvements

- add PostgreSQL support for production-ready storage
- improve classification with an LLM-based route suggestion layer
- add support for email and ticketing integrations
- expand the dashboard with KPIs such as response time and backlog volume
- implement user authentication and approval workflows for route decisions

## Notes

This project is intentionally practical and modular. It is built to demonstrate a realistic automation use case and can be expanded into a more complete enterprise workflow system.
