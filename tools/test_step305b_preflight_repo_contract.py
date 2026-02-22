#!/usr/bin/env python3
"""Step 305B - Preflight repo contract for quelonio-pages-v2."""

from __future__ import annotations

import json
import shutil
import subprocess
import sys
import uuid
from pathlib import Path
from typing import Tuple

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "tools" / "preflight_repo.py"
TMP_BASE = ROOT / "data" / "tmp"


def _run(args: list[str], cwd: Path) -> Tuple[int, str, str]:
    cp = subprocess.run(
        [sys.executable, str(SCRIPT), *args],
        cwd=str(cwd),
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        timeout=60,
        check=False,
    )
    return int(cp.returncode), cp.stdout, cp.stderr


def _check(name: str, ok: bool, detail: str) -> bool:
    print(f"[{'PASS' if ok else 'FAIL'}] {name} ({detail})")
    return ok


def _make_repo(base: Path, repo_name: str, with_markers: bool) -> Path:
    repo = base / repo_name
    repo.mkdir(parents=True, exist_ok=True)
    if with_markers:
        (repo / "docs").mkdir(parents=True, exist_ok=True)
        (repo / "tools").mkdir(parents=True, exist_ok=True)
        (repo / "mkdocs.yml").write_text("site_name: test\n", encoding="utf-8")
        (repo / "tools" / "README.md").write_text("# tools\n", encoding="utf-8")
    return repo


def main() -> int:
    print("=" * 60)
    print("Step 305B - preflight repo/venv contract")
    print("=" * 60)

    checks: list[bool] = []
    work = TMP_BASE / f"step305b_{uuid.uuid4().hex}"
    work.mkdir(parents=True, exist_ok=True)

    try:
        valid_repo = _make_repo(work, "quelonio-pages-v2", with_markers=True)
        subdir = valid_repo / "docs" / "sub"
        subdir.mkdir(parents=True, exist_ok=True)

        ok_code, ok_out, ok_err = _run(["--no-require-venv", "--json"], cwd=subdir)
        try:
            ok_payload = json.loads(ok_out)
        except Exception:
            ok_payload = {}

        checks.append(_check("valid_repo_exit_zero", ok_code == 0, f"exit_code={ok_code}"))
        checks.append(_check("valid_repo_no_stderr", ok_err.strip() == "", f"stderr_len={len(ok_err.strip())}"))
        checks.append(_check("valid_repo_json_parseable", isinstance(ok_payload, dict), f"type={type(ok_payload).__name__}"))
        checks.append(_check("valid_repo_ok_true", bool(ok_payload.get("ok")) is True, f"ok={ok_payload.get('ok')}"))
        checks.append(
            _check(
                "valid_repo_has_fields",
                all(k in ok_payload for k in ("ok", "repo_root", "checks")),
                f"keys={sorted(ok_payload.keys()) if isinstance(ok_payload, dict) else []}",
            )
        )
        checks.append(
            _check(
                "root_found_from_subdir",
                str(ok_payload.get("repo_root") or "").endswith("quelonio-pages-v2"),
                f"repo_root={ok_payload.get('repo_root')}",
            )
        )

        invalid_repo = _make_repo(work, "otro-repo", with_markers=False)
        bad_code, bad_out, _ = _run(["--no-require-venv", "--max-up", "0", "--json"], cwd=invalid_repo)
        try:
            bad_payload = json.loads(bad_out)
        except Exception:
            bad_payload = {}

        checks.append(_check("invalid_repo_exit_one", bad_code == 1, f"exit_code={bad_code}"))
        checks.append(_check("invalid_repo_ok_false", bool(bad_payload.get("ok")) is False, f"ok={bad_payload.get('ok')}"))

        txt_ok_code, txt_ok_out, _ = _run(["--no-require-venv"], cwd=valid_repo)
        txt_bad_code, txt_bad_out, _ = _run(["--no-require-venv", "--max-up", "0"], cwd=invalid_repo)
        checks.append(_check("text_mode_has_PASS", "[PASS]" in txt_ok_out and txt_ok_code == 0, f"exit_code={txt_ok_code}"))
        checks.append(_check("text_mode_has_FAIL", "[FAIL]" in txt_bad_out and txt_bad_code == 1, f"exit_code={txt_bad_code}"))
    finally:
        shutil.rmtree(work, ignore_errors=True)

    if all(checks):
        print("ALL TESTS PASSED!")
        print("[PASS] Step 305B")
        return 0

    print("[FAIL] Step 305B")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
