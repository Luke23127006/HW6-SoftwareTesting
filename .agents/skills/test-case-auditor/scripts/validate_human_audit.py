import sys
from pathlib import Path
import yaml

ALLOWED = {"VALID", "INVALID", "INCOMPLETE"}

def main():
    if len(sys.argv) != 2:
        raise SystemExit("Usage: validate_human_audit.py <audit.yaml>")

    entries = yaml.safe_load(
        Path(sys.argv[1]).read_text(encoding="utf-8")
    ) or []

    errors = []
    counts = {value: 0 for value in ALLOWED}

    for index, entry in enumerate(entries):
        test_id = entry.get("test_id", f"entry[{index}]")
        human = entry.get("human_review") or {}
        verdict = human.get("verdict")
        reasoning = human.get("reasoning")

        if verdict not in ALLOWED:
            errors.append(f"{test_id}: missing/invalid human verdict")
        else:
            counts[verdict] += 1

        if not reasoning:
            errors.append(f"{test_id}: human reasoning is required")

        if verdict in {"INVALID", "INCOMPLETE"}:
            correction = entry.get("correction") or {}
            if not correction.get("description"):
                errors.append(
                    f"{test_id}: correction description required for {verdict}"
                )

    print(f"Total audit entries: {len(entries)}")
    for verdict in sorted(ALLOWED):
        print(f"{verdict}: {counts[verdict]}")

    if errors:
        for error in errors:
            print("ERROR", error)
        raise SystemExit(1)

    print("Human audit COMPLETE")

if __name__ == "__main__":
    main()
