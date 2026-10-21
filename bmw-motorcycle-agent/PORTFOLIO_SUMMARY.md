# Automotive Service Workflow Automation

## Short project summary

Built an AI-assisted workflow automation platform for automotive after-sales operations. The system receives service requests, classifies issues, estimates priority, detects missing information, recommends the appropriate support team, stores case history, and presents operational metrics through a dashboard.

## CV version

**Automotive Service Workflow Automation | Python, FastAPI, Streamlit, Java, Spring Boot, SQL, n8n**

- Developed an end-to-end service-case triage workflow for technical faults, warranty cases, parts requests, and general service requests.
- Implemented rule-based AI-assisted classification, priority estimation, missing-field detection, and team-routing recommendations.
- Built a FastAPI backend with SQLite persistence, an optional PostgreSQL configuration, and a Streamlit operations dashboard.
- Added a Java Spring Boot integration layer to demonstrate enterprise-style routing and service integration.
- Created automated Python and Java tests and an n8n workflow example for event-driven orchestration.

## Five-line portfolio description

I built an automotive service workflow automation platform for after-sales operations.  
It classifies incoming requests, estimates urgency, detects missing information, and recommends the correct support team.  
The platform combines Python, FastAPI, SQL, Streamlit, Java, Spring Boot, and n8n concepts.  
It includes a REST API, persistent case history, an operational dashboard, and automated tests.  
The architecture is designed to evolve from a local proof of concept into an enterprise workflow service.

## LinkedIn / portfolio description

I developed an AI-assisted service workflow automation platform focused on automotive after-sales operations. The application automates the initial triage of service requests by identifying categories such as technical faults, warranty cases, parts requests, and general service requests. It also estimates priority, detects missing information, recommends the responsible team, stores case history, and exposes operational metrics through a Streamlit dashboard.

The project uses Python and FastAPI for the core workflow API, SQLite with an optional PostgreSQL setup for persistence, Java and Spring Boot for an enterprise-style integration layer, and an n8n workflow example for event-driven orchestration. The implementation includes automated tests and a fallback architecture that remains runnable without external AI credentials.

## What I built

- A structured service-request intake API
- A reusable workflow orchestration layer
- Classification for technical, warranty, parts, and service cases
- Priority estimation based on issue severity
- Missing-field detection for incomplete requests
- Recommended routing to specialist teams
- SQLite-backed case history
- Optional PostgreSQL deployment configuration
- Streamlit dashboard with case and routing metrics
- Java Spring Boot routing service
- n8n workflow orchestration example
- Python and Java automated tests

## What I learned

- How to translate a business process into an executable workflow
- How to separate intake, classification, business rules, storage, and presentation layers
- How to design AI-assisted automation with a reliable fallback path
- How Python services can coexist with Java enterprise integration components
- How to model operational data for reporting and auditability
- How to expose automation capabilities through REST APIs
- How to validate workflow behavior with focused automated tests
- How to design a proof of concept that can evolve toward production deployment

## Potential business impact

The platform is intended to help service organizations:

- reduce manual request triage
- improve routing consistency
- shorten response times
- identify urgent cases earlier
- reduce back-and-forth caused by missing information
- improve visibility into workload and team assignment
- create a foundation for measurable process automation

Example target metrics for a production pilot:

- 70–90% of routine requests pre-classified automatically
- triage time reduced from hours to minutes
- fewer cases routed to the wrong team
- improved visibility into high-priority backlog
- measurable reduction in manual data entry

## Suggested interview explanation

> I wanted to build more than a chatbot, so I focused on the complete business process. A request enters the system, is normalized and classified, enriched with business rules, assigned a priority, routed to a responsible team, stored for auditability, and displayed through operational reporting. I also separated the Python proof-of-concept workflow from a Java Spring Boot integration layer to reflect how such a solution could fit into an enterprise environment.

## Project links

- Main project documentation: [README.md](./README.md)
- Python application: [app/](./app/)
- Java service: [backend-java/](./backend-java/)
- Dashboard: [dashboard.py](./dashboard.py)
- n8n workflow: [sample-workflow.json](./n8n/sample-workflow.json)
