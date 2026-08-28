import argparse
from pathlib import Path
import yaml

VALID_STATUS = {"pending", "in_progress", "done", "blocked"}

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--state", default="state/hw06-state.yaml")
    parser.add_argument("--section", required=True)
    parser.add_argument("--field", required=True)
    parser.add_argument("--value", required=True)
    args = parser.parse_args()

    path = Path(args.state)
    if not path.exists():
        raise SystemExit(f"State file not found: {path}")

    data = yaml.safe_load(path.read_text(encoding="utf-8"))

    if args.section not in data:
        raise SystemExit(f"Unknown state section: {args.section}")
    if args.field not in data[args.section]:
        raise SystemExit(f"Unknown state field: {args.section}.{args.field}")

    old = data[args.section][args.field]

    if isinstance(old, int):
        try:
            value = int(args.value)
        except ValueError:
            raise SystemExit(f"{args.field} expects an integer")
    else:
        value = args.value
        if value not in VALID_STATUS:
            raise SystemExit(f"Status must be one of: {sorted(VALID_STATUS)}")

    data[args.section][args.field] = value
    path.write_text(
        yaml.safe_dump(data, sort_keys=False, allow_unicode=True),
        encoding="utf-8"
    )

    print(f"Updated {args.section}.{args.field}: {old!r} -> {value!r}")

if __name__ == "__main__":
    main()
