# Exchange Analysis — Implementation Plan

This document is the working plan for building the Korean equity market microstructure
analysis (KOSPI + KOSDAQ) described in `PROJECT.md`. It defines phases, deliverables,
checkpoints, and a per-task status board.

---

## 1. Goals & Deliverables

**Primary goal:** produce a complete, accurate, and easily navigable reference of KOSPI
and KOSDAQ market microstructure rules, sufficient to inform execution-algorithm design.

**Deliverables:**

1. `docs/` — raw documentation database
   - Topic-scoped Markdown files (one per analysis area, per market where they differ)
   - `images/` — diagrams, screenshots, tables captured from sources
   - `sources/` — archived PDFs / HTML snapshots of official sources for traceability
   - `index.yaml` (or `index.json`) — assembly index: ordering, titles, file refs, market tags
2. `site/` — generated HTML documentation
   - Static site built from the raw docs
   - Light (pastel white) and dark (pastel) themes, user-toggleable
   - Navigation, search, and per-topic deep-links
3. `PROJECT_IMPLEMENTATION.md` (this file) — kept current as work progresses

**Out of scope (per `PROJECT.md`):** Nextrade, ATS / PTS, derivatives markets.

---

## 2. Status Legend

Use these markers in the status board (Section 8) and inline checkpoints:

- `[ ]` — not started
- `[~]` — in progress
- `[x]` — complete
- `[!]` — blocked / needs decision (note the blocker)
- `[-]` — deferred / descoped (note why)

Each task line ends with a `— status: <marker>` so the file is greppable and easy to update.

---

## 3. Phase Overview

| Phase | Title                                        | Output                                  |
|-------|----------------------------------------------|------------------------------------------|
| 0     | Project setup & conventions                  | repo skeleton, index schema, style guide |
| 1     | Source discovery & inventory                 | `sources/INVENTORY.md` + archived sources|
| 2     | Topic research — KOSPI                       | one Markdown file per topic              |
| 3     | Topic research — KOSDAQ (delta + full)       | KOSDAQ Markdown files                    |
| 4     | Cross-market comparison                      | `comparison.md`                          |
| 5     | HTML site generator                          | `site/` build pipeline + themes          |
| 6     | QA, cross-check, and freeze v1               | reviewed v1.0 docs + site                |

Phases 2 and 3 may run partially in parallel per topic once the source inventory is solid.

---

## 4. Phase Details

### Phase 0 — Project setup & conventions

**Objective:** lock in the repo layout, file-naming rules, the index schema, and a small
Markdown style guide so later phases don't churn on cosmetics.

Tasks:

- 0.1 Create folder layout: `docs/kospi/`, `docs/kosdaq/`, `docs/common/`, `docs/images/`, `docs/sources/` — status: [x]
- 0.2 Decide index format (`yaml` vs `json`) and write schema: ordered sections, per-entry `title`, `file`, `markets[]`, `tags[]`, `last_reviewed` — status: [x] *(chose YAML for inline comments + diff-friendliness; schema documented in `docs/index.yaml` header and seeded with placeholder entries for every topic in Phase 2/3)*
- 0.3 Write `docs/STYLE.md` covering: heading levels, citation style (link + archived-source ref), table conventions, units (KRW, bps, %), and how to mark KOSPI-only vs KOSDAQ-only callouts — status: [x]
- 0.4 Add a `Makefile` or `tasks.py` entry-point stub for `build`, `lint`, and `serve` — status: [x] *(`tasks.py` chosen over Makefile for Windows-friendliness; tasks: install, gen-nav, build, serve, lint, clean. `tools/gen_nav.py` is a stub until 5.1; `requirements.txt` pins major versions.)*
- 0.5 Decide HTML generator approach (e.g. MkDocs Material, Docusaurus, Astro Starlight, or a small custom Python/Node script) and record the choice with rationale — status: [x] *(MkDocs Material, pinned major, built-in search, no interactive embeds — decision recorded in `decisions/0001-html-generator.md`)*

**Checkpoint 0:** repo skeleton committed; `index.yaml` parses; `STYLE.md` agreed; generator
choice documented. — status: [x]

---

### Phase 1 — Source discovery & inventory

**Objective:** assemble the authoritative source list before writing any topic prose, so
every later claim has a citation.

Tasks:

- 1.1 Crawl the two KRX entry points from `PROJECT.md` and list every linked sub-page relevant to the in-scope topics — status: [x] *(both entry points are tabbed containers; full tour structure is 5 sections × N tabs per market — see INVENTORY.md)*
- 1.2 Identify and record official rulebooks / member regulations (KRX Business Regulation, KOSDAQ Business Regulation, Enforcement Rules) — status: [~] *(3 of 4 archived from `rule.krx.co.kr` (KRX Legal Portal): KOSPI BR (210200859, 132 articles), KOSPI BR Enforcement Rule (210203562, 151 articles), KOSDAQ BR (210164370, 72 articles), all effective late Apr 2026, all Korean authoritative. **KOSDAQ BR Enforcement Rule bookid not yet located** — see R6.)*
- 1.3 Identify supplementary official sources: FSC / FSS notices on short selling, KRX press releases on VI/CB threshold changes — status: [ ]
- 1.4 Archive each source: PDF/HTML into `docs/sources/` with a stable filename and a row in `INVENTORY.md` (URL, fetch date, language, version/effective date) — status: [~] *(62 sources archived: 59 tour pages + 3 authoritative Korean rulebooks; FSC/FSS notices for short selling + KOSDAQ Enforcement Rule still pending)*
- 1.5 Flag English vs Korean originals; note where Korean is authoritative and English is only a translation — status: [~] *(3 Korean rulebooks tagged `language: ko`, `authoritative: true`; 59 English tour pages tagged `authoritative: false`. Per-source `parent:` linking will engage if/when an English translation of a Korean original is added.)*

**Checkpoint 1:** `docs/sources/INVENTORY.md` covers every in-scope topic with at least one
primary source per topic per market. — status: [~] *(8 of 9 primary topics covered for both markets via tour pages; **amendments** has zero coverage in the tour and must be sourced from rulebooks before Checkpoint 1 can close)*

---

### Phase 2 — Topic research, KOSPI

**Objective:** one focused Markdown file per topic for the KOSPI market. Each file follows
the same template (see 0.3) so the site builder can render them uniformly.

Per-topic template:
1. Summary (3–5 bullet points an algo developer needs to know)
2. Detailed rules
3. Numeric parameters / thresholds (in tables)
4. Worked examples or diagrams where helpful
5. Edge cases & open questions
6. Sources (link + archived ref)
7. `last_reviewed: YYYY-MM-DD`

Topic tasks (KOSPI):

- 2.1 `market_hours.md` — regular session, pre/post sessions, holidays, half-days — status: [x] *(template-validation pass; cites BR §4/5/10/33 + Enforcement Rule §8/11; lint clean. Pymarkdown config added at `.pymarkdown.json` to allow frontmatter and disable hard line-length cap.)*
- 2.2 `auctions.md` — opening, closing, and any intraday call auctions; matching rules; random-end mechanics — status: [x] *(222 lines; cites BR §22/23/24/37 + Enforcement Rule §34/35/67-2; covers single-price vs continuous, 5 single-price events, random-end, 동시호가 quantity-allocation, A-Blox; 3 worked examples including the KRW 20,150 upper-limit allocation; 5 edge cases / open questions flagged; lint clean)*
- 2.3 `price_ranges.md` — daily price limits, base price determination, tick sizes by price band — status: [x] *(236 lines; cites BR §20/21/22.2.1/37.1 + Enforcement Rule §30/31/32/33; covers ±30 % default band, leveraged ETF/ETN scaling, day-1 +300 %/-60 % newly-listed band, liquidation-issue carve-out, 7-band tick schedule, 1-share / 10-cert ELW lot exception, base-price special cases (split, ex-div, opening-price-base method, transfers from KOSDAQ); 3 worked examples including limit-at-limit vs market-order priority equivalence with execution-price divergence; 6 edge cases / open questions flagged; lint clean)*
- 2.4 `order_types.md` — limit, market, conditional, IOC/FOK, MOO/MOC, and any KRX-specific types; per-session eligibility — status: [ ]
- 2.5 `trading_rules.md` — order priority, matching algorithm, self-match prevention, lot sizes — status: [ ]
- 2.6 `volatility_interruption.md` — static VI, dynamic VI, trigger thresholds, cool-off duration, resumption auction — status: [ ]
- 2.7 `circuit_breakers.md` — index-level CB tiers, trigger conditions, halt durations, side-wide vs symbol — status: [ ]
- 2.8 `amendments.md` — price-amend and quantity-amend semantics, priority impact, partial-fill handling — status: [ ]
- 2.9 `short_selling.md` — eligibility (covered vs naked), uptick / price rules, designated lists, reporting — status: [ ]
- 2.10 `other_topics.md` — sweep of additional areas surfaced during Phase 1 (e.g. block trades, after-hours single price, error trade rules) — status: [ ]

**Checkpoint 2:** all KOSPI topic files exist, conform to the template, cite at least one
primary source each, and have a non-empty Summary section. — status: [ ]

---

### Phase 3 — Topic research, KOSDAQ

**Objective:** mirror Phase 2 for KOSDAQ. For topics where rules are identical to KOSPI, a
short file pointing to the shared `docs/common/` write-up + a "KOSDAQ-specific notes"
section is acceptable; for topics with material differences, write a full file.

Tasks (one per Phase 2 topic, in the same order):

- 3.1 KOSDAQ `market_hours.md` (delta or full) — status: [ ]
- 3.2 KOSDAQ `auctions.md` — status: [ ]
- 3.3 KOSDAQ `price_ranges.md` — status: [ ]
- 3.4 KOSDAQ `order_types.md` — status: [ ]
- 3.5 KOSDAQ `trading_rules.md` — status: [ ]
- 3.6 KOSDAQ `volatility_interruption.md` — status: [ ]
- 3.7 KOSDAQ `circuit_breakers.md` — status: [ ]
- 3.8 KOSDAQ `amendments.md` — status: [ ]
- 3.9 KOSDAQ `short_selling.md` — status: [ ]
- 3.10 KOSDAQ `other_topics.md` — status: [ ]

**Checkpoint 3:** every KOSPI topic has a corresponding KOSDAQ entry (delta or full); index
file is updated with `markets:` tags. — status: [ ]

---

### Phase 4 — Cross-market comparison

**Objective:** a single page that contrasts KOSPI and KOSDAQ side-by-side, optimised for
quick lookup by an algo developer.

Tasks:

- 4.1 Build a comparison table per topic (one row per parameter, columns: KOSPI / KOSDAQ / notes) — status: [ ]
- 4.2 Highlight rules that diverge in ways that affect execution algos (price-limit %, VI thresholds, CB tiers, short-sale eligibility lists) — status: [ ]
- 4.3 Add a short "implications for execution" paragraph per divergence — status: [ ]

**Checkpoint 4:** `comparison.md` reviewed and linked from the index. — status: [ ]

---

### Phase 5 — HTML site generator

**Objective:** turn the raw Markdown + index + images into a navigable, themed static site.

Tasks:

- 5.1 Scaffold the chosen generator (decision from 0.5) and wire it to read `index.yaml` for sidebar order — status: [ ]
- 5.2 Implement two themes: pastel-white (default light) and pastel-dark; expose a toggle in the header that persists via `localStorage` — status: [ ]
- 5.3 Configure search across all topics — status: [ ]
- 5.4 Render Markdown tables, code blocks, and images correctly; verify image paths resolve from `docs/images/` — status: [ ]
- 5.5 Add per-page metadata header: market badge (KOSPI / KOSDAQ / both), `last_reviewed` date, source links — status: [ ]
- 5.6 Produce a `make build` / `make serve` workflow; verify the built site is fully static (no server runtime) — status: [ ]
- 5.7 Visual QA pass on both themes across topic pages, comparison page, and the landing page — status: [ ]

**Checkpoint 5:** `make build` produces a working `site/` directory; both themes verified in
a browser; navigation and search work end-to-end. — status: [ ]

---

### Phase 6 — QA, cross-check, and freeze v1

**Objective:** every claim is sourced; every page is reviewed; the v1.0 tag is cut.

Tasks:

- 6.1 Citation audit: every numeric threshold and every "must / shall / may not" statement has an inline source ref — status: [ ]
- 6.2 Freshness audit: every page has `last_reviewed` within the last 30 days at freeze time — status: [ ]
- 6.3 Cross-link audit: each topic links to its KOSDAQ/KOSPI counterpart and to the comparison page — status: [ ]
- 6.4 Spot-check 3 random claims per topic against the archived source — status: [ ]
- 6.5 Build the site clean from scratch, verify no broken links — status: [ ]
- 6.6 Tag `v1.0` and write a short `CHANGELOG.md` entry — status: [ ]

**Checkpoint 6:** v1.0 frozen; site reproducible from a clean checkout. — status: [ ]

---

## 5. Checkpoint Summary

A compact view of the gate checkpoints — update these in lockstep with the phase tasks:

- Checkpoint 0 — repo skeleton + conventions agreed — status: [x]
- Checkpoint 1 — source inventory complete — status: [~]
- Checkpoint 2 — KOSPI topic files complete — status: [ ]
- Checkpoint 3 — KOSDAQ topic files complete — status: [ ]
- Checkpoint 4 — comparison page complete — status: [ ]
- Checkpoint 5 — HTML site builds with both themes — status: [ ]
- Checkpoint 6 — v1.0 frozen — status: [ ]

---

## 6. Risks & Open Questions

Track here so they don't get lost between phases:

- R1 — Korean-only rulebooks: machine translation may introduce subtle errors on legal
  language. *Mitigation:* archive the Korean original alongside the translation; flag any
  passage where the translation is load-bearing for a numeric threshold. — status: [ ]
- R2 — Rule changes mid-project: KRX periodically updates VI bands, CB tiers, and
  short-sale rules. *Mitigation:* `last_reviewed` field + a Phase 6 freshness audit. — status: [ ]
- R3 — Generator choice (0.5) affects 5.x effort substantially; defer 5.x scaffolding until
  0.5 is decided. — status: [ ]
- R4 — Scope creep into ATS/PTS/Nextrade: explicitly out of scope per `PROJECT.md`; if a
  source page mixes them in, extract only the KOSPI/KOSDAQ-relevant content. — status: [ ]
- R5 — **Amendments topic has no source coverage** in the KRX English tour (Phase 1.1
  surveyed all 59 tour fragments across both markets and found zero hits). *Mitigation:*
  must be sourced from KRX Business Regulation / Enforcement Rule articles during 1.2,
  before Checkpoint 1 can close. If those don't cover it explicitly either, escalate to
  KRX directly (`kospimkt.global@krx.co.kr` / `kosdaqmkt.global@krx.co.kr`). — status: [x] *(resolved 2026-04-30: KOSPI BR Enforcement Rule has 71 hits on "정정" (amend) including 정정방법, 정정범위, 정정신고; KOSPI BR has 26, KOSDAQ BR has 10. Topic prose for amendments will draw from the Korean rulebooks when Phase 2/3 starts.)*
- R6 — **KOSDAQ Business Regulation Enforcement Rule (코스닥시장 업무규정 시행세칙) bookid
  not yet located** on the KRX Legal Portal. The portal's recent-revisions list shows the
  3 we have but not this one; the search.do endpoint requires POST and the regulationMain.do
  endpoint requires session-cookie navigation that didn't yield it in the time-boxed hunt.
  *Mitigation:* try POSTing to `/web/search.do` with a properly-formed CSRF, browse the
  regulationMain.do tree manually with a real browser, or escalate via
  `kosdaqmkt.global@krx.co.kr`. *Impact if unresolved:* KOSDAQ-side amendment / VI / CB
  numeric thresholds will need to be inferred from the KOSDAQ Business Regulation alone
  (which has 72 articles, less detailed than KOSPI's 132+151 combined). — status: [ ]

---

## 7. Working Conventions

- Update this file as the single source of truth for status. Don't track status in commit
  messages or external trackers.
- When a task moves to `[~]` or `[x]`, update the matching Checkpoint line if the gate
  condition is now satisfied.
- New tasks discovered mid-flight: add them to the relevant phase with a stable ID
  (e.g. `2.11`) rather than renumbering existing ones.
- Cite, don't paraphrase from memory. If you can't find a source for a claim, it goes in
  "Edge cases & open questions" until sourced.

---

## 8. Status Board (compact)

Quick overview to scan without reading the whole file. Mirror status updates here.

```
Phase 0 — setup                    [x] [x] [x] [x] [x]
Phase 1 — sources                  [x] [~] [ ] [~] [~]
Phase 2 — KOSPI topics             [x] [x] [x] [ ] [ ] [ ] [ ] [ ] [ ] [ ]
Phase 3 — KOSDAQ topics            [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ]
Phase 4 — comparison               [ ] [ ] [ ]
Phase 5 — HTML site                [ ] [ ] [ ] [ ] [ ] [ ] [ ]
Phase 6 — QA & freeze              [ ] [ ] [ ] [ ] [ ] [ ]

Checkpoints:                       0[x] 1[~] 2[ ] 3[ ] 4[ ] 5[ ] 6[ ]
```
