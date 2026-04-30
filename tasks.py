#!/usr/bin/env python3
"""
tasks.py — project entry-point dispatcher.

Usage:
    python tasks.py <task>
    python tasks.py --list

Tasks are intentionally thin wrappers around mkdocs and the helpers under
tools/. Heavy logic does not live here.
"""

from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DOCS = ROOT / "docs"
SITE = ROOT / "site"
TOOLS = ROOT / "tools"
MKDOCS_YML = ROOT / "mkdocs.yml"


def _require(*executables: str) -> None:
    missing = [e for e in executables if not shutil.which(e)]
    if missing:
        sys.exit(
            f"missing executables on PATH: {', '.join(missing)}\n"
            f"hint: run `python tasks.py install` first."
        )


def _gen_nav() -> int:
    return subprocess.call([sys.executable, str(TOOLS / "gen_nav.py")])


def task_install() -> int:
    """Install pinned Python dependencies from requirements.txt."""
    return subprocess.call(
        [sys.executable, "-m", "pip", "install", "-r", str(ROOT / "requirements.txt")]
    )


def task_gen_nav() -> int:
    """Regenerate the mkdocs.yml nav block from docs/index.yaml. (Phase 5.1)"""
    return _gen_nav()


def task_gen_inventory() -> int:
    """Regenerate docs/sources/INVENTORY.md from docs/sources/sources.yaml."""
    return subprocess.call([sys.executable, str(TOOLS / "gen_inventory.py")])


def task_build() -> int:
    """Build the static HTML site into ./site/."""
    _require("mkdocs")
    rc = _gen_nav()
    if rc != 0:
        return rc
    if not MKDOCS_YML.exists():
        sys.exit("mkdocs.yml not present yet — Phase 5.1 must complete first.")
    # NOTE: --strict is deferred to the Phase 6.5 freeze gate. While docs are
    # being written, forward-refs to not-yet-existing counterpart pages emit
    # warnings that are expected, not bugs.
    return subprocess.call(["mkdocs", "build", "--clean"])


def task_serve() -> int:
    """Run the mkdocs dev server on http://localhost:8000."""
    _require("mkdocs")
    rc = _gen_nav()
    if rc != 0:
        return rc
    if not MKDOCS_YML.exists():
        sys.exit("mkdocs.yml not present yet — Phase 5.1 must complete first.")
    return subprocess.call(["mkdocs", "serve"])


def task_lint() -> int:
    """Lint all Markdown under docs/ with pymarkdown."""
    _require("pymarkdown")
    return subprocess.call(
        ["pymarkdown", "--config", str(ROOT / ".pymarkdown.json"), "scan", str(DOCS)]
    )


def task_clean() -> int:
    """Remove the generated site/ directory."""
    if SITE.exists():
        shutil.rmtree(SITE)
        print(f"clean: removed {SITE}")
    else:
        print(f"clean: {SITE} does not exist; nothing to do")
    return 0


TASKS = {
    "install": task_install,
    "gen-nav": task_gen_nav,
    "gen-inventory": task_gen_inventory,
    "build": task_build,
    "serve": task_serve,
    "lint": task_lint,
    "clean": task_clean,
}


def _print_task_list() -> None:
    width = max(len(n) for n in TASKS)
    for name, fn in TASKS.items():
        first_line = (fn.__doc__ or "").strip().splitlines()[0] if fn.__doc__ else ""
        print(f"  {name:<{width}}  {first_line}")


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Project entry-point dispatcher.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument(
        "task",
        nargs="?",
        choices=list(TASKS.keys()),
        help="Task to run.",
    )
    parser.add_argument(
        "--list",
        action="store_true",
        help="List available tasks and exit.",
    )
    args = parser.parse_args()

    if args.list or not args.task:
        _print_task_list()
        return 0

    return TASKS[args.task]()


if __name__ == "__main__":
    sys.exit(main())
