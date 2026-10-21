from __future__ import annotations

import os
from typing import Any, Dict, List

try:
    import psycopg2
except ImportError:  # pragma: no cover - optional dependency
    psycopg2 = None

from app.config import DB_BACKEND, POSTGRES_URL, SQLITE_PATH
from app.database import get_connection, list_cases


class StorageAdapter:
    """Selects the active persistence backend based on environment configuration."""

    def __init__(self) -> None:
        self.backend = DB_BACKEND.lower()
        if self.backend == "postgres" and psycopg2 is None:
            self.backend = "sqlite"

    def save_case(self, payload: Dict[str, Any]) -> int:
        if self.backend == "postgres":
            return self._save_postgres_case(payload)
        return self._save_sqlite_case(payload)

    def fetch_cases(self) -> List[Dict[str, Any]]:
        if self.backend == "postgres":
            return self._fetch_postgres_cases()
        return list_cases(SQLITE_PATH)

    def _save_sqlite_case(self, payload: Dict[str, Any]) -> int:
        from app.database import insert_case

        return insert_case(payload, SQLITE_PATH)

    def _save_postgres_case(self, payload: Dict[str, Any]) -> int:
        try:
            with psycopg2.connect(POSTGRES_URL) as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        """
                        INSERT INTO service_cases (
                            organization_name,
                            requester_name,
                            asset_name,
                            asset_id,
                            issue_summary,
                            request_type,
                            issue_category,
                            priority,
                            route_to,
                            summary,
                            confidence,
                            missing_fields
                        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                        RETURNING id
                        """,
                        (
                            payload["organization_name"],
                            payload["requester_name"],
                            payload["asset_name"],
                            payload["asset_id"],
                            payload["issue_summary"],
                            payload["request_type"],
                            payload["issue_category"],
                            payload["priority"],
                            payload["route_to"],
                            payload["summary"],
                            float(payload["confidence"]),
                            "; ".join(payload.get("missing_fields", [])),
                        ),
                    )
                    row_id = cursor.fetchone()[0]
                    connection.commit()
                    return int(row_id)
        except Exception:
            return self._save_sqlite_case(payload)

    def _fetch_postgres_cases(self) -> List[Dict[str, Any]]:
        try:
            with psycopg2.connect(POSTGRES_URL) as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "SELECT * FROM service_cases ORDER BY created_at DESC"
                    )
                    rows = cursor.fetchall()
                    columns = [
                        "id",
                        "organization_name",
                        "requester_name",
                        "asset_name",
                        "asset_id",
                        "issue_summary",
                        "request_type",
                        "issue_category",
                        "priority",
                        "route_to",
                        "summary",
                        "confidence",
                        "missing_fields",
                        "created_at",
                    ]
                    return [dict(zip(columns, row)) for row in rows]
        except Exception:
            return list_cases(SQLITE_PATH)
