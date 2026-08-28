from pathlib import Path
import sys
import yaml

ROOT = Path.cwd()
REQ = ROOT / ".agents" / "skills" / "submission-validator" / "references" / "requirements.yaml"

def nonempty(path):
    return path.exists() and path.is_file() and path.stat().st_size > 0

def main():
    if not REQ.exists():
        raise SystemExit(f"Requirements file not found: {REQ}")

    requirements = yaml.safe_load(REQ.read_text(encoding="utf-8"))

    blockers = []
    warnings = []

    for relative in requirements.get("required_files", []):
        if not nonempty(ROOT / relative):
            blockers.append(f"Missing or empty required file: {relative}")

    for group in requirements.get("required_any", []):
        paths = group.get("paths", [])
        if not any(nonempty(ROOT / p) for p in paths):
            blockers.append(
                f"Missing {group.get('label', 'required artifact')}: {', '.join(paths)}"
            )

    min_ai = int(requirements.get("min_ai_tests_per_api", 35))
    min_human = int(requirements.get("min_human_tests_per_api", 5))

    for api_name, metadata in requirements.get("apis", {}).items():
        folder = ROOT / metadata["folder"]

        generated = folder / "generated-tests.yaml"
        human = folder / "human-tests.yaml"
        audit = folder / "audit.yaml"

        if not generated.exists():
            blockers.append(f"{api_name}: generated-tests.yaml missing")
        else:
            items = yaml.safe_load(generated.read_text(encoding="utf-8")) or []
            if len(items) < min_ai:
                blockers.append(
                    f"{api_name}: only {len(items)} AI tests (minimum {min_ai})"
                )

        if not human.exists():
            blockers.append(f"{api_name}: human-tests.yaml missing")
        else:
            items = yaml.safe_load(human.read_text(encoding="utf-8")) or []
            confirmed = [
                t for t in items
                if t.get("source") == "HUMAN"
                and t.get("human_confirmation") is True
            ]
            if len(confirmed) < min_human:
                blockers.append(
                    f"{api_name}: only {len(confirmed)} confirmed human tests (minimum {min_human})"
                )

        if not audit.exists():
            blockers.append(f"{api_name}: audit.yaml missing")
        else:
            entries = yaml.safe_load(audit.read_text(encoding="utf-8")) or []
            incomplete = [
                e.get("test_id")
                for e in entries
                if not (e.get("human_review") or {}).get("verdict")
                or not (e.get("human_review") or {}).get("reasoning")
            ]
            if incomplete:
                blockers.append(
                    f"{api_name}: human audit incomplete for {len(incomplete)} test(s)"
                )

    reports = ROOT / "reports"
    reports.mkdir(parents=True, exist_ok=True)

    lines = ["HW06 Submission Validation", "=" * 28, ""]

    if blockers:
        lines.append("BLOCKERS")
        lines.extend(f"- {b}" for b in blockers)
        lines.append("")

    if warnings:
        lines.append("WARNINGS")
        lines.extend(f"- {w}" for w in warnings)
        lines.append("")

    status = "NOT READY" if blockers else "READY"
    lines.append(f"Status: {status}")

    (reports / "submission-validation.txt").write_text(
        "\n".join(lines) + "\n",
        encoding="utf-8"
    )

    print("\n".join(lines))

    if blockers:
        sys.exit(1)

if __name__ == "__main__":
    main()
