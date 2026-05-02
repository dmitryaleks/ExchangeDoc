---
title: "Volatility Interruption (KOSPI)"
markets: [KOSPI]
last_reviewed: 2026-04-30
sources:
  - KRX-RULE-KOSPI-BR-KO
  - KRX-RULE-KOSPI-BR-ENFORCE-KO
  - KRX-TOUR-KOSPI-OPS-T9
  - KRX-TOUR-KOSPI-OPS-T8
---

> See also: [Volatility Interruption (KOSDAQ)](../kosdaq/volatility_interruption.md), [Circuit Breakers (KOSPI)](./circuit_breakers.md), [Auctions (KOSPI)](./auctions.md), [Trading Rules (KOSPI)](./trading_rules.md), [Comparison](../common/comparison.md).

## Summary

- KRX implements two volatility-interruption (변동성완화장치, *byeon-dong-seong wan-hwa jang-chi*; commonly **VI**) mechanisms — Dynamic VI (동적VI) and Static VI (정적VI) — both via the per-issue trade-execution-method change rule [KRX-RULE-KOSPI-BR-KO §26-2; KRX-RULE-KOSPI-BR-ENFORCE-KO §41-2; KRX-TOUR-KOSPI-OPS-T9].
- **Dynamic VI** triggers when the *tentative* match price moves by ≥ a per-security rate from the **immediately preceding price** (last trade, or base price before the opening print) [KRX-RULE-KOSPI-BR-KO §26-2.1.1]. **Static VI** triggers when it moves by ≥ 10 % from the **last single-price-determined price** (i.e. the prior call-auction print, or the day's base price before the opening single-price clears) [KRX-RULE-KOSPI-BR-KO §26-2.1.2; KRX-RULE-KOSPI-BR-ENFORCE-KO §41-2.2].
- Dynamic VI rates are **3 % for KOSPI 200 constituents** and **6 % for other shares** during continuous trading; the closing-call receipt window applies a reduced **2 % / 4 %**; on equity-derivatives expiry days the closing-call rate for the underlying is further reduced to **1 %** [KRX-RULE-KOSPI-BR-ENFORCE-KO §41-2.1, proviso].
- When a VI fires, the matching method is switched to a 2-minute single-price call auction, after which trading resumes — continuous reverts to continuous, single-price extends its participation window [KRX-RULE-KOSPI-BR-ENFORCE-KO §41-2.3; KRX-TOUR-KOSPI-OPS-T9]. Standard §22 price-then-time priority applies during the resumption auction.
- VI does **not** apply to liquidation issues, short-term-overheat issues, abnormal-rise single-price issues, designated-investment-warning issues, low-liquidity / preferred-share single-price issues, or newly-listed shares/DRs on listing day (since 2021-10-18) [KRX-RULE-KOSPI-BR-ENFORCE-KO §41-2.4; KRX-TOUR-KOSPI-OPS-T9]. A circuit-breaker cancels any in-flight VI; one VI in progress blocks another from triggering on the same issue [KRX-TOUR-KOSPI-OPS-T9].

## Detailed rules

### Mechanism — per-issue trade-execution-method change

VI is implemented through Article 26-2 of the Business Regulation, the per-issue trade-execution-method change rule [KRX-RULE-KOSPI-BR-KO §26-2.1]. When a quotation's tentative match price (잠정적인 체결가격, *jam-jeong-jeok-in che-gyeol-ga-gyeok*) crosses one of the rate thresholds set by Enforcement Rule §41-2, KRX **changes the matching method to a single-price call auction (단일가매매)** under §23 — or, if the issue is already in single-price mode, **extends the participation window** for that auction [KRX-RULE-KOSPI-BR-KO §26-2.1; KRX-RULE-KOSPI-BR-ENFORCE-KO §41-2.3].

The two thresholds — Dynamic VI and Static VI — sit on different reference prices:

- **Dynamic VI** (BR §26-2.1.1) — measured from "the price at the receipt time of the quotation, the immediately preceding price (직전의 가격)." This is the last trade print, or the day's base price before the opening trade prints. Suited to spotting **short-burst** moves driven by supply-demand imbalance or fat-finger orders [KRX-TOUR-KOSPI-OPS-T9].
- **Static VI** (BR §26-2.1.2) — measured from "the immediately preceding single-price-determined price." That is the most recent single-price call auction's clearing price (e.g. the opening print, the previous VI-resumption print) — or, before the opening print, the day's base price [KRX-RULE-KOSPI-BR-KO §26-2.1.2; KRX-TOUR-KOSPI-OPS-T9]. Suited to spotting **cumulative** drift across many small trades during continuous mode.

Both VIs are evaluated continuously against incoming quotations. There is no daily cap on VI events per issue [KRX-TOUR-KOSPI-OPS-T9].

### Dynamic VI — rates and applied sessions

Dynamic VI rates are set by category in [KRX-RULE-KOSPI-BR-ENFORCE-KO §41-2.1]:

- **Shares (주권)** [§41-2.1.1]:
  - KOSPI 200 constituents: 3 %.
  - All other shares: 6 %.
- **ETF and ETN units** [§41-2.1.2]:
  - 1× linked (or inversely linked, |k| ≤ 1) to KOSPI 200, KOSPI 100, KOSPI 50, KRX 100, debt-only indices, or similar indices, **and** Capital Markets Act §4-52.1 securities and their derivatives: 3 %.
  - Other indices, leveraged products with |k| > 1, sector / foreign / commodity indices: 6 %.
- **Foreign DRs and beneficiary certificates** [§41-2.1.3]: 6 %.

The 3 % / 6 % rates apply during the **continuous** session and the **off-hours single-price** session. During the **closing single-price receipt window** (15:20–15:30 KST) the rates are reduced to **2 % / 4 %** [§41-2.1 proviso]. On the **last trading day of equity-related derivatives products** (per Derivatives Market Business Regulation §3.2.1), for the underlying assets (or KOSPI 200 / KOSDAQ 150 / sector-index constituents and single-stock-derivative underlyings), the closing-call rate is further reduced to **1 %** [§41-2.1 proviso]. The derivatives-expiry tightening narrows the cone of acceptable settlement-print disturbance to 1 %, recognising that the closing print of the underlying determines derivatives settlement.

Dynamic VI is **applied** during [KRX-TOUR-KOSPI-OPS-T9]:

- The continuous session (09:00–15:20 KST).
- The closing single-price receipt window (15:20–15:30 KST).
- The off-hours single-price session (16:00–18:00 KST).

Dynamic VI is **not** applied during the opening single-price receipt window — opening prints have no "immediately preceding" intraday print to anchor against, and the rate would compare to the day's base price, which is exactly what Static VI does instead.

### Static VI — rate, anchor, and applied sessions

Static VI uses a single rate of **10 %** for all eligible security categories [KRX-RULE-KOSPI-BR-ENFORCE-KO §41-2.2]. The reference is the most recent single-price-determined price (직전 단일가격, *jik-jeon dan-il-ga-gyeok*) — chronologically:

- Before the opening print: the day's base price (기준가격, *gi-jun-ga-gyeok*). Effectively a ±10 % cone around the prior close.
- After the opening print: the opening print itself.
- After any later single-price resumption: that resumption's clearing price.

Static VI is applied during [KRX-TOUR-KOSPI-OPS-T9]:

- The continuous session.
- The opening single-price receipt window.
- The closing single-price receipt window.

Note that Static VI runs **during** the opening receipt window — so a wildly-skewed indicative print before 09:00 can fire Static VI even though no actual trade has happened yet. Static VI is **not** applied during the off-hours single-price session.

### Resumption auction (cool-off)

When a VI fires, KRX takes one of two actions, depending on the current matching mode [KRX-RULE-KOSPI-BR-ENFORCE-KO §41-2.3]:

1. **Currently in continuous mode (§24)** — switch to single-price mode (§23) for the duration of the §35.1.4 receipt window — **2 minutes**. Orders received during that 2-minute window participate in a single-price call auction; standard §22 price-then-time priority applies [KRX-TOUR-KOSPI-OPS-T9]. After the call clears, continuous trading resumes.
2. **Currently in single-price mode (§23) — receipt window already open** — extend the existing receipt window by 2 minutes (§35.1.4 duration) before clearing.

Practical effect: every VI event consumes ~2 minutes of trading time and produces **one** auction print. The post-VI clearing price becomes the new "last single-price-determined price" for Static VI purposes — meaning a Static VI cannot re-trigger immediately on the post-VI continuous prints unless cumulative drift again exceeds 10 % from the new anchor [KRX-RULE-KOSPI-BR-ENFORCE-KO §41-2.4.4 — implicit via the §23.1.5 first-price exclusion].

Random-end (§35.1) does **not** apply to VI resumption auctions — the §35.1.4 receipt window is the closing-call window's entry; VI uses its 2-minute duration without the random-end overhang. (See [Auctions § Random-end mechanism](./auctions.md#random-end-mechanism) for the random-end scope.)

### Exclusions — issues VI does not apply to

VI is bypassed for the following issues, per [KRX-RULE-KOSPI-BR-ENFORCE-KO §41-2.4]:

1. **Liquidation issues (정리매매종목)** — already trade with no price limit (see [Price Ranges § Special-case price limits](./price_ranges.md#special-case-price-limits)).
2. **Short-term overheat issues (단기과열종목)** — separately stabilised via the §38-2 / §56-2 single-price mechanism running for 3 trading days [KRX-RULE-KOSPI-BR-KO §106-2; KRX-TOUR-KOSPI-OPS-T8].
3. **Abnormal-rise single-price issues (이상급등 단일가매매종목)**.
4. **Designated investment-warning issues (투자유의종목)**.
5. **Low-liquidity single-price issues** and **preferred-share single-price issues** (under §56-3.1, §56-4.1).
6. **Newly listed shares or DRs — listing day only** (added 2021-10-18 per [KRX-TOUR-KOSPI-OPS-T9]). Excludes transfers from KOSDAQ to KOSPI or vice versa — those still receive VI on the cross-market listing day.
7. **Within-day halt resumption** — when single-price is used to determine the resumption price under §23.1.2 (market-wide reopen) or §23.1.3 (individual-issue reopen). VI would otherwise stack on top of an already-disrupted matching event.
8. **Cascading VI suppression** — if a method-change first price (§23.1.5) again exceeds the rate threshold, the chained VI does not fire. So at most one VI per quote-burst.
9. **Small-stock filter** — for issues priced under KRW 1,000, if the tentative price is within **3 ticks** of the immediately preceding price, no VI [§41-2.4.6]. This stops 1-tick noise from firing VI on penny stocks where 6 % of the price is less than 3 ticks.
10. **KRX discretion** — KRX may bypass VI for any other market-administration reason [§41-2.4.7].

KRX may also adjust the §41-2.1 / §41-2.2 rates downward or upward when "applying the standard rates is markedly difficult" given quotation flow and market conditions [§41-2.5].

### Overlap with other stabilization mechanisms

Two precedence rules govern interactions between VI and other stabilization mechanisms [KRX-TOUR-KOSPI-OPS-T9]:

- **Circuit Breaker (CB) cancels VI.** When an index-level CB fires (per BR §25 — see [Circuit Breakers (KOSPI)](./circuit_breakers.md)), any in-progress per-issue stabilization is cancelled.
- **VI-in-progress blocks another VI** on the same issue. While a VI-triggered single-price call auction is running, a second VI cannot fire on the same issue.

A third precedence rule sits inside the §13-2 self-match-prevention mechanism [KRX-RULE-KOSPI-BR-ENFORCE-KO §41-2.6]: VI evaluates the *post-SMP* tentative price. So an HSA-ID-tagged self-trade-cancel under §13-2 runs first; if the surviving quotation's tentative price still triggers VI, only then does VI fire. Order of operations: SMP → VI evaluation → method change.

### Disclosure

When VI is triggered (or a method change occurs), KRX publishes the fact in real time per [KRX-RULE-KOSPI-BR-ENFORCE-KO §41-3]. The disclosure carries the issue ID, the trigger type (Dynamic / Static), the trigger time, and the resumption time. Members consume this via the standard market-data feed.

## Parameters & thresholds

### Table 1 — VI rates by category and session

| Category                                                                 | Continuous (09:00–15:20) | Closing call (15:20–15:30) | Off-hours single-price (16:00–18:00) | Source                                 |
|--------------------------------------------------------------------------|-------------------------:|---------------------------:|-------------------------------------:|----------------------------------------|
| Dynamic — KOSPI 200 constituent shares                                   |                    3 %   |                       2 %  |                              3 %     | [KRX-RULE-KOSPI-BR-ENFORCE-KO §41-2.1.1.a, proviso] |
| Dynamic — KOSPI 200 underlying on derivatives expiry day, closing call   |                    n/a   |                       1 %  |                              n/a     | [KRX-RULE-KOSPI-BR-ENFORCE-KO §41-2.1, proviso 2]   |
| Dynamic — Other shares                                                   |                    6 %   |                       4 %  |                              6 %     | [KRX-RULE-KOSPI-BR-ENFORCE-KO §41-2.1.1.b, proviso] |
| Dynamic — ETF/ETN linked 1× (incl. inverse) to KOSPI200/100/50, KRX100, debt indices |               3 %  |                       2 %  |                              3 %     | [KRX-RULE-KOSPI-BR-ENFORCE-KO §41-2.1.2.a, proviso] |
| Dynamic — Other ETF/ETN (sector, foreign, commodity, leveraged)          |                    6 %   |                       4 %  |                              6 %     | [KRX-RULE-KOSPI-BR-ENFORCE-KO §41-2.1.2.b, proviso] |
| Dynamic — Foreign DR, beneficiary certs                                  |                    6 %   |                       4 %  |                              6 %     | [KRX-RULE-KOSPI-BR-ENFORCE-KO §41-2.1.3, proviso]   |
| Static — all eligible (against last single-price-determined price)       |                   10 %   |                      10 %  |                              n/a     | [KRX-RULE-KOSPI-BR-ENFORCE-KO §41-2.2]              |

"n/a" in the off-hours column for Static VI: Static VI is not applied during off-hours single-price (16:00–18:00). Dynamic VI in off-hours uses the same rate as the continuous session.

### Table 2 — Reference prices

| VI type    | Phase                                  | Reference price                                                  | Source                                                |
|------------|----------------------------------------|------------------------------------------------------------------|-------------------------------------------------------|
| Dynamic    | Before opening print                   | Day's base price (기준가격)                                       | [KRX-TOUR-KOSPI-OPS-T9]                               |
| Dynamic    | After opening print, intraday          | Immediately preceding trade price (직전의 가격)                   | [KRX-RULE-KOSPI-BR-KO §26-2.1.1]                      |
| Static     | Before opening print                   | Day's base price                                                  | [KRX-TOUR-KOSPI-OPS-T9]                               |
| Static     | After opening print                    | Most recent single-price-determined price                         | [KRX-RULE-KOSPI-BR-KO §26-2.1.2]                      |

### Table 3 — Action and timing

| Mechanism            | Trigger condition (tentative price vs reference)            | Action                                                       | Duration                       |
|----------------------|--------------------------------------------------------------|---------------------------------------------------------------|--------------------------------|
| VI from continuous   | |Δ| ≥ rate × reference                                       | Switch to single-price (§23) for §35.1.4 receipt window      | 2 minutes                      |
| VI from single-price | |Δ| ≥ rate × reference                                       | Extend single-price participation window by §35.1.4 duration | 2 minutes (additional)         |
| Random-end on resumption | n/a                                                      | None — VI auctions do not carry the §35.1 random-end          | n/a                            |

Source for the duration: [KRX-RULE-KOSPI-BR-ENFORCE-KO §41-2.3 (refers to §35.1.4); KRX-TOUR-KOSPI-OPS-T9 ("2 minutes")].

### Table 4 — Exclusions

| #  | Exclusion class                                                            | Source                                            |
|----|-----------------------------------------------------------------------------|---------------------------------------------------|
| 1  | Liquidation issues (정리매매종목)                                          | [KRX-RULE-KOSPI-BR-ENFORCE-KO §41-2.4.1]          |
| 2  | Short-term overheat issues (단기과열종목)                                  | [KRX-RULE-KOSPI-BR-ENFORCE-KO §41-2.4.2]          |
| 3  | Abnormal-rise single-price issues (이상급등 단일가매매종목)                | [KRX-RULE-KOSPI-BR-ENFORCE-KO §41-2.4.2-2]        |
| 4  | Designated investment-warning issues (투자유의종목)                        | [KRX-RULE-KOSPI-BR-ENFORCE-KO §41-2.4.2-3]        |
| 5  | Low-liquidity / preferred-share single-price issues (§56-3.1, §56-4.1)     | [KRX-RULE-KOSPI-BR-ENFORCE-KO §41-2.4.2-4]        |
| 6  | Newly listed shares/DRs — listing day only (excl. KOSPI ↔ KOSDAQ transfers) | [KRX-RULE-KOSPI-BR-ENFORCE-KO §41-2.4.2-5; KRX-TOUR-KOSPI-OPS-T9] |
| 7  | Within-day halt resumption single-price (§23.1.2, §23.1.3)                 | [KRX-RULE-KOSPI-BR-ENFORCE-KO §41-2.4.3]          |
| 8  | Cascading VI — first price after a method-change again exceeds threshold   | [KRX-RULE-KOSPI-BR-ENFORCE-KO §41-2.4.4]          |
| 9  | Small-stock filter (price < 1,000 KRW; |Δ| ≤ 3 ticks)                       | [KRX-RULE-KOSPI-BR-ENFORCE-KO §41-2.4.6]          |
| 10 | KRX discretion (market administration)                                     | [KRX-RULE-KOSPI-BR-ENFORCE-KO §41-2.4.7]          |

## Worked examples

### Example A — Dynamic VI on a KOSPI 200 stock

A KOSPI 200 stock has last traded at **KRW 50,000** at 13:30. At 13:31 a buy-market quote sweeps the book, generating a tentative match price of **KRW 51,600**. The dynamic-VI rate for KOSPI 200 in continuous mode is 3 %.

- Trigger threshold: 50,000 × 1.03 = 51,500. Tentative 51,600 ≥ 51,500 → **Dynamic VI fires** [KRX-RULE-KOSPI-BR-ENFORCE-KO §41-2.1.1.a].
- Action: continuous → single-price call for 2 minutes [KRX-RULE-KOSPI-BR-ENFORCE-KO §41-2.3.1].
- Receipt window: 13:31–13:33. All orders received in the window participate.
- At 13:33 the call clears at, say, **KRW 51,400**. Continuous trading resumes immediately. The "last single-price-determined price" for Static VI now becomes 51,400 (a new anchor).
- A second Dynamic VI cannot retrigger on the **same** 13:31 burst. A new burst at 13:35 that sweeps to e.g. KRW 53,000 (= 51,400 × 1.031) would fire a fresh Dynamic VI.

### Example B — Static VI on cumulative drift

A non-KOSPI-200 share opens at **KRW 10,000** at 09:00 (the opening single-price determined price). Continuous trading drifts the price gradually upward — many small Dynamic-VI-not-firing trades — and at 11:00 a quotation generates a tentative match of **KRW 11,050**. The Dynamic-VI rate (6 %) compares to the immediately preceding trade price (e.g. KRW 10,990), and the Δ = 60 → no Dynamic VI. But Static VI compares to the last single-price-determined price (10,000):

- Static threshold: 10,000 × 1.10 = 11,000. Tentative 11,050 ≥ 11,000 → **Static VI fires** [KRX-RULE-KOSPI-BR-ENFORCE-KO §41-2.2].
- Action: switch to single-price for 2 minutes.
- At 11:02 the call clears at, say, **KRW 11,020**. The new "last single-price-determined price" becomes 11,020 — Static VI's next threshold is 11,020 × 1.10 = 12,122.

This is the design intent: Dynamic VI catches **bursts**, Static VI catches **cumulative drift** — an issue that drifts up by 0.5 % per minute over 20 minutes never fires Dynamic VI but will fire Static VI when the cumulative move crosses 10 %.

### Example C — closing-call VI on a derivatives expiry day

It is the last trading day of KOSPI 200 futures and options. A KOSPI 200 constituent's reference price entering the closing call (15:20) is **KRW 80,000**. A late-arriving sell-imbalance produces a tentative closing print of **KRW 79,150** at 15:25.

- Standard closing-call dynamic rate for KOSPI 200: 2 %. Threshold: 80,000 × 0.98 = 78,400. Tentative 79,150 ≥ 78,400 → no VI under the standard rate.
- But this is a derivatives-expiry day. The proviso reduces the rate to **1 %** for the underlying [KRX-RULE-KOSPI-BR-ENFORCE-KO §41-2.1, proviso 2]. Threshold: 80,000 × 0.99 = 79,200. Tentative 79,150 < 79,200 → **Dynamic VI fires**.
- Action: extend the closing-call participation window by 2 more minutes [KRX-RULE-KOSPI-BR-ENFORCE-KO §41-2.3.2].
- The eventual closing print determines the futures/options settlement value. The 1 % cone narrows the disturbance window relative to a non-expiry day's 2 % cone — this is the rule's purpose.

## Edge cases & open questions

- Edge case: §41-2.4.4 says VI does not fire when the post-method-change first price (§23.1.5) again exceeds the rate threshold. So a second consecutive VI on the same imbalance is suppressed. But the rule does not specify what happens if the *next continuous trade* (after a few normal trades) again exceeds the threshold against the new anchor — the standard re-evaluation should fire Dynamic VI again, but the rule's "cascading VI" wording is potentially over-broad. Verify by reviewing real VI logs before relying on a particular cascading model.
- Edge case: The 1 % derivatives-expiry rate applies only to the **closing-call receipt window** of the underlying — not to the continuous session of the same day. So a 2 % move at 11:00 on expiry day does not fire Dynamic VI (3 % continuous threshold still applies); only the closing call from 15:20 onward uses the tightened cone. Algos hedging into the close should treat the threshold as session-dependent, not day-dependent.
- Edge case: The §41-2.4.6 small-stock filter ("3 ticks for issues under KRW 1,000") is **only** an exclusion — no VI even if the percentage exceeds the rate. A KRW 800 share with a 5-tick (= 5 KRW = 0.625 %) move will not fire Dynamic VI even though larger-percentage Dynamic-VI events typically do; conversely, a 60 KRW move on a KRW 800 share (= 7.5 % move, = 60 ticks) does fire. The filter switches off below the 3-tick mark.
- Edge case: VI does not fire when SMP cancels the matchable quantity first [KRX-RULE-KOSPI-BR-ENFORCE-KO §41-2.6]. So an HSA-tagged self-trade that would otherwise have driven a 3 %+ tentative print is cancelled at the SMP stage; VI sees only the surviving non-self quantity. Members operating with both SMP and VI-sensitive strategies should treat SMP as VI-suppressing in the limit.
- Open question: VI applied to ETF/ETN underlyings — §41-2.1.2 categorizes ETF/ETN by index linkage and leverage multiple, but the categorization references "1× (or inversely linked) to KOSPI200…" without defining what "linked" means precisely for synthetic / TRS-based ETFs. Verify against ETF Listing Regulation §149-3 before classifying a structured product.
- Open question: The "newly-listed listing-day exception" of [KRX-TOUR-KOSPI-OPS-T9] is dated 2021-10-18 and is reflected in §41-2.4.2-5. The tour notes the carve-out **excludes** transfers from KOSPI to KOSDAQ or vice versa — those keep VI on listing day. Whether re-listings (재상장종목) and merger-listings (합병상장종목) are covered by §41-2.4.2-5 is not explicit; the rule says "주권 또는 주식예탁증권의 상장일 당일" (newly-listed shares/DRs on listing day), which arguably includes re-listings. Confirm before treating any first-day post-merger trade as VI-exempt.
- Unsourced claim: [KRX-TOUR-KOSPI-OPS-T9] gives the historical "Oct 18th, 2021" date for the newly-listed-on-listing-day exception. The rulebook does not preserve the exact addition date of §41-2.4.2-5; the 2021-09-29 amendment marker on §41-2.4 does include a §41-2.4.2-5 paragraph but the marker is one of many in that round. Treat the 2021-10-18 effective date as overview color.

## Sources

- `KRX-RULE-KOSPI-BR-KO` — KOSPI Market Business Regulation (유가증권시장 업무규정, *yu-ga-jeung-gwon si-jang eom-mu gyu-jeong*), bookid 210200859, effective 2026-04-28. Articles cited: §23 (Single-price auction — referenced as the matching method during VI), §25 (Index-level CB — referenced for CB precedence), §26-2 (Per-issue trade-execution-method change — the parent rule for both VI types), §106-2 (Short-term overheat issue designation — referenced for the overheat exclusion).
- `KRX-RULE-KOSPI-BR-ENFORCE-KO` — KOSPI BR Enforcement Rule (유가증권시장 업무규정 시행세칙, *yu-ga-jeung-gwon si-jang eom-mu gyu-jeong si-haeng se-chik*), bookid 210203562, effective 2026-04-28. Articles cited: §35.1.4 (Single-price receipt window duration — 2 minutes — referenced from §41-2.3), §41-2 (VI rates, action, exclusions, KRX-discretion adjustment, SMP precedence — the central article), §41-3 (VI public disclosure — referenced), §56-2 (Short-term overheat trade-execution method — referenced), §56-3 / §56-4 (Low-liquidity / preferred-share single-price method — referenced for the exclusion list).
- `KRX-TOUR-KOSPI-OPS-T9` — KRX overview "Volatility Interruption (VI)"; English, not authoritative. Used for the Dynamic vs Static framing, the rate table (cross-referenced against §41-2.1), the 2-minute resumption-auction duration, the applied-session list, the newly-listed-on-listing-day exception (2021-10-18), and the CB-cancels-VI / VI-blocks-VI overlap rules. The "no daily cap on VI events" claim is also from this tour.
- `KRX-TOUR-KOSPI-OPS-T8` — KRX overview "Short-term Volatility Measures (overheat)"; English, not authoritative. Used only for the cross-reference to the separate single-price-for-3-trading-days mechanism that keeps overheat issues out of the VI flow.
