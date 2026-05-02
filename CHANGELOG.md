# Changelog

All notable changes to this project documented per release. Date format `YYYY-MM-DD`.

## v1.0 — 2026-05-02

First reviewable drop of the KOSPI + KOSDAQ microstructure reference.

### Documentation

**KOSPI topic chain** — 10 full files under `docs/kospi/`:

- `market_hours.md`, `auctions.md`, `price_ranges.md`, `order_types.md`, `trading_rules.md`, `volatility_interruption.md`, `circuit_breakers.md`, `amendments.md`, `short_selling.md`, `other_topics.md`. Each cites the Korean-authoritative KOSPI Business Regulation (bookid 210200859) and KOSPI BR Enforcement Rule (bookid 210203562) effective 2026-04-28, plus the relevant KRX overview tour pages.

**KOSDAQ topic chain** — 10 delta-style files under `docs/kosdaq/`:

- Substantively follow the KOSPI write-ups; each records the KOSDAQ-side citations (KOSDAQ Business Regulation bookid 210164370) plus the per-topic deltas. Material divergences surfaced and documented per-topic:
  - **Sidecar** dual-condition trigger (KOSDAQ 150 futures ≥ 6 % AND KOSDAQ 150 index ≥ 3 % for 1 min) vs KOSPI's single-condition 5 % trigger.
  - **A-Blox** at KRW 200M / 1-share lot vs KOSPI KRW 500M / 100-share lot.
  - **KOSDAQ-only 1 % rule** — quotations exceeding 1 % of listed shares rejected unless block-trading.
  - **LP duty trigger** at 2 % spread on KOSDAQ vs 3 % on KOSPI; 3-consecutive-lowest-rating suspension in §12-2.2.3.가 vs KOSPI tour's 2-consecutive.
  - **Off-hours block / basket** minimums KRW 50M / KRW 200M + 5 items vs KOSPI KRW 100M.
  - **Program-trading non-arbitrage threshold** at ≥ 10 KOSDAQ Index constituents vs ≥ 15 KOSPI 200 issues.
  - **Trade-type categories** T+0 + T+2 only on KOSDAQ (no T+1).
  - **KOSDAQ-only price-disparity cooling-off** for preferred / new / SIC stocks: 3-trading-day halt at ≥ 200 % base-price divergence with 20 %-rise continuation cycle.
  - **Mass-erroneous-trade relief** narrower security scope on KOSDAQ §27-2 (excludes ETF / ETN / ELW) vs KOSPI §28-2.
  - **CB linked-derivatives** halt scope: KOSDAQ 150 index futures + single-stock futures (KOSDAQ) vs KOSPI 200/100/50 futures + options (KOSPI).

**Cross-market comparison** — `docs/common/comparison.md`:

- 17-row top-level "what is materially different" table.
- 10 per-topic parameter tables with KOSPI / KOSDAQ / notes columns and "Implications for execution" paragraphs.
- 7 cross-cutting patterns documented: KOSDAQ co-locates rules, BR article-number swap registry, identical numeric thresholds, 2026-03-04 corporate-growth-investment-fund additions (KOSDAQ-only), 2025-02-05 midpoint + stop-limit lockstep, 2022-12-07 disconnect-cancel lockstep, 2015-11-04 mass-erroneous-trade lockstep.

**Site introduction** — `docs/common/introduction.md`:

- Reading-paths guide, scope statement, citation conventions, R6-status notice.

**KOSPI other_topics.md correction** — added the previously-omitted §28-2 mass-erroneous-trade-relief mechanism. Surfaced and documented across both markets when the KOSDAQ-side §27-2 was extracted.

### Site (HTML) generator

- **MkDocs Material** scaffold with hand-written `mkdocs.yml` + sentinel-bracketed generated nav block.
- `tools/gen_nav.py` reads `docs/index.yaml` and rewrites the nav block; entries pointing to non-existent files are skipped with a stderr warning. Final v1.0 nav: 22 entries across 6 sections (Overview / Sessions & Auctions / Prices & Orders / Volatility Safeguards / Short Selling / Other Topics), 0 skipped.
- **Pastel-light** and **pastel-dark** palettes implemented in `docs/_extra.css` via Material's CSS-variable override pattern: warm-cream + dusty-blue + soft-rose accent (light); deep-cool-slate + desaturated-teal + lavender accent (dark). Both palettes include palette-aware market badge styling.
- **Per-page metadata banner** via `mkdocs_hooks.py` `on_page_markdown` hook: market badge (KOSPI / KOSDAQ / Both pill), `last_reviewed` date, source-inventory IDs as inline `<code>` chips. Banner surfaces on every page that carries a `markets:` frontmatter key.
- Built site is fully static — `python tasks.py build` → `site/` directory + `search_index.json` + assets, no runtime needed.

### Sources

- 62 sources in `docs/sources/INVENTORY.md`: 3 Korean-authoritative rulebooks (KOSPI BR + KOSPI BR Enforcement Rule + KOSDAQ BR) + 59 KRX overview tour pages.
- **R6 unresolved**: KOSDAQ Business Regulation Enforcement Rule (코스닥시장 업무규정 시행세칙) was not located on the KRX Legal Portal during Phase 1. KOSDAQ-side parameter values flagged with R6 are sourced from KRX overview tour pages and are believed to mirror the corresponding KOSPI Enforcement Rule articles, pending the KOSDAQ Enforcement Rule archive. Affects citation depth on every KOSDAQ topic; bounded by the strict-vs-tour-source labelling throughout.

### Tooling

- `tasks.py` entry-point with `install`, `gen-nav`, `gen-inventory`, `build`, `serve`, `lint`, `clean` targets.
- `tools/gen_nav.py` — index-driven nav rewriter.
- `tools/gen_inventory.py` — `sources.yaml` → `INVENTORY.md` rewriter.
- `mkdocs_hooks.py` — per-page metadata banner.
- Markdown lint via `pymarkdown` with `.pymarkdown.json` config (frontmatter-tolerant; line-length cap relaxed for long parameter tables).

### Decisions

- `decisions/0001-html-generator.md` — chose MkDocs Material for the static-site generator (single binary dependency, built-in search, no JS interactive embeds required).

### Quality gates passed

- All 22 content files (10 KOSPI topic + 10 KOSDAQ delta + comparison + introduction) carry `last_reviewed` within 30 days at v1.0 freeze (2026-04-30 to 2026-05-02).
- `python tasks.py lint` clean.
- `python tasks.py clean && python tasks.py build` produces `site/` in <1s with **zero anchor-mismatch warnings**.
- Cross-link audit (Phase 6.3): 19 broken anchor slugs fixed in a bulk pass after building the site once and inspecting MkDocs's actual heading slug output.
- Every KOSPI topic file has a "See also" link to its KOSDAQ counterpart and to `comparison.md`; every KOSDAQ delta file links back to its KOSPI counterpart and to comparison.

### Known gaps deferred past v1.0

- **R6** — KOSDAQ Enforcement Rule still not archived. Most affects: amendments (no general cancel-and-correct BR article on KOSDAQ; entirely delegated to ER), short-selling per-quotation pre-quote-check articles, VI per-rate-bucket tour-only sourcing, CB +1 %-from-prior-phase carve-out wording.
- **Visual QA** (5.7) — pastel-light + pastel-dark palettes and the metadata banner verified at the HTML-output level; in-browser walk-through of both themes pending interactive review.
- **Citation completeness** (6.1) — automated density check (citation count + article-reference count per page) passed; full per-numeric-threshold and per-must/shall-statement verification against archived source remains a deeper review pass.
- **Spot-check** (6.4) — 3 random claims per topic against archived source has not been executed; recommended as a final pass before the v1.0 tag is published externally.

### Repository state

- Branch: `main`.
- This commit captures: 20 topic Markdown files, 1 comparison page, 1 introduction page, MkDocs configuration + hooks + theme overrides, 19 anchor-link fixes, and the per-task notes in `PROJECT_IMPLEMENTATION.md` documenting the closure of Phases 3 + 4 (full) and 5 + 6 (mostly).
- Status board after this commit:
  ```
  Phase 0 — setup                    [x] [x] [x] [x] [x]
  Phase 1 — sources                  [x] [~] [ ] [~] [~]
  Phase 2 — KOSPI topics             [x] [x] [x] [x] [x] [x] [x] [x] [x] [x]
  Phase 3 — KOSDAQ topics            [x] [x] [x] [x] [x] [x] [x] [x] [x] [x]
  Phase 4 — comparison               [x] [x] [x]
  Phase 5 — HTML site                [x] [x] [x] [x] [x] [x] [~]
  Phase 6 — QA & freeze              [~] [x] [x] [ ] [x] [ ]

  Checkpoints:                       0[x] 1[~] 2[x] 3[x] 4[x] 5[~] 6[ ]
  ```
