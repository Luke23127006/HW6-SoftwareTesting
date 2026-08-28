import argparse
import json
from pathlib import Path

import yaml
from jsonschema import Draft202012Validator

ALLOWED_REASONS = {
    "PROMPT_GAP",
    "MODEL_LIMITATION",
    "API_CHARACTERISTIC",
    "CROSS_FIELD_INTERACTION",
    "STATE_COMPLEXITY",
    "SECURITY_CONTEXT",
    "SPEC_AMBIGUITY",
}

def find_root(start: Path) -> Path:
    current = start.resolve()
    for candidate in [current, *current.parents]:
        if (candidate / "schemas" / "test-case.schema.json").exists():
            return candidate
    raise SystemExit("Could not locate repository root.")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("suite")
    parser.add_argument("--min-count", type=int, default=5)
    args = parser.parse_args()

    tests = yaml.safe_load(
        Path(args.suite).read_text(encoding="utf-8")
    ) or []

    root = find_root(Path.cwd())
    schema = json.loads(
        (root / "schemas" / "test-case.schema.json").read_text(encoding="utf-8")
    )
    validator = Draft202012Validator(schema)

    errors = []

    for index, test in enumerate(tests):
        test_id = test.get("id", f"test[{index}]")

        for error in validator.iter_errors(test):
            errors.append(
                f"{test_id} {list(error.absolute_path)}: {error.message}"
            )

        if test.get("source") != "HUMAN":
            errors.append(f"{test_id}: source must be HUMAN")

        if test.get("human_confirmation") is not True:
            errors.append(f"{test_id}: human_confirmation must be true")

        why = test.get("why_ai_missed") or {}

        if why.get("category") not in ALLOWED_REASONS:
            errors.append(f"{test_id}: invalid why_ai_missed.category")

        if not why.get("explanation"):
            errors.append(f"{test_id}: why_ai_missed.explanation is required")

    if len(tests) < args.min_count:
        errors.append(
            f"Only {len(tests)} confirmed human tests; minimum is {args.min_count}"
        )

    if errors:
        for error in errors:
            print("ERROR", error)
        raise SystemExit(1)

    print(f"Human extension suite VALID: {len(tests)} tests")

if __name__ == "__main__":
    main()
