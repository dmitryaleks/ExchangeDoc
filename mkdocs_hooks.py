"""
mkdocs_hooks.py — per-page metadata banner (Phase 5.5).

For each rendered topic page, prepends a meta banner showing:
  * a market badge (KOSPI / KOSDAQ / Both),
  * the page's `last_reviewed` date,
  * the page's `sources` IDs as inline code.

The data comes from each page's YAML frontmatter, which mkdocs surfaces as
`page.meta`. Pages without a `markets` key (e.g. README files, the auto-
generated 404) are passed through untouched.
"""

from __future__ import annotations


def _market_badge(markets: list[str] | None) -> str:
    if not markets:
        return ""
    norm = [m.upper() for m in markets]
    if "KOSPI" in norm and "KOSDAQ" in norm:
        return '<span class="market-badge both">KOSPI &amp; KOSDAQ</span>'
    if "KOSPI" in norm:
        return '<span class="market-badge kospi">KOSPI</span>'
    if "KOSDAQ" in norm:
        return '<span class="market-badge kosdaq">KOSDAQ</span>'
    return ""


def _last_reviewed(value: object) -> str:
    if value in (None, "", "null"):
        return ""
    return (
        '<span class="last-reviewed">'
        '<span class="label">Last reviewed:</span>'
        f'{value}'
        '</span>'
    )


def _sources(values: list[str] | None) -> str:
    if not values:
        return ""
    items = " ".join(f"<code>{v}</code>" for v in values)
    return (
        '<span class="sources">'
        '<span class="label">Sources:</span>'
        f'{items}'
        '</span>'
    )


def on_page_markdown(markdown: str, *, page, config, files):
    """Inject a metadata banner above the page body if frontmatter is present."""
    meta = page.meta or {}
    markets = meta.get("markets")
    if not markets:
        return markdown

    badge = _market_badge(markets if isinstance(markets, list) else [markets])
    reviewed = _last_reviewed(meta.get("last_reviewed"))
    sources = _sources(meta.get("sources"))

    parts = [p for p in (badge, reviewed, sources) if p]
    if not parts:
        return markdown

    banner = (
        '<div class="page-meta" markdown="0">\n'
        + "\n".join(parts)
        + "\n</div>\n\n"
    )
    return banner + markdown
