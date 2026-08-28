import re
import sys
from pathlib import Path

def main():
    if len(sys.argv) != 2:
        raise SystemExit("Usage: validate_word_count.py <markdown-file>")

    text = Path(sys.argv[1]).read_text(encoding="utf-8")
    text = re.sub(r"```.*?```", " ", text, flags=re.S)
    text = re.sub(r"[#>*_`\[\]\(\)]", " ", text)

    words = re.findall(r"\b[\w’'-]+\b", text, flags=re.UNICODE)
    count = len(words)

    print(f"Word count: {count}")

    if not 200 <= count <= 300:
        raise SystemExit("AI Critique must contain 200–300 words.")

    print("AI Critique length VALID")

if __name__ == "__main__":
    main()
