---
title: "Order Types & Quotation Conditions (KOSDAQ)"
markets: [KOSDAQ]
last_reviewed: 2026-05-01
sources:
  - KRX-RULE-KOSDAQ-BR-KO
  - KRX-TOUR-KOSDAQ-METHOD-T1
  - KRX-TOUR-KOSDAQ-METHOD-T5
---

> See also: [Order Types (KOSPI)](../kospi/order_types.md), [Auctions (KOSDAQ)](./auctions.md), [Price Ranges (KOSDAQ)](./price_ranges.md), [Comparison](../common/comparison.md).

**Delta file.** KOSDAQ recognizes the **same 8 quotation types** as KOSPI, the **same per-session eligibility matrix**, the **same** conditional-limit conversion at the closing-call open, the **same** stop-limit activation logic, and the **same** IOC / FOK / self-match-prevention conditions [KRX-RULE-KOSDAQ-BR-KO §2; KRX-TOUR-KOSDAQ-METHOD-T5]. The deltas are: (1) the **KOSDAQ-only "1 % rule"** — quotations exceeding 1 % of listed shares are rejected unless block-trading [KRX-TOUR-KOSDAQ-METHOD-T1]; (2) article-numbering remap (KOSDAQ §9 vs KOSPI §9 + §11-2; KOSDAQ §12-2 to §12-6 for the LP framework vs KOSPI's parallel articles); and (3) all granular Enforcement-Rule citations (deemed-price formulas, per-security × per-session matrix, conditional-limit conversion priority, stop-limit activation priority, IOC/FOK semantics) cannot be authoritatively cited until R6 resolves. This file points to the [KOSPI write-up](../kospi/order_types.md) for shared content.

## Summary

- **Eight quotation types**, identical to KOSPI: 지정가 (limit), 시장가 (market), 조건부지정가 (*jo-geon-bu ji-jeong-ga*; conditional-limit, LMC), 최유리지정가 (*choe-yu-ri ji-jeong-ga*; best-counterparty limit), 최우선지정가 (*choe-u-seon ji-jeong-ga*; best-same-side limit), 경쟁대량매매호가 (*gyeong-jaeng dae-ryang mae-mae ho-ga*; competitive-block / A-Blox), 중간가호가 (*jung-gan-ga ho-ga*; midpoint, added 2025-02-05), and 스톱지정가호가 (*seu-top ji-jeong-ga ho-ga*; stop-limit, added 2025-02-05) [KRX-RULE-KOSDAQ-BR-KO §2.4].
- **Per-security eligibility, conditional-limit conversion logic, stop-limit activation rules, and input restrictions** are all delegated to the KOSDAQ Enforcement Rule [KRX-RULE-KOSDAQ-BR-KO §9.3, §9.4]. R6 unresolved — KOSDAQ Enforcement Rule article numbers cannot yet be cited; substance is believed to mirror KOSPI Enforcement Rule §10 / §13 / §14 / §15 / §15-2 verbatim.
- **Per-session eligibility matrix** matches KOSPI per [KRX-TOUR-KOSDAQ-METHOD-T5]: limit and market types eligible across all sessions; LMC, immediately-executable (= best-counterparty), and best-limit (= best-same-side) eligible only during continuous trading; off-hours sessions are limit-only.
- **KOSDAQ-only constraint — the 1 % rule** [KRX-TOUR-KOSDAQ-METHOD-T1]: any quotation whose quantity exceeds 1 % of an issue's listed shares is rejected unless routed via a block-trading mechanism (intraday block, off-hours block, intraday or off-hours competitive block / A-Blox, or basket). KOSPI does not impose this size cap.
- **Pre-quote validation** is required by the member before submission [KRX-RULE-KOSDAQ-BR-KO §9.7]; if the member system has failed and the member is using the KRX-provided terminal, the §9.7 validation is waived [KRX-RULE-KOSDAQ-BR-KO §9.8, added 2015-11-04].

## Detailed rules

For full prose on the eight quotation types, the deemed-price formulas for best-counterparty / best-same-side / market / midpoint, the conditional-limit (LMC) conversion at 15:20 KST with its priority rules, the stop-limit activation logic and its post-activation time-priority retention, the IOC / FOK / self-match-prevention conditions, and the cancellation-vs-correction asymmetry, see [KOSPI § Detailed rules](../kospi/order_types.md#detailed-rules).

### Article-number remap

| KOSDAQ BR article | KOSPI BR article | Topic                                                                                  |
|-------------------|------------------|----------------------------------------------------------------------------------------|
| §2.4              | §2.4             | Definitions of the 8 quotation types (KOSDAQ §2.4 cross-references §18 for LMC, §19-3 / §21-2 for competitive-block — KOSPI uses §23 / §31 for the same cross-references) |
| §9                | §9               | Quotation submission                                                                   |
| §9.3              | §9.3             | Per-security eligibility (delegated to ER)                                              |
| §9.4              | §9.4             | Input restrictions, LMC conversion, stop-limit activation priority (delegated to ER)    |
| §9.7              | §11-2            | Pre-quote validation by member                                                          |
| §9.8              | (no analogue)    | Member-terminal fallback during member-system failure (KOSDAQ has this carve-out; KOSPI's analogue is §17.4 BR — not yet cross-checked) |
| §9-2              | §17 (KOSPI BR)   | Short-sale quote restriction (KOSDAQ has this in §9-2 right next to general-quote rules; KOSPI moves it to §17 — see [Short Selling](../kospi/short_selling.md))                          |
| §12-2 to §12-6    | (LP framework)   | Liquidity-Provider system — KOSDAQ has its 5 LP articles inline; KOSPI has the same framework with different article numbers (operational tour [KRX-TOUR-KOSPI-OPS-T7]) |
| §13               | (sidecar / program) | Sidecar / program-trading quote management — covered in [Other Topics (KOSDAQ)](./other_topics.md), see §13 deltas there        |

### Delta vs KOSPI

#### KOSDAQ-only 1 % rule [KRX-TOUR-KOSDAQ-METHOD-T1]

> "To minimize possible impacts and mistakes, a quotation whose quantity exceeds 1 % of listed stocks cannot be placed if such quotation is not for block trading."

This is **KOSDAQ-only**. KOSPI does not have a parallel 1 %-of-listed-shares cap on regular-session quotations. The rule's exemption channels for legitimate large-size flow are:

- Intraday block (장중대량매매, *jang-jung dae-ryang mae-mae*) per [KRX-RULE-KOSDAQ-BR-KO §19-2].
- Intraday competitive block / A-Blox per [KRX-RULE-KOSDAQ-BR-KO §19-3] — see [Auctions § A-Blox](./auctions.md#delta-vs-kospi).
- Intraday basket (장중바스켓매매, *jang-jung ba-seu-ket mae-mae*) per [KRX-RULE-KOSDAQ-BR-KO §19-4].
- Off-hours block (시간외대량매매) per [KRX-RULE-KOSDAQ-BR-KO §21].
- Off-hours competitive block (시간외경쟁대량매매) per [KRX-RULE-KOSDAQ-BR-KO §21-2] (pre-open only).
- Off-hours basket (시간외바스켓매매) per [KRX-RULE-KOSDAQ-BR-KO §21-4].

For an algorithm sized to take 1 % or more of a KOSDAQ issue's listed shares in a single quotation, the **only** path is one of these block/basket routes. A regular-session limit, market, conditional-limit, best-counterparty, best-same-side, midpoint, or stop-limit at >1 % of listed shares is rejected at the member pre-quote check (§9.7) before reaching the order book. Per-issue float / listed-share counts are published on the KRX disclosure portal; an execution algo must consult that count before submitting.

The 1 % rule also implicitly caps per-iceberg and per-VWAP-slice quantities — a single child slice cannot exceed 1 % of listed shares. Multi-slice strategies are unaffected as long as each slice respects the 1 % cap.

#### LP framework — KOSDAQ §12-4 spread trigger ≤ 2 % (KOSPI uses 3 %)

KOSDAQ §12-4.1.1 sets the LP-quote trigger as a contract-set spread within **2 %**: "주권의 경우 호가스프레드비율이 2% 이내로서 해당 주권상장법인과 유동성공급계약을 체결한 회원이 거래소에 신고한 비율" (for stocks, within a 2 % spread ratio as reported by the LP-contracted member). The numeric 2 %-cap on what an LP may contract is **tighter** than the KOSPI cap of 3 %. The actual spread-tightening trigger fires when the observed bid-ask spread exceeds the LP-contract-reported ratio (which is anywhere ≤ 2 % on KOSDAQ).

For an execution algo using LP-quote presence as a liquidity signal, this means a KOSDAQ LP responds to a tighter spread divergence than a KOSPI LP. See [Other Topics (KOSDAQ) § Liquidity Provider](./other_topics.md) for the full LP delta. (To be filled when 3.10 lands.)

#### Pre-quote validation in BR §9.7 (vs KOSPI §11-2)

KOSDAQ §9.7 keeps the member's pre-submission validation duty *inside* §9 (Quotation submission), rather than splitting it into a separate §11-2 article as KOSPI does. The substance is identical: the member checks the quote for "호가의 적합성 등 세칙으로 정하는 사항" (quote-validity items as set by the Enforcement Rule) before forwarding to KRX. R6 unresolved means we cannot enumerate the validation checklist authoritatively, but it is believed to mirror KOSPI Enforcement Rule §12-2.3 (price tick, lot, daily limit, off-tick stop, security-eligibility, condition-eligibility, etc.).

#### KOSDAQ §9.8 member-terminal fallback (no direct KOSPI analogue cited)

§9.8 (added 2015-11-04) allows a member that has experienced a member-system failure to submit quotations through a KRX-provided "회원증권단말기" (member-securities-terminal). When this fallback is in use, **the §9.7 pre-quote validation is waived** — the terminal is trusted as a backstop. This carve-out exists structurally on KOSPI as well (in BR §17.4 by the cross-reference style, though we have not yet pulled it for KOSPI). When designing risk filters that mirror KRX validation, an execution algo must distinguish "normal-system flow with §9.7 enforced" from "member-terminal flow with §9.7 waived" — the latter does not have member-side input filtering.

#### Short-sale quote restriction in §9-2 (vs KOSPI's §17)

KOSDAQ co-locates the short-sale quote restriction immediately after §9 (general quotation submission), as §9-2. KOSPI moves the same content to §17. The substantive rules are believed to be identical: the FSCMA §180 framework, the 8 deemed-not-short carve-outs, the member duty cycle, and the deemed-verification opt-out path with the 120-day breach reset all apply on both markets. The KOSDAQ §9-2.4 specifically references the 120-day-after-breach period for the deemed-verification opt-out — same as KOSPI Enforcement Rule §17.4. See [Short Selling (KOSPI)](../kospi/short_selling.md) for the full framework; KOSDAQ-side article numbers will be in [Short Selling (KOSDAQ)](./short_selling.md) when 3.9 lands.

## Parameters & thresholds

### Table 1 — Quotation types (KOSDAQ)

| #  | Korean              | English label                | Key article                     | Price source                                            |
|----|---------------------|------------------------------|---------------------------------|---------------------------------------------------------|
| 1  | 지정가호가           | Limit                        | [KRX-RULE-KOSDAQ-BR-KO §2.4.1]  | Member-specified                                        |
| 2  | 시장가호가           | Market                       | [KRX-RULE-KOSDAQ-BR-KO §2.4.2]  | Deemed via §18.3 / §19.2 (see [Auctions](./auctions.md)) |
| 3  | 조건부지정가호가     | Conditional-limit (LMC)      | [KRX-RULE-KOSDAQ-BR-KO §2.4.5]  | Limit during continuous; converts to market at the closing-call receipt-window open |
| 4  | 최유리지정가호가     | Best-counterparty limit      | [KRX-RULE-KOSDAQ-BR-KO §2.4.3]  | Best opposite-side quote at receipt (formula in KOSDAQ ER, R6 unresolved) |
| 5  | 최우선지정가호가     | Best-same-side limit         | [KRX-RULE-KOSDAQ-BR-KO §2.4.4]  | Best same-side quote at receipt (formula in KOSDAQ ER, R6 unresolved) |
| 6  | 경쟁대량매매호가     | Competitive block (A-Blox)   | [KRX-RULE-KOSDAQ-BR-KO §2.4.6]  | VWAP per §19-3 / §21-2 (see [Auctions § A-Blox](./auctions.md#delta-vs-kospi)) |
| 7  | 중간가호가           | Midpoint                     | [KRX-RULE-KOSDAQ-BR-KO §2.4.7]  | `floor((best_bid + best_ask) / 2)` KRW                  |
| 8  | 스톱지정가호가       | Stop-limit                   | [KRX-RULE-KOSDAQ-BR-KO §2.4.8]  | Member-specified limit; activated when stop is crossed  |

KOSDAQ §2.4 sub-paragraph numbers diverge slightly from KOSPI's: KOSDAQ assigns conditional-limit to **§2.4.5** (KOSPI §2.4.3), best-counterparty to **§2.4.3** (KOSPI §2.4.4), and best-same-side to **§2.4.4** (KOSPI §2.4.5). The set of 8 types is the same, but the sub-paragraph indices have been shuffled — cite by name, not by sub-paragraph number, when working across both markets.

### Table 2 — Per-session eligibility (KOSDAQ tour)

Per [KRX-TOUR-KOSDAQ-METHOD-T5]:

| Type                                | 08:30–09:00 (opening call) | 09:00–15:20 (continuous) | 15:20–15:30 (closing call) | IOC / FOK |
|-------------------------------------|:--------------------------:|:------------------------:|:--------------------------:|:----------:|
| Limit                               |             ✔              |            ✔             |             ✔              |     ✔ (continuous only) |
| Market                              |             ✔              |            ✔             |             ✔              |     ✔ (continuous only) |
| Conditional-limit (LMC)             |             ✔              |            ✔             |             ✗              |     ✗ |
| Best-counterparty (immediately exec.) |           ✗              |            ✔             |             ✗              |     ✔ |
| Best-same-side (best limit)         |             ✗              |            ✔             |             ✗              |     ✗ |

The tour table only enumerates 5 of the 8 types (limit, market, LMC, best-counterparty, best-same-side); midpoint, stop-limit, and competitive-block are not included in the tour. Per the BR §9.4 delegation and the KOSPI Enforcement Rule §14 analogue, the missing types follow the KOSPI matrix: midpoint and stop-limit are continuous-only and excluded from off-hours and from any single-price auction window; competitive-block runs on a separate book (A-Blox) with its own session.

LMC restrictions per [KRX-TOUR-KOSDAQ-METHOD-T5]: "Limit-to-market-on-close orders are **not allowed** for the quotations to determine the first price of the initial listing, re-listing, etc., short-selling, and the quotations to determine the closing prices." Identical restriction set to KOSPI Enforcement Rule §14.2.1.s / .ja / .pa / .ha — see [KOSPI § Per-session and per-issue restrictions](../kospi/order_types.md#per-session-and-per-issue-restrictions).

### Table 3 — KOSDAQ-only 1 % rule

| Constraint                | Threshold                                              | Source                            |
|---------------------------|--------------------------------------------------------|-----------------------------------|
| Per-quotation max quantity | **1 %** of listed shares for the issue                | [KRX-TOUR-KOSDAQ-METHOD-T1]       |
| Exemption                 | Block trading (intraday / off-hours / competitive / basket) | [KRX-TOUR-KOSDAQ-METHOD-T1]       |

### Table 4 — Quotation conditions

Same as KOSPI per [KRX-TOUR-KOSDAQ-METHOD-T5]:

| Condition                  | Effect                                                                       | Source                                            |
|----------------------------|------------------------------------------------------------------------------|---------------------------------------------------|
| IOC                        | Cancel any unmatched portion immediately                                     | KOSDAQ §9.4 (delegated to ER, R6 unresolved); per KOSPI ER §13.3.1 |
| FOK                        | Cancel all if any portion cannot be matched immediately                      | KOSDAQ §9.4; per KOSPI ER §13.3.2                |
| Self-match-prevention      | HSA-only; cancel one or both sides on same-HSA-ID match (3 sub-modes)        | KOSDAQ §9.4; per KOSPI ER §13-2                   |

IOC / FOK eligibility per session per the tour: continuous trading only — not eligible during opening or closing call auctions. SMP active only during continuous trading.

## Worked examples

The KOSPI worked examples — Example A (best-counterparty on a non-empty book), Example B (LMC conversion at 15:20), Example C (stop-limit activation and post-activation priority retention) — all carry over to KOSDAQ unchanged because the underlying rules are identical. See [KOSPI § Worked examples](../kospi/order_types.md#worked-examples).

### Example D — KOSDAQ 1 % rule rejection

A KOSDAQ-listed issue has 100,000,000 listed shares. An algorithm submits a buy limit for 1,500,000 shares at the regular session.

- The 1 % cap is 100,000,000 × 0.01 = 1,000,000 shares per quotation.
- The 1,500,000-share quotation exceeds the 1 % cap → **rejected at the member pre-quote check** (§9.7) before reaching the KRX order book [KRX-TOUR-KOSDAQ-METHOD-T1].

The algorithm's options:

1. Split into multiple regular-session quotations, each ≤ 1,000,000 shares.
2. Route the entire quantity via the intraday block (장중대량매매) — minimum size 5,000 × lot or KRW 100M, well below 1.5M shares for any liquid name.
3. Route via A-Blox — minimum size KRW 200M (per [Auctions § A-Blox](./auctions.md#delta-vs-kospi)).

The same algorithm on KOSPI faces no such cap (KOSPI does not have the 1 % rule). For an execution algo running cross-market, the per-iceberg-slice / per-VWAP-slice configuration must respect the 1 % cap on the KOSDAQ side — a uniform slice size that is fine on KOSPI may exceed 1 % on a small KOSDAQ name.

## Edge cases & open questions

- Edge case: The 1 % rule is sourced only from the KRX overview tour [KRX-TOUR-KOSDAQ-METHOD-T1]; the corresponding article in the KOSDAQ Enforcement Rule (likely the analogue of KOSPI Enforcement Rule §12-2.5 호가의 수량제한 / quantity restriction) cannot yet be cited authoritatively (R6). Phase 6 freshness audit must verify against the KOSDAQ Enforcement Rule when archived.
- Edge case: The 1 % rule's denominator is "listed shares" — but for issues with multiple share classes (preferred + common), it is unclear whether the cap applies to the per-class listed count or the aggregated count. KOSDAQ-METHOD-T1 does not specify. Cross-check before working on cross-class arbitrage strategies.
- Edge case: KOSDAQ §2.4 sub-paragraph numbering for best-counterparty (§2.4.3) vs conditional-limit (§2.4.5) is *swapped* relative to KOSPI §2.4. A reader familiar with KOSPI sub-paragraph indices should re-anchor to type names when reading KOSDAQ. This is a tour-pages-and-text-prose issue, not a substantive rule change — both books enumerate the same 8 types.
- Edge case: The §9.8 member-terminal fallback waives §9.7 validation. Under failover scenarios, the only validation between member input and the KRX order book is the KRX-side input check (§14.1 of the Enforcement Rule analogue, R6). Risk-management strategies that assume member-side filtering will not catch a malformed quote during a member-system outage.
- Open question: KOSDAQ §12-4.1.1's 2 % LP-spread cap vs KOSPI's 3 % cap — does the same numeric divergence appear in the LP-quote-quantity rule (KOSPI's "5 × trading lot") or only on the spread-cap dimension? KOSDAQ §12-5 sets the submission method but the per-side minimum quote size is delegated to the ER (R6 unresolved). [KRX-TOUR-KOSDAQ-METHOD-T7] is the operational tour for KOSDAQ LP — to be cited in `other_topics.md` (3.10).
- Open question: The KOSDAQ §9.4-delegated stop-limit activation priority is believed to mirror KOSPI Enforcement Rule §15-2.1 (sell stops: higher stop activates first; buy stops: lower stop activates first; ties broken by stop-quote receipt time). Cross-check at R6 / Phase 6.
- Open question: KOSDAQ §9.4-delegated LMC conversion priority — KOSPI ER §15.1 sets sell LMCs to convert lowest-price-first and buy LMCs highest-price-first, ties broken by receipt time. Substance is believed identical on KOSDAQ; cross-check at R6 / Phase 6.
- Open question: The 2025-02-05 amendment that added midpoint and stop-limit on KOSPI is structurally mirrored on KOSDAQ §2.4.7 / §2.4.8 (added in the same amendment cycle). Whether the KOSDAQ §9.4 stop-limit-activation delegate is the same KOSDAQ ER §15-2 analogue (with the 2025-02-27 effective date matching KOSPI's) needs R6 confirmation.

## Sources

- `KRX-RULE-KOSDAQ-BR-KO` — KOSDAQ Market Business Regulation (코스닥시장 업무규정), bookid 210164370, effective 2026-04-28. Articles cited: §2 (Definitions — 8 quotation types with the §2.4 sub-paragraph index swap relative to KOSPI), §9 (Quotation submission — §9.3 per-security eligibility delegated, §9.4 input restrictions / LMC conversion / stop-limit priority delegated, §9.7 pre-quote validation, §9.8 member-terminal fallback added 2015-11-04), §9-2 (Short-sale quote restriction — co-located in the order-types territory), §10 (Treasury-stock quotation — referenced), §11 (Treasury-stock buy-quote market-disruption special case — referenced), §12 (Treasury-stock trust trading — referenced), §12-2 to §12-6 (Liquidity Provider framework — §12-4.1.1 has the 2 % spread cap delta vs KOSPI's 3 %; full LP write-up will appear in [Other Topics (KOSDAQ)](./other_topics.md) under task 3.10), §13 (Sidecar / program-trading quote management — covered in [Other Topics (KOSDAQ)](./other_topics.md), see §13 deltas).
- `KRX-TOUR-KOSDAQ-METHOD-T1` — KRX overview "Quotation quantity limit (1 % rule)" (KOSDAQ); English, not authoritative. **Sole source** for the KOSDAQ-only 1 %-of-listed-shares per-quotation cap; flagged for re-verification at R6 resolution.
- `KRX-TOUR-KOSDAQ-METHOD-T5` — KRX overview "Limit Orders / Order types" (KOSDAQ); English, not authoritative. Used for the per-session eligibility table (5 enumerated types), the LMC restriction set (excluding initial-listing first-price, re-listing first-price, short-sale, and closing-price determination), the IOC / FOK descriptive language, the deemed-price formulas for best-counterparty and best-same-side (matching KOSPI Enforcement Rule §3 / §4), and the cancellation-vs-correction rules.
