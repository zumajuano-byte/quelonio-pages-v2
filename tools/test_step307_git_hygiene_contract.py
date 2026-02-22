#!/usr/bin/env python3
"""Step 307 - Git hygiene contract for local artifacts."""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
GITIGNORE = ROOT / ".gitignore"

REQUIRED_PATTERNS = [
    "__pycache__",
    "*.py[cod]",
    "data/tmp/",
    "session-*.md",
]

FORBIDDEN_PATTERNS = [
    "docs/",
    "tools/",
    "*.md",
]


def _check(name: str, ok: bool, detail: str) -> bool:
    print(f"[{'PASS' if ok else 'FAIL'}] {name} ({detail})")
    return ok


def main() -> int:
    print("=" * 60)
    print("Step 307 - Git hygiene contract")
    print("=" * 60)

    checks: list[bool] = []

    checks.append(_check("gitignore_exists", GITIGNORE.exists(), str(GITIGNORE)))
    if not GITIGNORE.exists():
        print("[FAIL] Step 307")
        return 1

    text = GITIGNORE.read_text(encoding="utf-8")
    lines = {line.strip() for line in text.splitlines() if line.strip() and not line.strip().startswith("#")}

    for pattern in REQUIRED_PATTERNS:
        checks.append(_check(f"required::{pattern}", any(pattern in line for line in lines), pattern))

    for pattern in FORBIDDEN_PATTERNS:
        checks.append(_check(f"forbidden::{pattern}", pattern not in lines, pattern))

    if all(checks):
        print("ALL TESTS PASSED!")
        print("[PASS] Step 307")
        return 0

    print("[FAIL] Step 307")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
