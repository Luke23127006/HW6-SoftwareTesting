import json
import sys
from pathlib import Path

def main():
    if len(sys.argv) != 2:
        raise SystemExit("Usage: parse_newman.py <newman-report.json>")

    report_path = Path(sys.argv[1])
    if not report_path.exists():
        raise SystemExit(f"Newman JSON report not found: {report_path}")

    root = Path.cwd()
    data = json.loads(report_path.read_text(encoding="utf-8"))

    executions = data.get("run", {}).get("executions", [])
    results = []

    for execution in executions:
        item_name = (execution.get("item") or {}).get("name", "UNKNOWN")
        test_id = item_name.split("|", 1)[0].strip() if "|" in item_name else item_name

        assertions = execution.get("assertions") or []
        failed = [a for a in assertions if a.get("error")]
        response = execution.get("response") or {}

        results.append({
            "test_id": test_id,
            "status": "FAIL" if failed else "PASS",
            "classification": "SUT_BUG_CANDIDATE" if failed else "NONE",
            "expected": None,
            "actual": {
                "response_code": response.get("code")
            },
            "evidence": {
                "newman_source": str(report_path),
                "failed_assertions": [
                    {
                        "assertion": a.get("assertion"),
                        "error": a.get("error"),
                    }
                    for a in failed
                ],
            },
            "needs_human_confirmation": bool(failed),
        })

    reports = root / "reports"
    docs = root / "docs"

    reports.mkdir(parents=True, exist_ok=True)
    docs.mkdir(parents=True, exist_ok=True)

    (reports / "results.json").write_text(
        json.dumps(results, indent=2, ensure_ascii=False),
        encoding="utf-8"
    )

    total = len(results)
    passed = sum(r["status"] == "PASS" for r in results)
    failed_count = sum(r["status"] == "FAIL" for r in results)

    (docs / "test-summary.md").write_text(
        f"# Test Summary\n\n- Executed: **{total}**\n- Passed: **{passed}**\n- Failed: **{failed_count}**\n",
        encoding="utf-8"
    )

    lines = [
        "# Failure Analysis",
        "",
        "> Initial classifications are candidates only and require human review.",
        "",
    ]

    for result in results:
        if result["status"] == "FAIL":
            lines += [
                f"## {result['test_id']}",
                "",
                "- Initial classification: `SUT_BUG_CANDIDATE`",
                "- Human confirmation required: **yes**",
                f"- Response code: `{result['actual'].get('response_code')}`",
                "",
            ]

    if failed_count == 0:
        lines.append("No failed tests in this Newman run.")

    (reports / "failure-analysis.md").write_text(
        "\n".join(lines) + "\n",
        encoding="utf-8"
    )

    print(f"Parsed {total}: {passed} passed, {failed_count} failed.")

if __name__ == "__main__":
    main()
