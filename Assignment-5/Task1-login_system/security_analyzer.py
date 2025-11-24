import re
import sys
from pathlib import Path
from typing import Iterable, List, Tuple

PROJECT_ROOT = Path(__file__).parent

# Patterns for insecure logic / hardcoded creds
PATTERNS: List[Tuple[str, str]] = [
    (
        r"(?i)(username\s*==\s*['\"][^'\"]+['\"])\s*and\s*(password\s*==\s*['\"][^'\"]+['\"])",
        "Hardcoded username/password comparison",
    ),
    (
        r"(?i)(password|passwd|pwd|secret|token)\s*=\s*['\"][^'\"]+['\"]",
        "Credential-like variable assigned a string literal",
    ),
    (
        r"(?i)(SECRET_KEY)\s*=\s*['\"][^'\"]+['\"]",
        "Hardcoded Flask SECRET_KEY",
    ),
    (
        r"(?i)(app\.run\(.*debug\s*=\s*True.*\))",
        "Flask debug=True enabled",
    ),
    (
        r"(?i)hashlib\.(md5|sha1)\(.*\)",
        "Insecure hash function (md5/sha1) detected",
    ),
    (
        r"(?i)eval\(\s*input\(\s*\)\s*\)",
        "eval(input()) pattern",
    ),
    (
        r"(?i)exec\(.*input\(\)",
        "exec on user input",
    ),
    (
        r"(?i)INSERT\s+INTO\s+users\s*\([^\)]*password[^_][^\)]*\)",
        "Possible plaintext password storage in SQL INSERT",
    ),
]


def scan_text(text: str) -> List[Tuple[int, str, str]]:
    findings: List[Tuple[int, str, str]] = []
    for pattern, description in PATTERNS:
        for match in re.finditer(pattern, text):
            # Estimate line number from span
            start = match.start()
            line_num = text.count("\n", 0, start) + 1
            findings.append((line_num, description, match.group(0)))
    return findings


def iter_code_files(root: Path) -> Iterable[Path]:
    for path in root.rglob("*.py"):
        yield path


def main() -> int:
    any_findings = False
    for file in iter_code_files(PROJECT_ROOT):
        if file.name == Path(__file__).name:
            # Still scan this file too, but it's usually not necessary
            pass
        try:
            text = file.read_text(encoding="utf-8")
        except Exception as exc:  # pragma: no cover
            print(f"[warn] Could not read {file}: {exc}")
            continue
        findings = scan_text(text)
        if findings:
            any_findings = True
            print(f"\n[!] Findings in {file}:")
            for line_num, description, snippet in findings:
                print(f"  - Line {line_num}: {description}")
                print(f"    Snippet: {snippet.strip()}")
    if not any_findings:
        print("No insecure patterns or hardcoded credentials detected.")
    # Exit code: 1 if findings present to allow CI gating
    return 1 if any_findings else 0


if __name__ == "__main__":
    sys.exit(main())
