---
title: "Circuit Breakers (KOSDAQ)"
markets: [KOSDAQ]
last_reviewed: 2026-05-01
sources:
  - KRX-RULE-KOSDAQ-BR-KO
  - KRX-TOUR-KOSDAQ-OPS-T2
---

> See also: [Circuit Breakers (KOSPI)](../kospi/circuit_breakers.md), [Volatility Interruption (KOSDAQ)](./volatility_interruption.md), [Auctions (KOSDAQ)](./auctions.md), [Trading Rules (KOSDAQ)](./trading_rules.md), [Comparison](../common/comparison.md).

**Delta file.** KOSDAQ index-level circuit-breaker substance is **identical to KOSPI**: same 3-tier structure (8 % / 15 % / 20 %), same 1-minute persistence, same +1 %-from-prior-phase carve-out for phases 2 / 3, same 20-minute halt + 10-minute single-price resumption call for phases 1 / 2, same immediate close for phase 3, same once-per-phase-per-day cap, same 14:50 cutoff for phases 1 / 2 with phase 3 applicable through session end, same cancel-only-during-halt semantics for phases 1 / 2 (with bond market unaffected on both books). The deltas are: (1) **anchored on the KOSDAQ index** instead of KOSPI; (2) **article-numbering swap** — KOSDAQ §26 = KOSPI §25; (3) **linked-derivatives halt scope differs** — KOSDAQ CB also halts KOSDAQ 150 index futures and single-stock futures (vs KOSPI's KOSPI 200/100/50 futures + options); (4) granular Enforcement-Rule items (09:01 clock-start, +1 %-carve-out wording, 14:50 cutoff article number) cannot yet be cited authoritatively (R6 unresolved). This file points to the [KOSPI write-up](../kospi/circuit_breakers.md) for shared content.

## Summary

- KRX runs a 3-tier index-level circuit breaker on KOSDAQ, set out in [KRX-RULE-KOSDAQ-BR-KO §26]. Anchored on the **KOSDAQ index** (코스닥지수, *ko-seu-dak-ji-su*) — the broad-market index, not KOSDAQ 150 — relative to the prior trading day's final value.
- **Phase 1** (KOSDAQ §26.1.1): KOSDAQ index ≥ **8 %** lower than prior close, persisting **1 minute** → 20-min halt + 10-min single-price resumption.
- **Phase 2** (KOSDAQ §26.1.2): KOSDAQ index ≥ **15 %** lower than prior close after phase 1's halt-and-reopen, persisting 1 minute → 20-min halt + 10-min resumption. The +1 %-from-phase-1-trigger-value carve-out (analogous to KOSPI ER §39.1.1) is delegated to the KOSDAQ Enforcement Rule (R6 unresolved).
- **Phase 3** (KOSDAQ §26.1.3): KOSDAQ index ≥ **20 %** lower than prior close after phase 2's halt-and-reopen, persisting 1 minute → **immediate market-wide close** for the day. Same +1 %-from-phase-2 carve-out.
- Each phase fires at most **once per trading day**. Phases 1 / 2 are barred from triggering in the **last 40 minutes before close** (i.e. after 14:50 KST). Phase 3 may fire at any time, including in the last 40 minutes [KRX-TOUR-KOSDAQ-OPS-T2].
- During phases 1 / 2, **only cancellation orders** are accepted [KRX-RULE-KOSDAQ-BR-KO §26.1: "취소호가를 제외한 호가접수를 중단" — "halts quotation receipt except cancel quotations"]. Phase 3 closes the market entirely; no orders, including cancels, are accepted [KRX-TOUR-KOSDAQ-OPS-T2].
- Linked derivatives halted alongside KOSDAQ CB: **KOSDAQ 150 index futures** + **single-stock futures market** [KRX-TOUR-KOSDAQ-OPS-T2]. Bond market is unaffected (same as KOSPI).

## Detailed rules

For full prose on the trigger arithmetic, the +1 %-from-prior-phase carve-out logic, the 1-minute persistence clock starting 1 minute after 장개시 (*jang-gae-si*; nominal session-open time, 09:00 KST) — i.e. earliest phase-1 fire at 09:02, the cancel-only-during-halt rule, and CB-cancels-VI / CB-cancels-other-stabilization precedence, see [KOSPI § Detailed rules](../kospi/circuit_breakers.md#detailed-rules). The KOSDAQ articles map directly:

| KOSDAQ BR article | KOSPI BR article | Topic                                                                |
|-------------------|------------------|----------------------------------------------------------------------|
| §6                | §6               | Market-wide pause and reopen — referenced for the 20-min halt mechanism |
| §25               | §26              | Individual-issue trading halt (rumour, abnormal volume, settlement-failure-risk, market-surveillance referrals) |
| §25-2             | §27              | System-failure / quote-flooding emergency halt (KOSDAQ has it as §25-2 since 2005-05-13; KOSPI has the same content as §27) |
| **§26**           | **§25**          | **Index-level CB** — central article: 3-phase 8 % / 15 % / 20 % thresholds with halt/resumption actions |
| §27               | §28              | Error-trade correction by KRX                                          |
| §27-2             | §28-2            | Mass-erroneous-trade relief — both markets have it (added 2015-11-04)  |

### Delta vs KOSPI

#### Index anchor — KOSDAQ index, not KOSDAQ 150

KOSDAQ §26.1 reads "거래소는 코스닥지수의 수치가" (when the KOSDAQ index value...). The reference is the **KOSDAQ index** (broad-market) — *not* the KOSDAQ 150. KOSPI's §25 anchors on the KOSPI index (broad-market) — also the broad index. So both markets use their broad-market index as the CB anchor, not the narrow blue-chip subset. The 8 % / 15 % / 20 % thresholds are computed against the broad-index value's prior-day final.

#### Linked-derivatives halt scope

[KRX-TOUR-KOSDAQ-OPS-T2] explicitly enumerates the derivatives that are halted alongside the KOSDAQ CB:

> All orders (excluding cancellation orders) and trades in **KOSDAQ150 index futures, single stock futures market** are also halted.

Versus KOSPI's [KRX-TOUR-KOSPI-OPS-T2] which mentions:

> KRX-derivative markets linked to KOSPI (KOSPI 200 / 100 / 50 futures, options on those indices, etc.) are also halted.

So:

- **KOSDAQ CB halts:** KOSDAQ 150 index futures + single-stock futures.
- **KOSPI CB halts:** KOSPI 200 / 100 / 50 index futures + options on those indices.

Note that the **KOSDAQ tour does not mention options** in its derivatives list, while the KOSPI tour does. KOSDAQ 150 options exist (per the inventory of derivative products at the start of the KOSDAQ tour pages), so the omission is likely tour-page brevity rather than a substantive carve-out — but the Derivatives Market Business Regulation §27 analogue would be the authoritative source. Treat the KOSDAQ 150 options halt as expected behavior, pending Derivatives BR cross-pull.

For an execution algo running an index-arbitrage strategy across spot KOSDAQ + derivatives, the implication is:

- A KOSDAQ CB halts both legs simultaneously, so the cross-leg basis cannot widen during the halt (no live quotes on either side).
- The 10-minute resumption call on the spot side is matched by a similar resumption mechanism on the derivatives side — the futures market's reopen after a CB is governed by Derivatives Market BR §27 (not pulled in this project's source inventory).

#### Article-number swap — KOSDAQ §26 = KOSPI §25

The two markets effectively swap §25 and §26 between them:

- **KOSPI BR §25** = market-wide CB. **KOSDAQ BR §26** = same.
- **KOSPI BR §26** = individual-issue trading halt. **KOSDAQ BR §25** = same.

This is the most error-prone numbering delta in the project. When citing CB across both books, anchor on §26 for KOSDAQ and §25 for KOSPI.

#### KOSDAQ §26 is shorter than KOSPI §25 — granular details delegated more aggressively

KOSDAQ §26 has only 2 paragraphs (§26.1 with 3 sub-points enumerating the phases, and §26.2 delegating implementation details to the Enforcement Rule). KOSPI §25 has the same 3 phases plus more in-text wording on the halt-then-reopen mechanism. The KOSDAQ §26.1 explicit definition of "매매거래를 중단" (halt) — *"취소호가를 제외한 호가접수를 중단하는 것을 말한다"* (means halting quotation receipt except cancel quotations) — is inlined; KOSPI §25.1 leaves this to Enforcement Rule §13.1.1.

The KOSDAQ §26.2's delegation to the Enforcement Rule covers:

- The +1 %-from-prior-phase carve-out for phases 2 / 3 (analogous to KOSPI ER §39.1.1).
- The 14:50 cutoff for phases 1 / 2 (analogous to KOSPI ER §39.2 proviso).
- The 09:01 clock-start for the phase-1 1-minute persistence (analogous to KOSPI ER §39.4, added 2020-11-26).
- Resumption call mechanics (analogous to KOSPI ER §35.1).

R6 unresolved means none of these details can be cited authoritatively from the KOSDAQ ER side. The substance is believed to mirror KOSPI ER §39 verbatim — confirmed against the KOSDAQ tour's identical 8 % / 15 % / 20 % numbers, identical 1-minute persistence, identical 14:50 cutoff for phases 1 / 2, and identical phase-3 carve-out — but cross-check at R6 / Phase 6.

#### Bond market is unaffected (same as KOSPI)

Both KOSPI and KOSDAQ tours explicitly state that the bond market is not halted by an index-level CB. KOSDAQ-OPS-T2 says "all stock trades are halted... All orders... in KOSDAQ150 index futures, single stock futures market are also halted" — bond market is conspicuously absent from the halt scope.

## Parameters & thresholds

### Table 1 — KOSDAQ CB phases (anchored on KOSDAQ index)

| Phase | Trigger condition (vs prior trading day's KOSDAQ close)                        | Persistence | Action                                            | Source                                         |
|-------|--------------------------------------------------------------------------------|------------:|---------------------------------------------------|-------------------------------------------------|
| 1     | KOSDAQ ≤ 92 % of prior close                                                   |    1 minute | 20-min halt + 10-min single-price resumption call | [KRX-RULE-KOSDAQ-BR-KO §26.1.1; KRX-TOUR-KOSDAQ-OPS-T2] |
| 2     | KOSDAQ ≤ 85 % of prior close **AND** ≤ 99 % of phase-1 trigger value           |    1 minute | 20-min halt + 10-min single-price resumption call | [KRX-RULE-KOSDAQ-BR-KO §26.1.2; KRX-TOUR-KOSDAQ-OPS-T2] |
| 3     | KOSDAQ ≤ 80 % of prior close **AND** ≤ 99 % of phase-2 trigger value           |    1 minute | Immediate close for the day                       | [KRX-RULE-KOSDAQ-BR-KO §26.1.3; KRX-TOUR-KOSDAQ-OPS-T2] |

### Table 2 — Daily caps and timing windows

| Rule                                                              | Value                                                            | Source                                                |
|-------------------------------------------------------------------|------------------------------------------------------------------|-------------------------------------------------------|
| Maximum CB triggers per day, per phase                            | 1                                                                | [KRX-TOUR-KOSDAQ-OPS-T2]                              |
| Earliest possible Phase 1 trigger time                            | 09:02 KST (clock starts 09:01 + 1 min persistence)               | KOSDAQ Enforcement Rule analogue of KOSPI ER §39.4 (R6 unresolved) |
| Latest possible Phase 1 / Phase 2 trigger time                    | 14:50 KST (40 min before 15:30 close)                            | [KRX-TOUR-KOSDAQ-OPS-T2]                              |
| Latest possible Phase 3 trigger time                              | No upper bound — applies through the entire session              | [KRX-TOUR-KOSDAQ-OPS-T2]                              |

### Table 3 — Quotation behavior by phase

| Phase                                          | New orders | Corrections | Cancellations | Disconnect-cancel | Source                                          |
|------------------------------------------------|------------|-------------|---------------|-------------------|-------------------------------------------------|
| Phase 1 / Phase 2 halt (20 min)                | rejected   | rejected    | accepted      | accepted          | [KRX-RULE-KOSDAQ-BR-KO §26.1; KRX-TOUR-KOSDAQ-OPS-T2] |
| Phase 1 / Phase 2 resumption call (10 min)     | accepted   | accepted    | accepted      | accepted          | [KRX-TOUR-KOSDAQ-OPS-T2]                        |
| Phase 3 close                                  | rejected   | rejected    | rejected      | rejected          | [KRX-TOUR-KOSDAQ-OPS-T2]                        |

### Table 4 — Linked derivatives halted by KOSDAQ CB

Per [KRX-TOUR-KOSDAQ-OPS-T2]:

| Market segment                     | Halted? | Notes                                                  |
|------------------------------------|---------|---------------------------------------------------------|
| KOSDAQ stock spot                  | yes     | Phases 1 / 2 / 3                                       |
| KOSDAQ 150 index futures           | yes     | Phases 1 / 2; phase 3 closes for the day               |
| KOSDAQ 150 index options           | (likely yes) | Tour page omits options explicitly; per Derivatives BR §27 analogue, expected to halt |
| Single-stock futures (KOSDAQ underlyings) | yes | Phases 1 / 2; phase 3 closes for the day               |
| KOSDAQ-listed ETF / ETN spot       | (likely yes) | KRX phrasing "all stock trades" is broad enough to include them; not pinpointed in §26 |
| KOSDAQ bond market                 | no      | Not halted by CB                                        |

## Worked examples

### Example A — Phase 1 trigger and resumption (KOSDAQ)

Prior trading day's KOSDAQ close: **800.00**. Trading begins at 09:00 KST. By 11:14, KOSDAQ index has reached **736.00** (= 92 % of 800.00 = the phase-1 threshold).

- **11:15:00** — first crossing below 736.00 sustained at the second-by-second tick. Persistence clock starts.
- **11:16:00** — 1 minute elapsed and KOSDAQ still ≤ 736.00. **Phase 1 fires.**
- **11:16–11:36** — 20-minute halt. KOSDAQ-150 index futures and single-stock-futures markets are also halted [KRX-TOUR-KOSDAQ-OPS-T2]. Spot market accepts only cancel quotations [KRX-RULE-KOSDAQ-BR-KO §26.1].
- **11:36–11:46** — 10-minute single-price resumption-call receipt window opens. Standard §17 price-then-time priority. KRX may add a random-end of up to 30 s under the KOSDAQ Enforcement Rule analogue of KOSPI ER §35.1.
- **11:46:xx** — auction clears at, say, KOSDAQ implied value 728. Continuous trading resumes. The "phase-1 trigger value" — 736.00 — becomes the anchor for any future phase-2 evaluation.

### Example B — Phase 2 carve-out blocks an early refire (KOSDAQ)

Continuing from Example A. After resumption at 11:46, KOSDAQ slides to 720.00 at 12:00 — meeting the 15 % phase-2 threshold (720 ≤ 800 × 0.85 = 680). Wait, 720 > 680, so 15 % threshold not met. KOSDAQ continues to slide. At 14:30, KOSDAQ reaches **678.00** (= 84.75 % of prior close, = 15 % threshold met by 0.25 %).

- Phase-2 absolute condition: KOSDAQ ≤ 680 (= 800 × 0.85). 678 ≤ 680 → met.
- Phase-2 carve-out: KOSDAQ ≤ 99 % of phase-1 trigger value = 736 × 0.99 = 728.64. 678 ≤ 728.64 → carve-out condition met.
- Persistence: 1 minute starting at 14:30:00.
- 14:31:00 — both conditions still met → **Phase 2 fires**.
- 14:31–14:51 — 20-min halt. **But wait — the resumption call would extend to 14:51 + 10 min = 15:01**, leaving 29 minutes to close. The 14:50 cutoff applies to the *trigger time*, not the resumption end. Phase 2 firing at 14:31 is **within** the 14:50 cutoff (= 40 min before close), so it fires successfully.

If the same 678.00 threshold had only been met *after* 14:50 (say 14:51:00 with 1-min persistence ending at 14:52:00), then phase 2 would **not** fire — same as KOSPI Example C.

### Example C — Phase 3 firing through the late-session-cutoff carve-out

Same prior-day close (800.00). KOSDAQ has been sliding all day. At 14:51, KOSDAQ reaches 736.00 (= phase-1 threshold). Persistence clock starts.

- 14:52:00 — 1 minute elapsed; KOSDAQ still ≤ 736.00. **But 14:52 is after 14:50** — phase 1 does not fire.
- KOSDAQ continues to slide. At 15:00, KOSDAQ reaches **640.00** (= 80 % of 800.00 = phase-3 threshold).
- Phase 3's carve-out requires ≤ 99 % of phase-2 trigger value — but phase 2 never fired today. The phase-3 anchor falls back to the prior-day close [analogous to the KOSPI implicit reading]. Persistence clock starts at 15:00:00.
- 15:01:00 — 1 minute elapsed; KOSDAQ still ≤ 640. **Phase 3 fires** — within the 40-min-before-close window, by the §26.1.3 phrasing being read absolutely and §26.2's delegated proviso allowing late-session phase-3 firings [KRX-TOUR-KOSDAQ-OPS-T2 explicit: "phase 3 is triggered during that time period"].
- KOSDAQ market closes immediately for the day; closing print determined by the §26.1.3 procedure.

## Edge cases & open questions

- Edge case: KOSDAQ §26.2 delegates resumption-call mechanics, the +1 %-from-prior-phase carve-out, and the 14:50 cutoff to the Enforcement Rule. KOSDAQ Enforcement Rule (R6 unresolved) cannot yet be cited authoritatively. The KOSDAQ tour confirms the same numeric parameters as KOSPI but does not give article numbers; cross-check at R6 / Phase 6.
- Edge case: KOSDAQ-OPS-T2 omits "options" from the linked-derivatives-halt enumeration ("KOSDAQ 150 index futures, single stock futures market"). KOSDAQ 150 options exist as a product per the project source-inventory tour-page index. The omission is likely tour-page brevity, but the formal halt-scope authority is the Derivatives Market BR §27 (not in this project's source inventory). Treat KOSDAQ 150 options as expected-to-halt pending Derivatives BR cross-pull.
- Edge case: KOSDAQ §25-2 (system-failure / quote-flooding) is the analogue of KOSPI BR §27 — same 2005-05-13 effective date for that article on KOSDAQ, but the article number is 25-2 (vs KOSPI's flat §27). System-failure halts do not consume the daily phase-1 / phase-2 caps, same as KOSPI.
- Edge case: KOSDAQ §26 reads as anchored on "코스닥지수" (the KOSDAQ index) without specifying which index variant. KRX publishes multiple KOSDAQ-related indices (KOSDAQ broad, KOSDAQ 150, KOSDAQ Star, KOSDAQ Mid 300, etc.). The CB anchor is the KOSDAQ broad market index by convention and by the tour's "KOSDAQ index" wording — but in event of an index-name change or a new KOSDAQ-broad index variant, the article would need amendment.
- Open question: KOSPI §25's enumeration of CB-affected market scope includes "주식시장 등" (stock market etc.). KOSDAQ §26 says "시장의 모든 종목의 매매거래를 중단" (all-issues market halt) — narrower phrasing. Whether KOSDAQ-listed ETFs / ETNs are "종목" (issues) for §26 purposes — and therefore halted by the CB — is implicit in the broad phrasing but not explicitly stated. Cross-check before relying on KOSDAQ ETF / ETN halt behavior during a CB.
- Open question: The KOSDAQ §26.1.2 wording ("제1호 및 제2항에 따라 매매거래를 중단·재개한 후에도") explicitly requires phase 2 to fire only "after a phase-1 halt-and-reopen" — implying that without phase 1 firing first, phase 2 cannot fire. This is strict-monotonic — if KOSDAQ drops 15 % without first crossing 8 % (e.g. on a market gap-down at the open), the §26.1.2 trigger does not fire absent the §26.1.1 chain. The same pattern applies to phase 3 vs phase 2 [§26.1.3]. The natural next-trigger fall-through is to skip the missing phase, but the article text does not explicitly authorize this — verify against KRX implementation guide.
- Open question: Phase 3's §26.1.3 wording requires phase 2 to have fired first ("제2호에 따라 매매거래를 중단·재개한 후에도"). If phases 1 and 2 are barred by the 14:50 cutoff and KOSDAQ then drops to 20 %+ at 15:00, the §26.1.3 chain-condition is not met. The natural reading is that phase 3 still fires (skipping the missing earlier phases), per the §26.2 delegated proviso analogous to KOSPI ER §39.2. This was the basis of Example C above; confirm at R6.

## Sources

- `KRX-RULE-KOSDAQ-BR-KO` — KOSDAQ Market Business Regulation (코스닥시장 업무규정), bookid 210164370, effective 2026-04-28. Articles cited: §6 (Market-wide pause and reopen — referenced for the 20-min halt mechanism), §17 (Auction principle — referenced for the resumption-call price-then-time priority), §18 (Single-price auction — referenced for the resumption-call mechanism), §25 (Individual-issue halt — separate mechanism, ≠ market-wide CB), §25-2 (System-failure / quote-flooding emergency halt — added 2005-05-13, separate from CB), **§26** (Index-level CB — central article: 3-phase 8 % / 15 % / 20 % with halt/resumption actions; the analogue of KOSPI BR §25; §26.1's inline definition of "halt = halt quotation receipt except cancel quotations" matches KOSPI ER §13.1.1's halt-rule), §27 (Error-trade correction — referenced), §27-2 (Mass-erroneous-trade relief — both books have it).
- `KRX-TOUR-KOSDAQ-OPS-T2` — KRX overview "Circuit Breakers" (KOSDAQ); English, not authoritative. Used for the cancel-only-during-phases-1/2-halt language, the no-orders-in-phase-3 close, the once-per-phase-per-day cap, the 14:50 / 40-min cutoff for phases 1 / 2, the phase-3-applies-late-in-session statement, and the linked-derivatives-halt list (KOSDAQ 150 index futures + single-stock futures, with the omission of options-explicit-mention flagged for Derivatives BR cross-pull).
