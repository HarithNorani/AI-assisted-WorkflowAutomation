CREATE TABLE IF NOT EXISTS service_cases (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    organization_name TEXT NOT NULL,
    requester_name TEXT NOT NULL,
    asset_name TEXT NOT NULL,
    asset_id TEXT NOT NULL,
    issue_summary TEXT NOT NULL,
    request_type TEXT NOT NULL,
    issue_category TEXT NOT NULL,
    priority TEXT NOT NULL,
    route_to TEXT NOT NULL,
    summary TEXT NOT NULL,
    confidence REAL NOT NULL,
    missing_fields TEXT NOT NULL,
    created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
);
