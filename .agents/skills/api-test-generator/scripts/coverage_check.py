import json
import sys
from pathlib import Path
import yaml

CATEGORIES = [
    "functional", "domain", "boundary", "state",
    "authentication", "authorization", "security",
    "schema", "error-handling",
]

def main():
    if len(sys.argv) != 3:
        raise SystemExit(
            "Usage: coverage_check.py <generated-tests.yaml> <api-context.yaml>"
        )

    suite_path = Path(sys.argv[1])
    context_path = Path(sys.argv[2])

    tests = yaml.safe_load(suite_path.read_text(encoding="utf-8")) or []
    context = yaml.safe_load(context_path.read_text(encoding="utf-8")) or {}

    category_counts = {category: 0 for category in CATEGORIES}
    requirement_counts = {}

    for test in tests:
        category = test.get("category")
        if category in category_counts:
            category_counts[category] += 1

        for requirement in test.get("requirements", []):
            requirement_counts[requirement] = requirement_counts.get(requirement, 0) + 1

    warnings = []

    for sec in context.get("security_requirements", []):
        if requirement_counts.get(sec, 0) == 0:
            warnings.append(f"No generated test references {sec}")

    if category_counts["schema"] == 0:
        warnings.append("No schema validation tests found.")

    if context.get("states") and category_counts["state"] == 0:
        warnings.append("Context defines state behavior but no state tests were found.")

    report = {
        "test_count": len(tests),
        "category_counts": category_counts,
        "requirement_counts": requirement_counts,
        "context_security_requirements": context.get("security_requirements", []),
        "warnings": warnings,
    }

    suite_path.with_name("coverage.json").write_text(
        json.dumps(report, indent=2, ensure_ascii=False),
        encoding="utf-8"
    )

    lines = [
        "# Coverage Summary", "",
        f"- AI tests: **{len(tests)}**", "",
        "## Category Counts", "",
    ]

    for category, count in category_counts.items():
        lines.append(f"- `{category}`: {count}")

    lines += ["", "## Warnings", ""]
    lines += [f"- {w}" for w in warnings] if warnings else ["- None"]

    suite_path.with_name("coverage.md").write_text(
        "\n".join(lines) + "\n",
        encoding="utf-8"
    )

    print("Coverage report generated.")

if __name__ == "__main__":
    main()
