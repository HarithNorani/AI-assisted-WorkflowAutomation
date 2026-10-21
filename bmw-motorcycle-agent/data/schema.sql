CREATE TABLE IF NOT EXISTS service_cases (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    dealer_name TEXT NOT NULL,
    customer_name TEXT NOT NULL,
    vehicle_model TEXT NOT NULL,
    vin TEXT NOT NULL,
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
