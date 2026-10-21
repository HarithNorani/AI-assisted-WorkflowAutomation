from __future__ import annotations

import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

DB_BACKEND = os.getenv("DB_BACKEND", "sqlite")
SQLITE_PATH = os.getenv("SQLITE_PATH", str(BASE_DIR / "data" / "service_cases.db"))
POSTGRES_URL = os.getenv(
    "POSTGRES_URL",
    "postgresql://workflow_user:workflow_password@localhost:5432/workflow_cases",
)
USE_LLM = os.getenv("USE_LLM", "false").lower() in {"1", "true", "yes", "y"}
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
LLM_MODEL = os.getenv("LLM_MODEL", "gpt-4o-mini")
