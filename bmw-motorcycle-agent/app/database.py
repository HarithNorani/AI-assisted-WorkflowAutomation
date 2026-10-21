from __future__ import annotations

import sqlite3
from pathlib import Path
from typing import Any, Dict, List

ROOT_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT_DIR / "data"
DATABASE_PATH = DATA_DIR / "service_cases.db"


def get_connection(db_path: str | Path | None = None) -> sqlite3.Connection:
    target = Path(db_path) if db_path is not None else DATABASE_PATH
    target.parent.mkdir(parents=True, exist_ok=True)
    connection = sqlite3.connect(str(target))
    connection.row_factory = sqlite3.Row
    initialize_database(connection)
    return connection


def initialize_database(connection: sqlite3.Connection) -> None:
    connection.execute(
        """
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
        )
        """
    )
    connection.commit()


def insert_case(case_data: Dict[str, Any], db_path: str | Path | None = None) -> int:
    with get_connection(db_path) as connection:
        cursor = connection.execute(
            """
            INSERT INTO service_cases (
                dealer_name,
                customer_name,
                vehicle_model,
                vin,
                issue_summary,
                request_type,
                issue_category,
                priority,
                route_to,
                summary,
                confidence,
                missing_fields
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                case_data["dealer_name"],
                case_data["customer_name"],
                case_data["vehicle_model"],
                case_data["vin"],
                case_data["issue_summary"],
                case_data["request_type"],
                case_data["issue_category"],
                case_data["priority"],
                case_data["route_to"],
                case_data["summary"],
                float(case_data["confidence"]),
                "; ".join(case_data.get("missing_fields", [])),
            ),
        )
        connection.commit()
        return int(cursor.lastrowid)


def list_cases(db_path: str | Path | None = None) -> List[Dict[str, Any]]:
    with get_connection(db_path) as connection:
        rows = connection.execute(
            """
            SELECT *
            FROM service_cases
            ORDER BY created_at DESC
            """
        ).fetchall()
        return [dict(row) for row in rows]
