---
title: "Order Types & Quotation Conditions (KOSPI)"
markets: [KOSPI]
last_reviewed: 2026-04-30
sources:
  - KRX-RULE-KOSPI-BR-KO
  - KRX-RULE-KOSPI-BR-ENFORCE-KO
  - KRX-TOUR-KOSPI-BASIC-T2
  - KRX-TOUR-KOSPI-BASIC-T3
  - KRX-TOUR-KOSPI-BASIC-T7
  - KRX-TOUR-KOSPI-METHOD-T5
  - KRX-TOUR-KOSPI-METHOD-T8
---

> See also: [Order Types (KOSDAQ)](../kosdaq/order_types.md), [Auctions (KOSPI)](./auctions.md), [Price Ranges (KOSPI)](./price_ranges.md), [Comparison](../common/comparison.md).

## Summary

- The Business Regulation defines a quotation (호가, *ho-ga*) as a member's submitted intention to buy or sell, and enumerates **eight** quotation types: 지정가 (limit), 시장가 (market), 조건부지정가 (conditional-limit), 최유리지정가 (best-counterparty limit), 최우선지정가 (best-same-side limit), 경쟁대량매매 (competitive block), 중간가 (midpoint), and 스톱지정가 (stop-limit) [KRX-RULE-KOSPI-BR-KO §2.4]. The 중간가호가 (*jung-gan-ga ho-ga*) and 스톱지정가호가 (*seu-top ji-jeong-ga ho-ga*) types were added 2025-02-05.
- Eligibility by security: shares, foreign DRs, ETF units, and ETNs may use **all eight** types; subscription rights, subscription warrants, ELWs, beneficiary certificates (excl. ETF investment-trust units), and debt securities may use **limit only** [KRX-RULE-KOSPI-BR-ENFORCE-KO §10.1].
- A 조건부지정가 (*jo-geon-bu ji-jeong-ga*) — limit-to-market-on-close — operates as a limit during continuous trading and is automatically converted to a market quotation at the opening of the closing-call receipt window (15:20 KST), with conversion priority: low-price-first for sells, high-price-first for buys, ties broken by receipt time [KRX-RULE-KOSPI-BR-ENFORCE-KO §15].
- A stop-limit activates as a regular limit order when the last traded price (or base price if no trade has occurred yet) crosses the stop: ≤ stop for a sell stop, ≥ stop for a buy stop; once activated, the original stop-limit receipt time governs same-price tie-breaking under §22.2.2 [KRX-RULE-KOSPI-BR-ENFORCE-KO §4-3, §15-2].
- Two execution-time-of-life conditions are recognized — IOC (cancel unmatched portion) and FOK (cancel all if any portion can't match) — and a separate self-match-prevention (자전거래방지, *ja-jeon-geo-rae bang-ji*) condition is available to high-speed algorithmic traders [KRX-RULE-KOSPI-BR-ENFORCE-KO §13.2-13.3, §13-2].

## Detailed rules

### Quotation type taxonomy

A quotation (호가) is the member's expression of intention to buy or sell at the Exchange [KRX-RULE-KOSPI-BR-KO §2.4]. The Business Regulation enumerates eight types:

1. **Limit (지정가호가, *ji-jeong-ga ho-ga*)** — issue, quantity, and price specified [KRX-RULE-KOSPI-BR-KO §2.4.1]. A bid limit executes only at or below the specified price; an ask limit only at or above [KRX-TOUR-KOSPI-BASIC-T2].
2. **Market (시장가호가, *si-jang-ga ho-ga*)** — issue and quantity specified, no price; intended to trade immediately at the best available counter-side price [KRX-RULE-KOSPI-BR-KO §2.4.2; KRX-TOUR-KOSPI-BASIC-T2]. Deemed prices for matching purposes are set by §23.3 (single-price auctions) and §24.2 (continuous trading) — see [Auctions (KOSPI)](./auctions.md) for the deemed-price formulas.
3. **Conditional-limit (조건부지정가호가)** — a limit during the continuous session that is automatically converted to a market quotation when the closing single-price receipt window opens (per §23.1.4 and §15 of the Enforcement Rule) [KRX-RULE-KOSPI-BR-KO §2.4.3]. See *Conditional-limit conversion* below.
4. **Best-counterparty limit (최유리지정가호가, *choe-yu-ri ji-jeong-ga ho-ga*)** — issue and quantity specified; price is **deemed** at the best opposite-side quote at the moment the order is received [KRX-RULE-KOSPI-BR-KO §2.4.4]. Specifically, a sell 최유리 is deemed at the highest bid; a buy 최유리 is deemed at the lowest ask. Tour material describes this as an "immediately executable limit order" [KRX-TOUR-KOSPI-BASIC-T2]. See *Best-limit pricing rules* below.
5. **Best-same-side limit (최우선지정가호가, *choe-u-seon ji-jeong-ga ho-ga*)** — issue and quantity specified; price is **deemed** at the best same-side quote at the moment of receipt [KRX-RULE-KOSPI-BR-KO §2.4.5]. A sell 최우선 sits at the lowest existing ask; a buy 최우선 sits at the highest existing bid. Tour material calls this a "best limit order" [KRX-TOUR-KOSPI-BASIC-T2].
6. **Competitive block (경쟁대량매매호가, *gyeong-jaeng dae-ryang mae-mae ho-ga*)** — issue and quantity specified; price is the daily VWAP determined under §30-2.1 (intraday) or §34-3.1 (off-hours) [KRX-RULE-KOSPI-BR-KO §2.4.6]. Tour material refers to this as the A-Blox order type — see [Auctions (KOSPI) §A-Blox](./auctions.md#a-blox-auction-based-block-trade) for trading parameters.
7. **Midpoint (중간가호가)** — issue and quantity specified; price is **deemed** at the arithmetic mean of the best bid and best ask, with sub-KRW digits truncated [KRX-RULE-KOSPI-BR-KO §2.4.7; KRX-RULE-KOSPI-BR-ENFORCE-KO §4-2]. Valid only during continuous (multi-price) auctions; see *Midpoint validity rules* below. *(Added 2025-02-05.)*
8. **Stop-limit (스톱지정가호가)** — issue, quantity, and limit price specified, plus a stop price; the order takes effect as a regular limit order when the last traded price crosses the stop [KRX-RULE-KOSPI-BR-KO §2.4.8; KRX-RULE-KOSPI-BR-ENFORCE-KO §4-3]. *(Added 2025-02-05.)*

A ninth client-side order type is recognized at the customer-member layer: **목표가주문 (*mok-pyo-ga ju-mun*) — target-price order**, where the customer specifies a target price (e.g. VWAP) and the member splits it into multiple limit/market quotations [KRX-RULE-KOSPI-BR-KO §2.5.6; KRX-TOUR-KOSPI-BASIC-T2]. There is no corresponding quotation type at the Exchange — every order ultimately reaches the order book as one of the eight quotation types.

### Eligibility by security type

The Enforcement Rule fixes which quotation types may be used for each security category [KRX-RULE-KOSPI-BR-ENFORCE-KO §10.1]:

- **Group 1: shares (주권), foreign DRs, ETF units, ETNs** — all eight quotation types are available.
- **Group 2: subscription right certs (신주인수권증서), subscription right warrants (신주인수권증권), ELWs (주식워런트증권), beneficiary certs excluding ETF investment-trust units, and debt securities** — limit (지정가호가) only.

Group 2 securities therefore have no market, best-counterparty, best-same-side, conditional, midpoint, stop-limit, or competitive-block paths. Risk filters at the member level enforce this per §12-2.5 (호가의 종류제한 — quotation-type restriction) [KRX-RULE-KOSPI-BR-ENFORCE-KO §12-2.5.a].

### Per-session and per-issue restrictions

Beyond the security-level restrictions of §10.1, the Enforcement Rule prohibits specific (type × condition × situation) combinations — §14.2 has the full schedule. The execution-algo-relevant items are summarized in *Parameters & thresholds* (table 2). The most consequential restrictions:

- **Market and conditional-limit are not permitted for** [KRX-RULE-KOSPI-BR-ENFORCE-KO §14.2.1]: short sale with price restriction (§18), liquidity-provider quotes, market-maker quotes, treasury-stock orders, off-hours sessions (closing-price, single-price, block, basket), the first price of an opening-price-base 시가기준가종목 (*si-ga gi-jun-ga jong-mok*) issue, liquidation issues (정리매매종목), and competitive-block trading.
- **Conditional-limit specifically** is also prohibited for short-term overheat issues (단기과열종목, *dan-gi gwa-yeol jong-mok*), designated-investment-warning issues (투자유의종목), low-liquidity single-price issues, abnormal-rise single-price issues, type-A preferred-share single-price issues, and orders that already carry an IOC/FOK condition under §108.12.a [KRX-RULE-KOSPI-BR-ENFORCE-KO §14.2.1.s, .ja, .pa, .ha]. A conditional-limit submitted at the upper price limit on the buy side, or at the lower price limit on the sell side, is also rejected [KRX-RULE-KOSPI-BR-ENFORCE-KO §14.1.2-3].
- **Best-counterparty (최유리) and best-same-side (최우선) limit** are prohibited in the same situations as market/conditional-limit, with two carve-outs: best-same-side is allowed for market-maker quotes (§14.2.2.a.(1)), and condition-flagged best-same-side is allowed for competitive-block (§14.2.2.a.(2)). Both are prohibited from any single-price-auction receipt window [KRX-RULE-KOSPI-BR-ENFORCE-KO §14.2.2.a-b].
- **Midpoint** is prohibited from single-price auctions, off-hours sessions, opening-price-base first-price determination, liquidation issues, overheat / warning / low-liquidity / preferred-share single-price issues, and from the receipt window of any single-price auction [KRX-RULE-KOSPI-BR-ENFORCE-KO §14.2.4-2.a-b]. It is also prohibited when one side has no non-midpoint quotes during continuous trading [KRX-RULE-KOSPI-BR-ENFORCE-KO §14.2.4-2.la].
- **Stop-limit** has the same restriction set as midpoint (§14.2.4-3) plus the rule that the stop price must be on a tick and inside the daily price-limit band [KRX-RULE-KOSPI-BR-ENFORCE-KO §14.1.2-4].

### Best-limit pricing rules

The two best-limit types deem a price at receipt time. The rules differ for the two sides and for the empty-book case [KRX-RULE-KOSPI-BR-ENFORCE-KO §3-§4]:

| Type           | Side  | Deemed price                                                                                   |
|----------------|-------|-------------------------------------------------------------------------------------------------|
| 최유리지정가    | sell  | Highest existing bid (excluding 중간가 bids). If no bid: lowest ask − 1 tick (floored at 하한가). If neither side has any quote: previous price (rounded down to a tick). |
| 최유리지정가    | buy   | Lowest existing ask (excluding 중간가 asks). If no ask: highest bid + 1 tick (capped at 상한가). If neither side has any quote: previous price (rounded up to a tick). |
| 최우선지정가    | sell  | Lowest existing ask (excluding 중간가 asks). If none: previous price (rounded up to a tick).    |
| 최우선지정가    | buy   | Highest existing bid (excluding 중간가 bids). If none: previous price (rounded down to a tick). |

Once the deemed price is fixed at receipt, the order behaves as a normal limit at that price — its time priority under §22.2.2 is the receipt time, not the time at which the deemed price might have been recomputable.

### Midpoint validity rules

A midpoint quotation is priced at `floor((best_bid + best_ask) / 2)` in KRW (sub-KRW digits truncated, per Enforcement Rule §4-2). The price moves continuously as the two-side best quotes change; it is matched against limits, market orders, or other midpoint orders by standard price-then-time priority [KRX-TOUR-KOSPI-METHOD-T8].

The midpoint quotation is **suspended** in two cases [KRX-RULE-KOSPI-BR-ENFORCE-KO §13.2.2-3]:

- During a single-price auction receipt window: an unfilled midpoint received before the auction window is suspended for the duration of the window and reactivated when continuous trading resumes [KRX-RULE-KOSPI-BR-ENFORCE-KO §13.2.3].
- During continuous trading when one or both sides has no non-midpoint quote: the midpoint is suspended until both sides have at least one non-midpoint quote [KRX-RULE-KOSPI-BR-ENFORCE-KO §13.2.2].

A midpoint quotation that remains unfilled at the moment the closing single-price receipt window opens is considered **invalid** for the closing auction (its effect is not recognized) [KRX-RULE-KOSPI-BR-ENFORCE-KO §13.1.4-2]. It does not auto-convert to anything; it simply does not participate in closing-price determination. Midpoint quotations are also excluded from the 기세 (*gi-se*) special-quotation calculation — see *Special quotations* below.

### Conditional-limit conversion

A 조건부지정가호가 placed during the continuous session behaves identically to a regular limit at the same price until the closing single-price receipt window opens [KRX-TOUR-KOSPI-BASIC-T2]. At that moment (15:20 KST under §35.1.3), any unfilled conditional-limit quantity is **converted into a market quotation** for the closing auction [KRX-RULE-KOSPI-BR-ENFORCE-KO §15.1].

Conversion priority (when many conditional-limits convert at once) is set by §15.1:

1. Price priority — for sells, the **lowest-price** conditional-limit converts first; for buys, the **highest-price** converts first.
2. Time priority — among same-price conditional-limits, the earlier-received converts first.

The converted market quotation is deemed received at the start of the closing-auction receipt window, not at the original conditional-limit receipt time [KRX-RULE-KOSPI-BR-ENFORCE-KO §15.2]. There are two narrow exceptions: when the closing auction is part of a market-resumption-after-halt single-price (§35.1.3 latter clause), the converted-market is deemed received at the resumption moment; and when §35.1.4 proviso applies, the converted-market is deemed received 10 minutes before 장종료 (i.e. at 15:20 KST).

### Stop-limit activation

A stop-limit (스톱지정가호가) carries both a limit price and a stop price (스톱가격). It sits dormant in the system until activation, then takes effect as a regular limit at its limit price [KRX-RULE-KOSPI-BR-KO §2.4.8]. Activation conditions [KRX-RULE-KOSPI-BR-ENFORCE-KO §4-3]:

- **Sell stop:** activates when the last traded price ≤ stop price (or, if no trade has yet occurred today, the base price ≤ stop price).
- **Buy stop:** activates when the last traded price ≥ stop price (similarly with base price as the fallback comparator).

Activation priority — when several stop-limits cross their stops simultaneously [KRX-RULE-KOSPI-BR-ENFORCE-KO §15-2.1]:

1. For sell stops, **higher** stop price activates first; for buy stops, **lower** stop price activates first. (This mirrors the price-priority direction of conventional limit-order matching once activated.)
2. Same-stop ties broken by stop-quotation receipt time, earliest first.

Once activated, the resulting limit's time priority for §22.2.2 (same-price-tie-break) uses **the original stop-limit receipt time** — not the activation moment [KRX-RULE-KOSPI-BR-ENFORCE-KO §15-2.2]. So a stop-limit submitted at 09:30 and activated at 14:00 sits ahead of a regular limit submitted at 13:50 if both share the same limit price.

Stop-price input restrictions [KRX-RULE-KOSPI-BR-ENFORCE-KO §14.1.2-4]:

- The stop price must be inside the daily price-limit band (≤ 상한가 and ≥ 하한가).
- The stop price must be on a valid tick (per §32.2).

### Quotation conditions (IOC, FOK, self-match-prevention)

Beyond the eight quotation types, a member may attach **conditions** to a quotation per §108.12 of the Business Regulation:

- **IOC (즉시체결, 즉시취소; Immediate-Or-Cancel)** — any quantity not matched immediately is cancelled [KRX-RULE-KOSPI-BR-ENFORCE-KO §13.3.1]. IOC is permitted on limit, best-counterparty, best-same-side, and standard market quotations (subject to §14.2's per-situation matrix).
- **FOK (전량체결, 전량취소; Fill-Or-Kill)** — if the entire quantity cannot be matched immediately, the entire quotation is cancelled [KRX-RULE-KOSPI-BR-ENFORCE-KO §13.3.2]. Same eligibility profile as IOC.
- **Self-match-prevention (자전거래방지)** — available only to high-speed algorithmic traders sharing a registered HSA ID (고속알고리즘거래번호) [KRX-RULE-KOSPI-BR-ENFORCE-KO §13-2.1]. When two opposite-side quotations from the same HSA ID would match, the system applies one of three sub-conditions chosen by the member: cancel the older, cancel the newer, or cancel the matchable quantity from each. Active only during continuous trading (§13-2.2) and never during 동시호가 simultaneous-quotation matching at price limits.

When IOC and self-match-prevention are both attached, self-match-prevention runs first [KRX-RULE-KOSPI-BR-ENFORCE-KO §13-2.3].

### Cancellation and correction of quotations

The unfilled portion of a placed quotation may be cancelled or corrected; the filled portion cannot be undone [KRX-RULE-KOSPI-BR-KO §13; KRX-TOUR-KOSPI-BASIC-T3]. Correction rules:

- A correction is permitted only when changing the price or the quotation type (e.g. limit → best-counterparty) [KRX-TOUR-KOSPI-BASIC-T3].
- A correction that intends to change *quantity* — i.e. reduce or increase — or to leave the price unchanged is **not allowed** as a correction; reducing quantity is done by partial cancellation, and increasing quantity requires a new quotation.
- Correction resets the time-priority clock for the corrected quantity to the correction's receipt time [KRX-TOUR-KOSPI-BASIC-T3].
- Partial cancellation does **not** disturb the remaining quantity's original time priority [KRX-TOUR-KOSPI-BASIC-T3].

### Special quotations (특별호가) — closing-price formation when no trade matches

When the regular session ends with no trade matched, the Exchange uses a 기세 (*gi-se*) — the lowest ask priced below the day's base, or the highest bid priced above it — as the day's closing price; this 기세 also becomes the next-day base price [KRX-RULE-KOSPI-BR-KO §2.9; KRX-TOUR-KOSPI-BASIC-T7]. Two carve-outs:

- For preferred shares (종류주식) trading at more than 1.5× the corresponding common-share base price, **bid-side** 기세 is excluded [KRX-RULE-KOSPI-BR-ENFORCE-KO §6-3] — i.e. preferred shares cannot use a one-sided high bid to drag the closing price upward.
- **Midpoint quotations are excluded** from the 기세 calculation entirely [KRX-RULE-KOSPI-BR-KO §2.9].

The English tour [KRX-TOUR-KOSPI-BASIC-T7] uses "Special Quotations" as the term for this mechanism. The rulebook does not use 특별호가 (*teuk-byeol-ho-ga*) as a defined term.

## Parameters & thresholds

### Table 1 — Quotation types at a glance

| #  | Korean              | English label                | Key article                                  | Price source                                            |
|----|---------------------|------------------------------|----------------------------------------------|---------------------------------------------------------|
| 1  | 지정가호가           | Limit                        | [KRX-RULE-KOSPI-BR-KO §2.4.1]                | Member-specified                                        |
| 2  | 시장가호가           | Market                       | [KRX-RULE-KOSPI-BR-KO §2.4.2]                | Deemed via §23.3 / §24.2 (see Auctions)                 |
| 3  | 조건부지정가호가     | Conditional-limit (LMC)      | [KRX-RULE-KOSPI-BR-KO §2.4.3; -ENFORCE §15]  | Limit during continuous; converts to market at 15:20    |
| 4  | 최유리지정가호가     | Best-counterparty limit      | [KRX-RULE-KOSPI-BR-KO §2.4.4; -ENFORCE §3]   | Best opposite-side quote at receipt                     |
| 5  | 최우선지정가호가     | Best-same-side limit         | [KRX-RULE-KOSPI-BR-KO §2.4.5; -ENFORCE §4]   | Best same-side quote at receipt                         |
| 6  | 경쟁대량매매호가     | Competitive block (A-Blox)   | [KRX-RULE-KOSPI-BR-KO §2.4.6]                | VWAP per §30-2.1 / §34-3.1                              |
| 7  | 중간가호가           | Midpoint                     | [KRX-RULE-KOSPI-BR-KO §2.4.7; -ENFORCE §4-2] | `floor((best_bid + best_ask) / 2)` KRW                  |
| 8  | 스톱지정가호가       | Stop-limit                   | [KRX-RULE-KOSPI-BR-KO §2.4.8; -ENFORCE §4-3] | Member-specified limit; activated when stop is crossed  |

### Table 2 — Eligibility by security and session

A `✔` means the type is permitted for that security/session; `✗` means it is not. "Group 1" = shares, foreign DRs, ETF units, ETNs. "Group 2" = subscription rights/warrants, ELWs, beneficiary certs (excl. ETF investment-trust units), debt securities. Source: [KRX-RULE-KOSPI-BR-ENFORCE-KO §10.1, §14.2].

| Type          | Group 1 — continuous | Group 1 — single-price auction | Group 1 — off-hours | Group 2 (any session) |
|---------------|:--------------------:|:------------------------------:|:-------------------:|:---------------------:|
| Limit         |          ✔           |               ✔                |          ✔          |           ✔           |
| Market        |          ✔           |               ✔                |          ✗          |           ✗           |
| Conditional   |          ✔           |        n/a (auto-converts)     |          ✗          |           ✗           |
| Best-counter  |          ✔           |               ✗                |          ✗          |           ✗           |
| Best-same     |          ✔           |               ✗                |          ✗          |           ✗           |
| Competitive   |    ✗ (separate book) |               ✗                |          ✗          |           ✗           |
| Midpoint      |          ✔           |               ✗                |          ✗          |           ✗           |
| Stop-limit    |          ✔           |               ✗                |          ✗          |           ✗           |

Notes: "Off-hours" covers off-hours closing-price, off-hours single-price, off-hours block, and off-hours basket. The competitive-block (A-Blox) book is a separate auction track — see [Auctions (KOSPI) §A-Blox](./auctions.md#a-blox-auction-based-block-trade). Issue-level restrictions (liquidation issues, overheat issues, etc.) further narrow the matrix; see §14.2 for the full list.

### Table 3 — Quotation conditions

| Condition                  | Effect                                                                       | Source                                            |
|----------------------------|------------------------------------------------------------------------------|---------------------------------------------------|
| IOC                        | Cancel any unmatched portion immediately                                     | [KRX-RULE-KOSPI-BR-ENFORCE-KO §13.3.1]            |
| FOK                        | Cancel all if any portion cannot be matched immediately                      | [KRX-RULE-KOSPI-BR-ENFORCE-KO §13.3.2]            |
| Self-match-prevention      | HSA-only; cancel one or both sides on same-HSA-ID match (3 sub-modes)        | [KRX-RULE-KOSPI-BR-ENFORCE-KO §13-2]              |

IOC and FOK may be attached to limit, best-counterparty, best-same-side, and (subject to §14) market quotations; they may not be attached to conditional-limit, midpoint, stop-limit, or competitive-block quotations [KRX-RULE-KOSPI-BR-ENFORCE-KO §14.2.1.ha, §14.2.4-2, §14.2.4-3].

## Worked examples

### Example A — best-counterparty limit on a non-empty book

Order book at the moment a buy 최유리지정가 for 100 shares is received:

| Asks |  Price |  Bids |
|-----:|-------:|------:|
|  500 | 10,400 |       |
|  300 | 10,300 |       |
|      | 10,250 |  200  |
|      | 10,200 |  400  |

Per Enforcement Rule §3.2, the deemed price for a buy 최유리지정가 is the **lowest ask** at receipt = KRW 10,300. The order behaves from this point on as a regular limit at 10,300, with receipt time = the original 최유리지정가 receipt time. It will match against the 300-share ask at 10,300 immediately (price overlap, leading-order price = 10,300 per §24.3 — see [Auctions](./auctions.md)).

Contrast: a buy 최우선지정가 in the same book would be deemed at the **highest bid** = KRW 10,250 (per §4.2). It would not match anything; it would sit on top of the bid stack at 10,250.

### Example B — conditional-limit (LMC) conversion at the closing call

Buy conditional-limits resting on the book at 15:19:59 KST [KRX-RULE-KOSPI-BR-ENFORCE-KO §15.1]:

| Order  | Receipt time | Limit price (KRW) | Quantity |
|--------|--------------|------------------:|---------:|
| ①      | 09:01        |             9,800 |      500 |
| ②      | 09:05        |            10,000 |      200 |
| ③      | 13:30        |            10,000 |      300 |
| ④      | 14:50        |             9,950 |      400 |

At 15:20 KST the closing-call receipt window opens. All four conditional-limits convert to buy market quotations. Conversion priority — for buys, **higher price first**, ties broken by earlier receipt:

1. Order ② (10,000 / 09:05) — converted first.
2. Order ③ (10,000 / 13:30).
3. Order ④ (9,950 / 14:50).
4. Order ① (9,800 / 09:01).

All four converted-market quotations are deemed received at 15:20:00.000 — the original receipt times do not carry over [KRX-RULE-KOSPI-BR-ENFORCE-KO §15.2]. They participate in the closing single-price auction as buy market orders (deemed-priced per §23.3). Note: the relative ordering (②, ③, ④, ①) is what matters when several converted-market quotations sit at the same deemed price during single-price matching.

### Example C — sell stop-limit activation and post-activation priority

Two stop-limits resting on the book:

| Order  | Stop receipt | Stop price (KRW) | Limit price (KRW) | Quantity |
|--------|--------------|-----------------:|------------------:|---------:|
| Sₐ     | 10:00        |           10,200 |            10,150 |      100 |
| Sᵦ     | 11:30        |           10,250 |            10,200 |      200 |

Last traded price reaches KRW 10,250 at 13:00. Both sells satisfy "last_price ≤ stop" simultaneously [KRX-RULE-KOSPI-BR-ENFORCE-KO §4-3.1]. Activation priority [KRX-RULE-KOSPI-BR-ENFORCE-KO §15-2.1]: sell stops with **higher stop price activate first** → Sᵦ activates first (stop 10,250 > 10,200), Sₐ activates second.

After activation, both behave as regular sell limits. A separate regular sell limit Lᵧ at 10,200 was submitted at 12:00 (between the two stop receipts but before activation). Same-price tie-breaking at price 10,200 under §22.2.2 uses the **original stop-quotation receipt time** [KRX-RULE-KOSPI-BR-ENFORCE-KO §15-2.2]: Sᵦ at 10,200 has receipt time 11:30 — earlier than Lᵧ's 12:00 — so Sᵦ outranks Lᵧ in time priority despite Lᵧ being on the book first. This is the design choice that makes stop-limits valuable to algorithmic strategies: pre-staging cost is converted into time priority.

## Edge cases & open questions

- Edge case: §10.1 fixes eligibility by security category — but ETF investment-company shares (ETF 투자회사 주권) are explicitly excluded from "shares" in the §10.1.1 enumeration and are not separately listed. Their eligibility is not directly resolved by §10.1 and may default to limit-only via the §10.1.2 catch-all for "other beneficiary certificates." Verify the reading against ETF-specific provisions in the Listing Regulation before relying on this.
- Edge case: A conditional-limit submitted at the upper price limit (buy) or lower price limit (sell) is rejected at input per §14.1.2-3, **before** the conversion logic of §15 ever runs. Members targeting the closing call with a marketable conditional therefore have no way to express "convert me only if I am still alive at 15:20"; they have to choose at submission time whether to risk the price-limit-rejection.
- Edge case: §15-2.2 retains the original stop-limit receipt time for §22.2.2 priority **after** activation. This means a stop-limit submitted at the open and activated late in the session can outrank an entire day's regular limits at the same price. Algorithmic strategies that compute time-priority-based fill probabilities should treat unactivated stop-limits as priority-bearing inventory, not as latent.
- Edge case: A midpoint quotation that is suspended at the moment of the closing-call receipt-window open (§13.1.4-2) is treated as expired for the closing auction — but the rule text says "그 효력을 인정하지 아니한다" (its effect is not recognized), not "취소" (cancelled). Whether the unfilled quantity is returned to the member's order-management system as cancelled or simply expired-without-cancel is implementation-dependent and not specified by the rulebook.
- Open question: §13-2 self-match-prevention is restricted to **high-speed algorithmic** traders (고속알고리즘거래자) — i.e. those registered under §104-3. Whether non-HSA algorithmic traders or non-algorithmic members can achieve the same effect via cancel-then-replace is left unaddressed; the only rule-level prevention is the §13-2 condition. Cross-check against the FSC's market-misconduct guidance before designing internal SMP logic.
- Open question: Conditional-limit conversion priority (§15.1) uses **price** as the first sort key, with the unstated implication that the conditional's *limit* price (not its converted-market deemed price) is the sort key. The rule text is consistent with this reading but does not spell it out. For the closing call in Example B above, all four orders convert to market regardless of their original limit; the priority sort still uses the original limits.
- Unsourced claim: [KRX-TOUR-KOSPI-BASIC-T2] mentions a "Limit-to-Market-on-Close" English label and a 15:20 conversion time; the BR/ER text does not name this explicitly — the 15:20 anchor follows from §35.1.3's 10-minute closing-call receipt window. Treat the English label as overview color.

## Sources

- `KRX-RULE-KOSPI-BR-KO` — KOSPI Market Business Regulation (유가증권시장 업무규정, *yu-ga-jeung-gwon si-jang eom-mu gyu-jeong*), bookid 210200859, effective 2026-04-28. Articles cited: §2 (Definitions — including the 8 quotation types and 9 order types, 동시호가, 시가, 종가, 기세), §9 (Quotation method — delegates to Enforcement Rule), §10 (Receipt time), §12 (Quotation effect — delegates conditional-limit conversion and stop-limit priority to Enforcement Rule), §13 (Cancel and correct), §22 (Priority — referenced for time-priority interaction with stop-limits), §108 (Quotation conditions including IOC, FOK, self-match-prevention — referenced).
- `KRX-RULE-KOSPI-BR-ENFORCE-KO` — KOSPI BR Enforcement Rule (유가증권시장 업무규정 시행세칙, *yu-ga-jeung-gwon si-jang eom-mu gyu-jeong si-haeng se-chik*), bookid 210203562, effective 2026-04-28. Articles cited: §3 (최유리지정가 deemed price), §4 (최우선지정가 deemed price), §4-2 (중간가 deemed price; new 2025-02-27), §4-3 (스톱지정가 activation conditions; new 2025-02-27), §10 (Eligibility by security category), §13 (Quotation effect — invalid quotations, suspension cases, IOC/FOK), §13-2 (Self-match-prevention), §14 (Input restrictions, including stop-price tick check, conditional-limit at price-limit prohibition, and the full per-type × per-situation matrix in §14.2), §15 (Conditional-limit conversion to market), §15-2 (Stop-limit activation priority and time-priority retention; new 2025-02-27), §6-3 (기세-exclusion threshold for type-A preferred shares).
- `KRX-TOUR-KOSPI-BASIC-T2` — KRX overview "Limit Orders / Order types"; English, not authoritative. Used for English labels of the 8 quotation types plus 목표가주문, the descriptive language for stop-limit and midpoint, and the LMC = "Limit-to-Market-on-Close" framing (English label flagged as overview color).
- `KRX-TOUR-KOSPI-BASIC-T3` — KRX overview "What is a quotation?"; English, not authoritative. Used for the cancellation-and-correction rules (correction-resets-time-priority; partial-cancel-preserves-time-priority).
- `KRX-TOUR-KOSPI-BASIC-T7` — KRX overview "Special Quotations"; English, not authoritative. Used for the 기세 carve-outs (preferred-share excluded bids; midpoint excluded entirely) — these are spelled out in §6-3 of the Enforcement Rule but the tour gives the cleaner narrative.
- `KRX-TOUR-KOSPI-METHOD-T5` — KRX overview "Execution Method of Market Order at Continuous Trading"; English, not authoritative. Used as a cross-reference for the §24.2 deemed-price formulas; the worked examples in T5 are reproduced in [Auctions (KOSPI)](./auctions.md).
- `KRX-TOUR-KOSPI-METHOD-T8` — KRX overview "Midpoint Order Matching Method"; English, not authoritative. Used for the descriptive language around midpoint matching (continuous-only; matched against limits, market, and other midpoints; price-then-time priority).
