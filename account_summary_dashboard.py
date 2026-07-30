"""Local dashboard for the consolidated account-summary SQLite database."""

from __future__ import annotations

import argparse
import re
from datetime import datetime
from pathlib import Path

from flask import Flask, jsonify, render_template, request, send_file

from summary_database import (
    DEFAULT_DATABASE_PATH,
    create_excel_export,
    initialize_database,
    query_acknowledgements,
    query_progress,
    query_recent_failures,
    query_summary_page,
    query_summary_totals,
)


def create_dashboard_app(database_path: str | Path) -> Flask:
    app = Flask(__name__)
    resolved_database = initialize_database(database_path)
    app.config["ACCOUNT_SUMMARY_DATABASE"] = str(resolved_database)

    @app.route("/")
    def dashboard() -> str:
        return render_template(
            "account_summary_dashboard.html",
            database_name=resolved_database.name,
        )

    @app.route("/api/progress")
    def progress():
        return jsonify(query_progress(resolved_database))

    @app.route("/api/failures")
    def failures():
        limit = request.args.get("limit", default=10, type=int)
        return jsonify(
            {"failures": query_recent_failures(resolved_database, limit=limit)}
        )

    @app.route("/api/acknowledgements")
    def acknowledgements():
        search = request.args.get("q", default="", type=str)
        limit = request.args.get("limit", default=50, type=int)
        return jsonify(
            {
                "acknowledgements": query_acknowledgements(
                    resolved_database,
                    search=search,
                    limit=limit,
                )
            }
        )

    @app.route("/api/totals")
    def totals():
        acknowledgement = request.args.get("ack", default="ALL", type=str)
        return jsonify(
            query_summary_totals(
                resolved_database,
                acknowledgement=acknowledgement,
            )
        )

    @app.route("/api/summary")
    def summary():
        view = request.args.get("view", default="account", type=str)
        acknowledgement = request.args.get("ack", default="ALL", type=str)
        status = request.args.get("status", default="ALL", type=str)
        search = request.args.get("search", default="", type=str)
        page = request.args.get("page", default=1, type=int)
        page_size = request.args.get("page_size", default=100, type=int)
        return jsonify(
            query_summary_page(
                resolved_database,
                view=view,
                acknowledgement=acknowledgement,
                status=status,
                search=search,
                page=page,
                page_size=page_size,
            )
        )

    @app.route("/download/excel")
    def download_excel():
        acknowledgement = request.args.get("ack", default="ALL", type=str).strip()
        if not acknowledgement:
            acknowledgement = "ALL"
        output = create_excel_export(
            resolved_database,
            acknowledgement=acknowledgement,
        )
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        if acknowledgement.upper() == "ALL":
            filename = f"All_ACK_Account_Summary_{timestamp}.xlsx"
        else:
            safe_ack = re.sub(r"[^A-Za-z0-9_-]+", "_", acknowledgement)[:80]
            filename = f"ACK_{safe_ack}_Account_Summary_{timestamp}.xlsx"
        return send_file(
            output,
            mimetype=(
                "application/vnd.openxmlformats-officedocument."
                "spreadsheetml.sheet"
            ),
            as_attachment=True,
            download_name=filename,
        )

    return app


def build_argument_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Run the local account-summary dashboard."
    )
    parser.add_argument(
        "--database",
        type=Path,
        default=DEFAULT_DATABASE_PATH,
        help=f"SQLite database path (default: {DEFAULT_DATABASE_PATH})",
    )
    parser.add_argument("--host", default="127.0.0.1")
    parser.add_argument("--port", default=5002, type=int)
    parser.add_argument("--debug", action="store_true")
    return parser


def main() -> None:
    args = build_argument_parser().parse_args()
    app = create_dashboard_app(args.database.expanduser().resolve())
    app.run(
        host=args.host,
        port=args.port,
        debug=args.debug,
        use_reloader=False,
    )


if __name__ == "__main__":
    main()

