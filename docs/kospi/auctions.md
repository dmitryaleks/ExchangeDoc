---
title: "Auctions (KOSPI)"
markets: [KOSPI]
last_reviewed: 2026-04-30
sources:
  - KRX-RULE-KOSPI-BR-KO
  - KRX-RULE-KOSPI-BR-ENFORCE-KO
  - KRX-TOUR-KOSPI-METHOD-T1
  - KRX-TOUR-KOSPI-METHOD-T2
  - KRX-TOUR-KOSPI-METHOD-T4
  - KRX-TOUR-KOSPI-EXCEPT-T4
---

> See also: [Auctions (KOSDAQ)](../kosdaq/auctions.md), [Market Hours (KOSPI)](./market_hours.md), [Comparison](../common/comparison.md).

## Summary

- KOSPI uses two auction modes: a single-price call auction (단일가격에 의한 개별경쟁매매, *dan-il-ga-gyeok-e ui-han gae-byeol gyeong-jaeng mae-mae*) and a continuous double auction (복수가격에 의한 개별경쟁매매, *bok-su-ga-gyeok-e ui-han gae-byeol gyeong-jaeng mae-mae*) [KRX-RULE-KOSPI-BR-KO §22.1].
- Five events trigger a single-price auction: opening, closing, market-resumption-after-halt, post-method-change first price, and post-VI/CB resumption price [KRX-RULE-KOSPI-BR-KO §23.1].
- Every single-price auction closes at a randomly-determined moment within 30 seconds after the nominal close, to deter last-millisecond manipulation [KRX-RULE-KOSPI-BR-ENFORCE-KO §35.1].
- Order priority is price > time, with one exception: when the auction price is determined at the daily upper or lower price limit, orders at that limit are deemed simultaneous (동시호가, *dong-si-ho-ga*) and matched by quantity-priority instead of time-priority [KRX-RULE-KOSPI-BR-KO §22.2–22.3; KRX-RULE-KOSPI-BR-ENFORCE-KO §34].
- Auction-based block trading (A-Blox) is a separate, anonymous, VWAP-priced auction track for orders ≥ KRW 500,000,000 [KRX-TOUR-KOSPI-EXCEPT-T4].

## Detailed rules

### Two auction modes

The KOSPI Stock Market matches trades by individual competitive auction (개별경쟁매매, *gae-byeol gyeong-jaeng mae-mae*), of which there are two variants [KRX-RULE-KOSPI-BR-KO §22.1]:

- **Single-price auction** (단일가매매, *dan-il-ga mae-mae*) — orders accumulate during a window and clear in a single batch at a single equilibrium price.
- **Continuous auction** (복수가매매, *bok-su-ga mae-mae*) — orders match one-by-one as they arrive, at the price set by the earlier-entered order.

Each is governed by a dedicated article in the Business Regulation: §23 for single-price, §24 for continuous.

### When single-price auctions run

A single-price auction is used to determine each of the following prices [KRX-RULE-KOSPI-BR-KO §23.1]:

1. The opening price (시가, *si-ga*) of the regular session.
2. The first price after a market-wide trading resumption per §6.2 (e.g. after a system-failure restart).
3. The first price after trading is resumed for an individual issue per §25.1, §26.4, §107.4, the Listing Regulation §153.2, or the Disclosure Regulation §40.5 (i.e. after a halt — including circuit-breaker, VI, and disclosure-driven halts).
4. The closing price (종가, *jong-ga*) — i.e. the closing call auction at the end of the regular session.
5. The first price after the trade-execution method has been changed for an issue under §26-2.1 (e.g. when an issue is moved into single-price-only mode for liquidity reasons).

Outside those five events, the regular session runs in continuous mode [KRX-RULE-KOSPI-BR-KO §24.1].

The first trade on a newly-listed issue's listing day is also a single-price auction [KRX-RULE-KOSPI-BR-KO §37.1; -ENFORCE-KO §67-2].

### Single-price matching algorithm

For each single-price auction event, the Exchange determines a clearing price called the matching price (합치가격, *hap-chi-ga-gyeok*) — the price at which the cumulative ask quantity equals the cumulative bid quantity [KRX-RULE-KOSPI-BR-KO §23.4]. At that price:

1. All asks priced strictly below the matching price and all bids priced strictly above it are filled in full [KRX-RULE-KOSPI-BR-KO §23.4.1].
2. At the matching price itself, one side fills entirely; the other side fills to the extent of the matching quantity, in priority order per §22 [KRX-RULE-KOSPI-BR-KO §23.4.2].

If multiple matching prices exist [KRX-RULE-KOSPI-BR-KO §23.5]:

1. If one of the matching prices equals the previous price (직전의 가격, *jik-jeon-ui ga-gyeok*; including the indicative price 기세 (*gi-se*) when no trade has occurred yet), that price wins.
2. Otherwise, by closeness to the previous price, with sub-rules for whether the previous price is above the highest matching price, below the lowest, or in between (rules added in the 2025-02-05 amendment).

Market orders entering a single-price auction are deemed at one of several derived prices, depending on whether limit orders are present and on which side has greater volume [KRX-RULE-KOSPI-BR-KO §23.3]:

- **Market orders only on both sides:** deemed price = previous price (or rounded to the nearest tick), shifted ±1 tick toward the larger side if quantities differ, capped at the daily upper/lower price limit.
- **Mixed market and limit orders:** sell market is deemed at the lowest of (lowest ask limit – 1 tick, lowest bid limit, previous price). Buy market is deemed at the highest of (highest bid limit + 1 tick, highest ask limit, previous price).

Worked examples for the mixed case are in *Worked examples* below.

### Random-end mechanism

The window of orders participating in a single-price auction is not closed at the nominal end time. The Enforcement Rule sets [KRX-RULE-KOSPI-BR-ENFORCE-KO §35.1]:

> The range of orders participating in single-price competitive auction is: orders received during the time periods set in each of the following items, **and orders received during a time randomly determined by the Exchange within 30 seconds following the nominal end**, including any earlier-received unfilled orders.

The random extension applies to:

- The opening single-price auction — extension applied after 장개시 (*jang-gae-si*; nominal session-open time, 09:00 KST) [KRX-RULE-KOSPI-BR-ENFORCE-KO §35.1.1; KRX-RULE-KOSPI-BR-KO §10.1].
- The closing single-price auction — extension applied after 장종료 (*jang-jong-ryo*; nominal session-close time, 15:30 KST) [KRX-RULE-KOSPI-BR-ENFORCE-KO §35.1].
- The first-price auction for newly-listed issues — extension applied after 장개시 [KRX-RULE-KOSPI-BR-ENFORCE-KO §67-2].
- Resumption-after-halt single-price auctions, including the unit-matching point (단위매매체결시점, *dan-wi mae-mae che-gyeol si-jeom*) — see the Enforcement Rule's halt-specific articles [KRX-RULE-KOSPI-BR-ENFORCE-KO §35.1].

Practical effect: a participant cannot know the exact instant at which orders are no longer accepted into the auction window. The orders received during the random extension are pooled with orders received before the nominal end and matched in a single price-determination event [KRX-TOUR-KOSPI-METHOD-T1].

### Order priority and same-price tie-breaking

The default priority is two-level [KRX-RULE-KOSPI-BR-KO §22.2]:

1. **Price priority.** Lower asks outrank higher asks; higher bids outrank lower bids. Market orders outrank limit orders pricewise — except that a sell market order and a sell limit at the lower price limit are deemed equal, and a buy market order and a buy limit at the upper price limit are deemed equal [KRX-RULE-KOSPI-BR-KO §22.2.1].
2. **Time priority.** Among orders at the same price (and among market orders), the earlier-received order outranks the later-received one [KRX-RULE-KOSPI-BR-KO §22.2.2].

There is one important override: when a single-price auction (only opening, market-resumption, or halt-resumption — i.e. items 1–3 of §23.1) determines a price *at the daily upper or lower price limit*, orders at that limit are deemed simultaneous (동시호가) and time priority is suspended [KRX-RULE-KOSPI-BR-KO §22.3]. The same-price priority among simultaneous orders is set by the Enforcement Rule §34, which uses **quantity-priority** with a three-step allocation: see *Quantity allocation at price limits* below.

### Quantity allocation at price limits

When the auction price is set at the upper price limit, allocation among buy orders at the upper limit follows the quantity-priority rule from KRX-RULE-KOSPI-BR-ENFORCE-KO §34 (mirrored for sell orders at the lower limit) [KRX-TOUR-KOSPI-METHOD-T2]. Allocation proceeds in the following passes, in order, sequencing from largest order quantity to smallest within each pass:

1. **First pass** — to each eligible order: up to **100 × the trading lot** (매매수량단위, *mae-mae su-ryang dan-wi*).
2. **Second pass** — to each eligible order: **half** of the order's remaining unfilled balance (rounded to the nearest integer of the trading lot).
3. **Third pass** — the residue, allocated by the same priority sequence until the matched quantity is exhausted.

A worked example of this three-pass allocation is in *Worked examples* below.

### Continuous trading

Outside the single-price events of §23.1, the regular session matches in continuous mode [KRX-RULE-KOSPI-BR-KO §24.1]. The matching condition is a price overlap — the lowest ask is at or below the highest bid — at which point the trade prints at the price of the earlier-entered order (선행호가, *seon-haeng-ho-ga*; "leading quote") and is matched in priority order per §22.2 [KRX-RULE-KOSPI-BR-KO §24.3].

Market orders in continuous mode are deemed-priced per §24.2: a sell market trades at the lower of (lowest ask – 1 tick if no other ask exists; otherwise lowest bid limit). A buy market trades at the symmetric maximum.

### A-Blox — Auction-based Block Trade

A separate auction track exists for anonymous block trading. A-Blox (introduced 2010-11-29) accepts large orders that match continuously by time priority but settle at a session-VWAP price computed after the close [KRX-TOUR-KOSPI-EXCEPT-T4]. Key parameters are in *Parameters & thresholds*.

A-Blox order books are not published during the session — only an indicator of whether a buy or sell exists per security is disclosed [KRX-TOUR-KOSPI-EXCEPT-T4].

## Parameters & thresholds

### Auction events

| Auction event                                      | Mode          | Random extension                  | Source                                          |
|----------------------------------------------------|---------------|-----------------------------------|-------------------------------------------------|
| Opening price (시가)                               | single-price  | yes — up to 30 s after 09:00      | [KRX-RULE-KOSPI-BR-KO §23.1.1; -ENFORCE-KO §35.1] |
| Closing price (종가)                               | single-price  | yes — up to 30 s after 15:30      | [KRX-RULE-KOSPI-BR-KO §23.1.4; -ENFORCE-KO §35.1] |
| First price after market resumption                | single-price  | yes — up to 30 s after restart    | [KRX-RULE-KOSPI-BR-KO §23.1.2; -ENFORCE-KO §35.1] |
| First price after individual-issue resumption      | single-price  | yes — up to 30 s after restart    | [KRX-RULE-KOSPI-BR-KO §23.1.3; -ENFORCE-KO §35.1] |
| First price after trade-method change              | single-price  | yes — up to 30 s after switch     | [KRX-RULE-KOSPI-BR-KO §23.1.5; -ENFORCE-KO §35.1] |
| First price for newly-listed issue                 | single-price  | yes — up to 30 s after 09:00      | [KRX-RULE-KOSPI-BR-KO §37; -ENFORCE-KO §67-2]   |
| Continuous regular-session trading                 | multi-price   | n/a                               | [KRX-RULE-KOSPI-BR-KO §24]                      |

### A-Blox parameters

| Parameter                        | Value                                                            | Source                       |
|----------------------------------|------------------------------------------------------------------|------------------------------|
| Eligible securities              | Common stock, ETF, ETN, KDR (admin / liquidation issues excluded) | [KRX-TOUR-KOSPI-EXCEPT-T4]   |
| Pre-open trading window          | 08:00–09:00 KST                                                   | [KRX-TOUR-KOSPI-EXCEPT-T4]   |
| Regular-session trading window   | 09:00–15:00 KST                                                   | [KRX-TOUR-KOSPI-EXCEPT-T4]   |
| Matching method                  | Continuous, by time priority                                       | [KRX-TOUR-KOSPI-EXCEPT-T4]   |
| Execution price (off-hours)      | Session VWAP for the day                                          | [KRX-TOUR-KOSPI-EXCEPT-T4]   |
| Execution price (regular)        | VWAP from match time to session close                             | [KRX-TOUR-KOSPI-EXCEPT-T4]   |
| Execution price (no day-trade)   | Closing price (or base price if closing price unavailable)        | [KRX-TOUR-KOSPI-EXCEPT-T4]   |
| Minimum order size               | KRW 500,000,000 (base price × quotation quantity)                | [KRX-TOUR-KOSPI-EXCEPT-T4]   |
| Trading unit                     | 100 shares                                                        | [KRX-TOUR-KOSPI-EXCEPT-T4]   |
| Pre-close information disclosed  | Bid/ask presence indicator only                                    | [KRX-TOUR-KOSPI-EXCEPT-T4]   |

## Worked examples

### Example A — single-price auction with limit orders

(Tick size assumed KRW 50 for clarity. Adapted from [KRX-TOUR-KOSPI-METHOD-T1].)

| Sell qty | Price (KRW) | Buy qty   |
|---------:|------------:|----------:|
|    1,000 |      15,400 |           |
|      300 |      15,350 |           |
|      200 |      15,300 |     2,000 |
|      500 |      15,250 |     1,000 |
|      150 |      15,200 |       500 |
|          |      15,150 |       500 |
|          |      15,100 |       150 |

The matching algorithm finds the price where cumulative ask qty equals cumulative bid qty. At KRW 15,250 the cumulative ask is 1,000 + 300 + 200 + 500 = 2,000 and the cumulative bid is 2,000 + 1,000 = 3,000 (cumulating bids from highest down to the price). The matching price is KRW 15,250 [KRX-RULE-KOSPI-BR-KO §23.4]. At that price, time priority breaks ties for the buy side at 15,250 — the earlier 1,000-share order fills before the same-price later orders [KRX-RULE-KOSPI-BR-KO §22.2.2; KRX-TOUR-KOSPI-METHOD-T1].

### Example B — quantity allocation at the upper price limit

The opening price is determined at the upper limit of KRW 20,150. Buy orders at the upper limit are queued in the receipt order shown below; total buy qty at the limit is 16,200, against matchable sell qty of 13,100 [KRX-TOUR-KOSPI-METHOD-T2]. The trading lot is 1 share, so the "100 × trading lot" pass is 100 shares per order.

| Buy order | Receipt # | Quantity |
|-----------|----------:|---------:|
| Order ①   | 1         |    1,000 |
| Order ②   | 2         |      200 |
| Order ③   | 3         |   10,000 |
| Order ④   | 4         |    5,000 |

Allocation runs the three passes from largest order to smallest [KRX-RULE-KOSPI-BR-ENFORCE-KO §34]:

| Pass                      | Order ③ (10,000) | Order ④ (5,000) | Order ① (1,000) | Order ② (200) |
|---------------------------|----------------:|----------------:|----------------:|--------------:|
| 1. 100 × trading lot       | 100             | 100             | 100             | 100           |
| 2. Half of remaining       | 4,950           | 2,450           | 450             | 50            |
| 3. Residue (4,800 total)   | …               | …               | …               | …             |
| **Allocated total**        | 9,850           | 2,550           | 550             | 150           |

Order ③ receives the largest fill because it had the largest residual after the half-and-half passes, with the residue (4,800 shares) flowing to it under the same priority sequence [KRX-TOUR-KOSPI-METHOD-T2].

### Example C — market order in single-price auction with limits

(Tick size assumed KRW 100. Adapted from [KRX-TOUR-KOSPI-METHOD-T4] Example 1.)

A bid market order for 200 shares enters an auction with the following limit-order book:

| Asks |  Price |  Bids |
|-----:|-------:|------:|
|      | 10,800 |       |
|      | 10,700 |       |
|  200 | 10,600 |       |
|  200 | 10,500 |   200 |
|      | 10,400 |   200 |
|      | 10,300 | (last) |

The buy market is deemed at the highest of [KRX-RULE-KOSPI-BR-KO §23.3.3]:

- Highest bid limit + 1 tick: 10,500 + 100 = **10,600**.
- Highest ask limit: **10,600**.
- Previous price: **10,300** (last traded).

The deemed price is KRW 10,600. Cross with the available asks: 200 fills at 10,500 (the highest matchable counterparty) per the priority logic in §22.2 — note the deemed price is used to *participate*, not necessarily to *fill*; the actual print is at the matched counterparty's price [KRX-TOUR-KOSPI-METHOD-T4].

## Edge cases & open questions

- Edge case: §22.3's deemed-simultaneous (동시호가) override applies only to single-price events of §23.1 items 1–3 (opening, market-resumption, individual-resumption). The closing call auction (§23.1.4) is *not* listed in §22.3 — implying time-priority continues to apply at the closing limit price. Verify this interpretation against §35 receipt-window rules and §67/§68 (동시호가의 우선순위).
- Edge case: The Enforcement Rule's random-end window is up to 30 seconds, but §35.1 says "during a time *randomly determined* within 30 s" — i.e. zero seconds is allowed. There is no documented lower bound; in practice the extension is uniformly distributed but this is implementation-dependent.
- Open question: The market-orders-only deemed-price rule in §23.3.1 references "the previous price". For an opening single-price auction immediately after a market-wide reopen (§23.1.2), what is "the previous price" — the close of the prior trading day, the price at the moment of halt, or something else? Likely the prior close, but verify against §36 (단일가격 결정시 기준이 되는 가격).
- Open question: A-Blox parameters (KRW 500,000,000 minimum, 100-share lot, eligible-security list) are sourced from the English overview tour [KRX-TOUR-KOSPI-EXCEPT-T4]. The corresponding rulebook articles are §31 (장중대량매매, *jang-jung dae-ryang mae-mae*; intraday block trading) and adjacent — not yet read. Numeric thresholds in this section should be re-verified against the Korean text before v1.0.
- Edge case: The 2025-02-05 amendments to §23.5 split the "multiple matching prices" tie-break into three sub-cases by previous-price location relative to the matching range. Worth a worked example before v1.0; not produced here.
- Unsourced claim: KRX-TOUR-KOSPI-METHOD-T1 states the same-price priority shifted from simultaneous to time-priority "since September 2001". The rulebook does not preserve the historical change date. Treat the date as overview-tour color, not authoritative for any decision that turns on the timeline.

## Sources

- `KRX-RULE-KOSPI-BR-KO` — KOSPI Market Business Regulation (유가증권시장 업무규정, *yu-ga-jeung-gwon si-jang eom-mu gyu-jeong*), bookid 210200859, effective 2026-04-28. Articles cited: §22 (Principle of Competitive Auction), §23 (Single-Price Auction), §24 (Continuous Auction), §37 (First Price for Newly Listed Issues), §10 / §6.2 / §25.1 / §26.4 / §107.4 (referenced from §23.1).
- `KRX-RULE-KOSPI-BR-ENFORCE-KO` — KOSPI BR Enforcement Rule (유가증권시장 업무규정 시행세칙, *yu-ga-jeung-gwon si-jang eom-mu gyu-jeong si-haeng se-chik*), bookid 210203562, effective 2026-04-28. Articles cited: §34 (Same-Price Priority for 동시호가), §35 (Range of Single-Price-Auction Participating Orders — random-end mechanism), §36 (Reference price for single-price determination, referenced), §67-2 (Single-Price Auction for newly-listed first price).
- `KRX-TOUR-KOSPI-METHOD-T1` — KRX overview "Method of trading for periodic call auction"; English, not authoritative. Used for the random-end summary, the matching-priority worked example, and the September 2001 historical note (flagged as overview color).
- `KRX-TOUR-KOSPI-METHOD-T2` — KRX overview "Quantity allocation for periodic call auction at upper/lower price limit"; English, not authoritative. Used for the three-pass quantity-allocation worked example (Example B).
- `KRX-TOUR-KOSPI-METHOD-T4` — KRX overview "Execution Method of Market Orders at Single Price Auctions"; English, not authoritative. Used for the deemed-price worked example (Example C).
- `KRX-TOUR-KOSPI-EXCEPT-T4` — KRX overview "Auction-based Block Trade (A-Blox)"; English, not authoritative. Sole source for the A-Blox parameter table; numeric thresholds flagged for re-verification.
