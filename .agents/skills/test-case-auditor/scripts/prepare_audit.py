import sys
from pathlib import Path
import yaml

def main():
    if len(sys.argv) != 3:
        raise SystemExit(
            "Usage: prepare_audit.py <generated-tests.yaml> <audit.yaml>"
        )

    tests = yaml.safe_load(
        Path(sys.argv[1]).read_text(encoding="utf-8")
    ) or []

    entries = []

    for test in tests:
        entries.append({
            "test_id": test.get("id"),
            "ai_review": {
                "suggested_verdict": None,
                "reasoning": [],
            },
            "human_review": {
                "verdict": None,
                "reasoning": None,
            },
            "correction": {
                "required": False,
                "description": None,
            },
        })

    output = Path(sys.argv[2])
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(
        yaml.safe_dump(entries, sort_keys=False, allow_unicode=True),
        encoding="utf-8"
    )

    print(f"Prepared {len(entries)} audit records.")

if __name__ == "__main__":
    main()
