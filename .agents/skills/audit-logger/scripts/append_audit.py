import argparse
import re
import shutil
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

ROOT = Path.cwd()
AUDIT_PATH = ROOT / "docs" / "ai-audit.md"
RAW_LOG_DIR = ROOT / "ai-logs"

def next_interaction_id(text):
    numbers = [
        int(value)
        for value in re.findall(r"^## AI-(\d+)\s*$", text, flags=re.MULTILINE)
    ]
    return f"AI-{max(numbers, default=0) + 1:03d}"

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--prompt-file", required=True)
    parser.add_argument("--summary-file", required=True)
    parser.add_argument("--tool", default="ChatGPT / GPT-5.6 Sol")
    parser.add_argument("--artifact", action="append", default=[])
    parser.add_argument("--raw-output-file")
    args = parser.parse_args()

    AUDIT_PATH.parent.mkdir(parents=True, exist_ok=True)

    if AUDIT_PATH.exists():
        existing = AUDIT_PATH.read_text(encoding="utf-8")
    else:
        existing = "# AI Audit Report\n\n"
        AUDIT_PATH.write_text(existing, encoding="utf-8")

    interaction_id = next_interaction_id(existing)

    prompt = Path(args.prompt_file).read_text(encoding="utf-8").rstrip()
    summary = Path(args.summary_file).read_text(encoding="utf-8").rstrip()

    timestamp = datetime.now(
        ZoneInfo("Asia/Ho_Chi_Minh")
    ).strftime("%Y-%m-%d %H:%M:%S %Z")

    raw_reference = "NOT_RETAINED"

    if args.raw_output_file:
        RAW_LOG_DIR.mkdir(parents=True, exist_ok=True)
        destination = RAW_LOG_DIR / f"{interaction_id}.md"
        shutil.copy2(args.raw_output_file, destination)
        raw_reference = f"ai-logs/{destination.name}"

    artifacts = args.artifact or ["None"]
    artifact_lines = "\n".join(
        f"- `{artifact}`" for artifact in artifacts
    )

    block = (
        f"## {interaction_id}\n\n"
        f"**Tool:** {args.tool}  \n"
        f"**Time:** {timestamp}\n\n"
        f"### Prompt\n\n"
        f"```text\n{prompt}\n```\n\n"
        f"### AI Response Summary\n\n"
        f"{summary}\n\n"
        f"### Artifacts\n\n"
        f"{artifact_lines}\n\n"
        f"### Full Output Reference\n\n"
        f"`{raw_reference}`\n\n"
    )

    with AUDIT_PATH.open("a", encoding="utf-8") as handle:
        handle.write(block)

    print(f"Appended {interaction_id} to {AUDIT_PATH}")

if __name__ == "__main__":
    main()
