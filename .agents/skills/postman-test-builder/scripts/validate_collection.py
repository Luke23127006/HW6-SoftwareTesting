import json
import sys
from pathlib import Path

def walk(items):
    for item in items:
        if "item" in item:
            yield from walk(item["item"])
        else:
            yield item

def script_text(events):
    lines = []
    for event in events or []:
        exec_lines = (event.get("script") or {}).get("exec") or []
        lines.extend(exec_lines if isinstance(exec_lines, list) else [exec_lines])
    return "\n".join(lines)

def main():
    if len(sys.argv) != 2:
        raise SystemExit("Usage: validate_collection.py <collection.json>")

    data = json.loads(
        Path(sys.argv[1]).read_text(encoding="utf-8")
    )

    errors = []
    warnings = []

    root_script = script_text(data.get("event"))

    if "X-Student-Id" not in root_script or "studentId" not in root_script:
        errors.append("Missing collection-level X-Student-Id mechanism.")

    leaves = list(walk(data.get("item", [])))

    if not leaves:
        errors.append("Collection contains no executable request items.")

    for item in leaves:
        name = item.get("name", "")

        if "|" not in name:
            errors.append(f"Missing traceable test ID: {name}")

        script = script_text(item.get("event"))

        if not script.strip():
            errors.append(f"Missing test script: {name}")

        if "pm.expect(true).to.eql(true)" in script:
            warnings.append(f"Placeholder assertion remains: {name}")

    for warning in warnings:
        print("WARNING", warning)

    if errors:
        for error in errors:
            print("ERROR", error)
        raise SystemExit(1)

    print(f"Postman collection structurally VALID: {len(leaves)} requests")

if __name__ == "__main__":
    main()
