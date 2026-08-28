import json
import sys
from pathlib import Path

import yaml
from jsonschema import Draft202012Validator

def find_root(start: Path) -> Path:
    current = start.resolve()
    for candidate in [current, *current.parents]:
        if (candidate / "schemas" / "api-context.schema.json").exists():
            return candidate
    raise SystemExit("Could not locate repository root containing schemas/api-context.schema.json")

def main():
    if len(sys.argv) != 2:
        raise SystemExit("Usage: validate_context.py <api-context.yaml>")

    context_path = Path(sys.argv[1])
    if not context_path.exists():
        raise SystemExit(f"Context file not found: {context_path}")

    root = find_root(Path.cwd())
    schema = json.loads(
        (root / "schemas" / "api-context.schema.json").read_text(encoding="utf-8")
    )
    context = yaml.safe_load(context_path.read_text(encoding="utf-8"))

    errors = sorted(
        Draft202012Validator(schema).iter_errors(context),
        key=lambda e: list(e.absolute_path)
    )

    if errors:
        for error in errors:
            print(f"ERROR {list(error.absolute_path)}: {error.message}")
        raise SystemExit(1)

    print(f"API context VALID: {context_path}")

if __name__ == "__main__":
    main()
