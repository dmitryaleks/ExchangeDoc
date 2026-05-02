---
title: "KOSPI vs KOSDAQ Comparison"
markets: [KOSPI, KOSDAQ]
last_reviewed: 2026-05-02
sources:
  - KRX-RULE-KOSPI-BR-KO
  - KRX-RULE-KOSPI-BR-ENFORCE-KO
  - KRX-RULE-KOSDAQ-BR-KO
---

> Per-topic deep dives: see the [KOSPI](../kospi/market_hours.md) and [KOSDAQ](../kosdaq/market_hours.md) topic chains (use the sidebar to navigate the full set). This page is an execution-algo-oriented diff between the two markets.

This page contrasts KOSPI and KOSDAQ side-by-side, optimised for quick lookup by an algo developer. Each topic section has a parameter table (KOSPI / KOSDAQ / notes) followed by an **Implications for execution** paragraph per material divergence. KOSDAQ Enforcement Rule citations remain unresolved per project risk R6 — KOSDAQ-side parameter values flagged with R6 are sourced from KRX overview tour pages and are believed to mirror the corresponding KOSPI Enforcement Rule articles, pending the KOSDAQ Enforcement Rule archive.

## 0. Top-level — what is *materially* different

If you only read one section: KOSDAQ is **not** a numerically-cloned KOSPI. The list of meaningful divergences for an execution-algo design:

| # | Divergence                                                                                                | KOSPI value                            | KOSDAQ value                                  |
|---|-----------------------------------------------------------------------------------------------------------|----------------------------------------|------------------------------------------------|
| 1 | A-Blox minimum order size                                                                                 | KRW 500,000,000                        | **KRW 200,000,000**                            |
| 2 | A-Blox trading unit                                                                                       | 100 shares                             | **1 share**                                     |
| 3 | KOSDAQ-only **1 % rule** — per-quotation max quantity (regular session)                                   | (none — no parallel rule)              | **1 %** of listed shares (block-trade exempt)  |
| 4 | LP duty trigger — bid-ask spread                                                                          | 3 %                                    | **2 %**                                         |
| 5 | LP suspension — consecutive lowest-rating evaluations                                                     | 2 (per tour)                           | **3** (per BR)                                  |
| 6 | Sidecar trigger                                                                                            | KOSPI 200 futures ≥ 5 % for 1 min      | **KOSDAQ 150 futures ≥ 6 % AND KOSDAQ 150 index ≥ 3 % for 1 min** |
| 7 | Sidecar earliest fire time                                                                                | (implicit)                             | **09:05 KST** (explicit, §13.2)                |
| 8 | Program-trading non-arbitrage threshold                                                                    | ≥ 15 KOSPI 200 issues                  | **≥ 10 KOSDAQ Index constituents**             |
| 9 | Off-hours block — minimum order size                                                                      | KRW 100,000,000 (or 5,000 × lot)       | **KRW 50,000,000**                              |
| 10 | Off-hours basket — minimum order size                                                                    | KRW 100,000,000 (no item count)        | **KRW 200,000,000 + ≥ 5 items**                 |
| 11 | Trade-type categories                                                                                    | T+0, T+1, T+2                          | **T+0, T+2 only** (no T+1 enumerated)           |
| 12 | KOSDAQ-only price-disparity cooling-off for preferred / new / SIC stocks                                 | (none — KOSPI carves them out from VI but no halt) | **3-trading-day halt** at ≥ 200 % base-price divergence |
| 13 | Mass-erroneous-trade relief — eligible-security scope                                                    | Shares + DRs + ETFs + ETNs + ELWs + beneficiary certs | **Shares + DRs + corp-growth-fund only** (excludes ETF/ETN/ELW) |
| 14 | CB linked-derivatives halt scope                                                                          | KOSPI 200/100/50 futures + options     | **KOSDAQ 150 index futures + single-stock futures** |
| 15 | Default Dynamic VI rate for typical equity                                                                | 3 % (KOSPI 200) / 6 % (other)          | **6 %** (typical KOSDAQ equity is "Other")     |
| 16 | KRX-discretionary band override                                                                          | KOSPI BR §20.4 → ER §31.2.1            | KOSDAQ BR §14.3 → ER (R6)                      |
| 17 | LP framework eligible-security enumeration                                                                | Stocks + ETFs + ETNs + ELWs + low-turnover stocks | **Stocks (incl. foreign DRs) only** (BR-level) |

**Implications for execution.** The most consequential of these for a cross-market algo are:

- **Block / A-Blox sizing (1, 2, 9, 10).** A single "block-eligible" quantity threshold cannot be reused across markets. KOSDAQ has lower block thresholds (50M block, 200M A-Blox) but a stricter basket constraint (5+ items). The 1-share A-Blox lot on KOSDAQ vs the 100-share lot on KOSPI also breaks any quantity-quantization assumption shared between markets.
- **The 1 % rule (3).** A regular-session quotation > 1 % of listed shares is rejected on KOSDAQ at the member pre-quote check — there is no parallel cap on KOSPI. Per-iceberg-slice / per-VWAP-slice configuration must respect this on KOSDAQ for small-cap names. For an issue with 100M listed shares, the per-quote cap is 1M shares; an algo configured for 1.5M-share parent slices on KOSPI cannot mirror the same slice size on KOSDAQ without splitting or routing through a block channel.
- **Sidecar (6, 7).** The KOSDAQ dual-condition trigger is **stricter** (false-positive-suppressed). A futures-only spike that fires KOSPI sidecar may not fire KOSDAQ sidecar; an index-arbitrage strategy must model these as distinct events. The 09:05 earliest-fire on KOSDAQ also gives the first 5 minutes of the regular session sidecar-immunity that KOSPI's rules don't explicitly grant.
- **LP behaviour (4, 5, 17).** KOSDAQ LPs respond to **tighter spreads** (2 % vs 3 %) and face stricter long-term standing (3-consecutive vs 2-consecutive lowest rating). KOSDAQ-listed ETF / ETN LPs are not enumerated at the BR level — relying on the KOSDAQ LP framework to cover ETF / ETN passive resting-quote behaviour is shaky. Prefer the KOSPI cross-market reference structure (per KOSDAQ §9-3.2 short-selling exemptions) when reasoning about ETF / ETN LP coverage.
- **Mass-erroneous-trade relief (13).** A KOSDAQ-listed ETF / ETN fat-finger error has **no formal trade-relief mechanism**. KOSPI covers ETF / ETN errors under §28-2; KOSDAQ §27-2 does not. Risk-budgets for KOSDAQ ETF strategies must factor in irreversible-print exposure that KOSPI strategies don't share.
- **VI default rate (15).** A typical KOSDAQ-listed equity sits in the 6 % Dynamic VI bucket — Dynamic VI fires on KOSDAQ less often than on KOSPI for the same absolute price-percentage move. KOSDAQ-150-constituent stocks still get the 1 % cone on derivatives-expiry-day closing call, mirroring the KOSPI 200 treatment.

The remainder of this document expands the per-topic tables.

---

## 1. Market hours

| Parameter                                       | KOSPI                              | KOSDAQ                             | Notes                                                    |
|-------------------------------------------------|------------------------------------|------------------------------------|----------------------------------------------------------|
| Regular session                                 | 09:00–15:30 KST                   | 09:00–15:30 KST                   | Identical                                                |
| Intraday competitive-block (장중경쟁대량매매)     | 09:00–15:00 KST                   | 09:00–15:00 KST                   | Identical                                                |
| Pre-open off-hours (block / basket / competitive) | 08:00–09:00 KST                  | 08:00–09:00 KST                  | Identical                                                |
| Pre-open closing-price                          | 08:30–08:40 KST                   | 08:30–08:40 KST                   | Identical                                                |
| Post-close closing-price                        | 15:30–16:00 receipt; 15:40–16:00 trading | 15:30–16:00 receipt; 15:40–16:00 trading | Identical (10-min pre-trade buffer)                |
| Post-close single-price                         | 16:00–18:00 KST                   | 16:00–18:00 KST                   | Identical                                                |
| Post-close block / basket                       | 15:40–18:00 KST                   | 15:40–18:00 KST                   | Identical                                                |
| Holidays                                        | Saturdays + public + Workers' Day + Dec 31 + discretionary | Same 5 categories (different ordering, "연말의 1일간" framing for year-end) | Same effective behaviour |
| BR-level structure                              | §4 + §10 + §33                    | §4 inlined (no §33 for off-hours; KOSDAQ §10 = treasury stock) | Structural delta only |
| ER-level receipt-window granularity             | KOSPI ER §11                      | KOSDAQ ER (R6 unresolved)         | Authoritative gap for KOSDAQ                             |

**Implications for execution.** None — calendars and session timing are identical. The structural article-numbering offset (KOSDAQ inlines off-hours timing in §4) matters only for compliance citations.

---

## 2. Auctions

| Parameter                                       | KOSPI                              | KOSDAQ                             | Notes                                                    |
|-------------------------------------------------|------------------------------------|------------------------------------|----------------------------------------------------------|
| Auction principle article                       | §22                                | §17                                | Article-number swap                                       |
| Single-price auction article                    | §23                                | §18                                | Same 5-event list                                         |
| Continuous auction article                      | §24                                | §19                                | Identical leading-quote rule                              |
| Newly-listed first-price article                | §37                                | §22                                | KOSDAQ §22 says "세칙으로 달리 정할 수 있다" (ER may differ) — flexibility flag |
| 동시호가 carve-out scope                        | §22.3 (opening / market-resumption / individual-resumption only) | §17.3 (same 3 events) | Identical scope; closing call NOT included on either |
| 합치가격 (matching-price) algorithm             | Same                               | Same                               | Identical, including 2025-02-05 multi-matching-price tie-break amendments |
| Random-end (≤ 30 s after nominal close)         | KOSPI ER §35.1                    | KOSDAQ ER (R6) — confirmed by tour | Same behaviour                                            |
| 3-pass quantity allocation at price limits      | KOSPI ER §34                      | KOSDAQ ER (R6) — confirmed by tour | Same behaviour                                            |
| **A-Blox minimum order size**                  | **KRW 500,000,000**                | **KRW 200,000,000**                | **Material delta**                                       |
| **A-Blox trading unit**                         | **100 shares**                     | **1 share**                         | **Material delta**                                       |
| A-Blox trading window (regular)                 | 09:00–15:00 KST                   | 09:00–15:00 KST                   | Identical                                                |
| A-Blox trading window (pre-open)                | 08:00–09:00 KST                   | 08:00–09:00 KST                   | Identical                                                |
| A-Blox after-hours session                      | none                               | none                               | Identical                                                |
| Off-hours single-price disclosure shape         | 3-deep + EAP                       | 3-deep + EAP                       | Identical                                                |
| Continuous-trading disclosure shape             | 10-deep                            | 10-deep                            | Identical                                                |
| Opening-curtain delay                           | 10 minutes (08:30 → 08:40)         | 10 minutes (08:30 → 08:40)         | Identical                                                |

**Implications for execution.** The A-Blox parameter divergence is the only material difference. An execution algo running A-Blox flow across both markets must:

- Maintain **per-market block-eligibility tables** rather than a unified threshold.
- Adapt **quantity-quantization** at the block leg — KOSDAQ allows 1-share precision; KOSPI requires 100-share lots.
- Accept that a **smaller absolute notional (KRW 200M)** triggers KOSDAQ A-Blox eligibility, broadening the addressable order-size range.

The newly-listed-first-price flexibility flag in KOSDAQ §22 ("ER may differ") suggests KOSDAQ may diverge from KOSPI's uniform 60–400 % day-1 band on listing day for special cases (capital-reduction relisting, listing-change-after-spin-off). R6 confirmation needed before treating a KOSDAQ first-day band as 60–400 % unconditionally.

---

## 3. Price ranges & tick sizes

| Parameter                                       | KOSPI                              | KOSDAQ                             | Notes                                                    |
|-------------------------------------------------|------------------------------------|------------------------------------|----------------------------------------------------------|
| Daily price-limit band — default                | ±30 % of base price                | ±30 % of base price                | Identical                                                |
| Day-1 newly-listed band                         | 60 %–400 % of base                 | 60 %–400 % of base                 | Identical                                                |
| Liquidation-issue band                          | None (KRW 1 floor)                 | None (KRW 1 floor)                 | Identical (KOSDAQ §23.2 = KOSPI §20.3)                    |
| Tick-size schedule                              | 7-band (KRW 1 → KRW 1,000)         | 7-band (KRW 1 → KRW 1,000)         | Identical schedule                                        |
| ETF / ETN tick schedule                         | 2-band (KRW 1 / KRW 5)             | (R6 unresolved — believed same)    | Tour-confirmed for stocks                                |
| ELW tick                                         | KRW 5 flat                         | n/a (no ELW listings)              | KOSDAQ has no ELWs                                        |
| Trading lot                                      | 1 share / 1 cert (ELW: 10 cert)    | 1 share / 1 cert                   | KOSDAQ has no ELW exception                              |
| Price-limit-band article                        | §20 (BR-level)                     | §14 (BR-level)                     | Article-number swap                                       |
| Price-limit-band §20.1 / §14.1 enumerated securities | Shares + DRs + ETFs + ETNs + beneficiary certs | **Shares + DRs + corporate-growth-investment-fund securities** | **§14.1 narrower scope on KOSDAQ** |
| Tick / lot delegating article                   | §21 (BR-level) → ER §32 / §33      | §15 (BR-level) → ER (R6 unresolved) | Same delegation pattern                                   |
| Base-price formulas (split, ex-div, etc.)       | KOSPI ER §30                      | KOSDAQ ER (R6) — confirmed by tour | Same formulas                                            |
| KRX-discretionary band override                 | KOSPI BR §20.4 → ER §31.2.1       | KOSDAQ BR §14.3 → ER (R6)         | Same authority                                            |

**Implications for execution.** None on the rate-and-band side — band sizing and tick-size are identical. The §14.1 narrower-scope wrinkle means **KOSDAQ-listed ETF / ETN price-limit-band citations** require the KOSDAQ Enforcement Rule (R6) rather than the BR's main-article enumeration; until R6 resolves, treat KOSDAQ ETF / ETN ±30 % bands as inferred-by-tour. Phase 6 freshness audit must verify.

---

## 4. Order types & quotation conditions

| Parameter                                       | KOSPI                              | KOSDAQ                             | Notes                                                    |
|-------------------------------------------------|------------------------------------|------------------------------------|----------------------------------------------------------|
| Number of quotation types                       | 8                                  | 8                                  | Identical (limit, market, conditional, best-counter, best-same, competitive-block, midpoint, stop-limit) |
| Sub-paragraph indexing within §2.4              | conditional=§2.4.3; best-counter=§2.4.4; best-same=§2.4.5 | **conditional=§2.4.5; best-counter=§2.4.3; best-same=§2.4.4** | **Sub-paragraph index swap** |
| 2025-02-05 additions (midpoint + stop-limit)    | Yes                                | Yes                                | Identical effective date                                  |
| Per-session eligibility matrix                  | 5-type table per tour              | 5-type table per tour              | Identical (limit / market / LMC / best-counter / best-same; midpoint / stop-limit / competitive-block delegated to ER) |
| Conditional-limit conversion at closing-call open (15:20 KST) | KOSPI ER §15            | KOSDAQ ER (R6 unresolved)          | Same behaviour                                            |
| Stop-limit pre/post-activation correction rules | KOSPI ER §17.2.1-2 (added 2025-02-27) | KOSDAQ ER (R6 unresolved)         | Believed same effective date                              |
| IOC / FOK / SMP conditions                      | KOSPI ER §13.3 / §13-2             | KOSDAQ ER (R6 unresolved)          | Same behaviour                                            |
| **KOSDAQ-only "1 % rule"**                       | (none)                             | **Per-quotation max quantity = 1 % of listed shares** (block-trade exempt) | **Material divergence** |
| Pre-quote validation BR article                  | §11-2                              | §9.7                               | Article-number difference                                  |
| Member-terminal-fallback waiver                 | §17.4 (BR — not extracted)         | §9.8 (added 2015-11-04)            | Same waiver structure                                     |
| Short-sale quote restriction location           | §17 (separate article)             | §9-2 (co-located in order-types territory) | Different article placement                               |

**Implications for execution.** The 1 % rule is the headline. For KOSDAQ-listed issues:

- **Pre-flight check:** before submitting a regular-session quote, divide the requested quantity by the issue's listed-shares count; if > 1 %, route through a block channel (intraday block, off-hours block, A-Blox / competitive-block, or basket).
- **Slice sizing:** TWAP / VWAP child slices must each respect 1 % cap. For a 100M-listed-share issue, single slice ≤ 1M shares.
- **Iceberg / hidden quantities:** the 1 % cap applies to the quotation submitted, not to any iceberg's reservoir. A 1M-share submitted slice from a 5M-share iceberg pool is fine; a 2M-share single slice would not be.

The §2.4 sub-paragraph index swap is a quiet pitfall for compliance code that anchors on type-name → sub-paragraph indices; cite by type **name**, not by sub-paragraph number, when working across both markets.

---

## 5. Trading rules & matching

| Parameter                                       | KOSPI                              | KOSDAQ                             | Notes                                                    |
|-------------------------------------------------|------------------------------------|------------------------------------|----------------------------------------------------------|
| §22 / §17 priority hierarchy                     | Price > time > 동시호가 quantity   | Price > time > 동시호가 quantity   | Same hierarchy with same scope rules                      |
| **Trade-type categories**                        | T+0, T+1, T+2                      | **T+0, T+2 only** (no T+1)         | **Material structural delta**                            |
| Default settlement                              | T+2 보통거래                       | T+2 보통거래                       | Identical default                                         |
| Continuous-trading leading-quote rule           | KOSPI BR §24.3                     | KOSDAQ BR §19.3                    | Same                                                       |
| Halt-period cancel-only behaviour               | KOSPI ER §13.1.1                   | KOSDAQ §26.1 inline + ER (R6)      | Same behaviour                                            |
| Disconnect-cancel BR article                    | §13-2 (added 2022-12-07)           | §16-2 (added 2022-12-07)           | Same effective date, different article number             |
| HSA registration article                        | §104-3                             | **§50-3**                           | Article-number difference                                 |
| Mass-erroneous-trade relief — both markets      | §28-2 (added 2015-11-04)           | **§27-2 (added 2015-11-04)**       | **Both books have it — KOSPI other_topics.md has an error claiming "no formal trade busting"** |
| Mass-erroneous-trade relief eligible-security scope | Shares + DRs + ETFs + ETNs + ELWs + beneficiary certs | **Shares + DRs + corp-growth-fund only** | **KOSDAQ excludes ETF / ETN / ELW from relief eligibility** |
| Error-trade correction by KRX                   | §28                                 | §27                                 | Article-number swap                                       |
| Bulk cancel (HSA-keyed)                         | KOSPI ER §17-2 (rewritten 2022-12-22) | KOSDAQ ER (R6 unresolved)         | Believed same behaviour                                   |
| 10-deep continuous + 3-deep single-price disclosure | Yes                              | Yes                                | Identical disclosure shape                                |

**Implications for execution.**

- **Settlement-cycle exposure (trade-type categories):** algos that allocate cash buffers based on the existence of a T+1 settlement path **cannot reuse** that assumption on KOSDAQ. KOSDAQ has only T+0 and T+2 — any rule-specified T+1 KOSPI security has no parallel KOSDAQ instrument.
- **Mass-erroneous-trade relief (§28-2 / §27-2):** for an algorithmic strategy on **KOSPI ETF / ETN**, a fat-finger trade has a §28-2 relief path. The same trade on **KOSDAQ ETF / ETN** has no relief path — risk budgets must reflect this.

---

## 6. Volatility Interruption

| Parameter                                       | KOSPI                              | KOSDAQ                             | Notes                                                    |
|-------------------------------------------------|------------------------------------|------------------------------------|----------------------------------------------------------|
| VI parent article                               | §26-2 (BR)                         | §23-3 (BR)                         | Article-number swap                                       |
| Dynamic VI — KOSPI 200 / 100 / 50 / KRX 100 ETF rate | 3 % continuous / 2 % closing call / 3 % off-hours | 3 % continuous / 2 % closing call / 3 % off-hours | Same rate-table for these products |
| Dynamic VI — typical equity                      | 6 % (other shares)                 | **6 %** (other shares — incl. KOSDAQ 150 constituents) | Same rate but KOSDAQ-150-constituent stocks land here, not the 3 % bucket |
| Dynamic VI — derivatives-expiry-day closing call | 1 % for KOSPI 200 underlying        | **1 % for KOSPI 200 + KOSTAR/KOSDAQ 150 + sector-index + single-stock-derivative underlyings** | KOSDAQ tour explicitly extends to KOSDAQ 150 |
| Static VI rate                                   | 10 %                               | 10 %                               | Identical                                                 |
| Cool-off duration                                | 2 minutes                          | 2 minutes                          | Identical                                                 |
| Random-end on VI resumption                      | None                               | None                               | Identical                                                 |
| Exclusion list                                   | 10 cases (KOSPI ER §41-2.4)        | (R6 unresolved — believed same)    | Tour confirms 2 explicit cases (liquidation, overheat)    |
| **KOSDAQ-only price-disparity cooling-off**     | (none)                             | **3-trading-day halt at ≥ 200 % base-price divergence for preferred / new / SIC stocks** | **KOSDAQ-specific addition** |
| Continuation cycle                              | n/a                                | 20 % rise over 3 days re-triggers another 3-day halt | KOSDAQ-only                                               |
| Corporate-action exception window               | n/a                                | 4–2 trading days before submission deadline / base date | KOSDAQ-only                                               |

**Implications for execution.**

- **Effective rate bucket:** for a strategy that conditions on Dynamic-VI-firing probability, **KOSDAQ-listed equities are in the 6 % bucket by default** — Dynamic VI is less sensitive than KOSPI 200's 3 % cone. A typical 5 % intraday move on a KOSDAQ stock does not fire VI.
- **Derivatives-expiry-day closing-call** (1 % cone): KOSDAQ-150-constituent stocks **do** get the 1 % cone on the closing call of KOSPI-200 / KOSDAQ-150 derivatives expiry days. Algos hedging into the close on derivatives-expiry day must apply 1 % thresholds to KOSDAQ 150 constituents, not 4 % (the closing-call default).
- **Price-disparity cooling-off** is a **KOSDAQ-only multi-day halt mechanism**. Passive resting orders survive the halt but cannot fill until trading resumes. A trading-strategy holding any preferred / new / SIC KOSDAQ-listed stock at base ≥ 2× common base must factor in 3-day-halt-and-restart fill-probability.

---

## 7. Circuit Breakers

| Parameter                                       | KOSPI                              | KOSDAQ                             | Notes                                                    |
|-------------------------------------------------|------------------------------------|------------------------------------|----------------------------------------------------------|
| CB parent article                               | §25                                | **§26**                             | **Article-number swap**                                   |
| Index anchor                                    | KOSPI broad index                  | KOSDAQ broad index                  | Each market uses its own broad-market index               |
| Phase 1 trigger                                 | Index ≤ 92 % of prior close, 1-min persistence | Same | Identical                                                  |
| Phase 2 trigger                                 | Index ≤ 85 % of prior close + ≤ 99 % of phase-1 trigger value | Same | Identical                                                 |
| Phase 3 trigger                                 | Index ≤ 80 % of prior close + ≤ 99 % of phase-2 trigger value | Same | Identical                                                 |
| Phase 1 / 2 action                              | 20-min halt + 10-min single-price resumption | Same | Identical                                                 |
| Phase 3 action                                  | Immediate close for the day         | Same                                | Identical                                                  |
| Once-per-phase-per-day cap                       | Yes                                 | Yes                                 | Identical                                                  |
| 14:50 cutoff for phases 1 / 2                   | Yes                                 | Yes                                 | Identical                                                  |
| Phase 3 may fire after 14:50                    | Yes                                 | Yes                                 | Identical                                                  |
| Earliest fire time (phase 1)                    | 09:02 KST (clock starts 09:01)     | 09:02 KST (R6 unresolved)          | Same (KOSPI ER §39.4 codifies; KOSDAQ ER unconfirmed)     |
| **Linked derivatives halted**                    | KOSPI 200/100/50 futures + options on those indices | **KOSDAQ 150 index futures + single-stock futures market** | **Material delta** |
| Bond market unaffected                          | Yes                                 | Yes                                 | Identical                                                  |
| Cancel-only-during-halt rule                    | KOSPI ER §13.1.1                   | KOSDAQ §26.1 inline                | Same behaviour, different placement (KOSDAQ inlines the definition in BR)             |

**Implications for execution.**

- **Cross-market index-arbitrage:** during a CB on either market, the corresponding linked derivatives are halted. A KOSPI ↔ KOSDAQ basis-trade strategy must consider that **only the affected market's index-derivatives** are halted — the other market's derivatives may still trade. KOSPI futures continue trading during a KOSDAQ CB; KOSDAQ futures continue during a KOSPI CB. Same-market spot/derivative legs are co-halted; cross-market legs are not.
- **Bond market** is unaffected on both. A pure-bond strategy is CB-immune.

---

## 8. Order amendments — cancel & correct

| Parameter                                       | KOSPI                              | KOSDAQ                             | Notes                                                    |
|-------------------------------------------------|------------------------------------|------------------------------------|----------------------------------------------------------|
| General cancel-and-correct article              | §13 (BR — explicit)                | **(none — delegated via §9.4 catch-all to ER)** | **Most R6-affected topic**                                |
| Cancel-only-on-unfilled-quantity rule           | KOSPI BR §13.1                     | KOSDAQ ER (R6 unresolved) — by inference | Same rule                                                 |
| Partial-cancel-preserves-time-priority          | KOSPI ER §17.1                     | KOSDAQ ER (R6 unresolved) — by inference | Same rule                                                 |
| Correction-resets-time-priority                 | KOSPI ER §17.3                     | KOSDAQ ER (R6 unresolved) — by inference | Same rule                                                 |
| §17.2 correction transformation matrix          | Same-type with Δp; cross-type with same-deemed-price proviso | Believed same | R6 confirmation needed                                    |
| §17.2.1-2 stop-limit pre/post activation correction | KOSPI ER (added 2025-02-27)     | KOSDAQ ER (R6 unresolved)          | Same effective date believed                              |
| Disconnect-cancel BR article                    | §13-2 (added 2022-12-07)           | **§16-2 (added 2022-12-07)**       | Article-number difference, same content                   |
| Bulk cancel (HSA-keyed)                         | KOSPI ER §17-2 (rewritten 2022-12-22) | KOSDAQ ER (R6 unresolved)         | Same eligibility model                                    |

**Implications for execution.** None on the substantive rule side — both markets follow the same cancel/correct semantics. The R6-citation gap means **compliance audits** that anchor on KOSDAQ-side article references will encounter "delegated to ER" placeholders rather than concrete article numbers; resolving R6 is the cleanest path to closure.

---

## 9. Short selling

| Parameter                                       | KOSPI                              | KOSDAQ                             | Notes                                                    |
|-------------------------------------------------|------------------------------------|------------------------------------|----------------------------------------------------------|
| Short-sale quote restriction article            | §17 (BR)                           | §9-2 (BR)                          | Article-number swap                                       |
| Uptick rule article                              | §18 (BR)                           | §9-3 (BR)                          | Article-number swap                                       |
| Post-management escalation article              | §18-2 (BR)                         | §9-4 (BR)                          | Article-number swap                                       |
| Number of "deemed-not-short" carve-outs         | 8                                  | 8                                  | Same case list                                             |
| §17.1.3.b / §9-2.1.3.나 narrower scope on KOSDAQ | "ETF additional issuance"          | **"corporate-growth-investment-fund additional issuance"** (added 2026-03-04) | Different sub-paragraph allocation, same effective coverage |
| Uptick rule (default)                            | Above 직전의 가격                  | Above 직전의 가격                  | Identical                                                  |
| Uptick exception                                 | At 직전의 가격 if uptick           | At 직전의 가격 if uptick           | Identical                                                  |
| 8-case categorical exemption list                | KOSPI §18.2 enumerates 8           | KOSDAQ §9-3.2 has 7 enumerated + 1 sub (§6-2)  | Same effective coverage                                   |
| §18.2.5 / 6 / 7 / 7-2 LP-hedging exemptions     | Self-referential to KOSPI BR §20-2 | **References KOSPI BR §20-2** (cross-market) | KOSDAQ-side LPs hedging KOSDAQ ETFs face strict-vs-broad-reading question |
| Deemed-verification opt-out + 120-day breach reset | KOSPI BR §17.4                  | KOSDAQ BR §9-2.4                   | Identical 120-day duration                                |
| Post-management escalation matrix               | 40 / 80 / 120 days × 5억 / 10억    | 40 / 80 / 120 days × 5억 / 10억    | **Identical numeric matrix**                              |
| 2026-01-28 carve-out for FSCMA §208-7.2.1.라 entities | (likely parallel; not yet pulled) | KOSDAQ §9-4.2 added 2026-01-28 | KOSPI counterpart needs verification                      |

**Implications for execution.**

- **Cross-market LP hedging:** a KOSPI-listed-ETF LP selling KOSDAQ-side underlying short is **uptick-rule-exempt** under KOSDAQ §9-3.2.6. A KOSDAQ-listed-ETF LP doing the same is **likely not exempt** under the strict reading of §9-3.2.6's KOSPI-§20-2 cross-reference. KOSDAQ-LP execution algos for KOSDAQ-listed ETFs should pre-compute uptick-rule paths conservatively.
- **Naked-short violation cost:** the 40 / 80 / 120-day pre-deposit escalation is **identical across both markets**. A consigner's post-management escalation status is per-customer-per-member, not per-market — but the trigger conditions and tier durations are uniform.

---

## 10. Other topics (block, basket, sidecar, LP, overheat, treasury, error trades)

### 10a. Block / basket / A-Blox parameters

| Parameter                                       | KOSPI                              | KOSDAQ                             | Notes                                                    |
|-------------------------------------------------|------------------------------------|------------------------------------|----------------------------------------------------------|
| **Off-hours block minimum**                     | **KRW 100,000,000** (or 5,000 × lot; 500 × ETF/ETN) | **KRW 50,000,000**                | **Material delta**                                       |
| **Off-hours basket minimum**                    | KRW 100,000,000 (no item-count)    | **KRW 200,000,000 + ≥ 5 items**   | **Material delta**                                       |
| Regular-session block minimum                   | Same as off-hours block             | Same as off-hours block             | Same delta carries through                                |
| Regular-session basket minimum                  | Same as off-hours block             | Same as off-hours block             | Same delta carries through                                |
| **A-Blox minimum**                              | **KRW 500,000,000**                | **KRW 200,000,000**                | **Material delta**                                       |
| **A-Blox trading unit**                         | **100 shares**                     | **1 share**                         | **Material delta**                                       |
| A-Blox session windows                          | 08:00–09:00 + 09:00–15:00          | 08:00–09:00 + 09:00–15:00          | Identical                                                  |
| A-Blox after-hours session                      | none                                | none                                | Identical                                                  |
| Treasury-stock-from-government no-price-limit carve-out | Yes                          | Yes (per [KRX-TOUR-KOSDAQ-EXCEPT-T3]) | Identical                                                  |

### 10b. Sidecar / program-trading

| Parameter                                       | KOSPI                              | KOSDAQ                             | Notes                                                    |
|-------------------------------------------------|------------------------------------|------------------------------------|----------------------------------------------------------|
| Sidecar parent article                          | KOSPI ER §20                       | KOSDAQ BR §13                      | Different placement (KOSDAQ inlines in BR)                |
| Reference futures                                | KOSPI 200 most-traded               | **KOSDAQ 150 most-traded**         | Different underlying index                                |
| **Trigger condition**                           | Futures ≥ 5 % for 1 min (single)   | **Futures ≥ 6 % AND index ≥ 3 % for 1 min (dual)** | **Material delta**                                       |
| Suspension duration                             | 5 minutes                          | 5 minutes                           | Identical                                                  |
| Earliest fire time                              | (implicit)                          | **09:05 KST (§13.2 explicit)**     | KOSDAQ codifies the rule                                  |
| Daily cap (latest fire time)                    | 14:50 KST                          | 14:50 KST                           | Identical                                                  |
| Once-per-day cap                                 | Yes                                 | Yes                                 | Identical                                                  |
| CB-cancels-sidecar                              | Yes                                 | Yes                                 | Identical                                                  |
| **Program-trading non-arbitrage threshold**     | **≥ 15 KOSPI 200 issues**          | **≥ 10 KOSDAQ Index constituents** | **Material delta**                                       |
| Index-arbitrage reference                        | KOSPI 200                           | KOSDAQ 150 / KRX 300                | Each market uses its own derivatives-eligible indices      |

### 10c. Liquidity Provider (LP) system

| Parameter                                       | KOSPI                              | KOSDAQ                             | Notes                                                    |
|-------------------------------------------------|------------------------------------|------------------------------------|----------------------------------------------------------|
| LP-framework BR articles                        | KOSPI BR §20-2 / §20-3 / §20-4 / §20-5 / §20-6 | **KOSDAQ BR §12-2 / §12-3 / §12-4 / §12-5 / §12-6** | Article-number cluster shift |
| **Spread-tightening trigger**                   | Bid-ask spread > **3 %**           | Bid-ask spread > **2 %**            | **Material delta**                                       |
| Spread-tightening target                        | Reduce to ≤ 3 %                    | Reduce to ≤ 2 %                     | Each market's contract-set ratio                          |
| **LP response time**                             | (implied; not in tour)             | **5 minutes** (§12-4.1 explicit)   | KOSDAQ tour codifies; KOSPI silent                       |
| Minimum quote size                              | 5 × trading lot                    | 5 × trading lot                     | Identical (both per LP contract; KOSPI tour OPS-T7 explicit) |
| **Suspension on consecutive lowest rating**     | **2 consecutive** (KOSPI tour OPS-T7) | **3 consecutive** (KOSDAQ §12-2.2.3.가) | **Material delta** |
| Suspension duration                             | 1 year                              | 1 year                              | Identical                                                  |
| Quotation type                                   | Best-same-side limit (최우선지정가) or regular limit per LP contract | Same                                | Identical                                                  |
| **BR-level eligible securities**                 | Stocks + ETFs + ETNs + ELWs + low-turnover stocks | **Stocks (incl. foreign DRs) only** | **Material delta** — KOSDAQ ETF / ETN LP coverage not BR-enumerated |

### 10d. Short-term overheat designation

| Parameter                                       | KOSPI                              | KOSDAQ                             | Notes                                                    |
|-------------------------------------------------|------------------------------------|------------------------------------|----------------------------------------------------------|
| Designation parent article                      | §106-2 (BR) → ER §133 / §134       | §23-2 (BR) → ER (R6 unresolved)    | Article-number difference                                 |
| Triple-criterion thresholds                     | 130 % / 600 % / 150 % (rise / turnover / volatility)  | (R6 unresolved — believed same)   | Numbers from KOSPI ER §133-2.3                            |
| Designation duration                             | 3 trading days                      | 3 trading days                      | Identical                                                  |
| Single-price-only matching interval              | 30 minutes                          | 30 minutes                          | Identical                                                  |
| Allowed order types during overheat             | Limit, market, competitive-block (no IOC, FOK) | Limit, market, competitive-block (no IOC, FOK) | Identical |
| Designation extension trigger                   | "3 days at 120 % of pre-designation close" (KOSPI tour OPS-T8) | "3 (or 10) days at 20 % rise" (KOSDAQ tour OPS-T6) | Same substantive trigger — different framing |
| Top-100 carve-out                                | Top-100 by market cap (KOSPI + KOSDAQ; updated 2026-01-07) | (R6 unresolved — believed same) | KOSDAQ side flagged for confirmation                       |

### 10e. Treasury stock

| Parameter                                       | KOSPI                              | KOSDAQ                             | Notes                                                    |
|-------------------------------------------------|------------------------------------|------------------------------------|----------------------------------------------------------|
| Treasury-stock platform                          | A-Blox / KOSPI block-trade workflow | **K-Blox System**                  | Operational platform difference                           |
| 1 % of issued-shares cap                         | Yes                                 | Yes (per [KRX-TOUR-KOSDAQ-EXCEPT-T6]) | Identical                                                  |
| 25 % of monthly-average daily-volume formula     | Yes                                 | Yes                                 | Identical                                                  |
| 5-tick-scope bid / ask range                     | Yes                                 | Yes (per [KRX-TOUR-KOSDAQ-EXCEPT-T6]) | Identical                                                  |
| Type-restricted quotation eligibility            | No market / no conditional-limit   | No market / no conditional-limit (R6 unresolved) | Same                                                      |
| Investment-broker max-issuer cap                 | 5 companies                          | 5 companies (per [KRX-TOUR-KOSDAQ-EXCEPT-T6])   | Identical                                                  |

### 10f. Error trade

| Parameter                                       | KOSPI                              | KOSDAQ                             | Notes                                                    |
|-------------------------------------------------|------------------------------------|------------------------------------|----------------------------------------------------------|
| Error-trade correction by KRX                   | §28 (BR)                            | §27 (BR)                            | Article-number swap                                       |
| Mass-erroneous-trade relief by member request   | §28-2 (BR — added 2015-11-04)      | §27-2 (BR — added 2015-11-04)      | Same effective date                                        |
| **Eligible-security scope for §28-2 / §27-2**   | Shares + DRs + ETFs + ETNs + ELWs + beneficiary certs | **Shares + DRs + corp-growth-fund only** | **Material delta** |
| Print-finality default rule                     | KOSPI BR §13.1                      | KOSDAQ BR §17.1                     | Same rule                                                  |

**Implications for execution (10).**

- **Block / basket sizing (10a):** as discussed in section 0; per-market thresholds, no shared block-eligibility table.
- **Sidecar (10b):** the dual-condition design on KOSDAQ filters out futures-only false alarms. Index-arbitrage strategies should treat KOSDAQ sidecar fires as **co-occurring with index moves**, not as standalone futures-side events. A futures spike to 6 % without an index move ≥ 3 % does not fire KOSDAQ sidecar but may fire KOSPI sidecar.
- **LP behaviour (10c):** KOSDAQ LPs respond to **tighter spreads** (2 % vs 3 %), have **stricter long-term standing requirements** (3-consecutive-rating vs 2), and have a more limited BR-level eligible-security enumeration (stocks only, vs KOSPI's stocks + ETFs + ETNs + ELWs). For passive-resting strategies that condition on LP-quote presence as a liquidity signal, KOSDAQ LP intervention is **more frequent at given spread levels**.
- **Overheat (10d):** identical mechanics modulo the tour-language difference for the extension trigger ("3 days × 120 %" vs "3 or 10 days × 20 %"). The "or 10" KOSDAQ-side phrasing may indicate a severe-case extension; pending R6 confirmation.
- **Treasury stock (10e):** operationally K-Blox vs A-Blox; substantively identical for the per-day-quantity / price-scope rules. Algo-execution teams handling treasury-stock flow must integrate with the appropriate platform per market.
- **Error trade (10f):** the most underrated divergence — KOSDAQ ETF / ETN errors have **no formal trade-relief mechanism**. KOSPI strategies in ETF / ETN can rely on §28-2 as a fat-finger backstop; KOSDAQ ETF / ETN strategies cannot.

---

## Cross-market R6 status

KOSDAQ Enforcement Rule (코스닥시장 업무규정 시행세칙) was not located on the KRX Legal Portal during Phase 1 source-discovery (R6, see PROJECT_IMPLEMENTATION.md). The following parameters are sourced from KRX overview tour pages and are **believed to mirror** the corresponding KOSPI Enforcement Rule articles, pending R6 resolution:

- **Auctions:** random-end window (≤ 30 s), 3-pass quantity allocation at price limits, newly-listed first-price single-price extension (analogue of KOSPI ER §35.1 / §34 / §67-2).
- **Price ranges:** KOSDAQ ETF / ETN tick schedule, full base-price-formula details (analogue of KOSPI ER §32.2.2 / §30).
- **Order types:** per-security-category eligibility matrix, per-session × per-issue restriction matrix (KOSPI ER §10 / §14.2 analogue).
- **Trading rules:** pre-quote-check items per KOSDAQ §9.7 (KOSPI ER §12-2 analogue).
- **Volatility interruption:** rate table by category, exclusion list, SMP-before-VI ordering, KRX-discretionary rate adjustment (KOSPI ER §41-2 analogue); KOSDAQ-only price-disparity cooling-off article number unconfirmed.
- **Circuit breakers:** +1 %-from-prior-phase carve-out, 14:50 cutoff, 09:01 clock-start (KOSPI ER §39 analogue).
- **Amendments:** correction transformation matrix, time-priority reset, partial-cancel competitive-block proviso, stop-limit pre/post-activation correction, bulk-cancel HSA-keying, disconnect-cancel session-keying detail (KOSPI ER §17 / §17-2 / §17-3 analogue).
- **Short selling:** detailed per-quotation pre-quote check articles, KRX-discretionary covered-short restriction details (KOSPI ER §17.8 analogue).
- **Other topics:** ER-side overheat criteria, K-Blox treasury-stock platform-specific articles.

Phase 6 freshness audit must re-verify all R6-flagged parameters once the KOSDAQ Enforcement Rule is archived. Until then, strict citation depth on the KOSDAQ side is structurally limited.

---

## Cross-market recurring patterns — beyond per-topic deltas

A few cross-cutting patterns surface across multiple topics:

1. **KOSDAQ co-locates** several rules that KOSPI splits into separate articles (e.g. cancel-and-correct rule embedded in §9.4 catch-all on KOSDAQ vs explicit §13 on KOSPI; off-hours session timing inlined in §4.3 on KOSDAQ vs §4 + §33 on KOSPI; halt-quotation-receipt rule inlined in §26.1 on KOSDAQ vs ER §13.1.1 on KOSPI). The aggregate effect is fewer, denser articles in the KOSDAQ BR.

2. **Article-number swaps** between KOSDAQ and KOSPI BR are the rule, not the exception. Notable swaps (cite by content, not by number, when working across both):
   - CB: KOSDAQ §26 ↔ KOSPI §25.
   - Individual-issue halt: KOSDAQ §25 ↔ KOSPI §26.
   - Auction principle: KOSDAQ §17 ↔ KOSPI §22.
   - Single-price auction: KOSDAQ §18 ↔ KOSPI §23.
   - Continuous auction: KOSDAQ §19 ↔ KOSPI §24.
   - Price-limit band: KOSDAQ §14 ↔ KOSPI §20.
   - Tick / lot units: KOSDAQ §15 ↔ KOSPI §21.
   - Trade types: KOSDAQ §7-2 ↔ KOSPI §7.
   - Short-sale rule: KOSDAQ §9-2 / §9-3 / §9-4 ↔ KOSPI §17 / §18 / §18-2.
   - HSA registration: KOSDAQ §50-3 ↔ KOSPI §104-3.
   - Disconnect-cancel: KOSDAQ §16-2 ↔ KOSPI §13-2.
   - Mass-erroneous-trade relief: KOSDAQ §27-2 ↔ KOSPI §28-2.
   - LP framework: KOSDAQ §12-2 to §12-6 ↔ KOSPI §20-2 to §20-6 (similar cluster, shifted).

3. **Numeric thresholds** are mostly identical across markets (8 % / 15 % / 20 % CB tiers; 10 % Static VI; ±30 % daily band; 7-band tick schedule; 60 %–400 % day-1 newly-listed band; 1-min CB persistence; 2-min VI cool-off; 40 / 80 / 120-day short-sale escalation with KRW 5억 / 10억 thresholds). The numeric divergences cluster around: A-Blox / block thresholds, sidecar threshold, LP threshold, and program-trading-issues threshold.

4. **2026-03-04 amendments** (corporate-growth-investment-fund securities — added on KOSDAQ as §2.21 / §4.1.5 / §9-2.1.3.나 / §14.1 enumerated / §23-3 enumerated / §27-2 enumerated) are a KOSDAQ-only rule-set extension. KOSPI does not host this security class. Algorithmic strategies for the new fund class are exclusively a KOSDAQ-side concern.

5. **2025-02-05 amendments** (midpoint + stop-limit quotation types) landed in **lockstep across both books**. The corresponding KOSPI ER amendments (effective 2025-02-27) are mirrored on KOSDAQ ER (R6 unresolved); both books' BR-level definitions are at §2.4.

6. **2022-12-07 amendments** (disconnect-cancel) landed in lockstep on both books — KOSPI §13-2, KOSDAQ §16-2.

7. **2015-11-04 amendments** (mass-erroneous-trade relief) landed in lockstep on both books — KOSPI §28-2, KOSDAQ §27-2 — but with different security-scope enumerations (KOSDAQ narrower; excludes ETF / ETN / ELW).

## Sources

- `KRX-RULE-KOSPI-BR-KO` — KOSPI Market Business Regulation, bookid 210200859, effective 2026-04-28.
- `KRX-RULE-KOSPI-BR-ENFORCE-KO` — KOSPI BR Enforcement Rule, bookid 210203562, effective 2026-04-28.
- `KRX-RULE-KOSDAQ-BR-KO` — KOSDAQ Market Business Regulation, bookid 210164370, effective 2026-04-28.
- KOSDAQ Enforcement Rule — **not yet archived** (R6 unresolved).
- 59 KRX overview tour pages (KOSPI BASIC / METHOD / EXCEPT / OPS / TRUST + KOSDAQ BASIC / METHOD / EXCEPT / OPS / TRUST series) — see [`docs/sources/INVENTORY.md`](../sources/INVENTORY.md) for the full inventory.

Per-topic deep dives with full article-by-article citations:

- [Market Hours: KOSPI](../kospi/market_hours.md) / [KOSDAQ](../kosdaq/market_hours.md)
- [Auctions: KOSPI](../kospi/auctions.md) / [KOSDAQ](../kosdaq/auctions.md)
- [Price Ranges & Tick Sizes: KOSPI](../kospi/price_ranges.md) / [KOSDAQ](../kosdaq/price_ranges.md)
- [Order Types: KOSPI](../kospi/order_types.md) / [KOSDAQ](../kosdaq/order_types.md)
- [Trading Rules: KOSPI](../kospi/trading_rules.md) / [KOSDAQ](../kosdaq/trading_rules.md)
- [Volatility Interruption: KOSPI](../kospi/volatility_interruption.md) / [KOSDAQ](../kosdaq/volatility_interruption.md)
- [Circuit Breakers: KOSPI](../kospi/circuit_breakers.md) / [KOSDAQ](../kosdaq/circuit_breakers.md)
- [Order Amendments: KOSPI](../kospi/amendments.md) / [KOSDAQ](../kosdaq/amendments.md)
- [Short Selling: KOSPI](../kospi/short_selling.md) / [KOSDAQ](../kosdaq/short_selling.md)
- [Other Topics: KOSPI](../kospi/other_topics.md) / [KOSDAQ](../kosdaq/other_topics.md)
