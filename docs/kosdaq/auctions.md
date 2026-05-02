---
title: "Auctions (KOSDAQ)"
markets: [KOSDAQ]
last_reviewed: 2026-05-01
sources:
  - KRX-RULE-KOSDAQ-BR-KO
  - KRX-TOUR-KOSDAQ-METHOD-T6
  - KRX-TOUR-KOSDAQ-EXCEPT-T4
  - KRX-TOUR-KOSDAQ-EXCEPT-T5
---

> See also: [Auctions (KOSPI)](../kospi/auctions.md), [Market Hours (KOSDAQ)](./market_hours.md), [Comparison](../common/comparison.md).

**Delta file.** KOSDAQ auction substance is **identical to KOSPI** in all four core mechanisms — single-price vs continuous mode partition, the 5 single-price events, the price–time priority rule with the 동시호가 (*dong-si-ho-ga*; deemed-simultaneous) override at the daily price-limit at opening / market-resumption / individual-resumption, and the 합치가격 (*hap-chi-ga-gyeok*; matching price) algorithm. The only material parametric difference is **A-Blox** (auction-based block trade): KOSDAQ minimum is **KRW 200M** vs KOSPI **KRW 500M**, and the trading unit is **1 share** vs KOSPI **100 shares**. This file points to the [KOSPI write-up](../kospi/auctions.md) for shared content and records the KOSDAQ-side citations + the A-Blox delta + the article-numbering delta.

## Summary

- KOSDAQ uses two auction modes — single-price call auction (단일가격에 의한 개별경쟁매매) and continuous auction (복수가격에 의한 개별경쟁매매) — with the same 5 single-price events as KOSPI: opening, closing, market-resumption, individual-resumption, and post-method-change first price [KRX-RULE-KOSDAQ-BR-KO §18.1].
- Order priority is price > time, with the same 동시호가 override at upper / lower price limits during opening, market-resumption, and individual-resumption auctions (closing-call excluded) [KRX-RULE-KOSDAQ-BR-KO §17.2–17.3].
- 합치가격 determination, multiple-matching-price tie-break (with the 2025-02-05 amendments), and market-order deemed prices in single-price and continuous modes match KOSPI verbatim [KRX-RULE-KOSDAQ-BR-KO §18.3, §18.4, §18.5, §19.2].
- Random-end mechanism (up to 30 s after nominal close), 3-pass quantity allocation at price limits, and newly-listed first-price single-price auction with a 30 s random extension are delegated to the **KOSDAQ Enforcement Rule** (시행세칙) — **not yet archived** (R6 — see PROJECT_IMPLEMENTATION.md). KOSDAQ tour [KRX-TOUR-KOSDAQ-METHOD-T6] confirms the 30-second random close and the price-then-quantity priority at the upper / lower limit.
- **A-Blox (auction-based block trade) delta**: KOSDAQ minimum order size is **KRW 200,000,000** and trading unit is **1 share**, vs KOSPI's KRW 500,000,000 and 100-share lot [KRX-TOUR-KOSDAQ-EXCEPT-T4]. Eligible securities, trading hours (08:00–09:00 + 09:00–15:00), and VWAP-based execution price all match KOSPI.

## Detailed rules

For full prose on the two auction modes, the 5-event single-price trigger list, the matching-price algorithm, market-order deemed prices, random-end mechanism, the 동시호가 override scope, and the 3-pass quantity-allocation passes, see [KOSPI § Detailed rules](../kospi/auctions.md#detailed-rules). The KOSDAQ articles map directly onto KOSPI:

| KOSDAQ BR article | KOSPI BR article | Topic                                                                |
|-------------------|------------------|----------------------------------------------------------------------|
| §17               | §22              | Auction principle: price > time, with §17.3 / §22.3 동시호가 override |
| §18               | §23              | Single-price auction: 5-event list, market-order deemed prices, 합치가격 |
| §19               | §24              | Continuous auction: leading-quote (선행호가, *seon-haeng-ho-ga*) pricing  |
| §19-3             | §31              | Intraday competitive block (장중경쟁대량매매), VWAP-from-match-to-close |
| §22               | §37              | Newly-listed first-price                                              |
| §23-3             | §26-2            | Per-issue method change to single-price (used by VI / overheat)        |

### Delta vs KOSPI

#### A-Blox parameters (material)

A-Blox eligibility, trading hours, and execution-price formula match KOSPI; minimum order size and trading unit differ [KRX-TOUR-KOSDAQ-EXCEPT-T4]:

| Parameter                     | KOSDAQ                              | KOSPI                                | Source                                  |
|-------------------------------|-------------------------------------|--------------------------------------|-----------------------------------------|
| Minimum order size            | **KRW 200,000,000**                 | KRW 500,000,000                      | [KRX-TOUR-KOSDAQ-EXCEPT-T4 vs KRX-TOUR-KOSPI-EXCEPT-T4] |
| Trading unit                  | **1 share**                         | 100 shares                            | [KRX-TOUR-KOSDAQ-EXCEPT-T4 vs KRX-TOUR-KOSPI-EXCEPT-T4] |
| Eligible securities           | Stocks, KDRs (admin / liquidation excluded) | Stocks, ETFs, ETNs, KDRs (admin / liquidation excluded) | identical core; KOSDAQ tour drops ETF / ETN from its eligibility note (likely tour-page brevity, not a substantive exclusion — KOSPI ETFs that cross-list to KOSDAQ are rare in practice) |
| Pre-hours trading window      | 08:00–09:00 KST                     | 08:00–09:00 KST                      | identical                                |
| Regular-session trading window | 09:00–15:00 KST                    | 09:00–15:00 KST                      | identical                                |
| Off-hours execution price     | Session VWAP for the day            | Session VWAP for the day              | identical                                |
| Regular-session execution price | VWAP from match-time to close      | VWAP from match-time to close         | identical                                |
| No after-hours A-Blox session | yes (no post-close A-Blox)          | yes (no post-close A-Blox)            | identical                                |

The KRW 200M / 1-share configuration substantively lowers the threshold for KOSDAQ block-eligible flow vs KOSPI. An execution algo running across both markets cannot reuse a single "block-eligible" cut-off — the per-market table is required.

#### Article-number remapping

KOSDAQ §17 / §18 / §19 / §19-3 vs KOSPI §22 / §23 / §24 / §31. All cross-references inside the KOSDAQ Business Regulation use the KOSDAQ numbering. When citing KOSPI text from a KOSDAQ context, translate:

- "§22 (auction principle)" on KOSPI = KOSDAQ §17.
- "§22.3 (deemed-simultaneous override)" on KOSPI = KOSDAQ §17.3.
- "§23.1 (single-price 5-event list)" on KOSPI = KOSDAQ §18.1.
- "§23.4 (matching price algorithm)" on KOSPI = KOSDAQ §18.4.
- "§24 (continuous matching)" on KOSPI = KOSDAQ §19.
- "§31 (intraday competitive block, A-Blox precursor)" on KOSPI = KOSDAQ §19-3.

#### Single-price-only mode for liquidation issues

KOSDAQ §23.2 — "정리매매종목에는 호가의 가격제한폭을 두지 아니한다" (*jeong-ri-mae-mae-jong-mok-e-neun ho-ga-ui ga-gyeok-je-han-pok-eul du-ji a-ni-han-da*; "no price-limit band for liquidation issues") — matches KOSPI BR §20.3 verbatim. The 14-auctions-per-day single-price-only matching mechanism for liquidation issues is set in the KOSDAQ Enforcement Rule (R6 unresolved); KOSPI's analogue is in Enforcement Rule §56.

#### Single-price-only mode for short-term overheat

KOSDAQ §23-2 (단기과열종목 designation) and §23-3 (per-issue method change) align with KOSPI §26-2. The KOSDAQ Enforcement Rule analogue of KOSPI Enforcement Rule §133 / §134 (the 130 % / 600 % / 150 % triple criteria + 120 % extension cycle) is not directly cited until R6 resolves. The KOSDAQ-side overheat criteria are believed to be identical to KOSPI; cross-check at R6 resolution / Phase 6 freshness audit.

## Parameters & thresholds

### Auction events (identical to KOSPI)

The KOSPI auction-events table applies to KOSDAQ verbatim with article-number translation. See [KOSPI § Parameters & thresholds](../kospi/auctions.md#parameters-thresholds) for the canonical table.

| Auction event                                      | Mode          | Random extension                  | KOSDAQ source                                       |
|----------------------------------------------------|---------------|-----------------------------------|----------------------------------------------------|
| Opening price (시가)                               | single-price  | yes — up to 30 s after 09:00      | [KRX-RULE-KOSDAQ-BR-KO §18.1.1; KRX-TOUR-KOSDAQ-METHOD-T6]    |
| Closing price (장종료시의 가격)                    | single-price  | yes — up to 30 s after 15:30      | [KRX-RULE-KOSDAQ-BR-KO §18.1.2; KRX-TOUR-KOSDAQ-METHOD-T6]    |
| First price after market resumption                | single-price  | yes — up to 30 s after restart    | [KRX-RULE-KOSDAQ-BR-KO §18.1.3]                              |
| First price after individual-issue resumption      | single-price  | yes — up to 30 s after restart    | [KRX-RULE-KOSDAQ-BR-KO §18.1.4; KRX-TOUR-KOSDAQ-METHOD-T6]    |
| First price after trade-method change              | single-price  | yes — up to 30 s after switch     | [KRX-RULE-KOSDAQ-BR-KO §18.1.5; §23-3]                       |
| First price for newly-listed issue                 | single-price  | yes — up to 30 s after 09:00      | [KRX-RULE-KOSDAQ-BR-KO §22; KRX-TOUR-KOSDAQ-METHOD-T6]        |
| Continuous regular-session trading                 | multi-price   | n/a                               | [KRX-RULE-KOSDAQ-BR-KO §19]                                  |
| Off-hours single-price (16:00–18:00, 12 × 10-min)  | single-price  | yes — up to 30 s after each clear | [KRX-RULE-KOSDAQ-BR-KO §21-3.1]                              |

### A-Blox parameters (KOSDAQ)

| Parameter                        | Value                                                            | Source                       |
|----------------------------------|------------------------------------------------------------------|------------------------------|
| Eligible securities              | Stocks, KDRs (admin / liquidation issues excluded)               | [KRX-TOUR-KOSDAQ-EXCEPT-T4]  |
| Pre-open trading window          | 08:00–09:00 KST                                                   | [KRX-TOUR-KOSDAQ-EXCEPT-T4]  |
| Regular-session trading window   | 09:00–15:00 KST                                                   | [KRX-TOUR-KOSDAQ-EXCEPT-T4]  |
| Matching method                  | Continuous, by time priority                                       | [KRX-TOUR-KOSDAQ-EXCEPT-T4]  |
| Execution price (off-hours)      | Session VWAP for the day                                          | [KRX-TOUR-KOSDAQ-EXCEPT-T4]  |
| Execution price (regular)        | VWAP from match time to session close                             | [KRX-TOUR-KOSDAQ-EXCEPT-T4]  |
| **Minimum order size**           | **KRW 200,000,000** (base price × quotation quantity)            | [KRX-TOUR-KOSDAQ-EXCEPT-T4]  |
| **Trading unit**                 | **1 share**                                                       | [KRX-TOUR-KOSDAQ-EXCEPT-T4]  |
| No after-hours session            | yes — A-Blox not available post-close                             | [KRX-TOUR-KOSDAQ-EXCEPT-T4]  |

### Quotation disclosure during single-price auction (KOSDAQ)

[KRX-TOUR-KOSDAQ-EXCEPT-T5] reports the same disclosure shape as KOSPI:

| Mode                                                 | Disclosed during the window                                                                                                       | Source                       |
|------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------|------------------------------|
| Single-price auction (opening / closing / resumption / off-hours single-price) | Expected matching price + quantity; **3-deep** expected best bid/ask prices + quantities; if no cross is feasible, the most prior single-side bid or ask price + quantity | [KRX-TOUR-KOSDAQ-EXCEPT-T5] |
| Pre-open single-price registration window            | Disclosure starts **10 minutes after** order registration begins (matches KOSPI's 08:40 opening curtain)                          | [KRX-TOUR-KOSDAQ-EXCEPT-T5] |
| Continuous auction                                   | **10-deep** quotation book (10 best bids + 10 best asks)                                                                          | [KRX-TOUR-KOSDAQ-EXCEPT-T5] |
| Off-hours closing-price                              | Total remaining bid + ask quantities only (price is fixed at the close, so no price disclosure)                                   | [KRX-TOUR-KOSDAQ-EXCEPT-T5] |

## Worked examples

The KOSPI single-price auction matching example (Example A), the 3-pass quantity-allocation worked example at the upper price limit (Example B), and the market-order deemed-price worked example (Example C) all carry over to KOSDAQ unchanged because §17 / §18 of the KOSDAQ BR mirror §22 / §23 of the KOSPI BR. See [KOSPI § Worked examples](../kospi/auctions.md#worked-examples).

The only KOSDAQ-side parameter substitution would be in an A-Blox example, where the minimum-order test would fire at KRW 200M (rather than KRW 500M) and a 1-share-precision quantity (rather than a 100-share lot).

## Edge cases & open questions

- Edge case: KOSDAQ §21-3.3 explicitly defines off-hours single-price tradable price range as the intersection of the ±10 % cone (around the day's close) and the daily price-limit band — same construction as KOSPI. See [KOSPI Other Topics § Off-hours single-price](../kospi/other_topics.md#off-hours-single-price-trade) for the binding-bound discussion.
- Edge case: KOSDAQ §21-2 (시간외경쟁대량매매 (*si-gan-oe gyeong-jaeng dae-ryang mae-mae*; off-hours competitive-block) is restricted to the **pre-open** off-hours session (08:00–09:00) only. The KOSDAQ A-Blox tour caution "There is no competitive block trading in after-hours trading session" reflects this rule — the after-hours competitive block does not exist. KOSPI behaves identically.
- Edge case: KOSDAQ A-Blox eligibility per the tour drops ETF / ETN from its eligibility list (vs KOSPI's tour which includes them). KOSDAQ-listed ETFs / ETNs are scarce relative to KOSPI; whether the underlying rule actually excludes them or the tour-page list is just abbreviated requires reading the KOSDAQ Enforcement Rule (R6 unresolved). Treat the eligibility delta as tour-page-color until R6 confirms.
- Open question: The 3-pass quantity-allocation rule (100 × lot, then half-of-residual, then residue) is delegated to the KOSDAQ Enforcement Rule. KOSPI's Enforcement Rule §34 sets these; KOSDAQ's analogue cannot yet be cited (R6). The KOSDAQ tour [KRX-TOUR-KOSDAQ-METHOD-T6] confirms "the prior quantity shall be allocated first" with example "100, 500, 1000, 2000 shares" — consistent with the KOSPI 3-pass scheme but does not explicitly enumerate the three passes. Verify article numbers at R6 resolution.
- Open question: The newly-listed-issue first-price-auction-day random-extension window is delegated to the KOSDAQ Enforcement Rule (analogue of KOSPI §67-2). The §22 article on KOSDAQ explicitly says "세칙으로 달리 정할 수 있다" (*se-chik-eu-ro dal-li jeong-hal su it-da*; "may be set differently by Enforcement Rule") — which means there is *flexibility* for the KOSDAQ rule to differ from the KOSPI rule. Cross-check newly-listed-issue rules at R6 resolution; also see [KOSPI Price Ranges § Newly-listed-day band](../kospi/price_ranges.md) for the +300 % / -60 % first-day band that may or may not apply identically on KOSDAQ.
- Open question: KOSDAQ tour [KRX-TOUR-KOSDAQ-METHOD-T6] mentions "issues to be delisted" alongside "administrative issue" as triggering single-price-only matching. KOSDAQ §23.1.2 designates "정리매매종목" (*jeong-ri-mae-mae-jong-mok*; liquidation issues) for that mode; the §23.1.3 "단기과열종목" path is the short-term overheat case. Whether "administrative issue" (관리종목) is itself a single-price-only-mode trigger requires reading the KOSDAQ Listing Regulation (not in source inventory) and the Enforcement Rule for §23-3.
- Edge case: KOSDAQ §18.5 multiple-matching-price tie-break sub-cases were updated 2025-02-05 in lockstep with KOSPI §23.5. The substance of the three sub-cases (matching range above prior price, below prior price, straddling prior price) is identical. A worked example for each sub-case is not produced here — Phase 6 freshness audit should add one if a v1.0 reader is likely to encounter the case.

## Sources

- `KRX-RULE-KOSDAQ-BR-KO` — KOSDAQ Market Business Regulation (코스닥시장 업무규정), bookid 210164370, effective 2026-04-28. Articles cited: §17 (Auction principle and 동시호가 override), §18 (Single-price auction with 5-event list, market-order deemed prices, 합치가격, multi-matching-price tie-break with 2025-02-05 amendments), §19 (Continuous auction with leading-quote pricing), §19-3 (Intraday competitive block / A-Blox source article on KOSDAQ side), §21-2 (Off-hours competitive block, pre-open only), §21-3 (Off-hours single-price 16:00–18:00), §22 (Newly-listed first-price flexibility delegated to Enforcement Rule), §23 (Trading-method-change for liquidation, overheat, market-monitoring referrals), §23-2 (Short-term overheat designation), §23-3 (Per-issue method change to single-price).
- `KRX-TOUR-KOSDAQ-METHOD-T6` — KRX overview "Periodic call auction" (KOSDAQ); English, not authoritative. Used for the random-end summary, the price-then-quantity priority at upper / lower limits, and the off-hours periodic call auction (16:00–18:00, 12 × 10-min, ±10 % cone) confirmation.
- `KRX-TOUR-KOSDAQ-EXCEPT-T4` — KRX overview "Auction-based Block Trade (A-Blox)" (KOSDAQ); English, not authoritative. **Sole source** for the KOSDAQ-specific A-Blox parameters: KRW 200M minimum, 1-share trading unit, eligible-security list, no-after-hours-A-Blox cautionary note. Numeric thresholds flagged for re-verification at R6 resolution.
- `KRX-TOUR-KOSDAQ-EXCEPT-T5` — KRX overview "Quotation disclosure during single-price auction" (KOSDAQ); English, not authoritative. Used for the per-mode disclosure-shape table (3-deep single-price, 10-deep continuous, off-hours-closing-price total-only).
