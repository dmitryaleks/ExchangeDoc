---
title: "Other Topics (KOSPI)"
markets: [KOSPI]
last_reviewed: 2026-04-30
sources:
  - KRX-RULE-KOSPI-BR-KO
  - KRX-RULE-KOSPI-BR-ENFORCE-KO
  - KRX-TOUR-KOSPI-EXCEPT-T1
  - KRX-TOUR-KOSPI-EXCEPT-T2
  - KRX-TOUR-KOSPI-EXCEPT-T3
  - KRX-TOUR-KOSPI-EXCEPT-T6
  - KRX-TOUR-KOSPI-OPS-T4
  - KRX-TOUR-KOSPI-OPS-T7
  - KRX-TOUR-KOSPI-OPS-T8
---

> See also: [Market Hours (KOSPI)](./market_hours.md), [Auctions (KOSPI)](./auctions.md), [Volatility Interruption (KOSPI)](./volatility_interruption.md), [Circuit Breakers (KOSPI)](./circuit_breakers.md), [Other Topics (KOSDAQ)](../kosdaq/other_topics.md), [Comparison](../common/comparison.md).

## Summary

- This file is the catch-all for KOSPI topics that did not warrant a top-level file: **off-hours session details** (closing-price trade, single-price, block, basket), **regular-session block/basket trade**, **liquidation issues** (7-day single-price-only window with no price limit), **program trading + sidecar** (5 %-1-min-5-min suspension), **liquidity provider (LP) system** (3 % spread duty), **short-term overheat designation** (3-trading-day single-price-only matching), and **error-trade handling**.
- The off-hours sessions consume **08:00–09:00 KST** before the regular session and **15:40–18:00 KST** after. Closing-price trades (시간외종가매매, *si-gan-oe jong-ga mae-mae*) match at the day's close (or prior day's close for the pre-open window) by **time priority only** — no price competition [KRX-TOUR-KOSPI-EXCEPT-T1]. Off-hours single-price (시간외단일가매매, *si-gan-oe dan-il-ga mae-mae*) runs **12 × 10-minute single-price auctions** at ±10 % of the closing price, within the daily price-limit band [KRX-TOUR-KOSPI-EXCEPT-T1].
- Block / basket trades — both regular-session (장중대량매매 / 장중바스켓매매, *jang-jung dae-ryang mae-mae*) and off-hours (시간외대량매매 / 시간외바스켓매매) — require a minimum size of **5,000× the trading lot** (500× for ETF / ETN) or **KRW 100,000,000** notional, with both sides agreed [KRX-TOUR-KOSPI-EXCEPT-T2; KRX-TOUR-KOSPI-EXCEPT-T3].
- Liquidation issues (정리매매종목, *jeong-ri mae-mae jong-mok*) trade for **7 trading days** in **14 × 30-minute single-price auctions per day**, with **no daily price limit** [KRX-TOUR-KOSPI-EXCEPT-T6; KRX-RULE-KOSPI-BR-ENFORCE-KO §56].
- The **sidecar** halts program trading (program-buy on a 5 % uptick or program-sell on a 5 % downtick of the most-traded futures contract) for **5 minutes**; sidecar is suppressed in the last 40 minutes of the session and is cancelled by a CB [KRX-RULE-KOSPI-BR-ENFORCE-KO §20; KRX-TOUR-KOSPI-OPS-T4].
- The **liquidity-provider (LP) system** is a contractual obligation imposed on members for thinly-traded issues: tighten any spread > 3 % to ≤ 3 % with at least **5 × the trading lot** of quote size [KRX-TOUR-KOSPI-OPS-T7].
- **Short-term overheat issues (단기과열종목, *dan-gi gwa-yeol jong-mok*)** are designated when the joint price-rise + turnover + volatility criteria are met across two consecutive 10-day windows; once designated, the issue trades in **single-price-only** mode for **3 trading days** [KRX-RULE-KOSPI-BR-ENFORCE-KO §133, §134; KRX-TOUR-KOSPI-OPS-T8].

## Detailed rules

### Off-hours closing-price trade (시간외종가매매)

The off-hours closing-price trade is a non-competitive matching session that lets investors trade at the previous (pre-open) or current-day (post-close) closing price [KRX-TOUR-KOSPI-EXCEPT-T1]:

- **Trading hours.** 08:30–08:40 KST and 15:40–16:00 KST — 30 minutes total.
- **Quotation receipt hours.** 08:30–08:40 and 15:30–16:00 — 40 minutes total. Note the post-close window receives orders from 15:30 even though matching does not begin until 15:40 (see also [Market Hours § Edge cases](./market_hours.md#edge-cases-open-questions) for the 10-minute pre-trade buffer discussion).
- **Eligible securities.** Stock certificates, ETFs, ETNs, and KDRs **excluding** unexecuted issues of the day (i.e. issues with no trades during the regular session — these have no closing price to trade at).
- **Execution price.** Pre-open: the previous trading day's close. Post-close: the current day's close.
- **Order type.** Limit at the closing price only — no other types.
- **Matching.** Time priority only — earlier orders fill first. There is no price competition.
- **Cancel and correct.** Quantity may be reduced; the order may be cancelled. **Price may not be revised** — the price is fixed at the closing price [KRX-TOUR-KOSPI-EXCEPT-T1].
- **Trading unit.** 1 share.

### Off-hours single-price trade (시간외단일가매매)

A separate post-close session runs single-price auctions every 10 minutes [KRX-TOUR-KOSPI-EXCEPT-T1; KRX-RULE-KOSPI-BR-ENFORCE-KO §51-2]:

- **Trading hours.** 16:00–18:00 KST — 12 single-price auctions.
- **Method.** Periodic call auction every 10 minutes, with random-end (per [KRX-RULE-KOSPI-BR-ENFORCE-KO §35.1]) — see [Auctions § Random-end mechanism](./auctions.md#random-end-mechanism).
- **Price range.** ±10 % of the day's close, capped within the daily price-limit band (상한가 / 하한가, *sang-han-ga* / *ha-han-ga*; see [Price Ranges § Daily price limit](./price_ranges.md#daily-price-limit)).
- **Order type.** Limit only — no market, conditional, best-counterparty, best-same, midpoint, stop-limit, or competitive-block per [KRX-RULE-KOSPI-BR-ENFORCE-KO §14.2.1.ma].
- **Trading unit.** 1 share.

The 12-auction structure means the off-hours single-price effectively produces 12 distinct prints per session; market-data consumers should expect 12 sequence-numbered prints, not a continuous stream.

### Off-hours block trade (시간외대량매매)

Pre-open and post-close block trades are negotiated trades with a minimum-size guard [KRX-TOUR-KOSPI-EXCEPT-T2]:

- **Trading hours.** 08:00–09:00 KST + 15:40–18:00 KST — 200 minutes total.
- **Minimum order size.** ≥ 5,000 × the trading lot (≥ 500 × for ETF / ETN); **or** ≥ KRW 100,000,000 notional. The OR makes it possible to qualify for block-trade routing on either dimension.
- **Eligible securities.** Stock certificates, ETF, ETN, KDR — excluding issues with no trades during the regular session.
- **Execution price.** Negotiated between the buying and selling counterparties, **within the daily price-limit band** (상한가 / 하한가).
- **Order structure.** Pair of bid and ask orders with matching specifics (price, quantity, counterparty). Either the buy or the sell side must be from a single member.
- **Cancel and correct.** Allowed before execution.

The post-close block-trade window from 15:40 onward overlaps with the off-hours closing-price (until 16:00) and off-hours single-price (16:00–18:00) windows. A member can route block-eligible flow into block, leaving the remainder for the closing-price or single-price track.

### Regular-session block / basket trade (장중대량매매 / 장중바스켓매매)

Block / basket trades are also available during the regular session [KRX-TOUR-KOSPI-EXCEPT-T3]:

- **Trading hours.** 09:00–15:30 KST.
- **Minimum order size.** Same as off-hours block (≥ 5,000 × lot, 500 × for ETF/ETN, or ≥ KRW 100,000,000).
- **Execution price.** Negotiated, **within the high-low range of the day's prints up to the moment of order placement** — *not* the daily price-limit band. So the in-session block price is bounded by the dynamic intra-day range, which narrows as the session progresses.
- **Eligible securities.** Stock, ETF, ETN, KDR — excluding issues with no regular-session prints yet (i.e. before the opening single-price clears).
- **Order structure.** Pair of bid and ask orders with matching conditions; either side from a single member.
- **Cancel and correct.** Allowed before execution.

The regular-session block path is distinct from A-Blox (auction-based block trade — see [Auctions § A-Blox](./auctions.md#a-blox-auction-based-block-trade)). A-Blox uses a continuous-auction with VWAP execution; regular-session block uses pair-matching at a negotiated price.

### Liquidation issues (정리매매종목)

When KRX delists an issue, the issuer's shareholders get a 7-day window to liquidate via the liquidation-trading mechanism [KRX-TOUR-KOSPI-EXCEPT-T6; KRX-RULE-KOSPI-BR-ENFORCE-KO §56]:

- **Window length.** 7 trading days from delisting decision.
- **Matching method.** **14 × 30-minute single-price auctions per day** (i.e. one auction every 30 minutes throughout the regular session window of 09:00–15:30, with the closing-call falling on the last of these). The narrow auction cadence is intended to dampen the price-discovery instability of an exiting issue.
- **Daily price limit.** **None** [KRX-RULE-KOSPI-BR-KO §20.3] — see [Price Ranges § Daily price limit](./price_ranges.md#daily-price-limit). Liquidation issues can trade arbitrarily high or low (down to the KRW 1 minimum tick).
- **Cross-applicable rules.** Liquidation issues are excluded from VI [KRX-RULE-KOSPI-BR-ENFORCE-KO §41-2.4.1 — see VI doc § Exclusions](./volatility_interruption.md#exclusions-issues-vi-does-not-apply-to), excluded from §17.1.5 self-match-prevention via §14.1.5.a, and have type-restricted quotation eligibility (no market, no conditional, no best-counter, no best-same, no midpoint, no stop-limit, no competitive — limit only) per [KRX-RULE-KOSPI-BR-ENFORCE-KO §14.2.1.a].

### Program trading and the sidecar

**Program trading (프로그램매매, *peu-ro-geu-raem mae-mae*)** is defined in [KRX-RULE-KOSPI-BR-KO §2.20] as one of two transaction patterns:

- **Index arbitrage (지수차익거래)** — linked simultaneous trading of the index basket and the corresponding futures or options to profit from the basis spread.
- **Non-arbitrage program trading (비차익거래)** — same person concurrently submits orders on ≥ 15 issues in the KOSPI 200 stock-group within a defined timeframe [KRX-TOUR-KOSPI-OPS-T4].

The **sidecar** is the program-trading-specific halt mechanism [KRX-RULE-KOSPI-BR-ENFORCE-KO §20]:

- **Trigger.** The "reference issue" — the most-traded futures contract among the index futures linked to KOSPI per [KRX-RULE-KOSPI-BR-KO §16.1] — moves **≥ 5 %** above (or below) its base price, sustained for **1 minute** [KRX-RULE-KOSPI-BR-ENFORCE-KO §20.1].
- **Action.** A "validity suspension preliminary notice" (효력정지예고, *hyo-ryeok-jeong-ji ye-go*) is issued; if conditions persist, **program-buy quotations are suspended for 5 minutes** (on the upside) or **program-sell quotations are suspended for 5 minutes** (on the downside).
- **Restoration.** After the 5-minute suspension, program quotations resume in receipt order [KRX-TOUR-KOSPI-OPS-T4].
- **Daily cap.** Sidecar cannot fire after **40 minutes before 장종료** (i.e. after 14:50 KST) [KRX-TOUR-KOSPI-OPS-T4]. Sidecar is **cancelled** by a CB on the spot market [KRX-TOUR-KOSPI-OPS-T4] — see [Circuit Breakers § Interaction with VI and other stabilization](./circuit_breakers.md#interaction-with-vi-and-other-stabilization).
- **Restoration on re-cross.** If the futures price retraces back inside the ±5 % band, or if the futures-side trading is itself halted under Derivatives Market BR §76, the preliminary notice may be lifted [KRX-RULE-KOSPI-BR-ENFORCE-KO §20.2].

### Liquidity provider (LP) system

For inactive-trading issues, KRX engages member firms to provide continuous two-sided quotations under contract [KRX-TOUR-KOSPI-OPS-T7]:

- **Eligible securities.** Issues with liquidity below a threshold defined by KRX. Common cases: ETFs, ETNs, ELWs, and certain low-turnover stocks.
- **LP qualification.** A member that operates proprietary trading and has appointed an LP staffer. A member that received the lowest LP-evaluation rating for **two consecutive quarters** is suspended from the LP role for **1 year**.
- **LP duty.** When the bid-ask spread exceeds **3 %**, the LP must submit quotations to bring the spread back inside 3 %. The LP-quote minimum size is **5 × the trading lot** (or per the LP contract).
- **Quotation type.** LP quotations are best-same-side limits (최우선지정가호가) or regular limits, configurable per LP contract [KRX-RULE-KOSPI-BR-ENFORCE-KO §14.2.2.a.(1)].
- **Short-sale exemption.** LP-hedge sells of underlyings (for ELW, ETF, ETN LPs) are exempt from the §18 uptick rule per §18.2.5–7-2 — see [Short Selling § Uptick rule exemptions](./short_selling.md#uptick-rule-exemptions).

### Short-term overheat (단기과열종목)

When the joint price-rise + turnover + volatility metrics indicate an issue is overheated, KRX designates it for **3 trading days** of single-price-only matching [KRX-RULE-KOSPI-BR-ENFORCE-KO §133, §134; KRX-TOUR-KOSPI-OPS-T8]:

- **Designation criteria** (§133-2.3). All three of:
  1. **Price rise:** Today's close ≥ 130 % of the average close over the past 40 trading days.
  2. **Turnover:** Average daily turnover over the past 2 days ≥ 600 % of the average over the past 40 days. *(Daily turnover = (regular-session traded notional) / (close × listed-share count).)*
  3. **Volatility:** Average daily volatility over the past 2 days ≥ 150 % of the average over the past 40 days. *(Daily volatility = (high − low) / ((high + low) / 2).)*
- **Sequence.** A "preliminary designation notice" (지정예고, *ji-jeong-ye-go*) fires when criteria are met for the first time. A formal designation fires when criteria are met **again within 10 trading days** of the preliminary notice (with both qualifying days having a higher close than the preceding trading day's close).
- **Designation effect.** From the day after designation, the issue trades in **single-price-only** mode (per [KRX-RULE-KOSPI-BR-ENFORCE-KO §56-2]) for **3 trading days**.
- **Designation extension.** If the close on the last designation day is **≥ 120 %** of the close on the trading day before designation, the designation is extended by another 3-day cycle [KRX-RULE-KOSPI-BR-ENFORCE-KO §134.2]. Repeats until the 120 %-threshold no longer triggers.
- **Top-100 carve-out.** Issues among the **top 100 by market cap** across KOSPI + KOSDAQ are exempt from the overheat designation [KRX-RULE-KOSPI-BR-ENFORCE-KO §133.2 proviso]. (Updated 2026-01-07 from a prior threshold framework.)

Short-term overheat issues are also excluded from VI per [KRX-RULE-KOSPI-BR-ENFORCE-KO §41-2.4.2 — see VI doc § Exclusions](./volatility_interruption.md#exclusions-issues-vi-does-not-apply-to).

### Treasury stock trading

Treasury-stock acquisition and disposal by listed corporations is regulated under [KRX-RULE-KOSPI-BR-KO §35–§39]. The mechanism is operational-flow-heavy and outside the algo-execution scope of this documentation; the key constraints visible to an execution algo are:

- Treasury-stock orders are **not permitted as market or conditional-limit** [KRX-RULE-KOSPI-BR-ENFORCE-KO §14.2.1.la].
- Treasury-stock quote quantities are subject to the §57.1.3 quantity restriction (referenced from §12-2.3.d in [Trading Rules § Pre-quote control](./trading_rules.md#quotation-flow-receipt-recording-pre-quote-control)).

For full treasury-stock workflow detail, see KRX-TOUR-KOSPI-EXCEPT-T5 (not extracted in depth here — out of execution-algo scope).

### Error-trade rules

KRX has **two formal correction / relief mechanisms** for trades that have already printed: the §28 KRX-driven correction path (for matching-process errors detected by KRX itself), and the §28-2 mass-erroneous-trade relief path (member-requested, KRX-discretionary, gated to large-error criteria). Outside those paths, the §13.1 finality rule binds and error handling is resolved at the **member-customer level** via post-trade reconciliation.

- A trade printed on KRX is **final** at the moment of match [KRX-RULE-KOSPI-BR-KO §13.1] — see [Order Amendments § Scope of cancel and correct](./amendments.md#scope-of-cancel-and-correct).
- **§28 — error-trade correction by KRX.** When KRX detects a matching-process error (its own brokerage-process error or a member's quotation-input error), KRX may correct the trade record per the procedure set in the Enforcement Rule [KRX-RULE-KOSPI-BR-KO §28]. This is a narrow, KRX-driven correction path — it does not require a member request.
- **§28-2 — mass-erroneous-trade relief (대규모착오매매의 구제, *dae-gyu-mo-chak-o-mae-mae-ui gu-je*).** Added 2015-11-04. KRX may, on **member request**, relieve a "mass-erroneous trade" — a trade that the member or consigner agrees was contrary to original intent, where settlement-difficulty and market-disruption thresholds (set in the Enforcement Rule §51) are met [KRX-RULE-KOSPI-BR-KO §28-2.1]. Eligible securities: shares, foreign DRs, ETFs, ETNs, ELWs, beneficiary certificates. The §28-2.1 proviso ("시장상황의 급변, 그 밖에 시장관리상 필요하다고 인정하는 경우에는 제외") bars relief when KRX deems the broader market situation makes relief inappropriate. KOSDAQ has the parallel §27-2 with **narrower** security scope (excludes ETF / ETN / ELW) — see [Trading Rules (KOSDAQ)](../kosdaq/trading_rules.md#delta-vs-kospi).
- The member resolves a clearly-erroneous trade that does **not** meet the §28-2 thresholds by **internal off-exchange settlement** between member and customer (e.g. the member absorbs the error and books an internal P&L charge).
- For mass-quotation errors (e.g. a fat-finger from one HSA trader), the bulk-cancel facility (§17-2) and disconnect-cancel facility (§17-3) limit the *forward* exposure but do not retroactively undo prints — see [Order Amendments § Bulk cancel](./amendments.md#bulk-cancel).
- Cascading-error market-wide events (e.g. a 2013-style runaway algorithm) are handled by KRX-discretionary halt under [KRX-RULE-KOSPI-BR-KO §27] (system failure / quote flooding) — see [Circuit Breakers § Relationship to individual-issue halts](./circuit_breakers.md#relationship-to-individual-issue-halts).

The practical implication for an execution algo: a printed trade is reversible only via §28 (KRX-discretionary, narrow) or §28-2 (member-requested, gated to large-error thresholds); outside those paths, prints are final. Risk-budget for fat-finger errors at the member-system pre-quote level — the §28-2 relief path is a backstop, not a routine recovery mechanism.

## Parameters & thresholds

### Table 1 — Off-hours session matrix

| Session                                | Hours                              | Method                | Price/range                                    | Order types     | Source                                |
|----------------------------------------|------------------------------------|-----------------------|------------------------------------------------|-----------------|---------------------------------------|
| Off-hours closing-price (pre-open)     | 08:30–08:40 KST                    | Time priority         | Prior day's close (fixed)                       | Limit-at-close  | [KRX-TOUR-KOSPI-EXCEPT-T1]            |
| Off-hours closing-price (post-close)   | 15:40–16:00 KST                    | Time priority         | Day's close (fixed)                             | Limit-at-close  | [KRX-TOUR-KOSPI-EXCEPT-T1]            |
| Off-hours single-price                 | 16:00–18:00 KST                    | 12 × 10-min call auctions | ±10 % of day's close, within daily limit       | Limit only      | [KRX-TOUR-KOSPI-EXCEPT-T1]            |
| Off-hours block                        | 08:00–09:00 + 15:40–18:00          | Negotiated bid-ask pair | Within daily limit                              | Block-paired    | [KRX-TOUR-KOSPI-EXCEPT-T2]            |
| Off-hours basket                       | 08:00–09:00 + 15:40–18:00          | Negotiated basket pair | Within daily limit                              | Basket-paired   | [KRX-RULE-KOSPI-BR-ENFORCE-KO §11.2]  |
| Regular-session block                  | 09:00–15:30                        | Negotiated bid-ask pair | Within day's high–low range up to placement     | Block-paired    | [KRX-TOUR-KOSPI-EXCEPT-T3]            |
| Regular-session basket                 | 09:00–15:30                        | Negotiated basket pair | Within day's high–low range up to placement     | Basket-paired   | [KRX-TOUR-KOSPI-EXCEPT-T3]            |
| Regular-session A-Blox                 | 09:00–15:00                        | Continuous time-priority anonymous | VWAP-based                            | Competitive-block | [KRX-TOUR-KOSPI-EXCEPT-T4 — see auctions.md] |

### Table 2 — Block / basket minimum size

| Trade type                       | Minimum size                                            | Source                                  |
|----------------------------------|---------------------------------------------------------|-----------------------------------------|
| Off-hours block                  | ≥ 5,000 × trading lot (500 × for ETF/ETN), or ≥ KRW 100,000,000 | [KRX-TOUR-KOSPI-EXCEPT-T2]              |
| Off-hours basket                 | Same as off-hours block                                 | [KRX-TOUR-KOSPI-EXCEPT-T2]              |
| Regular-session block            | Same as off-hours block                                 | [KRX-TOUR-KOSPI-EXCEPT-T3]              |
| Regular-session basket           | Same as off-hours block                                 | [KRX-TOUR-KOSPI-EXCEPT-T3]              |
| Regular-session A-Blox           | ≥ KRW 500,000,000 (per A-Blox rules)                    | [KRX-TOUR-KOSPI-EXCEPT-T4 — see auctions.md] |

### Table 3 — Sidecar parameters

| Parameter                                 | Value                                          | Source                                  |
|-------------------------------------------|------------------------------------------------|-----------------------------------------|
| Trigger threshold                         | ≥ 5 % move on most-traded index futures        | [KRX-RULE-KOSPI-BR-ENFORCE-KO §20.1]    |
| Persistence requirement                   | 1 minute                                       | [KRX-RULE-KOSPI-BR-ENFORCE-KO §20.1]    |
| Suspension duration                       | 5 minutes                                      | [KRX-TOUR-KOSPI-OPS-T4]                 |
| Daily cap (latest fire time)              | 14:50 KST (40 min before 장종료)               | [KRX-TOUR-KOSPI-OPS-T4]                 |
| CB-cancels-sidecar                        | Yes                                            | [KRX-TOUR-KOSPI-OPS-T4]                 |
| Sidecar suppression on rebound            | Yes — when futures returns inside ±5 % band    | [KRX-RULE-KOSPI-BR-ENFORCE-KO §20.2]    |

### Table 4 — Short-term overheat designation criteria

| Criterion           | Threshold (vs prior 40-day average)                      | Source                                  |
|---------------------|----------------------------------------------------------|-----------------------------------------|
| Price rise          | ≥ 130 % of the 40-day average close                      | [KRX-RULE-KOSPI-BR-ENFORCE-KO §133-2.3.1] |
| Turnover            | 2-day average turnover ≥ 600 % of 40-day average         | [KRX-RULE-KOSPI-BR-ENFORCE-KO §133-2.3.2] |
| Volatility          | 2-day average volatility ≥ 150 % of 40-day average       | [KRX-RULE-KOSPI-BR-ENFORCE-KO §133-2.3.3] |
| Designation length  | 3 trading days, single-price-only                        | [KRX-RULE-KOSPI-BR-ENFORCE-KO §134.1]   |
| Extension trigger   | Designation-end close ≥ 120 % of pre-designation close   | [KRX-RULE-KOSPI-BR-ENFORCE-KO §134.2]   |
| Top-100 carve-out   | Issues in top-100 by market cap (KOSPI + KOSDAQ) exempt  | [KRX-RULE-KOSPI-BR-ENFORCE-KO §133.2 proviso, updated 2026-01-07] |

### Table 5 — LP duty

| Parameter                                | Value                                          | Source                                  |
|------------------------------------------|------------------------------------------------|-----------------------------------------|
| Spread tightening trigger                | Bid-ask spread > 3 %                           | [KRX-TOUR-KOSPI-OPS-T7]                 |
| Spread tightening target                 | Reduce spread to ≤ 3 %                         | [KRX-TOUR-KOSPI-OPS-T7]                 |
| Minimum quote size (each side)           | 5 × trading lot (or per LP contract)           | [KRX-TOUR-KOSPI-OPS-T7]                 |
| Suspension on lowest-rating consecutive  | 1 year, after 2 consecutive lowest ratings     | [KRX-TOUR-KOSPI-OPS-T7]                 |
| Quotation type                           | Best-same-side limit (최우선지정가호가) or regular limit per contract | [KRX-RULE-KOSPI-BR-ENFORCE-KO §14.2.2.a.(1)] |

## Worked examples

### Example A — off-hours single-price auction sequence

A KOSPI 200 stock closes at KRW 50,000 at 15:30. The day's daily price-limit band is 35,000 (lower) – 65,000 (upper) per [Price Ranges § Daily price limit](./price_ranges.md#daily-price-limit).

The off-hours single-price session runs 16:00–18:00. Per [KRX-TOUR-KOSPI-EXCEPT-T1] and [KRX-RULE-KOSPI-BR-ENFORCE-KO §51-2]:

- **Permitted price range.** ±10 % of the close → 45,000–55,000. The intra-day 35,000–65,000 band would be wider, so the off-hours rule is the binding constraint.
- **Auction cadence.** 12 single-price auctions: 16:10, 16:20, 16:30, …, 18:00. (Actually 12 = (18:00 − 16:00) / 10 min — the first clears at 16:10, the last at 18:00.)
- **Random end.** Each clears at a randomly-determined moment within 30 seconds of its nominal end [KRX-RULE-KOSPI-BR-ENFORCE-KO §35.1].
- **Order types.** Limit only [KRX-RULE-KOSPI-BR-ENFORCE-KO §14.2.1.ma].

A sell limit at KRW 56,000 submitted at 16:05 is **rejected** at the member pre-quote control — the price is outside the off-hours ±10 % cone (56,000 > 55,000) [KRX-RULE-KOSPI-BR-ENFORCE-KO §12-2.4.b — referenced from Trading Rules].

### Example B — sidecar trigger and resumption

Most-traded KOSPI 200 futures contract opens at 100.00 (base price). At 13:50, the futures contract trades at 95.00 (= 95 % of base, = 5 % drop). Persistence clock starts.

- **13:51:00** — futures still ≤ 95.00 for 1 minute. **Sidecar fires** [KRX-RULE-KOSPI-BR-ENFORCE-KO §20.1]: program-sell quotations on the spot market are suspended for 5 minutes.
- **13:51:00 → 13:56:00** — program-sell suspension. Program-buy quotations continue normally.
- **13:56:00** — suspension ends; program-sell quotations resume in receipt order.
- During the 5-minute window, the futures may continue to move; if it retraces back above 95.00, the **preliminary notice** for further sidecar action is lifted [KRX-RULE-KOSPI-BR-ENFORCE-KO §20.2].
- If KOSPI itself drops 8 % from prior close during the sidecar, **CB Phase 1 fires** and **cancels the sidecar** [KRX-TOUR-KOSPI-OPS-T4]; the spot market enters its 20-min CB halt instead.

### Example C — short-term overheat designation cascade

Issue X has 40-day average close 10,000 KRW, 40-day average daily turnover 0.5 %, 40-day average daily volatility 1.5 %.

- **Day T**: close = 13,500 (135 % of 40-day avg, > 130 % → criterion 1 met). 2-day average turnover = 3.5 % (700 % of 0.5 % = 700 % > 600 % → criterion 2 met). 2-day average volatility = 2.5 % (167 % of 1.5 %, > 150 % → criterion 3 met). Same-day close 13,500 > yesterday's close 12,800 → triggers preliminary notice.
- **Day T+1** — issue X carries the preliminary designation notice [KRX-RULE-KOSPI-BR-ENFORCE-KO §133-2.1.1].
- **Day T+5** (within 10-day window) — close = 16,000 (160 % of 40-day avg, still > 130 %). Turnover and volatility re-criteria also met. Same-day close 16,000 > yesterday's 15,500. **Re-met within 10 trading days** → formal designation criteria satisfied.
- **Day T+6** — issue X is **designated** as a short-term overheat issue [KRX-RULE-KOSPI-BR-ENFORCE-KO §133.1.1]. Trades single-price-only for the next 3 trading days (T+6, T+7, T+8) per §56-2.
- **Day T+9** — close = 19,500 (vs T+5 close 16,000 → 121.875 %). > 120 % → designation extends for another 3-day cycle (T+9, T+10, T+11) [KRX-RULE-KOSPI-BR-ENFORCE-KO §134.2].
- **Day T+12** — extension cycle ends. If the close on T+11 is < 120 % of T+8 close, designation is released; otherwise another 3-day extension.

## Edge cases & open questions

- Edge case: The off-hours closing-price post-close window receives orders from 15:30 but does not match until 15:40 — a 10-minute pre-trade buffer that is not visible in the rulebook text but is operational [KRX-TOUR-KOSPI-EXCEPT-T1; KRX-RULE-KOSPI-BR-ENFORCE-KO §11.2.b(1)]. See [Market Hours § Edge cases](./market_hours.md#edge-cases-open-questions) — this is the same buffer flagged there.
- Edge case: Off-hours single-price prices are bounded by ±10 % of the day's close **and** by the daily price-limit band. When the two diverge (e.g. an issue on its lower limit at the close, with the close = base × 0.7 = 7,000 KRW; the off-hours ±10 % range is 6,300–7,700 KRW; the daily lower limit is 7,000 KRW), the price floor is effectively the daily limit (7,000), not the off-hours ±10 % calculation. Algorithms targeting off-hours liquidity must compute both bounds.
- Edge case: Regular-session block / basket trades use the **dynamic intra-day high-low range up to the moment of order placement**, not the daily price-limit band [KRX-TOUR-KOSPI-EXCEPT-T3]. So a block trade priced inside the daily limit but outside today's intra-day range is rejected. The range narrows over the session for stocks trading inside a tight cone — block-trade pricing flexibility decreases through the day.
- Edge case: Liquidation issues' "no daily price limit" rule does not relax the smallest-tick floor of §31.1 — see [Price Ranges § Edge cases](./price_ranges.md#edge-cases-open-questions). A liquidation issue's lowest possible print is KRW 1.
- Edge case: Sidecar's "most-traded futures contract" reference [KRX-RULE-KOSPI-BR-ENFORCE-KO §20.1] is determined daily — typically the front-month KOSPI 200 futures, but on roll days the next-month contract may take over mid-session. The reference contract for sidecar-trigger purposes can shift mid-day; sidecar parameters track the new reference from the moment it becomes the most-traded.
- Edge case: Short-term overheat criteria are computed using prior 40-trading-day averages — but on-roll-on-listing for a newly-listed issue, the 40-day window is undefined. §133-2.4 carves out newly-listed issues with fewer than 20 days of regular-session prints in the prior 40 [KRX-RULE-KOSPI-BR-ENFORCE-KO §133-2.4.4]. So overheat designation does not apply to issues less than ~30 trading days from IPO.
- Open question: The error-trade-handling section above describes the operational pattern (member-customer reconciliation), but the rulebook does not have a formal "error trade" definition. Whether KRX has a discretionary trade-bust facility under §27 (system failure / quote flooding) for events beyond the bulk-cancel scope is not explicit. Verify against the Member System Access Guidelines for any KRX-discretionary post-trade adjustment authority.
- Open question: LP qualification §14.2.2.a.(1) allows best-same-side limits — see [Order Types § Per-session and per-issue restrictions](./order_types.md#per-session-and-per-issue-restrictions). But the specific LP-quotation-content rules (e.g. the 5×-lot minimum, the 3 % spread duty) are in the LP contract rather than the BR/ER. The contract terms are not archived in the source inventory; treat the OPS-T7 tour as the operational-summary source, not the authoritative contract.
- Open question: Program-trading definition §2.20 requires "≥ 15 issues in KOSPI 200" for non-arbitrage — the threshold is tied to the KOSPI 200 constituent set. For KOSDAQ 150 program trading, a similar threshold should apply via the KOSDAQ BR. Cross-check before designing cross-market program-trading strategies.
- Unsourced claim: [KRX-TOUR-KOSPI-OPS-T7]'s "1 year suspension on 2 consecutive lowest LP-evaluation ratings" detail is not in the BR/ER text; it is operational LP-contract language. Treat as overview color.

## Sources

- `KRX-RULE-KOSPI-BR-KO` — KOSPI Market Business Regulation (유가증권시장 업무규정, *yu-ga-jeung-gwon si-jang eom-mu gyu-jeong*), bookid 210200859, effective 2026-04-28. Articles cited: §2.20 (Program-trading definition; §2.20.1 index arbitrage, §2.20.2 non-arbitrage with the ≥15-issue threshold), §13 (Cancel-only-on-unfilled — referenced for error-handling), §16 (Reference issue for sidecar — referenced from §20 ER), §20 (Daily price limit — referenced for liquidation no-limit and off-hours range), §27 (System-failure halt — referenced for KRX-discretionary error handling), §35–§39 (Treasury stock — referenced).
- `KRX-RULE-KOSPI-BR-ENFORCE-KO` — KOSPI BR Enforcement Rule (유가증권시장 업무규정 시행세칙, *yu-ga-jeung-gwon si-jang eom-mu gyu-jeong si-haeng se-chik*), bookid 210203562, effective 2026-04-28. Articles cited: §11.2.b(1) (Off-hours closing-price receipt window — referenced for the 10-min pre-trade buffer), §14.2 (Per-type per-situation eligibility — referenced for off-hours-limit-only, treasury-stock restrictions, liquidation-issue restrictions, LP best-same-side carve-out), §20 (Sidecar — central article: 5 % trigger, 1-min persistence, suspension scope, restoration on rebound), §35.1 (Random-end — referenced for off-hours single-price auctions), §41-2.4 (VI exclusions — referenced for liquidation and overheat carve-outs), §51-2 (Off-hours single-price — referenced), §56 (Liquidation issues — referenced), §56-2 (Short-term overheat single-price-only mode — referenced), §133 (Short-term overheat designation criteria — central article: §133.1 designation triggers, §133.2 top-100 exemption, §133-2 preliminary notice + 40-day metrics), §134 (Designation release and 120 %-extension cycle).
- `KRX-TOUR-KOSPI-EXCEPT-T1` — KRX overview "Off-hours Closing Price Trade"; English, not authoritative. Used for the off-hours closing-price and off-hours single-price parameter tables (08:30–08:40 / 15:30–16:00 quotation receipt; 15:40–16:00 trading; 16:00–18:00 single-price; ±10 % cone; 12 × 10-min auctions; limit-only).
- `KRX-TOUR-KOSPI-EXCEPT-T2` — KRX overview "Off-hours Block Trade"; English, not authoritative. Used for the minimum-size threshold (≥ 5,000 × lot or ≥ KRW 100M; 500 × for ETF/ETN) and the negotiated-bid-ask-pair structure.
- `KRX-TOUR-KOSPI-EXCEPT-T3` — KRX overview "Regular Session Block/Basket Trade"; English, not authoritative. Used for the regular-session block / basket parameters and the dynamic-intra-day-high-low range constraint.
- `KRX-TOUR-KOSPI-EXCEPT-T6` — KRX overview "Trading of Liquidation Trading Issues"; English, not authoritative. Used for the 7-day window and the 14 × 30-minute single-price-auction-per-day mechanism.
- `KRX-TOUR-KOSPI-OPS-T4` — KRX overview "Program trading"; English, not authoritative. Used for the program-trading definition language (cross-referenced against §2.20 BR), the sidecar mechanism description, and the 14:50 cutoff and CB-cancels-sidecar precedence rules.
- `KRX-TOUR-KOSPI-OPS-T7` — KRX overview "Liquidity Provider (LP) system"; English, not authoritative. Used for the LP qualification language, the 3 % spread duty, the 5 × trading-lot minimum quote size, and the 1-year-on-2-consecutive-lowest-ratings suspension claim (flagged as operational LP-contract content).
- `KRX-TOUR-KOSPI-OPS-T8` — KRX overview "Short-term Volatility Measures (overheat)"; English, not authoritative. Used as a cross-reference and for the historical-color "since November 5, 2012" framing of the overheat-designation system. Current designation criteria are sourced from §133 / §134 of the Enforcement Rule.
