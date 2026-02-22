#!/usr/bin/env python3
"""Step 310 - Agent bootstrap idempotency contract (offline/deterministic)."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path
from typing import Sequence, Tuple

ROOT = Path(__file__).resolve().parents[1]
WRAPPER = ROOT / "agent_bootstrap.ps1"
PREFLIGHT = ROOT / "preflight_repo.ps1"
BUILD_LLMS = ROOT / "tools" / "build_llms_txt.py"
LLMS = ROOT / "llms.txt"
LLMS_FULL = ROOT / "llms-full.txt"
VENV = ROOT / ".venv"
TIMEOUT_S = 120


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


def _validate_common_markers(stdout: str, checks: list[bool], prefix: str) -> None:
    checks.append(_check(f"{prefix}_has_bootstrap_started", "Agent bootstrap iniciado" in stdout, "stdout marker"))
    checks.append(_check(f"{prefix}_has_preflight_ok", "Preflight OK" in stdout, "stdout marker"))
    checks.append(_check(f"{prefix}_has_bootstrap_done", "Agent bootstrap completado" in stdout, "stdout marker"))


def main() -> int:
    print("=" * 60)
    print("Step 310 - Agent bootstrap idempotency contract")
    print("=" * 60)

    checks: list[bool] = []

    checks.append(_check("wrapper_exists", WRAPPER.exists(), str(WRAPPER)))
    checks.append(_check("preflight_exists", PREFLIGHT.exists(), str(PREFLIGHT)))
    checks.append(_check("build_llms_exists", BUILD_LLMS.exists(), str(BUILD_LLMS)))
    checks.append(_check("llms_exists", LLMS.exists(), str(LLMS)))
    checks.append(_check("llms_full_exists", LLMS_FULL.exists(), str(LLMS_FULL)))
    checks.append(_check("venv_exists", VENV.exists(), str(VENV)))

    if not VENV.exists():
        print("[FAIL] .venv local no existe. Este contrato requiere entorno local configurado.")
        print("[FAIL] Step 310")
        return 1

    if not all(checks):
        print("[FAIL] Faltan prerequisitos de archivos.")
        print("[FAIL] Step 310")
        return 1

    try:
        code_skip, out_skip, err_skip = _run_wrapper(["-SkipLlms"])
        checks.append(_check("run_skipllms_exit_zero", code_skip == 0, f"exit_code={code_skip}"))
        _validate_common_markers(out_skip, checks, "run_skipllms")
        checks.append(_check("run_skipllms_stderr_empty", err_skip.strip() == "", f"stderr_len={len(err_skip.strip())}"))

        code_full_1, out_full_1, err_full_1 = _run_wrapper([])
        checks.append(_check("run_full_1_exit_zero", code_full_1 == 0, f"exit_code={code_full_1}"))
        _validate_common_markers(out_full_1, checks, "run_full_1")
        checks.append(_check("run_full_1_has_llms_generation_marker", "Generando llms.txt/llms-full.txt" in out_full_1, "stdout marker"))
        checks.append(_check("run_full_1_stderr_empty", err_full_1.strip() == "", f"stderr_len={len(err_full_1.strip())}"))

        code_full_2, out_full_2, err_full_2 = _run_wrapper([])
        checks.append(_check("run_full_2_exit_zero", code_full_2 == 0, f"exit_code={code_full_2}"))
        _validate_common_markers(out_full_2, checks, "run_full_2")
        checks.append(_check("run_full_2_has_llms_generation_marker", "Generando llms.txt/llms-full.txt" in out_full_2, "stdout marker"))
        checks.append(_check("run_full_2_stderr_empty", err_full_2.strip() == "", f"stderr_len={len(err_full_2.strip())}"))
    except subprocess.TimeoutExpired as exc:
        checks.append(_check("subprocess_timeout", False, f"timeout_s={TIMEOUT_S} cmd={exc.cmd}"))
        print("[FAIL] Step 310")
        return 1

    try:
        llms_text = LLMS.read_text(encoding="utf-8")
        llms_full_text = LLMS_FULL.read_text(encoding="utf-8")
        checks.append(_check("llms_utf8_readable", True, "ok"))
    except Exception as exc:
        checks.append(_check("llms_utf8_readable", False, str(exc)))
        llms_text = ""
        llms_full_text = ""

    checks.append(_check("llms_not_empty", len(llms_text.strip()) > 0, f"chars={len(llms_text)}"))
    checks.append(_check("llms_full_not_empty", len(llms_full_text.strip()) > 0, f"chars={len(llms_full_text)}"))
    checks.append(_check("llms_full_longer", len(llms_full_text) > len(llms_text), f"llms={len(llms_text)} full={len(llms_full_text)}"))

    if all(checks):
        print("ALL TESTS PASSED!")
        print("[PASS] Step 310")
        return 0

    print("[FAIL] Step 310")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
