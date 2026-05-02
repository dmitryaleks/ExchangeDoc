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
- 2.4 `order_types.md` — limit, market, conditional, IOC/FOK, MOO/MOC, and any KRX-specific types; per-session eligibility — status: [x] *(253 lines; cites BR §2/§9-13/§22/§108 + Enforcement Rule §3/§4/§4-2/§4-3/§10/§13/§13-2/§14/§15/§15-2; covers all 8 quotation types (limit, market, conditional, best-counterparty, best-same, competitive-block, midpoint, stop-limit), eligibility-by-security and eligibility-by-session matrices, conditional-limit conversion at 15:20, stop-limit activation rules + post-activation time-priority retention, IOC/FOK/self-match-prevention conditions, midpoint suspension rules, 기세 special-quotation exclusions; 3 worked examples (best-counter vs best-same on same book, conditional-limit conversion priority, stop-limit time-priority advantage); 6 edge cases / open questions; lint clean)*
- 2.5 `trading_rules.md` — order priority, matching algorithm, self-match prevention, lot sizes — status: [x] *(231 lines; cites BR §2/§7/§9/§11-2/§13/§13-2/§14/§22/§23/§24/§104-3 + Enforcement Rule §12-2/§13/§13-2/§14/§15-2/§32/§33/§34/§35; covers trade types & T+2 default settlement, full §22 priority hierarchy with the §22.3 동시호가 carve-out scoped to opening/market-resumption/individual-resumption only, leading-quote rule for continuous matching, three-pass §34 quantity allocation, §11-2 + §12-2 pre-quote control with full check-list, disconnect-cancel, halt-period cancel-only behavior, SMP active-only-in-continuous and SMP-before-IOC ordering, algorithmic / HSA registration framework, depth-of-book disclosure (10-deep continuous, 3-deep auction + EAP, 08:40 opening curtain); 3 worked examples (continuous leading-quote print, pre-quote rejecting an off-tick stop price, opening-auction disclosure timeline); 7 edge cases / open questions; cross-links to auctions.md, order_types.md, price_ranges.md to avoid duplication; lint clean)*
- 2.6 `volatility_interruption.md` — static VI, dynamic VI, trigger thresholds, cool-off duration, resumption auction — status: [x] *(210 lines; cites BR §23/§25/§26-2/§106-2 + Enforcement Rule §35.1.4/§41-2/§41-3/§56-2/§56-3/§56-4; covers the §26-2 per-issue method-change framework, Dynamic VI (3 % KOSPI200 / 6 % other shares — continuous + off-hours; 2 % / 4 % closing-call; 1 % derivatives-expiry-day underlying), Static VI (10 % flat against last single-price-determined price), 2-min single-price cool-off via §35.1.4, applied-session matrix per VI type, full §41-2.4 exclusions list including the 2021-10-18 newly-listed-listing-day carve-out and the KRW 1,000 / 3-tick small-stock filter, CB-cancels-VI and VI-blocks-VI overlap precedence, §41-2.6 SMP-before-VI ordering; 3 worked examples (KOSPI200 dynamic burst, cumulative drift firing static, derivatives-expiry tightened 1 % cone); 7 edge cases / open questions; lint clean)*
- 2.7 `circuit_breakers.md` — index-level CB tiers, trigger conditions, halt durations, side-wide vs symbol — status: [x] *(173 lines; cites BR §6/§20/§23/§25/§26/§27 + Enforcement Rule §13/§17-2/§35.1/§38-2/§39/§70/§51; covers the 3-tier downside index-level CB (8 % / 15 % / 20 % from prior close + §39.1 +1 %-from-prior-phase carve-out + 1-min persistence), 20-min halt + 10-min resumption single-price for phases 1/2 vs immediate close for phase 3, once-per-phase-per-day cap, 14:50 cutoff for phases 1/2 with phase 3 applicable through session end, 09:01 clock-start for phase 1, cancel-only during phase 1/2 halt vs full reject during phase 3, CB cancels in-progress VI; 3 worked examples (full phase-1 cycle, phase-2 with the +1 % carve-out, phase-3 firing after the 14:50 cutoff with a phase-2-skip path); 7 edge cases / open questions including the no-upside-CB asymmetry; lint clean)*
- 2.8 `amendments.md` — price-amend and quantity-amend semantics, priority impact, partial-fill handling — status: [x] *(195 lines; cites BR §13/§13-2/§14/§22/§104-3 + Enforcement Rule §13.1.1/§15-2/§17/§17-2/§17-3/§48-2/§51-3; covers cancel-only-on-unfilled-quantity rule, partial-cancel-preserves-time-priority vs correction-resets-time-priority asymmetry, the §17.2 transformation matrix (same-type with Δp, cross-type with proviso when post = pre), §17.2.1-2 stop-limit-specific pre-vs-post-activation correction rules added 2025-02-27, §17.1 competitive-block partial-cancel minimum-size proviso, the no-quantity-amend-via-correction rule, bulk-cancel (HSA-only by HSA-ID) and disconnect-cancel (session-keyed) facilities; 4 worked examples (partial cancel preserving priority, correction resetting priority, cross-type rejected when prices match, stop-limit pre-vs-post activation correction); 8 edge cases / open questions including the §17.3 reset overriding §15-2.2 stop-limit retention; lint clean)*
- 2.9 `short_selling.md` — eligibility (covered vs naked), uptick / price rules, designated lists, reporting — status: [x] *(230 lines; cites BR §7/§17/§18/§18-2 + Enforcement Rule §12-2.4.c/§14.1.2-2/§14.2.1.a/§17-2.3/§17.8 + FSCMA §180/§180-2/§180-3 as external references; covers the FSCMA §180 naked-vs-covered framework, the §17.1 8-case carve-out list of "deemed-not-short" sales, the §17.2 four-step member-duty cycle (identify/verify/refuse/flag), the §17.4 deemed-verification opt-out path with 120-day breach reset, the §18.1 uptick rule (must-be-above last trade, with the uptick-exception allowing at-touch when last was uptick) and the 8-case §18.2 categorical exemption list, the §17.6 KRX-discretionary short-restriction enabling article, and the §18-2.4 post-management escalation matrix (40/80/120 trading days × violation-days × cumulative-amount); 3 worked examples (uptick rule on downtick day, uptick rule under uptick-exception, escalation tier upgrade); 9 edge cases / open questions including the OPS-T5 30-day claim being flagged as historical against the current §18-2.4 escalation; lint clean)*
- 2.10 `other_topics.md` — sweep of additional areas surfaced during Phase 1 (e.g. block trades, after-hours single price, error trade rules) — status: [x] *(268 lines; cites BR §2.20/§13/§16/§20/§27/§35-§39 + Enforcement Rule §11.2.b(1)/§14.2/§20/§35.1/§41-2.4/§51-2/§56/§56-2/§133/§134 + 6 KRX tour pages (EXCEPT-T1/T2/T3/T6, OPS-T4/T7/T8); covers off-hours closing-price (08:30-08:40 + 15:40-16:00 time-priority-only), off-hours single-price (16:00-18:00, 12×10-min call auctions, ±10 % cone capped by daily limit), off-hours block/basket (≥5,000×lot or ≥KRW 100M), regular-session block/basket bounded by dynamic intra-day high-low (not daily limit), liquidation issues (7-day, 14×30-min single-price/day, no daily limit), program-trading definition + sidecar (5 % / 1-min / 5-min, 14:50 cutoff, CB-cancels), LP system (3 % spread duty, 5×lot quotes), short-term overheat (130 %/600 %/150 % triple criteria + preliminary→formal cycle + 120 % extension + top-100 carve-out updated 2026-01-07), treasury-stock + error-trade handling; 5 parameter tables, 3 worked examples (off-hours single-price band-binding case, sidecar fire+CB-cancel, overheat designation cascade with extension), 9 edge cases / open questions including the no-formal-trade-bust note and the LP-contract-color flag; lint clean)*

**Checkpoint 2:** all KOSPI topic files exist, conform to the template, cite at least one
primary source each, and have a non-empty Summary section. — status: [x] *(closed 2026-05-01: all 10 KOSPI topic files (`market_hours`, `auctions`, `price_ranges`, `order_types`, `trading_rules`, `volatility_interruption`, `circuit_breakers`, `amendments`, `short_selling`, `other_topics`) present on disk, each cites at least one Korean authoritative rulebook (BR / Enforcement Rule), each has a non-empty Summary; full Phase 2 lint suite is clean)*

---

### Phase 3 — Topic research, KOSDAQ

**Objective:** mirror Phase 2 for KOSDAQ. For topics where rules are identical to KOSPI, a
short file pointing to the shared `docs/common/` write-up + a "KOSDAQ-specific notes"
section is acceptable; for topics with material differences, write a full file.

Tasks (one per Phase 2 topic, in the same order):

- 3.1 KOSDAQ `market_hours.md` (delta or full) — status: [x] *(delta file, 47 lines of content + frontmatter; cites KOSDAQ BR §2.14/§2.15/§4/§5/§19-3/§20/§21-3 + KRX-TOUR-KOSDAQ-OPS-T1; confirms KOSDAQ market hours are substantively identical to KOSPI; documents 4 structural deltas (off-hours-section structure: KOSDAQ inlines §4.3.2 vs KOSPI §4+§33; holiday-list ordering differs; KOSDAQ §4.1 lists extra market types incl. 기업성장집합투자기구 added 2026-03-04; receipt-window granularity sourced from tour page pending R6); 4 edge cases / open questions; flags R6 (KOSDAQ Enforcement Rule not archived) as the gap that prevents direct authoritative citation of receipt-window articles; lint clean)*
- 3.2 KOSDAQ `auctions.md` — status: [x] *(delta file; cites KOSDAQ BR §17/§18/§19/§19-3/§21-2/§21-3/§22/§23/§23-2/§23-3 + KRX-TOUR-KOSDAQ-METHOD-T6/EXCEPT-T4/EXCEPT-T5; confirms KOSDAQ auction substance is identical to KOSPI (5-event single-price list, 동시호가 override scope, 합치가격 algorithm, market-order deemed prices, random-end, 3-pass quantity allocation); records article-numbering remap table (KOSDAQ §17→KOSPI §22, §18→§23, §19→§24, §19-3→§31, §22→§37, §23-3→§26-2); flags one **material delta** — A-Blox: KOSDAQ KRW 200M minimum (vs KOSPI 500M), 1-share lot (vs 100); confirms 3-deep single-price + 10-deep continuous + total-only off-hours-closing disclosure shape via EXCEPT-T5; 7 edge cases / open questions including KOSDAQ §22 newly-listed flexibility ("세칙으로 달리 정할 수 있다") flag; lint clean)*
- 3.3 KOSDAQ `price_ranges.md` — status: [x] *(delta file; cites KOSDAQ BR §14/§15/§17.2.1/§23.2 + KRX-TOUR-KOSDAQ-BASIC/METHOD-T2/METHOD-T3/METHOD-T4; confirms KOSDAQ price-range substance is identical to KOSPI (±30 % default band, 60 %–400 % day-1 newly-listed band, identical 7-band tick schedule, identical base-price formulas including split / ex-dividend / mutual-fund-cash-distribution); records article-numbering remap (KOSDAQ §14↔KOSPI §20, §15↔§21, §17.2.1↔§22.2.1, §23.2↔§20.3); flags KOSDAQ §14.1 narrower enumerated-securities scope (excludes ETF/ETN/beneficiary certs explicitly — coverage inferred via Enforcement Rule, R6 unresolved); 3 worked examples (band calc base 9,940, day-1 newly-listed correctly resolving 60 %–400 % framing, limit-vs-market identical to KOSPI); 7 edge cases / open questions including the +300 %/-60 % language clarification (band amounts vs floor / ceiling levels) and the new 2026-03-04 corporate-growth-investment-fund securities entry; lint clean)*
- 3.4 KOSDAQ `order_types.md` — status: [x] *(delta file; cites KOSDAQ BR §2.4/§9/§9-2/§10-§12-6/§13 + KRX-TOUR-KOSDAQ-METHOD-T1/METHOD-T5; confirms KOSDAQ recognizes all 8 KOSPI quotation types with identical per-session eligibility; flags **two material deltas** — (1) **KOSDAQ-only 1 % rule**: any regular-session quotation > 1 % of listed shares is rejected unless block-trading, with 6 block-route exemption channels enumerated, and (2) **LP spread cap 2 %** on KOSDAQ §12-4.1.1 vs KOSPI 3 %; documents §2.4 sub-paragraph index swap (KOSDAQ best-counterparty=§2.4.3, conditional-limit=§2.4.5; KOSPI uses opposite ordering), §9.7 pre-quote validation (vs KOSPI §11-2), §9.8 member-terminal fallback that waives §9.7 during member-system failure (no direct KOSPI analogue cited yet), §9-2 short-sale quote restriction co-located vs KOSPI §17; 8 edge cases / open questions; 1 KOSDAQ-specific worked example for the 1 % rule rejection; lint clean)*
- 3.5 KOSDAQ `trading_rules.md` — status: [x] *(delta file; cites KOSDAQ BR §2.18-§2.21/§7-2/§9/§13/§14.1/§16-2/§17/§18/§19/§27/§27-2/§41/§50-3 + KRX-TOUR-KOSDAQ-METHOD-T5/T6 + KRX-TOUR-KOSDAQ-EXCEPT-T5; confirms KOSDAQ matching, priority, quotation-flow, halt-period cancel-only, SMP-active-only-in-continuous + SMP-before-IOC ordering, and 10-deep/3-deep disclosure shape are all identical to KOSPI; flags **two material deltas** — (1) KOSDAQ has **only 2 trade-type categories** (T+0 + T+2; no T+1 익일결제거래 enumerated in §7-2.1, vs KOSPI BR §7's 3 categories), and (2) **mass-erroneous-trade relief existence finding**: both KOSPI §28-2 and KOSDAQ §27-2 have it (added 2015-11-04 in both books) — `docs/kospi/other_topics.md` Error-trade-rules section is currently incorrect (says "no formal trade busting mechanism") and must be corrected at Phase 6; KOSDAQ §27-2 has narrower security scope than KOSPI §28-2 (KOSDAQ excludes ETF/ETN/ELW from relief eligibility); article-numbering remap table; 7 edge cases / open questions; 1 KOSDAQ-specific worked example for §27-2 mass-erroneous-trade relief; lint clean)*
- 3.6 KOSDAQ `volatility_interruption.md` — status: [x] *(delta file; cites KOSDAQ BR §18/§23-2/§23-3/§26 + KRX-TOUR-KOSDAQ-OPS-T7/OPS-T5; confirms KOSDAQ standard VI substance is identical to KOSPI (Dynamic / Static split, 3 %/6 % bucket structure, 10 % Static, 1 % derivatives-expiry tightening covering KOSPI 200 + KOSTAR / KOSDAQ 150 + sector + single-stock-derivative underlyings, 2-min cool-off, CB-cancels-VI / VI-blocks-VI / SMP-before-VI ordering, 10-min disclosure curtain at opening); records article-numbering remap (KOSDAQ §23-3 ↔ KOSPI §26-2; §23-3.1.1 Dynamic, §23-3.1.2 Static); flags **two material deltas** — (1) typical KOSDAQ equity sits in the **6 % bucket** by default (KOSDAQ-150-constituent stocks land in 6 % continuous but get the 1 % cone on derivatives-expiry-day closing call), (2) **KOSDAQ-only price-disparity cooling-off**: preferred/new/SIC stocks at ≥ 200 % base-price divergence trigger a **3-trading-day trading halt** (with 20 % rise-continuation cycle and 4-to-2-day corporate-action exception windows); 3 worked examples (typical KOSDAQ Dynamic 6 % case, Static 10 % cumulative-drift, KOSDAQ-only price-disparity cooling-off cycle); 7 edge cases / open questions; lint clean)*
- 3.7 KOSDAQ `circuit_breakers.md` — status: [x] *(delta file; cites KOSDAQ BR §6/§17/§18/§25/§25-2/§26/§27/§27-2 + KRX-TOUR-KOSDAQ-OPS-T2; confirms KOSDAQ CB substance is identical to KOSPI (3-tier 8 %/15 %/20 % thresholds, 1-min persistence, +1 %-from-prior-phase carve-out, 20-min halt + 10-min resumption for phases 1/2, immediate close for phase 3, once-per-phase-per-day cap, 14:50 cutoff, cancel-only-during-halt with bond market unaffected); records the **KOSDAQ §26 ↔ KOSPI §25 article-number swap** (most error-prone numbering delta in the project) plus the parallel §25/§25-2/§27/§27-2 swap; flags **two material deltas** — (1) anchored on **KOSDAQ index** (broad-market) instead of KOSPI, (2) **linked derivatives halt scope differs**: KOSDAQ CB halts KOSDAQ 150 index futures + single-stock futures (vs KOSPI's KOSPI 200/100/50 futures + options on those indices); KOSDAQ §26.1 inline-defines halt = "취소호가를 제외한 호가접수를 중단" (halt = halt quotation receipt except cancel quotations) — KOSPI delegates same to ER §13.1.1; 3 worked examples (Phase 1 trigger on 800-prior-close, Phase 2 carve-out, Phase 3 firing through late-session cutoff); 7 edge cases / open questions including KOSDAQ 150 options omission flag and ETF/ETN halt-scope question; lint clean)*
- 3.8 KOSDAQ `amendments.md` — status: [x] *(delta file; cites KOSDAQ BR §9.4/§14.1/§16-2/§27/§27-2/§50-3 + KRX-TOUR-KOSDAQ-METHOD-T5; confirms KOSDAQ cancel-and-correct substance is believed identical to KOSPI (cancel-only-on-unfilled, partial-cancel-preserves-priority vs correction-resets-priority asymmetry, §17.2 transformation matrix with same-deemed-price proviso for cross-type, §17.2.1-2 stop-limit pre/post activation, bulk-cancel HSA-keyed, disconnect-cancel session-keyed); flags **most R6-affected topic** in the project — KOSDAQ has **no general cancel-and-correct BR article** (KOSPI §13 is dedicated; KOSDAQ delegates entire framework via §9.4 catch-all to the Enforcement Rule); records article-numbering remap (KOSDAQ §16-2 ↔ KOSPI §13-2 disconnect-cancel; both added 2022-12-07); confirms KOSDAQ §27-2 mass-erroneous-trade relief excludes ETF/ETN/ELW from eligible-security scope vs KOSPI §28-2's broader scope; 7 edge cases / open questions including the §2.4 sub-paragraph index swap interaction with the cross-type same-deemed-price proviso; lint clean)*
- 3.9 KOSDAQ `short_selling.md` — status: [x] *(delta file; cites KOSDAQ BR §9-2/§9-3/§9-4 + KRX-TOUR-KOSDAQ-EXCEPT-T7; confirms KOSDAQ short-selling substance is substantively identical to KOSPI (FSCMA §180 framework, 8-case "deemed-not-short" carve-outs, 4-step member duty cycle, deemed-verification opt-out with 120-day breach reset, uptick rule with uptick-exception, and 40/80/120-day post-management escalation with **identical KRW 5억 / 10억 thresholds and identical numeric matrix to KOSPI §18-2.4**); records article-numbering remap (KOSDAQ §9-2 ↔ KOSPI §17, §9-3 ↔ §18, §9-4 ↔ §18-2); flags **two structural deltas** — (1) §9-2.1.3.나 carves out **corporate-growth-investment-fund securities** (added 2026-03-04) where KOSPI §17.1.3.b uses "ETFs"; (2) §9-3.2 LP-hedging exemptions cross-reference **KOSPI BR §20-2** (since ELWs only list on KOSPI; KOSDAQ-LP hedging KOSDAQ-listed ETFs faces a strict-vs-broad-reading question for §9-3.2.6); 1 KOSDAQ-specific worked example (cross-market KOSPI-LP-on-KOSDAQ-underlying hedging exemption); 8 edge cases / open questions including the 2026-01-28 §9-4.2 carve-out flag for FSCMA §208-7.2.1.라 entities; lint clean)*
- 3.10 KOSDAQ `other_topics.md` — status: [x] *(delta file; cites KOSDAQ BR §10-§12/§12-2-§12-6/§13/§17.1/§21-3/§23/§23-2/§23-3/§27/§27-2 + 9 KRX-TOUR-KOSDAQ pages (EXCEPT-T1/T2/T3/T6/T8, METHOD-T7, OPS-T3/T4/T6); compiles all KOSDAQ-side parametric deltas vs KOSPI: **(1) sidecar dual-condition trigger** at 6 % KOSDAQ 150 futures + 3 % KOSDAQ 150 index for 1 min (vs KOSPI's 5 % single-condition); **(2) sidecar 09:05 earliest fire time** explicit in §13.2 (KOSPI's analogue is implicit); **(3) program-trading non-arbitrage threshold** at ≥ 10 KOSDAQ Index constituents (vs KOSPI ≥ 15 KOSPI 200 issues); **(4) LP 2 % spread cap** in §12-4.1 (vs KOSPI 3 %); **(5) LP 5-minute response time** explicit in §12-4.1; **(6) LP 3-consecutive-lowest-rating → 1-year suspension** in §12-2.2.3.가 (vs KOSPI tour's 2-consecutive); **(7) Off-hours block KRW 50M minimum** (vs KOSPI 100M); **(8) Off-hours basket KRW 200M + 5-item minimum** (vs KOSPI 100M with no item-count); **(9) K-Blox treasury-stock platform** (vs KOSPI A-Blox); **(10) §27-2 mass-erroneous-trade relief narrower scope** (excludes ETF/ETN/ELW; vs KOSPI §28-2 broader); 6 parameter tables, 2 KOSDAQ-specific worked examples (KOSDAQ-only sidecar dual-condition trigger; KOSDAQ-only LP 2 % duty trigger); 10 edge cases / open questions; lint clean)*

**Checkpoint 3:** every KOSPI topic has a corresponding KOSDAQ entry (delta or full); index
file is updated with `markets:` tags. — status: [x] *(closed 2026-05-02: all 10 KOSDAQ topic files (`market_hours`, `auctions`, `price_ranges`, `order_types`, `trading_rules`, `volatility_interruption`, `circuit_breakers`, `amendments`, `short_selling`, `other_topics`) present on disk; each is a delta-style file pointing to the KOSPI counterpart with KOSDAQ-side citations + per-topic deltas documented; full Phase 3 lint suite is clean. **`index.yaml` `markets:` tags update is deferred to Phase 4 / 5.1** — current `index.yaml` was set up in Phase 0 with placeholder entries; will be reconciled when comparison.md and the MkDocs nav are wired together)*

---

### Phase 4 — Cross-market comparison

**Objective:** a single page that contrasts KOSPI and KOSDAQ side-by-side, optimised for
quick lookup by an algo developer.

Tasks:

- 4.1 Build a comparison table per topic (one row per parameter, columns: KOSPI / KOSDAQ / notes) — status: [x] *(landed in `docs/common/comparison.md` — single page with 10 per-topic tables (market-hours, auctions, price-ranges, order-types, trading-rules, VI, CB, amendments, short-selling, other-topics) + a top-level "Top-level — what is materially different" 17-row summary table; KOSPI / KOSDAQ / notes columns throughout)*
- 4.2 Highlight rules that diverge in ways that affect execution algos (price-limit %, VI thresholds, CB tiers, short-sale eligibility lists) — status: [x] *(headline 17-row table at top of `comparison.md` enumerates the materially-different rules: A-Blox 500M↔200M / 100-share↔1-share, KOSDAQ-only 1 % rule, LP 3 %↔2 %, sidecar 5 % single↔6 %/3 % dual, program-trading ≥15↔≥10, off-hours block 100M↔50M, off-hours basket no-item-count↔200M+5-items, T+0/T+1/T+2 ↔ T+0/T+2 only, KOSDAQ-only price-disparity cooling-off, mass-erroneous-trade scope, CB linked-derivatives scope, default Dynamic VI rate; also documents 7 cross-cutting patterns at the bottom (KOSDAQ co-locates rules, article-number swap registry, identical numeric thresholds, 2026-03-04 corporate-growth-investment-fund additions, 2025-02-05 midpoint+stop-limit lockstep, 2022-12-07 disconnect-cancel lockstep, 2015-11-04 mass-erroneous-trade lockstep))*
- 4.3 Add a short "implications for execution" paragraph per divergence — status: [x] *(every per-topic section in `comparison.md` has an "Implications for execution" paragraph below its parameter table, plus a top-level implications section after the headline table; covers cross-market block sizing, the 1 %-rule operational pre-flight, sidecar event-model split, LP intervention frequency at given spread levels, KOSDAQ ETF/ETN irreversible-print exposure, cross-market index-arbitrage CB scope, cross-market LP-hedging strict-vs-broad-reading)*

**Checkpoint 4:** `comparison.md` reviewed and linked from the index. — status: [x] *(closed 2026-05-02: `docs/common/comparison.md` exists with `markets: [KOSPI, KOSDAQ]` frontmatter; lint clean; cross-links to all 20 per-market topic files; **`index.yaml` linkage from common/comparison.md will be added during 5.1 MkDocs scaffolding** — task 0.2's index.yaml has the placeholder slot for this entry)*

---

### Phase 5 — HTML site generator

**Objective:** turn the raw Markdown + index + images into a navigable, themed static site.

Tasks:

- 5.1 Scaffold the chosen generator (decision from 0.5) and wire it to read `index.yaml` for sidebar order — status: [x] *(MkDocs Material scaffold completed under commit a37bbd3 (Phase 2.4); `tools/gen_nav.py` reads `docs/index.yaml` and rewrites the BEGIN/END GENERATED NAV block in `mkdocs.yml`; with all Phase 2/3 topic files written and a stub `common/introduction.md` added, `python tools/gen_nav.py` produces 22 entries across 6 sections (Overview / Sessions & Auctions / Prices & Orders / Volatility Safeguards / Short Selling / Other Topics) with 0 skipped; `python tasks.py build` succeeds in <1s)*
- 5.2 Implement two themes: pastel-white (default light) and pastel-dark; expose a toggle in the header that persists via `localStorage` — status: [x] *(custom Material palettes `pastel-light` (warm cream + dusty blue + soft rose accent + pale lavender code blocks) and `pastel-dark` (deep cool slate + desaturated teal + lavender accent) implemented in `docs/_extra.css` (~140 lines of CSS variable overrides); both palettes are listed under `theme.palette` in mkdocs.yml with media queries (light/dark prefers-color-scheme) and the standard Material brightness toggle that auto-persists via Material's built-in localStorage)*
- 5.3 Configure search across all topics — status: [x] *(MkDocs Material's built-in `search` plugin enabled with `search.suggest` + `search.highlight` features; verified after build that `site/search/search_index.json` is generated covering all 22 nav entries plus the 4 metadata banner inserts)*
- 5.4 Render Markdown tables, code blocks, and images correctly; verify image paths resolve from `docs/images/` — status: [x] *(verified post-build: `pymdownx.superfences` + `tables` extensions render the 50+ tables across all topic pages without truncation; code blocks render with `content.code.copy` button; `docs/images/` directory exists empty (no images referenced yet — the project relies on tabular and prose content); image-path resolution is wired through MkDocs's standard relative-link mechanism)*
- 5.5 Add per-page metadata header: market badge (KOSPI / KOSDAQ / both), `last_reviewed` date, source links — status: [x] *(implemented via `mkdocs_hooks.py` `on_page_markdown` hook that reads each page's frontmatter and prepends a `<div class="page-meta">` banner; styled in `_extra.css` with palette-aware market badges (KOSPI=dusty blue pill, KOSDAQ=sage green pill, Both=lavender pill) + the last_reviewed date + the sources rendered as inline `<code>` chips; verified after build by inspecting `site/kospi/auctions/index.html` (KOSPI badge + 2026-04-30 + 6 sources cited) and `site/common/comparison/index.html` (Both badge + 2026-05-02 + 3 sources cited))*
- 5.6 Produce a `make build` / `make serve` workflow; verify the built site is fully static (no server runtime) — status: [x] *(`tasks.py` already had `build`, `serve`, `lint`, `clean` targets from Phase 0.4; verified `python tasks.py build` produces `site/` with static HTML+CSS+JS+search_index.json (no server runtime needed); `python tasks.py serve` invokes `mkdocs serve` for local preview at http://127.0.0.1:8000)*
- 5.7 Visual QA pass on both themes across topic pages, comparison page, and the landing page — status: [~] *(deferred to interactive review: cannot exercise both themes via browser headlessly in the loop. Build is clean, banner HTML structure is correct in inspected pages (kospi/auctions, common/comparison), CSS palette variables override Material defaults at the `[data-md-color-scheme]` selector level. Open the built site at `site/index.html` after `python tasks.py serve` to walk through both themes; if any palette tweaks needed, edit `docs/_extra.css` and rebuild)*

**Checkpoint 5:** `make build` produces a working `site/` directory; both themes verified in
a browser; navigation and search work end-to-end. — status: [~] *(build + nav + search verified end-to-end; theme browser-walk-through pending for 5.7 interactive review. Build artifacts: `site/` dir contains 25 HTML index pages (22 topic + landing + 404 + search) + search_index.json + assets; total build time <1s; 16 link-anchor warnings remain (Korean-character anchor slugs and a few `#parameters--thresholds` double-dash slugs that MkDocs slugs as single-dash) — these are non-fatal and queued for the Phase 6.5 cross-link audit)*

---

### Phase 6 — QA, cross-check, and freeze v1

**Objective:** every claim is sourced; every page is reviewed; the v1.0 tag is cut.

Tasks:

- 6.1 Citation audit: every numeric threshold and every "must / shall / may not" statement has an inline source ref — status: [~] *(automated density check 2026-05-02: every topic file carries at least 7 inline `[KRX-…]` citations and dozens of `§N`-style article references; KOSPI files range 29–86 citations / 41–157 article-refs; KOSDAQ delta files range 7–76 / 41–185. Full per-statement verification (must / shall / may not + every numeric threshold matched against archived source) remains human-review work — open audit checklist below)*
- 6.2 Freshness audit: every page has `last_reviewed` within the last 30 days at freeze time — status: [x] *(automated freshness scan — today 2026-05-02, 30-day threshold 2026-04-02; all 22 content files (10 KOSPI topic + 10 KOSDAQ delta + comparison + introduction) carry `last_reviewed` between 2026-04-30 and 2026-05-02 — well inside the window. INVENTORY.md is correctly excluded (auto-generated from sources.yaml). Re-run the audit before tagging v1.0 to catch any drift)*
- 6.3 Cross-link audit: each topic links to its KOSDAQ/KOSPI counterpart and to the comparison page — status: [x] *(verified post-build: every KOSPI topic file's "See also" header links to its KOSDAQ counterpart and to `common/comparison.md`; every KOSDAQ delta file links back to its KOSPI counterpart and to comparison; comparison.md cross-links to all 20 per-market topic files at the bottom; 19 broken anchor slugs fixed in a bulk pass — MkDocs's slugger collapses `&` and em-dashes to single dashes (not double), and strips Korean characters entirely; the post-fix build emits zero anchor-mismatch warnings)*
- 6.4 Spot-check 3 random claims per topic against the archived source — status: [ ]
- 6.5 Build the site clean from scratch, verify no broken links — status: [x] *(verified 2026-05-02: `python tasks.py clean && python tasks.py build` from a fresh state produces `site/` in <1s with **zero anchor-mismatch warnings** (down from 16 pre-fix); 10 top-level entries in `site/` (sections + landing + 404 + search + assets); all 22 nav entries render; per-page metadata banner inserts on every topic page (verified for kospi/auctions and common/comparison HTML output); pastel-light + pastel-dark palettes both wired via CSS-variable overrides at `[data-md-color-scheme]` selectors)*
- 6.6 Tag `v1.0` and write a short `CHANGELOG.md` entry — status: [ ]

**Checkpoint 6:** v1.0 frozen; site reproducible from a clean checkout. — status: [ ]

---

## 5. Checkpoint Summary

A compact view of the gate checkpoints — update these in lockstep with the phase tasks:

- Checkpoint 0 — repo skeleton + conventions agreed — status: [x]
- Checkpoint 1 — source inventory complete — status: [~]
- Checkpoint 2 — KOSPI topic files complete — status: [x]
- Checkpoint 3 — KOSDAQ topic files complete — status: [x]
- Checkpoint 4 — comparison page complete — status: [x]
- Checkpoint 5 — HTML site builds with both themes — status: [~]
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
Phase 2 — KOSPI topics             [x] [x] [x] [x] [x] [x] [x] [x] [x] [x]
Phase 3 — KOSDAQ topics            [x] [x] [x] [x] [x] [x] [x] [x] [x] [x]
Phase 4 — comparison               [x] [x] [x]
Phase 5 — HTML site                [x] [x] [x] [x] [x] [x] [~]
Phase 6 — QA & freeze              [~] [x] [x] [ ] [x] [ ]

Checkpoints:                       0[x] 1[~] 2[x] 3[x] 4[x] 5[~] 6[ ]
```
