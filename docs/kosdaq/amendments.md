---
title: "Order Amendments — Cancel & Correct (KOSDAQ)"
markets: [KOSDAQ]
last_reviewed: 2026-05-01
sources:
  - KRX-RULE-KOSDAQ-BR-KO
  - KRX-TOUR-KOSDAQ-METHOD-T5
---

> See also: [Order Amendments (KOSPI)](../kospi/amendments.md), [Order Types (KOSDAQ)](./order_types.md), [Trading Rules (KOSDAQ)](./trading_rules.md), [Auctions (KOSDAQ)](./auctions.md), [Comparison](../common/comparison.md).

**Delta file.** KOSDAQ cancel-and-correct substance is **believed identical to KOSPI**: same cancel-only-on-unfilled-quantity rule, same partial-cancel-preserves-time-priority vs correction-resets-time-priority asymmetry, same correction transformation matrix (same-type with Δp, cross-type with the same-deemed-price rejection proviso), same stop-limit pre-vs-post-activation correction rules added 2025-02-27, same bulk-cancel (HSA-only by HSA-ID) and disconnect-cancel (session-keyed) facilities. The deltas are: (1) **KOSDAQ has no general "cancel and correct" BR article** — KOSPI §13 has the high-level cancel-only-on-unfilled rule explicitly; on KOSDAQ this rule is fully delegated to the Enforcement Rule via §9.4; (2) **disconnect-cancel sits at §16-2** on KOSDAQ (vs KOSPI §13-2); (3) **R6 affects this topic more than any other** — virtually every parameterized rule (correction matrix, time-priority reset, bulk-cancel HSA-keying, partial-cancel competitive-block proviso) is in the KOSDAQ Enforcement Rule, which is not yet archived. This file points to the [KOSPI write-up](../kospi/amendments.md) for shared content and records the structural deltas.

## Summary

- An already-placed quotation may be cancelled or corrected only with respect to its **unfilled** quantity; filled portions are immutable. KOSDAQ delegates this rule to the Enforcement Rule via [KRX-RULE-KOSDAQ-BR-KO §9.4] ("호가에 관하여 필요한 사항은 세칙으로 정한다"; "matters concerning quotations shall be determined by the Enforcement Rule"). KOSPI's analogue is the explicit BR §13.1.
- **Cancellation** (취소, *chwi-so*): partial cancel **preserves the receipt time** of the remaining quantity for §17.2.2 time-priority purposes; full cancel removes the order entirely. Same rule as KOSPI [KRX-RULE-KOSPI-BR-ENFORCE-KO §17.1] — the KOSDAQ Enforcement Rule analogue cannot yet be cited (R6 unresolved).
- **Correction** (정정, *jeong-jeong*): permitted only when it results in a different price OR a different quotation type — pure quantity changes are not allowed via correction; reductions go through partial cancel and increases require a new quotation. A correction **resets** the §17.2.2 time priority. Same rule as KOSPI [KRX-RULE-KOSPI-BR-ENFORCE-KO §17.2 / §17.3]; KOSDAQ ER analogue not yet citable.
- **Stop-limit correction** (added 2025-02-27 on both books): before activation, the correction must change the limit price OR the stop price; after activation (i.e. the stop-limit has converted to a regular limit), the correction must change the limit price. Same rule as KOSPI; KOSDAQ ER §17.2.1-2 analogue not yet citable.
- **Bulk-cancel** and **disconnect-cancel** facilities: bulk-cancel is HSA-only by HSA-ID (per the KOSDAQ Enforcement Rule analogue of KOSPI ER §17-2); **disconnect-cancel is in [KRX-RULE-KOSDAQ-BR-KO §16-2]** (added 2022-12-07, the analogue of KOSPI BR §13-2 with the same effective date and substantively identical text). Disconnect-cancel scope is per-session, not per HSA-ID — same as KOSPI.

## Detailed rules

For full prose on the cancel-only-on-unfilled rule, the partial-cancel-preserves-time-priority vs correction-resets-time-priority asymmetry, the §17.2 correction transformation matrix (same-type with Δp; cross-type with the proviso that limit ↔ best-counter ↔ best-same crosses are rejected when post-correction price equals pre-correction deemed price), the §17.2.1-2 stop-limit pre-vs-post-activation correction rules, the §17.1 competitive-block partial-cancel minimum-size proviso, and the bulk-cancel (HSA-keyed) vs disconnect-cancel (session-keyed) distinction, see [KOSPI § Detailed rules](../kospi/amendments.md#detailed-rules). The KOSDAQ articles map:

| KOSDAQ BR article | KOSPI BR article | Topic                                                                |
|-------------------|------------------|----------------------------------------------------------------------|
| §9.4              | §13              | Cancel-and-correct — KOSDAQ delegates entire framework to ER; KOSPI has explicit §13 with §13.1 cancel-only-on-unfilled |
| §16-2             | §13-2            | Disconnect-cancel (접속해제 호가취소) — added 2022-12-07 in both books |
| §27               | §28              | Error-trade correction by KRX                                          |
| §27-2             | §28-2            | Mass-erroneous-trade relief — both books, added 2015-11-04            |
| KOSDAQ ER (R6)    | ER §17           | Cancel-and-correct full mechanics (R6 unresolved)                      |
| KOSDAQ ER (R6)    | ER §17-2         | Bulk cancel (HSA-keyed) — rewritten 2022-12-22 on KOSPI side          |
| KOSDAQ ER (R6)    | ER §17-3         | Disconnect-cancel full mechanics — rewritten 2022-12-22                |
| KOSDAQ ER (R6)    | ER §15-2         | Stop-limit time-priority retention — referenced for §17.2.1-2 / §17.3 interaction |

### Delta vs KOSPI

#### KOSDAQ has no general cancel-and-correct BR article

KOSPI BR §13 is a dedicated "취소 및 정정" (Cancel and correct) article that establishes the unfilled-only-scope rule explicitly (§13.1) and delegates further mechanics to the Enforcement Rule (§13.2). KOSDAQ has **no** parallel article — KOSDAQ §13 is the sidecar article. The cancel-and-correct framework on KOSDAQ is entirely embedded within:

- §9.4: "호가입력의 제한, 조건부지정가호가의 전환, 스톱지정가호가의 지정가호가로서의 효력 발생 우선순위, **그 밖에 호가에 관하여 필요한 사항은 세칙으로 정한다**" — "input restrictions, conditional-limit conversion, stop-limit activation priority, and other matters concerning quotations shall be determined by Enforcement Rule." The "other matters concerning quotations" catch-all is what carries cancel-and-correct delegation on KOSDAQ.
- §16-2: disconnect-cancel facility (added 2022-12-07).
- §27: error-trade correction by KRX (member-side request to KRX to fix an error during the matching process).
- §27-2: mass-erroneous-trade relief (member-side request for relief from a fat-finger trade — see [Trading Rules § Delta vs KOSPI](./trading_rules.md#delta-vs-kospi)).

Substantively, the rule outcome is the same: cancel/correct unfilled portions, with partial-cancel preserving and correction resetting time priority. But the KOSDAQ structural choice means there is no clean, citation-able BR article for the unfilled-only rule itself — every parameterized rule (the correction transformation matrix, the time-priority reset on correction, the partial-cancel competitive-block minimum-size proviso, the stop-limit pre-vs-post activation correction rule, the bulk-cancel HSA-keying, the disconnect-cancel session-keying detail) lives in the KOSDAQ Enforcement Rule, which is not yet archived (R6).

This is the **most R6-affected topic** in the project. Until the KOSDAQ Enforcement Rule is archived, KOSDAQ-side amendment-rule citations cannot match the KOSPI-side depth. Phase 6 freshness audit must re-pull every parameterized claim once R6 resolves.

#### Disconnect-cancel article number — KOSDAQ §16-2 vs KOSPI §13-2

Both books added their disconnect-cancel BR article on 2022-12-07. The text is substantively identical:

> 회원은 회원시스템과 거래소시스템의 연결이 해제된 것으로 인정되는 상황으로서 세칙으로 정하는 경우에는 일정한 범위의 호가를 한꺼번에 취소할 것(이하 "접속해제 호가취소"라 한다)을 사전에 거래소에 신청할 수 있고, 이 경우 거래소는 세칙에서 정하는 바에 따라 호가를 취소할 수 있다.

Translation: a member may pre-register, with KRX, a "disconnect-cancel" (접속해제 호가취소) rule that triggers a bulk cancel of a defined range of quotations when the member-system loses its connection to KRX. Detailed mechanics (e.g. session-keying, the cross-session-correction-withdraws-from-pool rule, the debt-securities exclusion, the system-failure-decline carve-out) are in the Enforcement Rule (KOSDAQ ER §17-3 analogue, R6 unresolved).

The article-number difference (KOSDAQ §16-2 vs KOSPI §13-2) is consistent with the broader article-numbering offset between the two books: KOSDAQ's market-administration / quote-control cluster sits at §13–§16-2, while KOSPI's sits at §11-2 / §13 / §13-2.

#### Bulk cancel — KOSDAQ also has it, but BR-side article number unclear

KOSPI ER §17-2 (rewritten 2022-12-22) is the bulk-cancel (일괄호가취소, *il-gwal ho-ga chwi-so*) article. The KOSDAQ Enforcement Rule analogue is R6-unresolved; the KOSDAQ BR doesn't have a high-level bulk-cancel article (KOSPI doesn't either — bulk cancel is entirely in the ER on both books). HSA registration on KOSDAQ is at §50-3 (vs KOSPI §104-3) — see [Trading Rules § Delta vs KOSPI](./trading_rules.md#delta-vs-kospi); bulk-cancel eligibility on KOSDAQ should follow the same HSA-only gating, but the ER Annex 1-3-equivalent for KOSDAQ has not been pulled.

#### Mass-erroneous-trade relief — already covered in `trading_rules.md`

KOSDAQ §27-2 is the mass-erroneous-trade-relief article. Detailed write-up is in [Trading Rules § Delta vs KOSPI](./trading_rules.md#delta-vs-kospi) under the Mass-erroneous-trade relief subsection. The relevant cross-link from amendments to trading_rules is: when a fat-finger trade prints, the cancel-and-correct framework alone cannot unwind it (§17.1's general unfilled-only rule means a print is final), but the §27-2 mass-erroneous-trade-relief mechanism may unwind it on member request, subject to KRX discretion and ER-defined criteria.

KOSDAQ §27-2 has a **narrower security scope** than KOSPI §28-2: KOSDAQ excludes ETF / ETN / ELW from relief eligibility (KOSDAQ-listed ETF / ETN errors revert to the §17.1 finality rule). KOSPI §28-2 includes ETFs / ETNs / ELWs / beneficiary certs.

## Parameters & thresholds

### Table 1 — Cancel and correct effect on time priority (KOSDAQ — believed identical to KOSPI)

| Operation                                  | Time priority of remaining quantity                              | Source                                          |
|--------------------------------------------|------------------------------------------------------------------|-------------------------------------------------|
| Partial cancel                             | Preserved at original receipt time                               | KOSDAQ ER analogue of KOSPI ER §17.1 (R6 unresolved); per KOSPI [KRX-TOUR-KOSPI-BASIC-T3] descriptive language |
| Full cancel                                | n/a (entire quantity removed)                                    | KOSDAQ ER analogue of KOSPI ER §17.1 (R6)       |
| Correction (any type)                      | Reset to correction's receipt time                               | KOSDAQ ER analogue of KOSPI ER §17.3 (R6)       |
| New quotation                              | New receipt time for the entire new quantity                     | [KRX-RULE-KOSDAQ-BR-KO §14.1]                   |
| Stop-limit, post-activation correction     | Reset to correction's receipt time (overrides ER §15-2 retention) | KOSDAQ ER analogue of KOSPI ER §17.2.1-2.b / §17.3 (R6) |

### Table 2 — Bulk-cancel and disconnect-cancel (KOSDAQ)

| Facility                  | Trigger                                  | Scope                                                                | Eligibility                       | Source                                          |
|---------------------------|------------------------------------------|----------------------------------------------------------------------|------------------------------------|-------------------------------------------------|
| Bulk cancel (일괄호가취소) | Member-initiated risk-management request | All unfilled, by HSA ID within an issue                              | HSA-registered traders only        | KOSDAQ ER analogue of KOSPI ER §17-2 (R6 unresolved); KOSDAQ HSA registration at [§50-3] |
| Disconnect cancel (접속해제 호가취소) | Member-system disconnect from Exchange   | All unfilled submitted via the pre-registered session                | Any member; pre-registration required | [KRX-RULE-KOSDAQ-BR-KO §16-2]                  |

Both facilities exclude debt-securities trading from scope (per the KOSDAQ ER §17-3.3 analogue, R6 unresolved). Mass-erroneous-trade relief — see [Trading Rules § Delta vs KOSPI](./trading_rules.md#delta-vs-kospi) — is the only mechanism that can unwind a *printed* trade (vs cancel/correct, which apply only to unfilled quantity).

## Worked examples

The KOSPI worked examples — Example A (partial cancel preserving time priority on a 1,000-share buy limit), Example B (same-type correction resetting time priority), Example C (cross-type correction with same deemed price → rejected), Example D (stop-limit correction before vs after activation) — all carry over to KOSDAQ unchanged because the underlying rules (in the KOSDAQ Enforcement Rule, believed to mirror KOSPI ER §17 / §15-2 verbatim) follow the same mechanics. See [KOSPI § Worked examples](../kospi/amendments.md#worked-examples).

The only KOSDAQ-specific consideration is that confidence in the parameter values (Δp must change, post-correction price ≠ pre-correction deemed price for the cross-type-rejection proviso, stop-price-on-tick check, etc.) depends on R6 resolution. Until then, treat the KOSPI-side parameters as **strongly inferred** for KOSDAQ via the parallel BR structure, with R6 / Phase 6 cross-check required before relying on a particular numeric threshold.

## Edge cases & open questions

- Edge case: KOSDAQ has no general cancel-and-correct BR article. The §9.4 "other matters concerning quotations" delegate is the structural anchor; the substantive rule (cancel only on unfilled, partial-cancel-preserves-priority, correction-resets-priority) is in the KOSDAQ Enforcement Rule. R6 unresolved means the unfilled-only rule cannot be cited authoritatively from a KOSDAQ BR article — only via the KOSPI cross-reference.
- Edge case: KOSDAQ §16-2 (disconnect-cancel) is the only cancel-and-correct article in the KOSDAQ BR. The article gives only the high-level enabling rule; detailed session-keying, debt-securities exclusion, system-failure-decline carve-out, and the cross-session-correction-withdraws-from-pool rule are in the KOSDAQ Enforcement Rule (R6 unresolved).
- Edge case: The 2025-02-27 stop-limit-correction rules (§17.2.1-2 on KOSPI ER) are the most-recently-added cancel-and-correct provisions on KOSPI. The KOSDAQ ER analogue effective date is believed to be the same (2025-02-27), since the BR-side stop-limit definition was added 2025-02-05 in lockstep across both books. Cross-check at R6 / Phase 6.
- Edge case: KOSDAQ §27-2 mass-erroneous-trade relief excludes ETF / ETN / ELW from the eligible-security list (vs KOSPI §28-2 including them). For a KOSDAQ-listed ETF / ETN fat-finger error, no relief mechanism applies — the §17.1 finality rule binds. ELW is moot on KOSDAQ (no ELW listings); ETF / ETN listings exist and are exposed to this scope gap.
- Open question: KOSDAQ ER analogue of KOSPI ER §17.1 competitive-block partial-cancel minimum-size proviso — KOSPI restricts a competitive-block (A-Blox) partial cancel to one that leaves residual ≥ KRW 500M (or ≥ KRW 200M on KOSDAQ per [Auctions § A-Blox](./auctions.md#delta-vs-kospi)?). Whether the KOSDAQ ER applies the same KRW 200M minimum proviso to KOSDAQ A-Blox partial cancels is unresolved; the KOSDAQ A-Blox tour table doesn't address partial-cancel minimums.
- Open question: KOSDAQ ER analogue of KOSPI ER §17-2 (bulk cancel) Annex 1-3 — the KOSPI Annex enumerates bulk-cancel cancel conditions (HSA ID + issue + cancel-now message). The KOSDAQ ER Annex 1-3 has not been pulled (R6); whether KOSDAQ supports the same per-condition member-initiated bulk-cancel triggers (e.g. P&L threshold, exposure threshold) cannot yet be confirmed.
- Open question: KOSPI ER §17.2.2 "same deemed price → reject" cross-type proviso applies only to the limit ↔ best-counter ↔ best-same triangle. On KOSDAQ, the §2.4 sub-paragraph index swap (best-counterparty=§2.4.3, conditional-limit=§2.4.5; KOSPI uses opposite ordering — see [Order Types § Detailed rules](./order_types.md#detailed-rules)) means the type-name-to-index-number mapping differs. The substantive proviso (same deemed price → reject) should still apply to the same triangle of types on KOSDAQ; the article cross-reference is by type name in the ER, not by sub-paragraph index. Cross-check at R6.

## Sources

- `KRX-RULE-KOSDAQ-BR-KO` — KOSDAQ Market Business Regulation (코스닥시장 업무규정), bookid 210164370, effective 2026-04-28. Articles cited: §9.4 (Quotation submission — delegates "other matters concerning quotations" to the Enforcement Rule, which is where the cancel-and-correct framework lives on KOSDAQ; KOSPI has the explicit §13 instead), §14.1 (Quotation recording in receipt order — referenced for new-quote-receipt-time behavior), §16-2 (**Disconnect-cancel** — added 2022-12-07; the analogue of KOSPI BR §13-2 with substantively identical text), §27 (Error-trade correction by KRX — referenced), §27-2 (Mass-erroneous-trade relief — added 2015-11-04 in both books; KOSDAQ §27-2 has narrower security scope than KOSPI §28-2 — full write-up in [Trading Rules § Delta vs KOSPI](./trading_rules.md#delta-vs-kospi)), §50-3 (HSA-trader registration — referenced for bulk-cancel eligibility).
- `KRX-TOUR-KOSDAQ-METHOD-T5` — KRX overview "Limit Orders / Order types" (KOSDAQ); English, not authoritative. Used for the cancellation-vs-correction descriptive language: "Cancellations, in part or whole, allowed" and "Price corrections allowed. Quantity corrections, in part or whole, allowed when converting into a market order [or limit order]." The corresponding rulebook articles for the time-priority effects of partial cancel vs correction are in the KOSDAQ Enforcement Rule (R6 unresolved).
