#!/usr/bin/env python3
"""Step 308 - Agent bootstrap wrapper contract."""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WRAPPER = ROOT / "agent_bootstrap.ps1"


def _check(name: str, ok: bool, detail: str) -> bool:
    print(f"[{'PASS' if ok else 'FAIL'}] {name} ({detail})")
    return ok


def main() -> int:
    print("=" * 60)
    print("Step 308 - Agent bootstrap contract")
    print("=" * 60)

    checks: list[bool] = []

    checks.append(_check("wrapper_exists", WRAPPER.exists(), str(WRAPPER)))
    if not WRAPPER.exists():
        print("[FAIL] Step 308")
        return 1

    text = WRAPPER.read_text(encoding="utf-8")
    lower = text.lower()

    checks.append(_check("invokes_preflight_script", "preflight_repo.ps1" in lower, "preflight_repo.ps1"))
    checks.append(_check("invokes_build_llms", "tools\\build_llms_txt.py" in lower, "tools\\build_llms_txt.py"))
    checks.append(_check("supports_skip_llms", "[switch]$skipllms" in lower and "skipllms" in lower, "-SkipLlms"))
    checks.append(_check("preflight_first", lower.find("preflight_repo.ps1") < lower.find("build_llms_txt.py"), "order preflight->build"))
    checks.append(_check("propagates_exit_code", "$lastexitcode" in lower and "exit $" in lower, "LASTEXITCODE + exit"))
    checks.append(_check("passes_remaining_args_to_preflight", "valuefromremainingarguments" in lower and "@preflightargs" in lower, "args passthrough"))

    if all(checks):
        print("ALL TESTS PASSED!")
        print("[PASS] Step 308")
        return 0

    print("[FAIL] Step 308")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
