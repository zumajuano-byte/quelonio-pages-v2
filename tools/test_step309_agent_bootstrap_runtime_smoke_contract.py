#!/usr/bin/env python3
"""Step 309 - Runtime smoke contract for agent_bootstrap.ps1."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path
from typing import Sequence, Tuple

ROOT = Path(__file__).resolve().parents[1]
WRAPPER = ROOT / "agent_bootstrap.ps1"
VENV_DIR = ROOT / ".venv"
TIMEOUT_S = 60


def _check(name: str, ok: bool, detail: str) -> bool:
    print(f"[{'PASS' if ok else 'FAIL'}] {name} ({detail})")
    return ok


def _run_wrapper(args: Sequence[str]) -> Tuple[int, str, str]:
    cmd = [
        "powershell",
        "-NoProfile",
        "-ExecutionPolicy",
        "Bypass",
        "-File",
        str(WRAPPER),
        *args,
    ]
    cp = subprocess.run(
        cmd,
        cwd=str(ROOT),
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        timeout=TIMEOUT_S,
        check=False,
    )
    return int(cp.returncode), cp.stdout, cp.stderr


def main() -> int:
    print("=" * 60)
    print("Step 309 - agent_bootstrap runtime smoke contract")
    print("=" * 60)

    checks: list[bool] = []

    checks.append(_check("wrapper_exists", WRAPPER.exists(), str(WRAPPER)))
    checks.append(_check("venv_exists", VENV_DIR.exists(), str(VENV_DIR)))
    if not WRAPPER.exists() or not VENV_DIR.exists():
        print("[FAIL] Missing required runtime prerequisites (.venv and/or wrapper).")
        print("[FAIL] Step 309")
        return 1

    try:
        code_a, out_a, err_a = _run_wrapper(["-SkipLlms"])
    except subprocess.TimeoutExpired:
        checks.append(_check("run_skipllms_timeout", False, f"timeout_s={TIMEOUT_S}"))
        print("[FAIL] Step 309")
        return 1

    checks.append(_check("run_skipllms_exit_zero", code_a == 0, f"exit_code={code_a}"))
    checks.append(_check("run_skipllms_stdout_bootstrap_started", "[INFO] Agent bootstrap iniciado" in out_a, "stdout marker"))
    checks.append(_check("run_skipllms_stdout_preflight_ok", "[PASS] Preflight OK" in out_a, "stdout marker"))
    checks.append(_check("run_skipllms_stdout_bootstrap_done", "[PASS] Agent bootstrap completado" in out_a, "stdout marker"))
    checks.append(_check("run_skipllms_stderr_empty", err_a.strip() == "", f"stderr_len={len(err_a.strip())}"))

    try:
        code_b, out_b, err_b = _run_wrapper(["-SkipLlms", "--no-require-venv"])
    except subprocess.TimeoutExpired:
        checks.append(_check("run_skipllms_no_venv_timeout", False, f"timeout_s={TIMEOUT_S}"))
        print("[FAIL] Step 309")
        return 1

    checks.append(_check("run_skipllms_no_venv_exit_zero", code_b == 0, f"exit_code={code_b}"))
    checks.append(_check("run_skipllms_no_venv_stdout_bootstrap_started", "[INFO] Agent bootstrap iniciado" in out_b, "stdout marker"))
    checks.append(_check("run_skipllms_no_venv_stdout_preflight_ok", "[PASS] Preflight OK" in out_b, "stdout marker"))
    checks.append(_check("run_skipllms_no_venv_stdout_bootstrap_done", "[PASS] Agent bootstrap completado" in out_b, "stdout marker"))
    checks.append(_check("run_skipllms_no_venv_stderr_empty", err_b.strip() == "", f"stderr_len={len(err_b.strip())}"))

    if all(checks):
        print("ALL TESTS PASSED!")
        print("[PASS] Step 309")
        return 0

    print("[FAIL] Step 309")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
