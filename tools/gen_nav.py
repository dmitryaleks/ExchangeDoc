#!/usr/bin/env python3
"""
gen_nav.py — read docs/index.yaml and rewrite the nav block in mkdocs.yml.

The contract (decisions/0001-html-generator.md §10): docs/index.yaml is the
single source of truth for sidebar order. mkdocs.yml is hand-maintained
except for the lines between the BEGIN/END GENERATED NAV sentinels — those
get rewritten by this script.

Entries in index.yaml that point to files which do not yet exist on disk
are skipped with a stderr warning. This lets the build succeed during
phases where the docs tree is intentionally partial; missing files re-enter
the nav automatically as soon as they are written.
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
DOCS = ROOT / "docs"
INDEX = DOCS / "index.yaml"
MKDOCS_YML = ROOT / "mkdocs.yml"

BEGIN = "# === BEGIN GENERATED NAV ==="
END = "# === END GENERATED NAV ==="


def _build_nav(data: dict) -> tuple[list, list[str]]:
    """Return (nav, warnings). nav is a list-of-mappings ready for YAML dump."""
    nav: list = []
    warnings: list[str] = []

    sections = data.get("sections", []) or []
    for section in sections:
        title = section.get("title") or section.get("id") or "Untitled"
        entries = section.get("entries", []) or []

        section_items: list = []
        for entry in entries:
            file_rel = entry.get("file")
            entry_title = entry.get("title") or file_rel or "Untitled entry"
            if not file_rel:
                warnings.append(f"section {title!r}: entry missing 'file': {entry!r}")
                continue
            if not (DOCS / file_rel).is_file():
                warnings.append(
                    f"skipping (file not found): {file_rel} — {entry_title!r}"
                )
                continue
            section_items.append({entry_title: file_rel})

        if section_items:
            nav.append({title: section_items})

    return nav, warnings


def _render_block(nav: list) -> str:
    """Render the generated nav block (sentinels + nav: YAML)."""
    body = yaml.safe_dump(
        {"nav": nav}, sort_keys=False, allow_unicode=True, default_flow_style=False
    )
    return f"{BEGIN}\n{body.rstrip()}\n{END}\n"


def _splice(text: str, replacement: str) -> str:
    """Replace the BEGIN..END block in `text` with `replacement`."""
    start = text.find(BEGIN)
    end = text.find(END)
    if start == -1 or end == -1 or end < start:
        sys.exit(
            f"gen_nav: sentinels not found in {MKDOCS_YML}.\n"
            f"  expected lines containing {BEGIN!r} and {END!r}."
        )
    end_line_end = text.find("\n", end)
    if end_line_end == -1:
        end_line_end = len(text)
    else:
        end_line_end += 1
    return text[:start] + replacement + text[end_line_end:]


def main() -> int:
    if not INDEX.exists():
        print(f"gen_nav: missing {INDEX}", file=sys.stderr)
        return 1
    if not MKDOCS_YML.exists():
        print(f"gen_nav: missing {MKDOCS_YML}", file=sys.stderr)
        return 1

    with INDEX.open(encoding="utf-8") as f:
        data = yaml.safe_load(f) or {}

    nav, warnings = _build_nav(data)

    for w in warnings:
        print(f"gen_nav: {w}", file=sys.stderr)

    block = _render_block(nav)
    original = MKDOCS_YML.read_text(encoding="utf-8")
    updated = _splice(original, block)

    if updated != original:
        MKDOCS_YML.write_text(updated, encoding="utf-8")
        print(f"gen_nav: rewrote nav block in {MKDOCS_YML.name} "
              f"({sum(len(list(s.values())[0]) for s in nav)} entries, "
              f"{len(nav)} sections, {len(warnings)} skipped).")
    else:
        print(f"gen_nav: nav block unchanged "
              f"({sum(len(list(s.values())[0]) for s in nav)} entries, "
              f"{len(nav)} sections, {len(warnings)} skipped).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
