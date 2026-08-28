import argparse
import json
from pathlib import Path

import yaml
from jsonschema import Draft202012Validator

def find_root(start: Path) -> Path:
    current = start.resolve()
    for candidate in [current, *current.parents]:
        if (candidate / "schemas" / "test-case.schema.json").exists():
            return candidate
    raise SystemExit("Could not locate repository root.")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("suite")
    parser.add_argument("--min-count", type=int, default=35)
    args = parser.parse_args()

    suite_path = Path(args.suite)
    tests = yaml.safe_load(suite_path.read_text(encoding="utf-8")) or []

    if not isinstance(tests, list):
        raise SystemExit("Suite must be a YAML list.")

    root = find_root(Path.cwd())
    schema = json.loads(
        (root / "schemas" / "test-case.schema.json").read_text(encoding="utf-8")
    )
    validator = Draft202012Validator(schema)

    errors = []
    ids = []

    for index, test in enumerate(tests):
        ids.append(test.get("id"))

        for error in validator.iter_errors(test):
            errors.append(
                f"test[{index}] {list(error.absolute_path)}: {error.message}"
            )

        if test.get("source") != "AI":
            errors.append(
                f"{test.get('id', f'test[{index}]')}: generated suite must use source: AI"
            )

    duplicate_ids = sorted({
        test_id for test_id in ids
        if test_id and ids.count(test_id) > 1
    })

    if duplicate_ids:
        errors.append(f"Duplicate test IDs: {duplicate_ids}")

    if len(tests) < args.min_count:
        errors.append(
            f"Only {len(tests)} tests found; minimum required is {args.min_count}"
        )

    if errors:
        for error in errors:
            print("ERROR", error)
        raise SystemExit(1)

    print(f"AI test suite VALID: {len(tests)} test cases")

if __name__ == "__main__":
    main()
