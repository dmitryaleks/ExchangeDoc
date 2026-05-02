---
title: "Circuit Breakers (KOSPI)"
markets: [KOSPI]
last_reviewed: 2026-04-30
sources:
  - KRX-RULE-KOSPI-BR-KO
  - KRX-RULE-KOSPI-BR-ENFORCE-KO
  - KRX-TOUR-KOSPI-OPS-T2
  - KRX-TOUR-KOSPI-OPS-T3
---

> See also: [Circuit Breakers (KOSDAQ)](../kosdaq/circuit_breakers.md), [Volatility Interruption (KOSPI)](./volatility_interruption.md), [Auctions (KOSPI)](./auctions.md), [Trading Rules (KOSPI)](./trading_rules.md), [Comparison](../common/comparison.md).

## Summary

- KRX runs a 3-tier index-level circuit breaker (매매거래중단, *mae-mae geo-rae jung-dan*; commonly **CB**) anchored on the KOSPI index, set out in [KRX-RULE-KOSPI-BR-KO §25] and implemented by [KRX-RULE-KOSPI-BR-ENFORCE-KO §39].
- **Phase 1** fires when KOSPI drops ≥ **8 %** from the prior trading day's closing index value and the drop persists for **1 minute** [KRX-RULE-KOSPI-BR-KO §25.1.1]. **Phase 2** fires when KOSPI further drops ≥ 15 % from prior close **and** is at least 1 % below the phase-1 trigger level for 1 minute [KRX-RULE-KOSPI-BR-KO §25.1.2; KRX-RULE-KOSPI-BR-ENFORCE-KO §39.1.1]. **Phase 3** fires at ≥ 20 % from prior close + ≥ 1 % below the phase-2 level for 1 minute [KRX-RULE-KOSPI-BR-KO §25.1.3; KRX-RULE-KOSPI-BR-ENFORCE-KO §39.1.2].
- Phase 1 and Phase 2 each impose a **20-minute trading halt** followed by a **10-minute single-price resumption auction** [KRX-RULE-KOSPI-BR-KO §25.1.1–.2; KRX-TOUR-KOSPI-OPS-T2]. Phase 3 immediately **closes the market for the day** [KRX-RULE-KOSPI-BR-KO §25.1.3].
- Each phase may fire at most **once per trading day** [KRX-RULE-KOSPI-BR-ENFORCE-KO §39.2]. Phases 1 and 2 cannot fire **after 14:50 KST** (40 minutes before 장종료 / *jang-jong-ryo*; nominal session close); Phase 3 may fire at any time, including in the last 40 minutes [KRX-RULE-KOSPI-BR-ENFORCE-KO §39.2 proviso]. The 1-minute persistence clock for Phase 1 does not start until **1 minute after 장개시** (*jang-gae-si*; nominal session open, 09:00 KST) [KRX-RULE-KOSPI-BR-ENFORCE-KO §39.4].
- During a Phase 1 or Phase 2 halt, members may submit **cancellations only** for previously placed quotations; new orders and corrections are rejected [KRX-RULE-KOSPI-BR-ENFORCE-KO §13.1.1; KRX-TOUR-KOSPI-OPS-T2]. During Phase 3, **no quotations are accepted** at all — including cancels [KRX-TOUR-KOSPI-OPS-T2]. A CB also **cancels any in-progress per-issue stabilization** (notably VI) [KRX-TOUR-KOSPI-OPS-T9 — referenced from VI doc].

## Detailed rules

### Trigger conditions

The Business Regulation defines three CB phases, all anchored on the KOSPI index value relative to the prior trading day's final value [KRX-RULE-KOSPI-BR-KO §25.1]:

1. **Phase 1 (1차 매매거래중단, *il-cha mae-mae geo-rae jung-dan*)** — KOSPI is ≥ **8 %** lower than the prior trading day's final value, and the condition persists for **1 minute** [KRX-RULE-KOSPI-BR-KO §25.1.1]. Action: 20-minute halt, then resumption.
2. **Phase 2 (2차 매매거래중단)** — KOSPI is ≥ **15 %** lower than the prior trading day's final value, and at the same time is ≥ **1 %** lower than the index value at the moment Phase 1 was triggered, and the combined condition persists for **1 minute** [KRX-RULE-KOSPI-BR-KO §25.1.2; KRX-RULE-KOSPI-BR-ENFORCE-KO §39.1.1]. Action: 20-minute halt, then resumption.
3. **Phase 3 (3차 매매거래중단)** — KOSPI is ≥ **20 %** lower than the prior trading day's final value, and at the same time is ≥ **1 %** lower than the index value at the moment Phase 2 was triggered, and the combined condition persists for **1 minute** [KRX-RULE-KOSPI-BR-KO §25.1.3; KRX-RULE-KOSPI-BR-ENFORCE-KO §39.1.2]. Action: immediate market-wide close for the day — no resumption.

The "≥ X %" arithmetic uses the prior trading day's **final KOSPI value** (i.e. the closing print) as the reference. The phase-2 and phase-3 +1 % conditions are anchored on the index value at the **moment of the immediately preceding trigger**, not on the prior-day close — so phases 2 and 3 effectively require both an absolute drawdown threshold *and* an incremental drawdown from the previous trigger.

### Phase 2/3 exception — additional-drop and persistence requirement

Article §25.1.2 of the Business Regulation appears at first reading to require only the absolute 15 % threshold, but the Enforcement Rule §39.1.1 carves out an exception that, read in reverse, defines the operational trigger [KRX-RULE-KOSPI-BR-ENFORCE-KO §39.1]:

> The cases set forth in this Rule [where phase 2 / phase 3 do not fire] are: where the KOSPI value has not declined by 1 % or more from the index value at the moment of the [previous-phase] trading halt; or where it has declined by 1 % or more but the decline has not persisted for 1 minute.

So the practical phase-2 trigger is: absolute drop ≥ 15 % from prior close **AND** incremental drop ≥ 1 % from the index value at phase 1 **AND** the combined condition persists for 1 minute. Phase 3 follows the same pattern with the 20 % / 1 %-from-phase-2 / 1-minute logic. The carve-out exists because absent the +1 % requirement, phase 2 would inevitably fire any time KOSPI continued to slide after phase 1 (since 15 % > 8 %).

### Halt and resumption mechanics

When Phase 1 or Phase 2 fires [KRX-RULE-KOSPI-BR-KO §25.1.1, §25.1.2; KRX-TOUR-KOSPI-OPS-T2]:

- All quotation receipt for the KOSPI Stock Market is halted for **20 minutes**, except for cancel-quotations [KRX-RULE-KOSPI-BR-ENFORCE-KO §13.1.1]. This is implemented as the §6 market-pause mechanism scoped to the 20-min duration.
- KRX-derivative markets linked to KOSPI (KOSPI 200 / 100 / 50 futures, options on those indices, etc.) are **also halted** during the 20 minutes [KRX-TOUR-KOSPI-OPS-T2]. Bond markets are unaffected.
- After the 20-minute halt, KRX runs a **10-minute single-price resumption auction** to determine the resumption price under §23.1.2 (i.e. as a "first price after market reopen" single-price). Continuous trading resumes when the auction clears.
- The 10-minute resumption-auction window plus a possible random-end is governed by [KRX-RULE-KOSPI-BR-ENFORCE-KO §35.1] — see [Auctions § Random-end mechanism](./auctions.md#random-end-mechanism).

When Phase 3 fires [KRX-RULE-KOSPI-BR-KO §25.1.3]:

- All trading is halted **immediately** for the rest of the day.
- The closing print used for that day's official close is determined by the §38-2 / §51 closing-price rules applied to the latest pre-halt state — i.e. the last continuous-trading print.
- Cancel-quotations are **not** accepted during Phase 3 — the entire remaining session is dark [KRX-TOUR-KOSPI-OPS-T2].

### Daily-cap and end-of-day rules

The Enforcement Rule limits how often each phase may fire and when it may fire [KRX-RULE-KOSPI-BR-ENFORCE-KO §39.2]:

- **Once-per-day per phase.** Each of phases 1 and 2 may fire at most once during the trading day; their conditions are evaluated against the *first* occurrence of the trigger only.
- **No-fire window before close.** Phases 1 and 2 do **not** fire after **14:50 KST** (40 minutes before 장종료). The closing-call receipt window opens at 15:20, and the rule reserves at least 30 minutes between any phase-2 resumption and the close.
- **Phase 3 has no late-session carve-out.** Phase 3 may fire even within the last 40 minutes — closing the market for the day rather than resuming. The proviso in §39.2 explicitly states that "the [phase-3] halt and termination of trading shall apply even after 40 minutes before 장종료" [KRX-RULE-KOSPI-BR-ENFORCE-KO §39.2 proviso].

### 1-minute persistence — clock start

The 1-minute persistence requirement for phase 1 is anchored on the post-open clock — the clock starts **1 minute after 장개시 (09:00 KST)** [KRX-RULE-KOSPI-BR-ENFORCE-KO §39.4]. So the very-earliest a phase-1 CB can fire is 09:02 (1 minute clock start at 09:01 + 1 minute persistence). This rule was added 2020-11-26 to prevent CB triggers on the opening-print transient. The same start-after-1-minute behavior is **not** explicitly stated for the phase-2 and phase-3 persistence clocks; their 1-minute persistence logically starts the moment the prior-phase reset is complete, but the rule text is silent.

### Halt-period quotation behavior

During a Phase 1 / Phase 2 halt, the §13.1.1 halt-quotation rule applies [KRX-RULE-KOSPI-BR-ENFORCE-KO §13.1.1]:

- Any quotation submitted **during** the halt has no effect.
- A **cancellation** quotation submitted during the halt **is** honored — including bulk-cancel under §17-2 (disconnect-cancel) [KRX-RULE-KOSPI-BR-ENFORCE-KO §13.1.1 proviso].

This treatment is identical to the within-day individual-issue halt rule discussed in [Trading Rules § Cancellation, correction, and disconnect-cancel](./trading_rules.md#cancellation-correction-and-disconnect-cancel) — a CB just scopes the same mechanism market-wide.

During a Phase 3 close, the §13.1.1 proviso for cancels **does not apply** — the market is fully closed, and the cancel-during-halt behavior of phases 1/2 is replaced by a hard rejection of all submissions [KRX-TOUR-KOSPI-OPS-T2]. (Members holding undesired open quotations through a Phase 3 close must wait until the next trading day to act on them.)

### Interaction with VI and other stabilization

CB takes precedence over per-issue stabilization mechanisms [KRX-TOUR-KOSPI-OPS-T9]:

- **CB cancels in-progress VI.** When a CB fires while a VI-triggered single-price call auction is running on any individual issue, the VI auction is **cancelled**; the issue joins the market-wide halt and resumes via the post-CB resumption auction.
- **CB cancels other stabilization triggers.** Short-term-overheat single-price (§38-2 / §56-2), low-liquidity single-price (§56-3), and method-change first-price auctions (§23.1.5) are similarly cancelled by a CB.

The reverse precedence — VI suppressing CB — is not a defined behavior; CB triggers are evaluated against the index value, not against any individual-issue's tentative print, so VI cannot logically gate a CB.

System-failure halts under §27 of the Business Regulation (or §70 of the Enforcement Rule) are **separate** from CBs — they are operational, not market-state-driven, and do not consume the daily phase-1/2 caps.

### Relationship to individual-issue halts

CB is a **market-wide** halt. Individual-issue halts are a separate mechanism, governed by §26 of the Business Regulation (and the Listing / Disclosure Regulations), and used when [KRX-TOUR-KOSPI-OPS-T3]:

- A specific issue is subject to a rumor or a corporate-action disclosure that materially affects price.
- Trading volume or price for a specific issue moves abnormally and pre-disclosure clarification is required.

The standard individual-issue resumption pattern is: **30 minutes** after the post-disclosure inquiry response (per [KRX-TOUR-KOSPI-OPS-T3]), or — if disclosure occurs after 14:30 — resumption from the next trading day. Individual-issue halts do not consume CB phases; they are tracked separately.

## Parameters & thresholds

### Table 1 — CB phases

| Phase | Trigger condition (vs prior trading day's KOSPI close)                          | Persistence | Action                                            | Source                                          |
|-------|----------------------------------------------------------------------------------|------------:|---------------------------------------------------|-------------------------------------------------|
| 1     | KOSPI ≤ 92 % of prior close                                                      |    1 minute | 20-min halt + 10-min single-price resumption call | [KRX-RULE-KOSPI-BR-KO §25.1.1]                  |
| 2     | KOSPI ≤ 85 % of prior close **AND** ≤ 99 % of phase-1 trigger value              |    1 minute | 20-min halt + 10-min single-price resumption call | [KRX-RULE-KOSPI-BR-KO §25.1.2; -ENFORCE §39.1.1]|
| 3     | KOSPI ≤ 80 % of prior close **AND** ≤ 99 % of phase-2 trigger value              |    1 minute | Immediate close for the day                       | [KRX-RULE-KOSPI-BR-KO §25.1.3; -ENFORCE §39.1.2]|

### Table 2 — Daily caps and timing windows

| Rule                                                              | Value                                                            | Source                                          |
|-------------------------------------------------------------------|------------------------------------------------------------------|-------------------------------------------------|
| Maximum CB triggers per day, per phase                            | 1                                                                | [KRX-RULE-KOSPI-BR-ENFORCE-KO §39.2]            |
| Earliest possible Phase 1 trigger time                            | 09:02 KST (clock starts 09:01; 1 min persistence)                | [KRX-RULE-KOSPI-BR-ENFORCE-KO §39.4]            |
| Latest possible Phase 1 / Phase 2 trigger time                    | 14:50 KST (40 min before 15:30 close)                            | [KRX-RULE-KOSPI-BR-ENFORCE-KO §39.2]            |
| Latest possible Phase 3 trigger time                              | No upper bound — applies through the entire session              | [KRX-RULE-KOSPI-BR-ENFORCE-KO §39.2 proviso]    |

### Table 3 — Quotation behavior by phase

| Phase            | New orders | Corrections | Cancellations | Disconnect-cancel | Source                                      |
|------------------|------------|-------------|---------------|-------------------|---------------------------------------------|
| Phase 1 / Phase 2 halt (20 min)  | rejected   | rejected    | accepted      | accepted          | [KRX-RULE-KOSPI-BR-ENFORCE-KO §13.1.1]      |
| Phase 1 / Phase 2 resumption call (10 min)  | accepted | accepted | accepted      | accepted          | [KRX-RULE-KOSPI-BR-KO §23.1.2; -ENFORCE §35.1] |
| Phase 3 close      | rejected   | rejected    | rejected      | rejected          | [KRX-TOUR-KOSPI-OPS-T2]                     |

## Worked examples

### Example A — Phase 1 trigger and resumption

Prior trading day's KOSPI close: **2,500.00**. Trading begins at 09:00 KST. KOSPI moves down through the morning. At 11:14, KOSPI hits **2,300.00** (= 92 % of 2,500.00 = the phase-1 threshold). KOSPI continues to trade below 2,300.00 — at 11:15 it is 2,295.50, at 11:16 it is 2,289.10, ...

- **11:15:00** — first crossing below 2,300.00 sustained at the second-by-second tick. Persistence clock starts.
- **11:16:00** — 1 minute elapsed and KOSPI still ≤ 2,300.00. **Phase 1 fires.**
- **11:16–11:36** — 20-minute halt. KOSPI continues to be calculated for reference (futures markets are also halted), but the spot market accepts only cancel-quotations [KRX-RULE-KOSPI-BR-ENFORCE-KO §13.1.1].
- **11:36–11:46** — 10-minute single-price resumption-call receipt window opens. Standard §22 price-then-time priority [KRX-TOUR-KOSPI-OPS-T9 — VI doc shows the same matching mechanism]. KRX may add a random-end of up to 30 s under §35.1.
- **11:46:xx** — auction clears at, say, KOSPI implied value 2,278. Continuous trading resumes. The "phase-1 trigger value" — 2,300.00 — becomes the anchor for any future phase-2 evaluation.

### Example B — Phase 2 fires after additional 1 % drop

Continuing from Example A. After resumption, KOSPI continues to slide. By 13:50 it has reached **2,125.00** (= 85.0 % of 2,500.00). Phase 2's absolute threshold (15 %) is met. But the phase-2 carve-out also requires KOSPI to be ≤ 99 % of the **phase-1 trigger value (2,300)** = ≤ 2,277. 2,125 ≤ 2,277 → carve-out condition satisfied.

- 13:50:00 — both threshold conditions satisfied. Persistence clock starts.
- 13:51:00 — 1 minute elapsed and KOSPI still meets both conditions. **Phase 2 fires.**
- 13:51–14:11 — 20-min halt.
- 14:11–14:21 — 10-min resumption call.
- 14:21:xx — auction clears at, say, KOSPI implied 2,090. Continuous trading resumes. The "phase-2 trigger value" — 2,125 — becomes the anchor for any future phase-3 evaluation.

### Example C — Phase 1 cannot fire after 14:50

Same prior-day close (2,500.00). By 14:51 KOSPI has reached 2,290.00 (= 91.6 % of prior close, = phase-1 threshold met by 0.4 %). Persistence clock starts at 14:51:00.

- 14:52:00 — 1 minute elapsed and KOSPI is still below 2,300.00. **But the time of the trigger evaluation, 14:52:00, is after 14:50** — the §39.2 cutoff [KRX-RULE-KOSPI-BR-ENFORCE-KO §39.2]. **Phase 1 does not fire.**
- KOSPI continues to slide. By 15:00 it reaches 2,000.00 (= 80 % of prior close, = phase-3 threshold met).
- Phase 3's carve-out requires ≤ 99 % of phase-2 trigger value — but Phase 2 never fired today. The phase-3 anchor falls back to the prior-day close [KRX-RULE-KOSPI-BR-ENFORCE-KO §39.1.2 — implicit when prior phase did not occur]. Persistence clock starts at 15:00:00.
- 15:01:00 — 1 minute elapsed; KOSPI still ≤ 2,000. **Phase 3 fires** — even though we are inside the 40-min-before-close window [KRX-RULE-KOSPI-BR-ENFORCE-KO §39.2 proviso]. Market closes immediately for the day; closing print determined by the §38-2 / §51 last-pre-halt-state rules.

## Edge cases & open questions

- Edge case: §39.1.2 does not explicitly handle the case where Phase 2 did not fire (because either the +1 % carve-out wasn't met or the 14:50 cutoff was crossed) and KOSPI then drops to ≥ 20 %. The natural reading is that Phase 3 then evaluates against the prior-day close alone (no earlier-phase anchor exists), but the rule text reads the carve-out conditions in the affirmative. Verify against any KRX implementation guide before relying on Example C's phase-3-without-phase-2 path.
- Edge case: The 1-minute persistence clock for Phase 1 starts 1 minute after 장개시 (09:01) per §39.4. Whether the same clock-start is implicitly applied to Phase 2 / Phase 3 (i.e. immediately after a prior-phase resumption print) is not stated. The conservative interpretation is that the persistence clock for Phase 2 starts at the moment KOSPI re-crosses the threshold after the Phase 1 resumption auction completes; verify against KRX implementation.
- Edge case: §25 of the Business Regulation defines CB only on the **downside** ("8 % or more **decline**"). KRX has no upside-CB mechanism; large upside moves are addressed via per-issue VI (Static and Dynamic) and via the daily price-limit band [KRX-RULE-KOSPI-BR-KO §20]. Algorithmic strategies symmetrically positioned on the index should treat upside and downside risk asymmetrically with respect to halt probability.
- Edge case: §13.1.1 honors cancel-quotations during Phase 1/Phase 2 halts but does not explicitly extend the same rule to corrections. Per §13.1, corrections require both a price-or-type change and a quantity-preservation property; logically a correction is a (cancel + new-quote) atomic, and §13.1.1 forbids the new-quote leg. The only safe modification during a halt is therefore a pure cancel.
- Open question: Bond market is not halted by a CB (the OPS-T2 tour explicitly says "except bond market"); the rule article §25 reads as scoped to "주식시장 등" (stock market etc.). Whether ETF and ETN markets are included — they are listed under §4.1.2/2-2, separate from §4.1.1 stock — is not explicit in §25. The tour says "trades of all products" are halted, which suggests inclusion. Verify against ETF / ETN market-rule provisions before relying on a particular treatment.
- Open question: Phase 2's "+1 % from phase-1 trigger value" anchor uses the index value at the **moment the §25.1.1 condition was first met**, not the index value at the moment Phase 1 was *triggered* (which is 1 minute later). Whether the 1-minute persistence clock's start moment or end moment is the anchor is not crystal in §25.1.2 or §39.1.1; the natural reading is that the trigger time (i.e. the persistence-clock end) is the anchor. Confirm before designing strategies that assume the precise reference.
- Unsourced claim: [KRX-TOUR-KOSPI-OPS-T2] notes that the receipt of orders in linked KRX futures and options markets is also halted during phase 1/2. The §25 article scopes to "주식시장 등" and the actual derivatives-market halt is governed by the Derivatives Market Business Regulation §27; the cross-market coupling is operational rather than spelled out in the KOSPI BR. Treat the linked-derivatives-halt claim as accurate but operational.

## Sources

- `KRX-RULE-KOSPI-BR-KO` — KOSPI Market Business Regulation (유가증권시장 업무규정, *yu-ga-jeung-gwon si-jang eom-mu gyu-jeong*), bookid 210200859, effective 2026-04-28. Articles cited: §6 (Market pause and reopen — referenced for the 20-min halt mechanism), §20 (Daily price limit — referenced for upside-handling discussion), §23 (Single-price auction — used for resumption call), §25 (Index-level CB — central article: 8 % / 15 % / 20 % thresholds, action by phase), §26 (Individual-issue halt — referenced for individual vs market-wide distinction), §27 (System-failure halt — referenced for the system-vs-CB distinction).
- `KRX-RULE-KOSPI-BR-ENFORCE-KO` — KOSPI BR Enforcement Rule (유가증권시장 업무규정 시행세칙, *yu-ga-jeung-gwon si-jang eom-mu gyu-jeong si-haeng se-chik*), bookid 210203562, effective 2026-04-28. Articles cited: §13 (Quotation effect during halt — cancel-only behavior), §17-2 (Disconnect-cancel — referenced), §35.1 (Single-price receipt window with random-end — used for resumption call), §38-2 / §51 (Closing-price determination — referenced for the post-Phase-3 print), §39 (CB implementation — additional-1 %-drop carve-out, daily caps, 14:50 cutoff, Phase-3-applies-late-in-session proviso, 09:01-clock-start), §70 (System-failure halt — referenced as separate-from-CB).
- `KRX-TOUR-KOSPI-OPS-T2` — KRX overview "Circuit Breakers"; English, not authoritative. Used for the cancel-only-during-phase-1/2 halt-behavior, no-orders-in-phase-3, and the linked-derivatives-halt claim (flagged as operational). Also confirms the once-per-phase-per-day cap and the 14:50 / 40-min cutoff.
- `KRX-TOUR-KOSPI-OPS-T3` — KRX overview "Suspension of individual issues & resumption"; English, not authoritative. Used only for the individual-issue-halt resumption pattern (30-minute post-disclosure resumption; next-day if disclosure after 14:30) — included for the CB-vs-individual-halt distinction.
