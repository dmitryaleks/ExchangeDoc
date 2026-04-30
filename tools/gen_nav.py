#!/usr/bin/env python3
"""
gen_nav.py — read docs/index.yaml and emit the mkdocs.yml nav block.

STATUS: stub. The real implementation lands in Phase 5.1
(see PROJECT_IMPLEMENTATION.md). For now this script verifies docs/index.yaml
is parseable and reports the section/entry count, so that `tasks.py build` can
chain it without exploding before mkdocs.yml exists.
"""

from __future__ import annotations

import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    sys.exit(
        "gen_nav: pyyaml is not installed.\n"
        "hint: run `python tasks.py install` first."
    )

ROOT = Path(__file__).resolve().parent.parent
INDEX = ROOT / "docs" / "index.yaml"


def main() -> int:
    if not INDEX.exists():
        print(f"gen_nav: missing {INDEX}", file=sys.stderr)
        return 1

    with INDEX.open(encoding="utf-8") as f:
        data = yaml.safe_load(f)

    sections = data.get("sections", []) or []
    n_entries = sum(len(s.get("entries", []) or []) for s in sections)
    print(
        f"gen_nav: docs/index.yaml parses OK "
        f"({len(sections)} sections, {n_entries} entries)."
    )
    print("gen_nav: nav emission TODO — see PROJECT_IMPLEMENTATION.md §5.1.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
