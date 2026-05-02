---
title: "Trading Rules & Matching (KOSDAQ)"
markets: [KOSDAQ]
last_reviewed: 2026-05-01
sources:
  - KRX-RULE-KOSDAQ-BR-KO
  - KRX-TOUR-KOSDAQ-METHOD-T5
  - KRX-TOUR-KOSDAQ-METHOD-T6
  - KRX-TOUR-KOSDAQ-EXCEPT-T5
---

> See also: [Trading Rules (KOSPI)](../kospi/trading_rules.md), [Order Types (KOSDAQ)](./order_types.md), [Auctions (KOSDAQ)](./auctions.md), [Price Ranges (KOSDAQ)](./price_ranges.md), [Comparison](../common/comparison.md).

**Delta file.** KOSDAQ matching, priority, and quotation-flow rules are **substantively identical** to KOSPI: same individual-competitive-auction matching, same price > time > 동시호가-quantity priority hierarchy with the carve-out scoped to opening / market-resumption / individual-resumption single-price events at the upper / lower limit, same three-pass quantity allocation, same leading-quote rule for continuous matching, same pre-quote validation requirement, same halt-period cancel-only behavior, same SMP-active-only-in-continuous + SMP-before-IOC ordering, and the same 10-deep continuous + 3-deep single-price disclosure shape. The deltas are: (1) **only 2 trade-type categories** (T+0 and T+2) vs KOSPI's 3 (no T+1 익일결제거래 (*ik-il gyeol-je geo-rae*; next-day-settlement) on KOSDAQ); (2) **article-numbering remap**; (3) **R6 citation gap** for granular Enforcement-Rule items. This file points to the [KOSPI write-up](../kospi/trading_rules.md) for shared content.

## Summary

- KOSDAQ matches all on-exchange trades by individual competitive auction — single-price (단일가매매) for the 5 events listed in §18.1, continuous (복수가매매) outside those windows [KRX-RULE-KOSDAQ-BR-KO §17.1, §18, §19]. Detailed mechanics in [Auctions (KOSDAQ)](./auctions.md).
- Default matching priority is **price-then-time** with the same market-vs-limit equivalence at price limits [KRX-RULE-KOSDAQ-BR-KO §17.2]. The 동시호가 quantity-priority carve-out is scoped to single-price auctions of items §18.1.1, §18.1.3, §18.1.4 (opening, market-resumption, individual-resumption) at the daily upper / lower limit only — exactly the same scope as KOSPI [KRX-RULE-KOSDAQ-BR-KO §17.3].
- **Trade-type delta — only 2 categories on KOSDAQ:** §7-2.1.1 당일결제거래 (T+0) and §7-2.1.2 보통거래 (T+2). KOSPI has a third category, T+1 익일결제거래 (*ik-il gyeol-je geo-rae*; next-day-settlement), per KOSPI BR §7.1.2; KOSDAQ does not enumerate T+1. All listed-securities trades default to T+2 보통거래 unless the Enforcement Rule specifies otherwise [KRX-RULE-KOSDAQ-BR-KO §7-2.4].
- Pre-quote validation is required by the member [KRX-RULE-KOSDAQ-BR-KO §9.7]; the §9.7 check is **waived** when the member is using the KRX-provided emergency terminal during member-system failure [KRX-RULE-KOSDAQ-BR-KO §9.8].
- Disconnect-cancel (접속해제 호가취소, *jeop-sok-hae-je ho-ga chwi-so*) is registered by the member in advance and triggered automatically on disconnection [KRX-RULE-KOSDAQ-BR-KO §16-2]. KRX has both an error-trade correction mechanism [§27] and a **mass-erroneous-trade relief** mechanism [§27-2, added 2015-11-04] — see *Mass-erroneous-trade relief* below.
- HSA (high-speed-algorithmic-trading) registration is in [KRX-RULE-KOSDAQ-BR-KO §50-3] (vs KOSPI §104-3); SMP is gated to HSA-registered traders.
- Depth-of-book disclosure is **10-deep** during continuous trading and **3-deep + expected matching price** during single-price auction receipt windows [KRX-TOUR-KOSDAQ-EXCEPT-T5; KRX-TOUR-KOSDAQ-METHOD-T6]. Same shape as KOSPI; the 08:30–08:40 opening-curtain (10-minute disclosure delay) applies on both markets.

## Detailed rules

For full prose on the matching algorithms, the §22 / §17 priority hierarchy, the 3-pass quantity allocation at price limits, the leading-quote rule for continuous matching, the SMP and IOC / FOK conditions, halt-period cancel-only behavior, the HSA framework, and the depth-of-book disclosure mechanics, see [KOSPI § Detailed rules](../kospi/trading_rules.md#detailed-rules). The KOSDAQ articles map directly:

| KOSDAQ BR article | KOSPI BR article | Topic                                                          |
|-------------------|------------------|----------------------------------------------------------------|
| §2.18             | §2.21            | 알고리즘거래 definition                                          |
| §2.19             | §2.22            | 고속 알고리즘거래 definition (with the colocation siting condition) |
| §2.20             | §2.23            | 고속 알고리즘거래자 definition (registered under §50-3 / §104-3)    |
| §7-2              | §7               | Trade types and settlement timing — **only 2 categories on KOSDAQ** vs KOSPI's 3 |
| §9                | §9               | Quotation submission                                              |
| §9.7              | §11-2            | Pre-quote validation by member                                    |
| §9.8              | §17.4 (BR — not yet pulled) | Member-terminal fallback during member-system failure (§9.7 waived) |
| §13               | §17 (KOSPI: program-trading-quote-management at §17 — not yet pulled) | Program-trading-quote management / sidecar (covered in [Other Topics (KOSDAQ)](./other_topics.md)) |
| §14.1             | §14.1            | Recording in receipt order                                        |
| §16-2             | §13-2            | Disconnect-cancel                                                  |
| §17               | §22              | Priority hierarchy — price > time > 동시호가-quantity            |
| §17.2.1           | §22.2.1          | Market-vs-limit-at-limit equivalence                              |
| §17.3             | §22.3            | 동시호가 carve-out scope (§18.1.1, §18.1.3, §18.1.4 only)         |
| §27               | §28              | Error-trade correction by KRX                                      |
| §27-2             | §28-2            | Mass-erroneous-trade relief — **both markets have this**, added 2015-11-04 |
| §50-3             | §104-3           | HSA-trader registration                                            |

### Delta vs KOSPI

#### Trade types — only T+0 and T+2 on KOSDAQ

KOSDAQ §7-2.1 enumerates **two** settlement-day categories:

1. **당일결제거래** (T+0) — settled the same day. Used in narrow rule-specified cases.
2. **보통거래** (T+2) — settled the third day from the trade day, holidays excluded from the day-count [KRX-RULE-KOSDAQ-BR-KO §7-2.2].

KOSPI §7.1 also lists a third category, **익일결제거래** (T+1, next-day-settlement). KOSDAQ §7-2 does **not** include T+1. The practical effect is small — listed-securities trades default to T+2 in both markets — but execution algos that use settlement-cycle inputs (e.g. for cash-management buffer sizing) must not assume a T+1 path is available on KOSDAQ.

#### Mass-erroneous-trade relief — both markets have it (correct interpretation)

KOSDAQ §27-2 (added 2015-11-04) is the mass-erroneous-trade relief article:

> 거래소는 정규시장의 매매거래시간 중 개별경쟁매매의 방법으로 거래된 주권, 외국주식예탁증권 및 기업성장집합투자기구 집합투자증권과 관련하여 회원 또는 위탁자의 착오로 인하여 본래의 의사와 다르게 성립된 매매거래 중 **대규모착오매매**(결제가 곤란하고 시장에 혼란을 줄 우려가 있다고 인정하는 경우로서 세칙으로 정하는 요건을 충족하는 매매거래를 말한다)에 대하여 **회원의 신청이 있는 경우에는 이를 구제할 수 있다**.

Translation: KRX may, on member request, **relieve** a "mass-erroneous trade" (대규모착오매매, *dae-gyu-mo-chak-o-mae-mae*) — i.e. a trade that the member or consigner agrees was contrary to original intent, where settlement difficulty and market disruption thresholds (set in the Enforcement Rule) are met. KOSPI BR §28-2 is the verbatim parallel with the same 2015-11-04 effective date.

This is significant: the KOSPI write-up `docs/kospi/other_topics.md` § Error-trade rules currently says "KRX does not have a formal 'trade busting' mechanism that voids on-exchange prints retroactively" — that is **incorrect** as written; both KOSPI §28-2 and KOSDAQ §27-2 provide a formal trade-relief facility, gated to mass-erroneous criteria. The detailed criteria (size threshold, time window, price-divergence threshold) are in the Enforcement Rule. KOSPI Enforcement Rule has these criteria archived; KOSDAQ Enforcement Rule has them too (R6 unresolved). **Phase 6 freshness audit must correct the KOSPI other_topics.md error-trade-rules section**.

#### Pre-quote validation in §9.7 (KOSDAQ) vs §11-2 (KOSPI)

Both markets require the member to run the pre-quote conformance check before transmission. KOSDAQ keeps it inside §9 (Quotation submission); KOSPI moves it to a dedicated §11-2 article. Substance is the same — account, security, quantity, price, stop-price, type, margin, HSA-fields validation per the Enforcement Rule §12-2 analogue (R6 unresolved on KOSDAQ side). The member-terminal fallback during member-system failure waives the §9.7 check on KOSDAQ [§9.8] — same waiver structure as KOSPI BR §9.4 / §17.4.

#### Disconnect-cancel in §16-2 (KOSDAQ) vs §13-2 (KOSPI)

KOSDAQ §16-2 was added 2022-12-07; KOSPI §13-2 has the same content with same effective date. Substance: member pre-registers a disconnect-cancel rule; on disconnection, KRX applies the cancel automatically per the rule's defined range. The detailed range-definition and re-enrollment rules are in the Enforcement Rule (R6 unresolved on KOSDAQ side).

#### HSA registration in §50-3 (KOSDAQ) vs §104-3 (KOSPI)

The KOSDAQ BR's HSA-trader registration article is at §50-3 — much earlier in the article numbering than KOSPI's §104-3. The substance is the same: HSA-trader registration is a prerequisite to submitting any HSA-tagged quotation, and SMP availability is gated to HSA-registered traders. KOSDAQ §2.20 cross-references §50-3 in its 고속 알고리즘거래자 definition.

#### KOSDAQ §2.21 (added 2026-03-04) — corporate-growth-investment-fund securities

KOSDAQ §2.21 adds a definition for 기업성장집합투자기구 집합투자증권 (corporate-growth-investment-fund collective-investment securities — added 2026-03-04). This security class doesn't exist on KOSPI. The §17.1 / §18 / §19 matching mechanics apply to it identically; the per-class quotation-eligibility (limit-only vs full-eight) and any per-class price-limit treatment are delegated to the KOSDAQ Enforcement Rule (R6).

#### KOSDAQ §13 — sidecar (covered in `other_topics.md`)

KOSDAQ §13 is the program-trading-quote management / sidecar article. KOSDAQ-specific thresholds (6 % futures move + 3 % index move, 1-min persistence, 5-min suspension, 14:50 cutoff) differ from KOSPI's (5 % futures move only, with no separate index requirement). Full write-up will appear in [Other Topics (KOSDAQ)](./other_topics.md) when 3.10 lands.

## Parameters & thresholds

### Trade types (KOSDAQ — only 2 categories)

| Trade type      | Korean              | Settlement offset | Default for                                               | Source                                |
|------------------|---------------------|------------------:|-----------------------------------------------------------|---------------------------------------|
| 당일결제거래      | dang-il gyeol-je    |              T+0  | Specific block / basket variants per Enforcement Rule     | [KRX-RULE-KOSDAQ-BR-KO §7-2.1.1]      |
| 보통거래          | bo-tong geo-rae     |              T+2  | All listed-securities trades unless otherwise specified   | [KRX-RULE-KOSDAQ-BR-KO §7-2.1.2, §7-2.4] |

KOSPI has an additional **익일결제거래** (T+1) category that KOSDAQ does not.

### §17 priority levels (KOSDAQ)

Same hierarchy as KOSPI's §22:

| Level | Rule                                                       | Article                                       |
|-------|------------------------------------------------------------|-----------------------------------------------|
| 1     | Price priority (lower ask / higher bid wins)               | [KRX-RULE-KOSDAQ-BR-KO §17.2.1]               |
| 1a    | Market = limit-at-limit for price priority only            | [KRX-RULE-KOSDAQ-BR-KO §17.2.1 proviso]       |
| 2     | Time priority among same-price (and among markets)         | [KRX-RULE-KOSDAQ-BR-KO §17.2.2]               |
| 3     | 동시호가 quantity priority — single-price auction at limit, items §18.1.1, §18.1.3, §18.1.4 only | [KRX-RULE-KOSDAQ-BR-KO §17.3] |

### Quotation-information disclosure (KOSDAQ)

Per [KRX-TOUR-KOSDAQ-EXCEPT-T5; KRX-TOUR-KOSDAQ-METHOD-T6]:

| Phase                              | Levels disclosed (each side)         | Extra fields                          | Disclosure starts        | Source                                    |
|------------------------------------|--------------------------------------|---------------------------------------|--------------------------|-------------------------------------------|
| Continuous trading                 | 10 best                              | Total per side                        | At session start         | [KRX-TOUR-KOSDAQ-EXCEPT-T5]               |
| Single-price auction (receipt)     | 3 best                               | Expected matching price + quantity    | Throughout receipt window| [KRX-TOUR-KOSDAQ-EXCEPT-T5]               |
| Opening single-price (08:30–09:00) | 3 best                               | Expected matching price + quantity    | 08:40 (10 min delay)     | [KRX-TOUR-KOSDAQ-EXCEPT-T5]               |
| Off-hours closing-price            | 0 (price fixed)                      | Total remainder bid + ask quantity    | Throughout window         | [KRX-TOUR-KOSDAQ-EXCEPT-T5]               |
| A-Blox                             | 0                                    | Buy/sell-existence indicator only     | n/a                      | [KRX-TOUR-KOSDAQ-EXCEPT-T4 — see auctions.md] |

## Worked examples

The KOSPI worked examples — Example A (continuous matching with leading-quote price), Example B (pre-quote control rejecting a malformed stop-limit), Example C (opening-auction disclosure timeline) — all carry over to KOSDAQ unchanged because the underlying rules (KOSDAQ §17 / §18 / §19, §9.7, opening-curtain disclosure) mirror their KOSPI counterparts. See [KOSPI § Worked examples](../kospi/trading_rules.md#worked-examples).

### Example D — mass-erroneous-trade relief (KOSDAQ §27-2)

A consigner submits a buy market quotation intending 1,000 shares at the prevailing price (estimated KRW 30,000,000 notional). Due to a UI error, the quotation is sized at 1,000,000 shares; with the stock trading at KRW 30,000, the trade prints at total notional KRW 30,000,000,000 — 1,000× the intended exposure. The member identifies the error within minutes.

- The trade is **final** at the moment of match per §17.1's general rule.
- The member files for **mass-erroneous-trade relief** under §27-2.1: KRX may relieve the trade if (a) the trade is contrary to original intent, (b) settlement difficulty exists, (c) market-disruption risk is material, and (d) the Enforcement Rule criteria (size threshold, time window, price-divergence threshold) are met [KRX-RULE-KOSDAQ-BR-KO §27-2.1].
- KRX evaluates the application; the §27-2.1 proviso ("시장상황의 급변, 그 밖에 시장관리상 필요하다고 인정하는 경우에는 제외") bars relief when KRX deems the broader market situation (e.g. a price-volatility-driven event) makes relief inappropriate.
- If KRX grants relief, the trade is unwound by the procedure in the Enforcement Rule §27-2.2 (R6 unresolved on KOSDAQ side; KOSPI Enforcement Rule §51 sets the criteria — likely identical on KOSDAQ).

The mass-erroneous-trade relief is the **only** post-trade reversal mechanism inside KRX; outside this gate, the §17.1 finality rule binds. Members targeting risk-management strategies must therefore pre-quote-control fat-finger errors at the §9.7 check; once a trade prints, only mass-erroneous-trade-relief criteria can unwind it.

## Edge cases & open questions

- Edge case: KOSPI other_topics.md § Error-trade rules currently states "KRX does not have a formal 'trade busting' mechanism that voids on-exchange prints retroactively." This is **incorrect**. Both KOSPI §28-2 and KOSDAQ §27-2 provide formal mass-erroneous-trade relief, added 2015-11-04 in both books with substantively identical text. Phase 6 freshness audit should correct the KOSPI write-up, and the corresponding KOSDAQ other_topics.md (3.10) should reflect the parallel article.
- Edge case: KOSDAQ §27-2's relief is limited to "주권, 외국주식예탁증권 및 기업성장집합투자기구 집합투자증권" (shares, foreign DRs, and the new investment-fund securities). KOSPI §28-2 is broader: "주권, 외국주식예탁증권, 상장지수집합투자기구 집합투자증권, 상장지수증권, 주식워런트증권 및 수익증권" (shares, foreign DRs, ETFs, ETNs, ELWs, beneficiary certs). KOSDAQ ETF / ETN / ELW errors thus fall outside §27-2's scope and revert to the §17.1 finality rule. Cross-check before any KOSDAQ-side ETF-error-recovery design.
- Edge case: KOSDAQ §7-2 does not enumerate T+1. If the Enforcement Rule designates a particular KOSDAQ security for next-day settlement, the §7-2 enumeration would have to be amended first; until then, T+1 is structurally unavailable on KOSDAQ. This is a structural difference rather than a numeric parameter difference — easy to miss when porting a KOSPI cash-flow model to KOSDAQ.
- Edge case: KOSDAQ §17.3 동시호가 carve-out is scoped to §18.1.1, §18.1.3, §18.1.4 (opening, market-resumption, individual-resumption). The closing single-price (§18.1.2) and the trade-execution-method-change first-price (§18.1.5) do **not** trigger 동시호가 — same exclusion as KOSPI. A closing call that prints at the upper limit retains time priority among same-price quotations.
- Edge case: §50-3 HSA registration applies to "위탁자 또는 회원" (consigner or member-firm). On KOSDAQ, the §2.19 colocation condition requires the order system to be inside KRX's "회원전산센터" (member-data-center); §2.19 was amended 2026-03-04 to clarify the data-center scope (now includes "회원전산센터등" — the member-data-center-or-equivalent building). Practical effect: HSA eligibility on KOSDAQ is co-extensive with KRX colocation as of 2026-03-04.
- Open question: KOSDAQ §41 (위탁주문의 처리; consigner-order processing) sets the member's duty of care for consigner orders, including the "best-execution" obligation. The KOSPI parallel is §43 (also unsourced in the KOSPI write-up so far). Both articles delegate detailed reporting requirements (e.g. §41.4 "이상매매의 징후 또는 현상이 발생하여... 통지하여야 한다") to the Enforcement Rule. Whether KOSDAQ-side best-execution reporting differs from KOSPI requires R6 + KOSPI ER §41 / §43 cross-pull.
- Open question: KOSDAQ-METHOD-T5's "Available Types of Orders and Conditions by Sessions" table only enumerates 5 types; the missing 3 (competitive-block, midpoint, stop-limit) were added 2025-02-05. Whether the tour table will be updated to include them, or whether the tour reflects a pre-2025 view of the menu, is not stated. Cross-check the KOSDAQ Enforcement Rule analogue of KOSPI ER §14.2 at R6 / Phase 6.

## Sources

- `KRX-RULE-KOSDAQ-BR-KO` — KOSDAQ Market Business Regulation (코스닥시장 업무규정), bookid 210164370, effective 2026-04-28. Articles cited: §2 (Definitions — including §2.18 algo-trading, §2.19 HSA-trading with the 2026-03-04-amended colocation siting language, §2.20 HSA-trader, and §2.21 corporate-growth-investment-fund securities added 2026-03-04), §7-2 (Trade types — only 2 categories: T+0 and T+2; KOSPI's 3-category list is not mirrored), §9 (Quotation submission — §9.7 pre-quote validation, §9.8 member-terminal fallback waiving §9.7), §13 (Sidecar / program-trading quote management — covered in other_topics.md), §14.1 (Recording in receipt order), §16-2 (Disconnect-cancel — added 2022-12-07), §17 (Priority — §17.1 individual-competitive-auction, §17.2 price-then-time + market-vs-limit equivalence, §17.3 동시호가 carve-out), §18 (Single-price auction — referenced for §17.3 scope), §19 (Continuous matching — leading-quote rule), §27 (Error-trade correction by KRX), §27-2 (Mass-erroneous-trade relief — added 2015-11-04, substantively identical to KOSPI §28-2; security scope narrower than KOSPI §28-2), §41 (Consigner-order processing — referenced for best-execution duty), §50-3 (HSA-trader registration — referenced).
- `KRX-TOUR-KOSDAQ-METHOD-T5` — KRX overview "Limit Orders / Order types" (KOSDAQ); English, not authoritative. Used for the per-session order-type-and-condition matrix.
- `KRX-TOUR-KOSDAQ-METHOD-T6` — KRX overview "Periodic call auction" (KOSDAQ); English, not authoritative. Used for the random-end summary and the priority hierarchy at the upper / lower limit.
- `KRX-TOUR-KOSDAQ-EXCEPT-T5` — KRX overview "Quotation disclosure during single-price auction" (KOSDAQ); English, not authoritative. Used for the depth-of-book disclosure shape (10-deep continuous, 3-deep single-price, total-only off-hours-closing).
