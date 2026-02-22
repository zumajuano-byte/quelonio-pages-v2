#!/usr/bin/env python3
"""Preflight guardrail for quelonio-pages-v2 repo root and local venv."""

from __future__ import annotations

import argparse
import json
import platform
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional, Sequence, Tuple

DEFAULT_REPO_NAME = "quelonio-pages-v2"
DEFAULT_MARKERS = (
    "mkdocs.yml",
    "docs",
    "tools/README.md",
)


def _norm(path: Path) -> str:
    try:
        return str(path.resolve())
    except Exception:
        return str(path)


def find_repo_root(start_dir: Path, repo_name: str, markers: Sequence[str], max_up: int) -> Optional[Path]:
    current = start_dir.resolve()
    for _ in range(max_up + 1):
        has_markers = all((current / marker).exists() for marker in markers)
        name_matches = current.name.lower() == repo_name.lower()
        if has_markers and name_matches:
            return current
        if current.parent == current:
            break
        current = current.parent
    return None


def build_checks(
    start_dir: Path,
    repo_name: str,
    markers: Sequence[str],
    require_venv: bool,
    max_up: int,
) -> Tuple[bool, Optional[Path], List[Dict[str, Any]], Dict[str, Any]]:
    checks: List[Dict[str, Any]] = []
    repo_root = find_repo_root(start_dir=start_dir, repo_name=repo_name, markers=markers, max_up=max_up)

    checks.append(
        {
            "name": "repo_root_detected",
            "ok": repo_root is not None,
            "detail": _norm(repo_root) if repo_root else "root_not_found",
        }
    )

    markers_ok = bool(repo_root and all((repo_root / marker).exists() for marker in markers))
    checks.append(
        {
            "name": "required_markers_present",
            "ok": markers_ok,
            "detail": ", ".join(markers),
        }
    )

    venv_path = (repo_root / ".venv") if repo_root is not None else None
    venv_present = bool(venv_path and venv_path.exists() and venv_path.is_dir())
    checks.append(
        {
            "name": "local_venv_present",
            "ok": (venv_present if require_venv else True),
            "detail": _norm(venv_path) if venv_path else "repo_root_unavailable",
        }
    )

    exe_path = Path(sys.executable).resolve()
    in_repo_venv = False
    if venv_path is not None:
        try:
            in_repo_venv = str(exe_path).lower().startswith(str(venv_path.resolve()).lower())
        except Exception:
            in_repo_venv = False

    checks.append(
        {
            "name": "python_interpreter_from_repo_venv",
            "ok": (in_repo_venv if require_venv else True),
            "detail": _norm(exe_path),
        }
    )

    py_ok = sys.version_info >= (3, 9)
    checks.append(
        {
            "name": "python_version_supported",
            "ok": py_ok,
            "detail": platform.python_version(),
        }
    )

    meta = {
        "cwd": _norm(start_dir),
        "repo_name": repo_name,
        "max_up": max_up,
        "require_venv": require_venv,
        "python_executable": _norm(exe_path),
        "python_version": platform.python_version(),
    }

    ok = all(bool(item.get("ok")) for item in checks)
    return ok, repo_root, checks, meta


def parse_args(argv: Optional[Sequence[str]] = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Preflight repo/venv checks for quelonio-pages-v2")
    parser.add_argument("--repo-name", default=DEFAULT_REPO_NAME)
    parser.add_argument("--no-require-venv", action="store_true")
    parser.add_argument("--max-up", type=int, default=5)
    parser.add_argument("--json", action="store_true")
    return parser.parse_args(argv)


def _print_text(ok: bool, repo_root: Optional[Path], checks: Sequence[Dict[str, Any]], meta: Dict[str, Any]) -> None:
    print("=" * 60)
    print("Preflight Repo/Venv - quelonio-pages-v2")
    print("=" * 60)
    print(f"[INFO] cwd={meta['cwd']}")
    print(f"[INFO] repo_root={_norm(repo_root) if repo_root else 'NOT_FOUND'}")
    print(f"[INFO] python={meta['python_executable']}")
    print(f"[INFO] python_version={meta['python_version']}")
    print(f"[INFO] require_venv={meta['require_venv']}")
    for check in checks:
        status = "PASS" if check.get("ok") else "FAIL"
        print(f"[{status}] {check.get('name')} ({check.get('detail')})")
    print("[PASS] preflight_repo" if ok else "[FAIL] preflight_repo")


def main(argv: Optional[Sequence[str]] = None) -> int:
    args = parse_args(argv)
    max_up = max(0, int(args.max_up))
    ok, repo_root, checks, meta = build_checks(
        start_dir=Path.cwd(),
        repo_name=str(args.repo_name),
        markers=DEFAULT_MARKERS,
        require_venv=not bool(args.no_require_venv),
        max_up=max_up,
    )

    payload: Dict[str, Any] = {
        "schema_version": "preflight.repo.v1",
        "ok": ok,
        "repo_root": _norm(repo_root) if repo_root else None,
        "checks": checks,
        "meta": meta,
    }

    if args.json:
        print(json.dumps(payload, ensure_ascii=True, indent=2))
    else:
        _print_text(ok=ok, repo_root=repo_root, checks=checks, meta=meta)

    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
