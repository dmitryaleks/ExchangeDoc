---
title: "Order Amendments — Cancel & Correct (KOSPI)"
markets: [KOSPI]
last_reviewed: 2026-04-30
sources:
  - KRX-RULE-KOSPI-BR-KO
  - KRX-RULE-KOSPI-BR-ENFORCE-KO
  - KRX-TOUR-KOSPI-BASIC-T3
---

> See also: [Order Amendments (KOSDAQ)](../kosdaq/amendments.md), [Order Types (KOSPI)](./order_types.md), [Trading Rules (KOSPI)](./trading_rules.md), [Auctions (KOSPI)](./auctions.md), [Comparison](../common/comparison.md).

## Summary

- An already-placed quotation (호가, *ho-ga*) may be cancelled or corrected only with respect to its **unfilled** quantity; filled portions are immutable [KRX-RULE-KOSPI-BR-KO §13.1].
- **Cancellation** may be partial or full. A partial cancel **preserves the receipt time** of the remaining quantity for §22.2.2 time-priority purposes [KRX-RULE-KOSPI-BR-ENFORCE-KO §17.1; KRX-TOUR-KOSPI-BASIC-T3].
- **Correction** is permitted only when it results in a **different price** or a **different quotation type** — pure quantity changes are not allowed via correction; reductions go through partial cancel and increases require a new quotation [KRX-RULE-KOSPI-BR-ENFORCE-KO §17.2; KRX-TOUR-KOSPI-BASIC-T3]. A correction **resets** the §22.2.2 time priority of the corrected quantity to the correction's receipt time [KRX-RULE-KOSPI-BR-ENFORCE-KO §17.3].
- Stop-limit (스톱지정가호가, *seu-top ji-jeong-ga ho-ga*) correction depends on activation state: **before activation** the correction must change the limit price *or* the stop price; **after activation** (i.e. the stop-limit has converted to a regular limit per §15-2) the correction must change the limit price [KRX-RULE-KOSPI-BR-ENFORCE-KO §17.2.1-2]. *(Added 2025-02-27.)*
- Two member-level bulk-cancel facilities are available for risk management: **bulk-cancel (일괄호가취소, *il-gwal ho-ga chwi-so*)** — HSA-trader-only, by HSA-ID — and **disconnect-cancel (접속해제 호가취소, *jeop-sok-hae-je ho-ga chwi-so*)** — pre-registered cancel rule that fires when the member-system loses its session connection [KRX-RULE-KOSPI-BR-ENFORCE-KO §17-2, §17-3].

## Detailed rules

### Scope of cancel and correct

Article 13 of the Business Regulation establishes the basic principle [KRX-RULE-KOSPI-BR-KO §13.1]:

> Cancellation and correction of a quotation shall apply only to the quantity for which a trade has not yet been concluded.

Filled quantity is final at the moment of match; no rule mechanism exists to undo a print. The full procedural detail of what a member may cancel, what may be corrected, and into what, is delegated to the Enforcement Rule [KRX-RULE-KOSPI-BR-KO §13.2].

### Cancellation

A member may cancel all or part of a quotation's unfilled quantity [KRX-RULE-KOSPI-BR-ENFORCE-KO §17.1]. The behavioral rules:

- **Partial cancel preserves time priority** for the remaining quantity. A 1,000-share order that has had 200 shares filled, then has its remaining 800 partially cancelled to 500, retains its original receipt time for §22.2.2 priority on the surviving 500 [KRX-TOUR-KOSPI-BASIC-T3]. Compare with a correction, which resets time priority — see *Correction* below.
- **Competitive-block (경쟁대량매매호가) partial cancel** is only allowed if the post-cancel remaining quantity still satisfies the minimum quantity requirements set in [KRX-RULE-KOSPI-BR-ENFORCE-KO §48-2.3, §51-3.3] (i.e. the A-Blox / off-hours competitive-block minimum order size — see [Auctions § A-Blox](./auctions.md#a-blox-auction-based-block-trade)) [KRX-RULE-KOSPI-BR-ENFORCE-KO §17.1 proviso]. A partial cancel that would drop the order below the minimum is rejected; the member must full-cancel and re-place if they intend to size down past the threshold.
- **Quantity increase is not a cancel.** To increase the quantity of an existing order, the member submits a fresh quotation; the new quotation gets a fresh receipt time. There is no "correction to add quantity" path.

Cancel quotations are honored even during a trading halt [KRX-RULE-KOSPI-BR-ENFORCE-KO §13.1.1 proviso] — see [Trading Rules § Cancellation, correction, and disconnect-cancel](./trading_rules.md#cancellation-correction-and-disconnect-cancel) for the halt-period rule. They are *not* honored during a Phase-3 circuit breaker [KRX-TOUR-KOSPI-OPS-T2 — see Circuit Breakers](./circuit_breakers.md#halt-period-quotation-behavior).

### Correction — what is allowed

The Enforcement Rule §17.2 lists the permitted correction transformations [KRX-RULE-KOSPI-BR-ENFORCE-KO §17.2]:

1. **Same-type correction** (§17.2.1) — for limit (지정가호가), conditional-limit (조건부지정가호가), best-counterparty limit (최유리지정가호가), and best-same-side limit (최우선지정가호가): the member may correct all or part of the quantity to a **different price**. For best-counterparty and best-same-side, the *deemed* price (per Enforcement Rule §3 / §4) before vs after must differ — see [Order Types § Best-limit pricing rules](./order_types.md#best-limit-pricing-rules).
2. **Stop-limit same-type correction** (§17.2.1-2) — added 2025-02-27:
   - **Before activation:** the limit price OR the stop price must change. (The member can move the trigger up/down without touching the limit, or vice versa.)
   - **After activation:** the limit price must change. The stop price is no longer relevant — the order is now a regular limit.
3. **Cross-type correction** (§17.2.2) — the member may correct from one of {limit, market, conditional-limit, best-counterparty limit, best-same-side limit} to any other type in that set, **except** to/from midpoint or stop-limit. Three cases get special treatment:
   - Limit → best-counterparty or best-same-side.
   - Best-counterparty → limit or best-same-side.
   - Best-same-side → limit or best-counterparty.
   In each of these three cross-corrections, if the **post-correction price** equals the **pre-correction price**, the correction is rejected (no-op). For all other cross-type corrections, the price difference is implicit in the type difference and the correction is accepted.

Correction transformations **not** permitted by §17.2:

- Any correction **involving midpoint or stop-limit as a target type** (other than stop-limit-to-stop-limit). Midpoint and stop-limit are isolated — once placed, they can be cancelled but not converted.
- Any correction that **changes only the quantity** while keeping price and type unchanged. Per [KRX-TOUR-KOSPI-BASIC-T3]: "corrections intending to change the quantity of already placed quotations or intending not to change the price of the quotation is not allowed." Quantity reductions go through partial cancel; increases require a new quotation.

### Correction — time priority impact

A correction takes effect at the moment the correction quotation is received [KRX-RULE-KOSPI-BR-ENFORCE-KO §17.3]:

> When a quotation is corrected pursuant to paragraph 2, its effect shall arise at the time the correction quotation is received.

Operational consequence: **time priority resets** to the correction's receipt time for the entire corrected quantity. A member that places a 10:00 limit at KRW 10,000 and corrects to KRW 10,050 at 11:00 surrenders the 10:00 priority entirely — the corrected order's §22.2.2 time stamp is 11:00.

This is **asymmetric** with partial cancel: a partial cancel preserves time priority for the surviving quantity, while a correction overwrites it. The choice between cancel-and-replace and correct-in-place therefore has different priority cost. For a member sliding a limit up by one tick during a fast market:

- **Correct in place** — single message, time priority resets.
- **Partial-cancel + new quote** — two messages, time priority of the cancelled-portion is irrelevant (gone), new quote gets fresh time.
- Both paths produce the same end-state priority (a brand-new resting order at the new price with the current timestamp), so the trade-off is **latency / atomicity** rather than priority cost. (Correction is atomic; cancel + new is not.)

A safer way to slide a price up while preserving the *original* time priority is impossible by design — KRX deliberately restricts time-priority-preserving amendments to **partial cancel only** [KRX-TOUR-KOSPI-BASIC-T3]. There is no "amend-in-place preserve-priority" path.

### Bulk cancel — 일괄호가취소

A high-speed-algorithmic trader may pre-register a **bulk cancel** condition with KRX [KRX-RULE-KOSPI-BR-ENFORCE-KO §17-2.1]. The conditions for eligibility:

1. The cancel must be for **risk-management purposes**.
2. The quotations being cancelled must be submitted via an HSA-registered account (per [KRX-RULE-KOSPI-BR-KO §104-3.3] — see [Trading Rules § Algorithmic and high-speed-algorithmic trading](./trading_rules.md#algorithmic-and-high-speed-algorithmic-trading)).

Bulk cancel is keyed by **HSA ID within an issue** — i.e. the member nominates "cancel all open quotations for issue X submitted under HSA ID Y." The detailed cancel-condition specification (per-security, per-condition list) is in Annex 1-3 of the Enforcement Rule [§17-2.1].

Operational notes:

- KRX may decline to process a bulk cancel during system failure or other market-administration concern [KRX-RULE-KOSPI-BR-ENFORCE-KO §17-2.2].
- Members must retain bulk-cancel records for 10 years and produce them on KRX request [KRX-RULE-KOSPI-BR-ENFORCE-KO §17-2.3].
- This article was rewritten 2022-12-22; pre-2022 the bulk-cancel mechanism was scoped differently.

### Disconnect cancel — 접속해제 호가취소

A separate facility, disconnect-cancel, fires when the member-system loses its connection to the Exchange system [KRX-RULE-KOSPI-BR-KO §13-2.1; KRX-RULE-KOSPI-BR-ENFORCE-KO §17-3]. Pre-registration steps:

1. Member submits a disconnect-cancel application via the procedure in [KRX-RULE-KOSPI-BR-ENFORCE-KO §17-3.4] (referencing the *Member System Access Guidelines* §8.5).
2. The member specifies the **session** to be cancelled-on-disconnect — disconnect-cancel scope is per session, not per HSA ID [KRX-RULE-KOSPI-BR-ENFORCE-KO §17-3.2].

Behavioral rules:

- The cancel scope is **all unfilled quotations submitted via the registered session** that have not been cancelled or corrected via another session [KRX-RULE-KOSPI-BR-ENFORCE-KO §17-3.2]. Cross-session corrections / cancels effectively withdraw a quotation from the disconnect-cancel pool.
- **Debt-securities trading is excluded** from disconnect-cancel scope [KRX-RULE-KOSPI-BR-ENFORCE-KO §17-3.3].
- KRX may decline to process a disconnect-cancel under system failure [KRX-RULE-KOSPI-BR-ENFORCE-KO §17-3.5].

The combined effect of bulk cancel and disconnect cancel is two layers of risk-management automation: bulk cancel for member-initiated emergency clearing (e.g. detected algorithm misbehavior), disconnect cancel for connectivity-loss safeguarding.

## Parameters & thresholds

### Table 1 — Allowed correction transformations

| From → To              | Limit | Market | Cond-limit | Best-counter | Best-same | Midpoint | Stop-limit |
|------------------------|:-----:|:------:|:----------:|:------------:|:---------:|:--------:|:----------:|
| Limit                  |  ✔ (Δp)  |   ✔    |     ✔      |    ✔ (Δp)    |  ✔ (Δp)   |    ✗     |     ✗      |
| Market                 |   ✔   |   —    |     ✔      |      ✔       |     ✔     |    ✗     |     ✗      |
| Cond-limit             |   ✔   |   ✔    |   ✔ (Δp)   |      ✔       |     ✔     |    ✗     |     ✗      |
| Best-counter           |  ✔ (Δp)  |   ✔    |     ✔      |   ✔ (Δp)     |  ✔ (Δp)   |    ✗     |     ✗      |
| Best-same              |  ✔ (Δp)  |   ✔    |     ✔      |   ✔ (Δp)     |  ✔ (Δp)   |    ✗     |     ✗      |
| Midpoint               |   ✗   |   ✗    |     ✗      |      ✗       |     ✗     |    —     |     ✗      |
| Stop-limit             |   ✗   |   ✗    |     ✗      |      ✗       |     ✗     |    ✗     |  ✔ (Δp/Δs) |

Legend: ✔ = correction permitted; ✗ = correction not permitted (must cancel and re-place); — = same-type same-instance no-op; Δp = price must change; Δs = stop price may change as the differentiating field. Source: [KRX-RULE-KOSPI-BR-ENFORCE-KO §17.2].

For stop-limit (last row), the precise rule depends on activation state — see *Correction — what is allowed* §3 above.

### Table 2 — Cancel and correct effect on time priority

| Operation                                  | Time priority of remaining quantity                              | Source                                          |
|--------------------------------------------|------------------------------------------------------------------|-------------------------------------------------|
| Partial cancel                             | Preserved at original receipt time                               | [KRX-TOUR-KOSPI-BASIC-T3]                       |
| Full cancel                                | n/a (entire quantity removed)                                    | [KRX-RULE-KOSPI-BR-ENFORCE-KO §17.1]            |
| Correction (any type)                      | Reset to correction's receipt time                               | [KRX-RULE-KOSPI-BR-ENFORCE-KO §17.3]            |
| New quotation                              | New receipt time for the entire new quantity                     | [KRX-RULE-KOSPI-BR-KO §14.1]                    |
| Stop-limit, post-activation correction     | Reset to correction's receipt time (overrides §15-2.2 retention) | [KRX-RULE-KOSPI-BR-ENFORCE-KO §17.2.1-2.b, §17.3] |

The last row is worth noting: an unactivated stop-limit retains its original receipt time when activated [KRX-RULE-KOSPI-BR-ENFORCE-KO §15-2.2]. But if the member *corrects* the stop-limit (in either pre- or post-activation state) under §17.2.1-2, the correction's §17.3 reset overrides the §15-2.2 retention. So a strategy that relies on stop-limit pre-staging for time priority (see [Order Types § Stop-limit activation](./order_types.md#stop-limit-activation)) loses that benefit if the limit price is amended post-activation.

### Table 3 — Bulk-cancel and disconnect-cancel

| Facility                  | Trigger                                  | Scope                                                                | Eligibility                       | Source                                          |
|---------------------------|------------------------------------------|----------------------------------------------------------------------|------------------------------------|-------------------------------------------------|
| Bulk cancel (일괄호가취소) | Member-initiated risk-management request | All unfilled, by HSA ID within an issue                              | HSA-registered traders only        | [KRX-RULE-KOSPI-BR-ENFORCE-KO §17-2.1]          |
| Disconnect cancel (접속해제 호가취소) | Member-system disconnect from Exchange   | All unfilled submitted via the pre-registered session                | Any member; pre-registration required | [KRX-RULE-KOSPI-BR-KO §13-2.1; -ENFORCE §17-3] |

Both facilities exclude debt-securities trading from scope (per §17-3.3 for disconnect-cancel; bulk-cancel scope is per Annex 1-3 which mirrors the same exclusion).

## Worked examples

### Example A — partial cancel preserving time priority

A member places a buy limit at KRW 10,000 for 1,000 shares at 10:00:00. By 10:30:00, 200 shares have been filled (residual quantity 800). At 10:31:00 the member partially cancels 300 shares — leaving residual 500.

- The remaining 500 shares carry time priority **10:00:00** [KRX-TOUR-KOSPI-BASIC-T3] — the original receipt time, not the partial-cancel time.
- A new buy limit at KRW 10,000 for 100 shares submitted by another participant at 10:25:00 sits *behind* this 500-share order in the §22.2.2 time-priority queue, even though both face KRW 10,000 simultaneously.

### Example B — same-type correction triggers time-priority reset

A member places a buy limit at KRW 10,000 for 500 shares at 10:00:00. At 10:30:00 the member corrects the price to KRW 10,050 [KRX-RULE-KOSPI-BR-ENFORCE-KO §17.2.1].

- The corrected order takes effect at 10:30:00 receipt time [KRX-RULE-KOSPI-BR-ENFORCE-KO §17.3]. Original 10:00:00 priority is gone.
- A buy limit for 200 shares at KRW 10,050 submitted by another participant at 10:15:00 sits *ahead* of the corrected order — its time stamp 10:15:00 is earlier than the corrected order's 10:30:00.

Compare with the partial-cancel-then-new-place equivalent: cancel the 500 at 10:30:00, place fresh 500 at KRW 10,050 at 10:30:00.001 — same end-state priority. The two paths differ only in atomicity (correction is atomic; cancel-then-place is not).

### Example C — cross-type correction with same deemed price → rejected

A member places a buy best-counterparty limit (최유리지정가호가) for 200 shares at 10:00:00. The book at receipt has lowest ask = KRW 10,500 — so the deemed price is 10,500 [KRX-RULE-KOSPI-BR-ENFORCE-KO §3.2]. At 10:30:00 the member corrects the order to a regular buy limit, specifying price KRW 10,500.

- §17.2.2 cross-type correction (best-counterparty → limit) is normally permitted.
- But the proviso: if the post-correction price equals the pre-correction (deemed) price, the correction is **rejected** [KRX-RULE-KOSPI-BR-ENFORCE-KO §17.2.2 proviso]. Pre = 10,500 (deemed); post = 10,500 (specified) → rejected.
- To effect the same operational outcome, the member must full-cancel and re-place — two messages, no atomic guarantee.

### Example D — stop-limit correction before vs after activation

A member places a sell stop-limit (스톱지정가호가) at 10:00:00 with stop = KRW 10,200, limit = KRW 10,150, quantity 100.

- **Before activation** (last traded price still > 10,200): the member may correct **either** the stop price (e.g. to 10,250) **or** the limit price (e.g. to 10,180), and the correction is accepted under §17.2.1-2.a [KRX-RULE-KOSPI-BR-ENFORCE-KO §17.2.1-2.a]. Time priority resets to the correction's receipt time per §17.3.
- **After activation** (last traded price has crossed below 10,200; stop has activated and the order is now a regular limit at 10,150): the stop price is no longer meaningful; only the limit price may be corrected [KRX-RULE-KOSPI-BR-ENFORCE-KO §17.2.1-2.b]. Time priority resets to the correction time, **overriding** the §15-2.2 retention of the original 10:00:00 receipt time.

A member that wants to preserve the §15-2.2 time-priority benefit must therefore avoid post-activation corrections: full-cancel and accept that the priority is lost, or hold the original.

## Edge cases & open questions

- Edge case: §17.2.2's "same deemed price → reject" rule applies only to the three explicit cross-corrections (limit ↔ best-counter ↔ best-same). For other cross-corrections (e.g. limit → market, market → limit), the type change alone is sufficient and the price-equality check is not run. Algos that bounce a market order back to a limit at the deemed-execution price should not encounter the proviso.
- Edge case: Partial cancel of a competitive-block (경쟁대량매매호가) is allowed only if the residual remains above the §48-2.3 / §51-3.3 minimum (KRW 500,000,000 for A-Blox per [KRX-TOUR-KOSPI-EXCEPT-T4 — referenced from auctions.md]). A cancel that crosses the threshold is rejected, forcing full-cancel-and-replace if the member wants to size down. This is a quiet quirk for block-trade strategies that pre-stage size and trim after partial fills.
- Edge case: §17.3's "correction takes effect at receipt time" applies regardless of whether the correction crosses or improves the existing book. A correction that moves the limit price *toward* the touch (more aggressive) and would have crossed an existing counter-side limit at the original time is matched at the *correction* receipt time against the *current* book — the original time is irrelevant for matching.
- Edge case: A correction that fails any pre-quote check at the member system (e.g. the new price falls outside the daily price-limit band per §12-2.4.b) is not transmitted to KRX — neither the original nor the correction is altered, but the member must explicitly handle this case. Pre-quote rejection of a correction does not auto-cancel the original.
- Open question: §17.2 enumerates eight corrections but does not address corrections involving **competitive-block** (경쟁대량매매호가) as the source or target type. The rule reads as if competitive-block can only be cancelled (with the §17.1 minimum-size proviso), not corrected — but the article does not say so explicitly. Verify against the A-Blox member specification before relying on a non-correction model.
- Open question: The bulk-cancel article (§17-2) was rewritten 2022-12-22 and references Annex 1-3 for cancel-condition specification. Annex 1-3 was not extracted in this document (it sits outside the §17 cluster). Whether bulk-cancel can be triggered by member-side conditions (e.g. P&L threshold, exposure threshold) or only by an explicit cancel-now message is left to Annex 1-3.
- Open question: Disconnect cancel scope is "session-keyed" per §17-3.2 but the rule does not say what counts as a "session" — a TCP connection? An OMnet session? A logical FIX session? The reference to *Member System Access Guidelines* §8.5 likely defines this; that document was not extracted here.
- Unsourced claim: [KRX-TOUR-KOSPI-BASIC-T3] states that a partial cancellation "still has the quotation receipt time unchanged" for the surviving quantity — this is the time-priority-preservation rule. The Enforcement Rule §17 does not state this in the affirmative; it is implied via the absence of any §17.3-style time-reset clause for cancellation. Treat the time-preservation behavior as well-attested but inferred from the rule structure.

## Sources

- `KRX-RULE-KOSPI-BR-KO` — KOSPI Market Business Regulation (유가증권시장 업무규정, *yu-ga-jeung-gwon si-jang eom-mu gyu-jeong*), bookid 210200859, effective 2026-04-28. Articles cited: §13 (Cancel and correct — high-level scope; unfilled-only restriction), §13-2 (Disconnect-cancel — high-level enabling article), §14 (Quotation recording in receipt order — referenced for new-quote-receipt-time behavior), §22 (Priority — referenced for time-priority interactions), §104-3 (HSA registration — referenced for bulk-cancel eligibility).
- `KRX-RULE-KOSPI-BR-ENFORCE-KO` — KOSPI BR Enforcement Rule (유가증권시장 업무규정 시행세칙, *yu-ga-jeung-gwon si-jang eom-mu gyu-jeong si-haeng se-chik*), bookid 210203562, effective 2026-04-28. Articles cited: §13.1.1 (Halt-period cancel-only behavior — referenced), §15-2 (Stop-limit time-priority retention — referenced for post-activation correction interaction), §17 (Cancel and correct — central article: §17.1 cancellation including competitive-block proviso, §17.2 correction transformations including same-type and cross-type with the §17.2.1-2 stop-limit-specific rules added 2025-02-27, §17.3 correction-takes-effect-at-receipt-time / time-priority reset), §17-2 (Bulk cancel — HSA-keyed risk-management cancel; rewritten 2022-12-22), §17-3 (Disconnect-cancel — session-keyed connectivity-loss cancel; rewritten 2022-12-22), §48-2 / §51-3 (Competitive-block minimum quantity — referenced for the §17.1 partial-cancel proviso).
- `KRX-TOUR-KOSPI-BASIC-T3` — KRX overview "What is a quotation?"; English, not authoritative. Used for: the cancellation-preserves-time-priority rule (the rulebook leaves this implicit), the "correction may not change quantity or keep the price unchanged" prohibition, the time-priority-resets-on-correction framing, and the partial-cancel-preserves-receipt-time behavior in plain English.
