#!/usr/bin/env python3
"""Step 306 - Contract for llms.txt and llms-full.txt artifacts."""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LLMS = ROOT / "llms.txt"
LLMS_FULL = ROOT / "llms-full.txt"

REQUIRED_TOKENS = [
    "quelonio",
    "biblia",
    "docs/01_agua/",
    "docs/02_malta/",
    "docs/03_levadura/",
    "docs/04_lupulo/",
    "docs/06_procesos_qa_qc/",
    "docs/98_verdad_negocio/",
]


def _check(name: str, ok: bool, detail: str) -> bool:
    print(f"[{'PASS' if ok else 'FAIL'}] {name} ({detail})")
    return ok


def main() -> int:
    print("=" * 60)
    print("Step 306 - llms.txt contract")
    print("=" * 60)

    checks: list[bool] = []

    checks.append(_check("llms_exists", LLMS.exists(), str(LLMS)))
    checks.append(_check("llms_full_exists", LLMS_FULL.exists(), str(LLMS_FULL)))
    if not LLMS.exists() or not LLMS_FULL.exists():
        print("[FAIL] Step 306")
        return 1

    try:
        llms_text = LLMS.read_text(encoding="utf-8")
        llms_full_text = LLMS_FULL.read_text(encoding="utf-8")
        utf8_ok = True
    except Exception as exc:
        llms_text = ""
        llms_full_text = ""
        utf8_ok = False
        checks.append(_check("utf8_readable", False, str(exc)))

    if utf8_ok:
        checks.append(_check("utf8_readable", True, "ok"))

    checks.append(_check("llms_not_empty", len(llms_text.strip()) > 0, f"chars={len(llms_text)}"))
    checks.append(_check("llms_full_not_empty", len(llms_full_text.strip()) > 0, f"chars={len(llms_full_text)}"))
    checks.append(_check("llms_full_longer", len(llms_full_text) > len(llms_text), f"llms={len(llms_text)} full={len(llms_full_text)}"))

    lower_llms = llms_text.lower()
    lower_full = llms_full_text.lower()

    for token in REQUIRED_TOKENS:
        checks.append(_check(f"contains::{token}", token in lower_llms or token in lower_full, token))

    section_hits = 0
    for token in ["agua", "malta", "levadura", "lupulo", "qa_qc", "verdad_negocio", "procesos"]:
        if token in lower_llms:
            section_hits += 1
    checks.append(_check("llms_has_curated_sections", section_hits >= 5, f"hits={section_hits}"))

    if all(checks):
        print("ALL TESTS PASSED!")
        print("[PASS] Step 306")
        return 0

    print("[FAIL] Step 306")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
