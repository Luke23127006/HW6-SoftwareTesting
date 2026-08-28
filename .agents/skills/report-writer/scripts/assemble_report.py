from pathlib import Path

ROOT = Path.cwd()
TEMPLATE = ROOT / ".agents" / "skills" / "report-writer" / "assets" / "report-template.md"
SECTIONS = ROOT / "docs" / "report-sections"
OUTPUT = ROOT / "docs" / "report.md"

def main():
    if not TEMPLATE.exists():
        raise SystemExit(f"Report template not found: {TEMPLATE}")

    SECTIONS.mkdir(parents=True, exist_ok=True)
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)

    parts = [TEMPLATE.read_text(encoding="utf-8").rstrip(), ""]

    section_files = sorted(SECTIONS.glob("*.md"))

    for file in section_files:
        parts += [
            f"<!-- BEGIN {file.name} -->",
            file.read_text(encoding="utf-8").rstrip(),
            f"<!-- END {file.name} -->",
            "",
        ]

    OUTPUT.write_text(
        "\n".join(parts).rstrip() + "\n",
        encoding="utf-8"
    )

    print(f"Assembled {OUTPUT} from {len(section_files)} section fragment(s).")

if __name__ == "__main__":
    main()
