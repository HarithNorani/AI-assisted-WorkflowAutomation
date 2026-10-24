from __future__ import annotations

import sqlite3
from html import escape
from pathlib import Path

import pandas as pd
import streamlit as st

from app.workflow import WorkflowOrchestrator

ROOT = Path(__file__).resolve().parent
DB_PATH = ROOT / "data" / "service_cases.db"


def inject_brand_styles() -> None:
    st.markdown(
        """
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Barlow:wght@300;400;500;600;700&display=swap');

        :root {
            --workflow-canvas: #000000;
            --workflow-surface: #1a1a1a;
            --workflow-surface-elevated: #262626;
            --workflow-ink: #ffffff;
            --workflow-body: #c7c7c7;
            --workflow-muted: #898989;
            --workflow-line: #3c3c3c;
            --workflow-blue: #1c69d4;
            --workflow-blue-light: #0066b1;
            --workflow-red: #e22718;
        }

        html, body, [class*="css"] {
            font-family: 'Barlow', system-ui, sans-serif;
        }

        .stApp {
            background: var(--workflow-canvas);
            color: var(--workflow-ink);
        }

        [data-testid="stHeader"] {
            background: transparent;
        }

        [data-testid="stSidebar"] {
            background: var(--workflow-surface);
            border-right: 1px solid var(--workflow-line);
        }

        [data-testid="stSidebar"] > div:first-child {
            padding-top: 2rem;
        }

        .block-container {
            max-width: 1440px;
            padding: 2.4rem 3.2rem 4rem;
        }

        .brand-bar {
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 2rem;
            padding-bottom: 1.5rem;
            border-bottom: 1px solid var(--workflow-line);
        }

        .brand-lockup {
            display: flex;
            align-items: center;
            gap: 1rem;
        }

        .brand-mark {
            display: grid;
            place-items: center;
            width: 2.6rem;
            height: 2.6rem;
            border: 2px solid var(--workflow-ink);
            border-radius: 50%;
            color: var(--workflow-ink);
            font-size: 0.62rem;
            font-weight: 700;
            letter-spacing: 0.04em;
        }

        .brand-name, .eyebrow, .section-label {
            text-transform: uppercase;
            letter-spacing: 0.12em;
            font-weight: 600;
        }

        .brand-name {
            font-size: 0.82rem;
            line-height: 1.1;
        }

        .brand-subtitle {
            margin-top: 0.3rem;
            color: var(--workflow-muted);
            font-size: 0.78rem;
        }

        .context-copy {
            color: var(--workflow-muted);
            font-size: 0.82rem;
            text-align: right;
        }

        .accent-stripe {
            display: flex;
            width: 5.5rem;
            height: 4px;
            margin-top: 0.55rem;
        }

        .accent-stripe span {
            flex: 1;
        }

        .accent-stripe span:nth-child(1) {
            background: var(--workflow-blue-light);
        }

        .accent-stripe span:nth-child(2) {
            background: var(--workflow-blue);
        }

        .accent-stripe span:nth-child(3) {
            background: var(--workflow-red);
        }

        .hero {
            display: flex;
            align-items: end;
            justify-content: space-between;
            gap: 2rem;
            padding: 3.4rem 0 2.2rem;
        }

        .eyebrow, .section-label {
            color: var(--workflow-blue);
            font-size: 0.72rem;
        }

        .hero h1 {
            margin: 0.55rem 0 0;
            color: var(--workflow-ink);
            font-size: clamp(2.4rem, 5vw, 4.8rem);
            font-weight: 700;
            line-height: 0.98;
            letter-spacing: -0.03em;
        }

        .hero-copy {
            max-width: 32rem;
            margin: 1rem 0 0;
            color: var(--workflow-body);
            font-size: 1.05rem;
            line-height: 1.45;
        }

        .hero-finding {
            min-width: 16rem;
            padding: 1.1rem 1.25rem;
            background: var(--workflow-surface);
            border-left: 3px solid var(--workflow-blue);
        }

        .hero-finding strong {
            display: block;
            margin-top: 0.35rem;
            color: var(--workflow-ink);
            font-size: 1.45rem;
        }

        .hero-finding span {
            color: var(--workflow-muted);
            font-size: 0.82rem;
        }

        [data-testid="stMetric"] {
            padding: 1.1rem 0.25rem 1.25rem;
            border-top: 2px solid var(--workflow-line);
            background: transparent;
        }

        [data-testid="stMetricLabel"] {
            color: var(--workflow-muted);
            font-size: 0.78rem;
            text-transform: uppercase;
            letter-spacing: 0.08em;
        }

        [data-testid="stMetricValue"] {
            color: var(--workflow-ink);
            font-size: 2.35rem;
            font-weight: 600;
        }

        [data-testid="stMetricDelta"] {
            color: var(--workflow-blue) !important;
        }

        h2, h3 {
            color: var(--workflow-ink) !important;
            font-weight: 600 !important;
            letter-spacing: -0.02em;
        }

        h2 {
            margin-top: 2.4rem !important;
            font-size: 1.55rem !important;
        }

        h3 {
            font-size: 1.05rem !important;
        }

        .section-heading {
            display: flex;
            align-items: baseline;
            justify-content: space-between;
            gap: 1rem;
            margin: 2.6rem 0 1rem;
            padding-bottom: 0.65rem;
            border-bottom: 1px solid var(--workflow-line);
        }

        .section-heading h2 {
            margin: 0 !important;
        }

        .section-heading span {
            color: var(--workflow-muted);
            font-size: 0.85rem;
        }

        .bar-list {
            display: grid;
            gap: 0.85rem;
            padding: 0.55rem 0 0.4rem;
        }

        .bar-row {
            display: grid;
            grid-template-columns: minmax(9rem, 1fr) 2fr 3rem;
            align-items: center;
            gap: 0.8rem;
            color: var(--workflow-body);
            font-size: 0.9rem;
        }

        .bar-track {
            height: 0.45rem;
            background: var(--workflow-surface-elevated);
        }

        .bar-fill {
            height: 100%;
            background: var(--workflow-blue);
        }

        .bar-value {
            color: var(--workflow-ink);
            text-align: right;
            font-variant-numeric: tabular-nums;
        }

        .stDataFrame {
            border: 1px solid var(--workflow-line);
        }

        [data-testid="stExpander"] {
            margin-top: 1.5rem;
            border: 1px solid var(--workflow-line);
            border-radius: 0;
            background: var(--workflow-surface);
        }

        [data-testid="stExpander"] summary {
            color: var(--workflow-ink);
        }

        @media (max-width: 700px) {
            .block-container { padding: 1.25rem 1rem 2.5rem; }
            .brand-bar, .hero { align-items: flex-start; flex-direction: column; }
            .context-copy { text-align: left; }
            .hero { padding-top: 2.4rem; }
            .hero-finding { width: 100%; }
            .bar-row { grid-template-columns: 1fr 1.3fr 2rem; gap: 0.5rem; }
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


@st.cache_data
def load_cases() -> pd.DataFrame:
    if not DB_PATH.exists():
        return pd.DataFrame(
            columns=[
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
        )

    connection = sqlite3.connect(DB_PATH)
    query = "SELECT * FROM service_cases ORDER BY created_at DESC"
    df = pd.read_sql_query(query, connection)
    connection.close()
    return df


def render_request_form() -> None:
    st.markdown(
        '<div class="section-heading"><h2>Submit a service request</h2>'
        '<span>Tell us what needs attention</span></div>',
        unsafe_allow_html=True,
    )
    st.caption("Complete the form below. We will classify the request and route it to the right team.")

    with st.form("service_request_form", clear_on_submit=True):
        first_col, second_col = st.columns(2)
        with first_col:
            requester_name = st.text_input("Your name", placeholder="Anna Schneider")
            organization_name = st.text_input("Organization", placeholder="Example Organization")
            asset_name = st.text_input("Affected service or asset", placeholder="Example Asset A")
        with second_col:
            asset_id = st.text_input("Asset or reference ID", placeholder="ASSET-001")
            request_type = st.selectbox(
                "What do you need help with?",
                options=["service_request", "technical_issue", "policy_case", "inventory_request"],
                format_func=lambda value: value.replace("_", " ").title(),
            )
        issue_summary = st.text_area(
            "Describe the issue or request",
            placeholder="Tell us what happened and what help you need.",
            height=120,
        )
        submitted = st.form_submit_button("Submit request", type="primary")

    if not submitted:
        return

    fields = {
        "Your name": requester_name,
        "Organization": organization_name,
        "Affected service or asset": asset_name,
        "Asset or reference ID": asset_id,
        "Description": issue_summary,
    }
    missing_fields = [label for label, value in fields.items() if not value.strip()]
    if missing_fields:
        st.error(f"Please complete: {', '.join(missing_fields)}.")
        return

    result = WorkflowOrchestrator().process_request(
        {
            "organization_name": organization_name,
            "requester_name": requester_name,
            "asset_name": asset_name,
            "asset_id": asset_id,
            "issue_summary": issue_summary,
            "request_type": request_type,
        }
    )
    load_cases.clear()
    st.success(f"Request submitted successfully. Your reference number is {result['case_id']}.")
    st.info(f"Recommended team: {result['route_to'].replace('_', ' ').title()}.")


def render_dashboard() -> None:
    st.set_page_config(page_title="Workflow Automation Case Radar", layout="wide")
    inject_brand_styles()

    st.markdown(
        """
        <header class="brand-bar">
            <div class="brand-lockup">
                <div class="brand-mark" aria-label="Workflow Automation">W</div>
                <div>
                    <div class="brand-name">Workflow Automation</div>
                    <div class="brand-subtitle">Service operations / Case radar</div>
                    <div class="accent-stripe" aria-hidden="true"><span></span><span></span><span></span></div>
                </div>
            </div>
            <div class="context-copy">Service workflow intelligence<br>Live operational view</div>
        </header>
        <section class="hero">
            <div>
                <div class="eyebrow">Service workflow dashboard</div>
                <h1>Cases in motion.</h1>
                <p class="hero-copy">A focused view of incoming service requests, their priority, and the team best placed to resolve them.</p>
            </div>
            <div class="hero-finding">
                <span>Screen question</span>
                <strong>Where needs attention?</strong>
                <span>Prioritise the next service decision.</span>
            </div>
        </section>
        """,
        unsafe_allow_html=True,
    )

    render_request_form()
    df = load_cases()
    if df.empty:
        st.warning("No service cases yet. Submit a request above to populate the operational view.")
        return

    df["created_at"] = pd.to_datetime(df["created_at"])

    total_cases = len(df)
    high_priority = (df["priority"] == "high").sum()
    total_tech = (df["issue_category"] == "technical_issue").sum()
    total_policy = (df["issue_category"] == "policy_case").sum()

    st.markdown('<div class="section-heading"><h2>Operational pulse</h2><span>Current case volume</span></div>', unsafe_allow_html=True)
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Total cases", total_cases)
    col2.metric("High priority", high_priority)
    col3.metric("Technical issues", total_tech)
    col4.metric("Policy cases", total_policy)

    category_counts = df["issue_category"].value_counts().rename_axis("category").reset_index(name="count")
    priority_counts = df["priority"].value_counts().rename_axis("priority").reset_index(name="count")
    route_counts = df["route_to"].value_counts().rename_axis("route").reset_index(name="count")

    st.markdown('<div class="section-heading"><h2>Routing signal</h2><span>Classification and recommended ownership</span></div>', unsafe_allow_html=True)
    left, right = st.columns(2)
    with left:
        st.markdown('<div class="section-label">Case categories</div>', unsafe_allow_html=True)
        max_count = max(int(category_counts["count"].max()), 1)
        category_rows = "".join(
            f'<div class="bar-row"><span>{escape(str(row.category).replace("_", " ").title())}</span>'
            f'<div class="bar-track"><div class="bar-fill" style="width: {int(row.count) / max_count * 100:.0f}%"></div></div>'
            f'<span class="bar-value">{int(row.count)}</span></div>'
            for row in category_counts.itertuples()
        )
        st.markdown(f'<div class="bar-list">{category_rows}</div>', unsafe_allow_html=True)
    with right:
        st.markdown('<div class="section-label">Recommended routes</div>', unsafe_allow_html=True)
        max_count = max(int(route_counts["count"].max()), 1)
        route_rows = "".join(
            f'<div class="bar-row"><span>{escape(str(row.route).replace("_", " ").title())}</span>'
            f'<div class="bar-track"><div class="bar-fill" style="width: {int(row.count) / max_count * 100:.0f}%"></div></div>'
            f'<span class="bar-value">{int(row.count)}</span></div>'
            for row in route_counts.itertuples()
        )
        st.markdown(f'<div class="bar-list">{route_rows}</div>', unsafe_allow_html=True)

    st.markdown(
        f'<div class="section-heading"><h2>Recent service cases</h2><span>{len(df)} cases in view</span></div>',
        unsafe_allow_html=True,
    )
    recent_cases = df[
        ["id", "organization_name", "requester_name", "asset_name", "issue_category", "priority", "route_to", "confidence", "created_at"]
    ].sort_values("created_at", ascending=False).copy()
    recent_cases["created_at"] = recent_cases["created_at"].dt.strftime("%d %b %Y, %H:%M")
    recent_cases["confidence"] = recent_cases["confidence"].map(lambda value: f"{value:.0%}")
    recent_cases = recent_cases.rename(
        columns={
            "id": "Case #",
            "organization_name": "Organization",
            "requester_name": "Requester",
            "asset_name": "Affected asset",
            "issue_category": "Category",
            "priority": "Priority",
            "route_to": "Assigned team",
            "confidence": "Confidence",
            "created_at": "Submitted",
        }
    )
    st.dataframe(recent_cases, use_container_width=True, hide_index=True)

    with st.expander("Operational details"):
        operational_details = df[
            ["id", "organization_name", "requester_name", "asset_name", "asset_id", "issue_category", "route_to", "summary", "missing_fields"]
        ].rename(
            columns={
                "id": "Case #",
                "organization_name": "Organization",
                "requester_name": "Requester",
                "asset_name": "Affected asset",
                "asset_id": "Asset ID",
                "issue_category": "Category",
                "route_to": "Assigned team",
                "summary": "Routing summary",
                "missing_fields": "Missing information",
            }
        )
        st.dataframe(operational_details, use_container_width=True, hide_index=True)


if __name__ == "__main__":
    render_dashboard()
