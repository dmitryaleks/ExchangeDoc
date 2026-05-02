---
title: "Other Topics (KOSDAQ)"
markets: [KOSDAQ]
last_reviewed: 2026-05-01
sources:
  - KRX-RULE-KOSDAQ-BR-KO
  - KRX-TOUR-KOSDAQ-EXCEPT-T1
  - KRX-TOUR-KOSDAQ-EXCEPT-T2
  - KRX-TOUR-KOSDAQ-EXCEPT-T3
  - KRX-TOUR-KOSDAQ-EXCEPT-T6
  - KRX-TOUR-KOSDAQ-EXCEPT-T8
  - KRX-TOUR-KOSDAQ-METHOD-T7
  - KRX-TOUR-KOSDAQ-OPS-T3
  - KRX-TOUR-KOSDAQ-OPS-T4
  - KRX-TOUR-KOSDAQ-OPS-T6
---

> See also: [Market Hours (KOSDAQ)](./market_hours.md), [Auctions (KOSDAQ)](./auctions.md), [Volatility Interruption (KOSDAQ)](./volatility_interruption.md), [Circuit Breakers (KOSDAQ)](./circuit_breakers.md), [Other Topics (KOSPI)](../kospi/other_topics.md), [Comparison](../common/comparison.md).

**Delta file.** This file is the catch-all for KOSDAQ topics that did not warrant a top-level file: **off-hours session details**, **regular-session block / basket / competitive-block trade**, **liquidation issues**, **program-trading + sidecar**, **liquidity provider (LP) system**, **short-term overheat designation**, **treasury-stock trading**, and **error-trade handling**. Most of the substance mirrors the KOSPI write-up, but several **material parametric deltas** are surfaced below: the sidecar 6 %/3 % dual-condition trigger, the LP 2 % spread cap, the off-hours block KRW 50M minimum, the basket KRW 200M + 5-item minimum, the program-trading non-arbitrage ≥ 10-issues threshold, and the LP 3-consecutive-lowest-rating → 1-year suspension rule. This file points to [KOSPI § Other Topics](../kospi/other_topics.md) for shared content.

## Summary

- **Off-hours sessions** consume **08:00–09:00 KST** (pre-open) and **15:40–18:00 KST** (post-close) — same windows as KOSPI [KRX-TOUR-KOSDAQ-EXCEPT-T1; KRX-TOUR-KOSDAQ-EXCEPT-T2]. Closing-price (시간외종가매매, *si-gan-oe jong-ga mae-mae*) trades at the day's close (or prior day's close pre-open) by **time priority only**; off-hours single-price (시간외단일가매매) runs **12 × 10-minute single-price auctions** at ±10 % of the closing price within the daily limit.
- **Block / basket trades — KOSDAQ-specific minimums** [KRX-TOUR-KOSDAQ-EXCEPT-T3]: block trading minimum **KRW 50,000,000** (vs KOSPI's KRW 100M); basket trading minimum **5+ items + KRW 200,000,000** (vs KOSPI's KRW 100M with no item-count requirement). The KOSDAQ minimums are intentionally tuned to KOSDAQ's smaller-cap profile.
- **Liquidation issues (정리매매종목)** trade for **7 trading days** in **14 × 30-minute single-price auctions per day**, with **no daily price limit** — same as KOSPI [KRX-TOUR-KOSDAQ-EXCEPT-T8; KRX-RULE-KOSDAQ-BR-KO §23.2].
- **Sidecar — KOSDAQ-specific dual-condition trigger** [KRX-RULE-KOSDAQ-BR-KO §13; KRX-TOUR-KOSDAQ-OPS-T3]: KOSDAQ 150 index futures move ≥ **6 %** **AND** KOSDAQ 150 index move ≥ **3 %** from prior close, **both for 1 minute**. KOSPI sidecar uses a **single-condition** trigger (KOSPI 200 futures ≥ 5 %, no separate index condition). Same 5-minute suspension; same 14:50 cutoff (장종료 40분 전); same CB-cancels-sidecar rule.
- **Program-trading non-arbitrage definition — ≥ 10 issues on KOSDAQ vs ≥ 15 on KOSPI** [KRX-TOUR-KOSDAQ-OPS-T3, KRX-TOUR-KOSDAQ-OPS-T4]. KOSDAQ uses "10 or more constituents of KOSDAQ Index"; KOSPI uses "15 or more issues in the KOSPI 200 stock-group."
- **Liquidity-provider system — KOSDAQ-specific 2 % spread cap** [KRX-RULE-KOSDAQ-BR-KO §12-2 to §12-6; KRX-TOUR-KOSDAQ-METHOD-T7]: bid-ask spread > **2 %** triggers obligatory LP quote (vs KOSPI's 3 %). LP must respond **within 5 minutes** of the trigger. Suspension after **3 consecutive lowest-rating evaluations** (vs KOSPI's 2 consecutive) for **1 year** [KRX-RULE-KOSDAQ-BR-KO §12-2.2.3.가].
- **Short-term overheat issues (단기과열종목)** — same designation framework as KOSPI but with extension trigger phrasing **"3 or 10 trading days"** at **20 %** threshold (vs KOSPI's "3 days" at 120 %) [KRX-TOUR-KOSDAQ-OPS-T6]; once designated, single-price-only matching every **30 minutes** (limit + market + competitive-block orders only; IOC/FOK not allowed) [KRX-RULE-KOSDAQ-BR-KO §23-2; KRX-TOUR-KOSDAQ-OPS-T6].
- **Treasury-stock trading** uses a **K-Blox** platform reference (KOSDAQ-side block-trading platform); operational details (1 % of issued shares cap, 25 % of monthly average daily volume, 5-tick scope range) match KOSPI [KRX-TOUR-KOSDAQ-EXCEPT-T6].
- **Error-trade rules** are covered by KOSDAQ §27 (KRX-driven correction) and §27-2 (mass-erroneous-trade relief, with **narrower security scope** than KOSPI §28-2 — excludes ETF / ETN / ELW). See [Trading Rules § Mass-erroneous-trade relief — both markets have it](./trading_rules.md#delta-vs-kospi).

## Detailed rules

### Off-hours closing-price trade (시간외종가매매)

Identical structure to KOSPI per [KRX-TOUR-KOSDAQ-EXCEPT-T1]:

- **Trading hours.** 08:30–08:40 KST (pre-open) and 15:40–16:00 KST (post-close) — 30 minutes total. Quotation receipt: 08:30–08:40 (pre) and 15:30–16:00 (post — note the 10-minute pre-trade buffer 15:30→15:40, same as KOSPI).
- **Eligible securities.** All listed issues including initially-listed new stock; excluding issues without regular-session transactions or abnormal-closing issues. Administrative issues are excluded from pre-hours session on the designation day [KRX-TOUR-KOSDAQ-EXCEPT-T1].
- **Execution price.** Pre-open: previous trading day's close. Post-close: current day's close. Limit-at-close only.
- **Matching.** Time priority only — no price competition.
- **Cancel and correct.** Quantity may be reduced; orders may be cancelled. Price may not be revised (the price is fixed at the closing price).
- **Trading unit.** 1 share.

### Off-hours single-price trade (시간외단일가매매)

Per [KRX-TOUR-KOSDAQ-EXCEPT-T2; KRX-RULE-KOSDAQ-BR-KO §21-3]:

- **Trading hours.** 16:00–18:00 KST — 12 single-price auctions every 10 minutes with random-end activated.
- **Price range.** ±10 % of the day's close, capped within the daily price-limit band.
- **Order type.** Limit only — market order is not allowed [KRX-TOUR-KOSDAQ-EXCEPT-T2 explicit: "Only limit order can be registered (market order is not allowed)"]. Same as KOSPI (which delegates this restriction to KOSPI ER §14.2.1.ma).
- **Trading unit.** 1 share.

12 distinct prints per session; market-data consumers should expect 12 sequence-numbered prints, same shape as KOSPI off-hours single-price.

### Off-hours and regular-session block / basket trade

Per [KRX-TOUR-KOSDAQ-EXCEPT-T3], with **KOSDAQ-specific minimum-size thresholds**:

| Trade type                             | Trading hours              | Price range                                  | Minimum quantity                                     |
|----------------------------------------|----------------------------|-----------------------------------------------|------------------------------------------------------|
| Regular-session block (장중대량매매)    | 09:00–15:30 KST            | Within the day's high–low range up to placement | **KRW 50,000,000** (block) / **KRW 200,000,000 + 5+ items** (basket) |
| Off-hours block (시간외대량매매)        | 08:00–09:00 + 15:40–18:00 | Within daily price-limit band                  | Same minimums as regular-session                     |

**Comparison to KOSPI:**

- **KOSDAQ block minimum:** KRW 50 million notional. **KOSPI block minimum:** "5,000 × trading lot (500 × for ETF / ETN), or KRW 100 million" — KOSDAQ's threshold is 50 % lower (and structurally simpler — no lot-multiple alternative).
- **KOSDAQ basket minimum:** **5 + items + KRW 200 million** — i.e. a basket must contain at least 5 different issues *and* total at least KRW 200 million notional. **KOSPI basket minimum:** same rules as block (no item-count requirement). The 5-item floor is **KOSDAQ-only**.
- **Carve-out:** for treasury-stock buybacks from government / Deposit Insurance Corporation, the daily-price-limit constraint does not apply — same as KOSPI but inlined in the KOSDAQ tour.

The "one buy or sell side from a single securities company" requirement applies on both markets.

### Liquidation issues (정리매매종목)

Per [KRX-TOUR-KOSDAQ-EXCEPT-T8; KRX-RULE-KOSDAQ-BR-KO §23.2]:

- **Window length.** 7 trading days from delisting decision.
- **Matching method.** **14 × 30-minute single-price auctions per day** during regular session. Limit orders only.
- **Daily price limit.** **None** [KRX-RULE-KOSDAQ-BR-KO §23.2 — verbatim parallel to KOSPI BR §20.3].
- **Off-hours behaviour.** "Trading by last traded price" (즉 시간외종가매매) applies the same daily price limits as a normal issue; "trading by single-price auction" (시간외단일가매매) has no daily price limits [KRX-TOUR-KOSDAQ-EXCEPT-T8 explicit].
- **Cross-applicable rules.** Liquidation issues are excluded from VI per [KRX-RULE-KOSDAQ-BR-KO §23-3 → KOSDAQ ER §41-2 analogue (R6 unresolved)] — see [Volatility Interruption § Exclusions (KOSDAQ)](./volatility_interruption.md). Quotation type-restrictions (no market, no conditional, no best-counter, no best-same, no midpoint, no stop-limit, no competitive — limit only) apply per the KOSDAQ ER §14 analogue.

### Program trading + sidecar

KOSDAQ §13 has the program-trading-quote-management / sidecar article with **KOSDAQ-specific parameters**:

#### Program-trading definition

[KRX-TOUR-KOSDAQ-OPS-T4]:

- **Index arbitrage** — linked simultaneous trading of an index basket (such as KOSDAQ 150 / KRX 300) and the corresponding futures or options on that index, to profit from the basis spread.
- **Non-arbitrage program trading** — same person concurrently buys or sells **≥ 10 constituents of the KOSDAQ Index** within a defined timeframe.

The KOSDAQ Index is calculated by KRX based on total aggregate market value with base date **1996-07-01**, per the KOSDAQ-OPS-T4 tour's parenthetical. The "≥ 10" non-arbitrage threshold is **lower** than KOSPI's "≥ 15 issues in the KOSPI 200 stock-group" — meaning the KOSDAQ definition is **broader** (catches smaller program-trade strategies).

#### Sidecar (KOSDAQ §13 — dual-condition trigger)

[KRX-RULE-KOSDAQ-BR-KO §13.1; KRX-TOUR-KOSDAQ-OPS-T3]:

> 거래소는 「파생상품시장 업무규정」 제3조제2항제1호의 국내지수선물시장에서 거래되는 코스닥 150을 기초자산으로 하는 선물거래종목 중 직전 매매거래일의 거래량이 가장 많은 종목... 의 가격이 같은 규정 제70조제2항에 따른 기준가격 대비 **100분의 6 이상** 상승(또는 하락)하고 코스닥 150의 수치가 직전 매매거래일의 최종수치 대비 **100분의 3 이상** 상승(또는 하락)하여 **동시에 1분간 지속**되는 경우 해당 시점부터 **5분간** 접수된 프로그램매매의 매수호가(또는 매도호가)의 효력을 정지한다.

Translation: KOSDAQ sidecar fires when (a) the most-traded KOSDAQ 150 futures contract moves ≥ **6 %** above or below its base price, **and** (b) the KOSDAQ 150 index moves ≥ **3 %** above or below its previous-day close, **both conditions persisting simultaneously for 1 minute**.

**Key parameter table:**

| Parameter                                 | KOSDAQ                                          | KOSPI                                       |
|-------------------------------------------|-------------------------------------------------|---------------------------------------------|
| Reference futures                          | KOSDAQ 150 index futures, most-traded           | KOSPI 200 futures, most-traded              |
| Trigger threshold #1 (futures)             | ≥ 6 %                                            | ≥ 5 %                                       |
| Trigger threshold #2 (index)               | ≥ 3 %                                            | (no separate index condition)               |
| Persistence requirement                    | 1 minute (both conditions)                       | 1 minute                                    |
| Suspension duration                        | 5 minutes                                        | 5 minutes                                   |
| Daily cap (latest fire time)               | 14:50 KST                                       | 14:50 KST                                   |
| CB-cancels-sidecar                          | Yes — per KOSDAQ §13.3.3 referencing §26        | Yes                                         |
| Earliest fire time (after open)             | 09:05 KST (5 min after 장개시 per §13.2)         | (no equivalent earliest-fire rule extracted; KOSPI sidecar fires from 09:00 in principle) |

The 6 %/3 % **dual condition** is a KOSDAQ-only design — KOSPI's sidecar uses a single-condition 5 % trigger on the futures only, with no separate index condition. The dual-condition design is intended to filter out futures-only spikes that aren't reflected in the underlying index, reducing false-positive sidecar fires on KOSDAQ.

The **09:05 earliest fire time** (per §13.2's "장개시 후 5분이 경과한 때부터 계산하며") is also KOSDAQ-only in the explicit-rule form. KOSPI's analogue is implicit; KOSDAQ's §13.2 codifies it explicitly.

#### Restoration

After the 5-minute suspension, program-trading quotations resume in receipt order [KRX-TOUR-KOSDAQ-OPS-T3]. Sidecar is also released:

1. 5 minutes have elapsed from sidecar firing.
2. 14:50 KST is reached (40 min before close).
3. CB has fired on the spot market under [KRX-RULE-KOSDAQ-BR-KO §26] and trading has resumed (CB cancels sidecar) — see [Circuit Breakers (KOSDAQ)](./circuit_breakers.md).

### Liquidity-provider (LP) system (KOSDAQ §12-2 to §12-6)

KOSDAQ's LP framework is at §12-2 to §12-6 of the BR. Key parameters per [KRX-RULE-KOSDAQ-BR-KO §12-4; KRX-TOUR-KOSDAQ-METHOD-T7]:

#### Spread-tightening trigger — KOSDAQ-only 2 % cap

KOSDAQ §12-4.1.1 reads:

> 주권의 경우 호가스프레드비율이 **2% 이내**로서 해당 주권상장법인과 유동성공급계약을 체결한 회원이 거래소에 신고한 비율

Translation: "for stocks, within a 2 % spread ratio as reported by the LP-contracted member." So:

- **KOSDAQ LP duty triggers when the bid-ask spread exceeds the LP-contract-reported ratio**, where the contract ratio must be ≤ 2 %.
- **KOSPI LP duty triggers at 3 % spread** (or LP-contract ratio ≤ 3 %).

The **2 % cap is KOSDAQ-only**. An execution algo using LP-quote presence as a liquidity signal should expect a **tighter spread response on KOSDAQ** than on KOSPI.

#### Response time — 5 minutes

KOSDAQ §12-4.1: "그 때부터 **5분 이내에** 유동성공급호가를 제출하여야 한다" — within **5 minutes** of the trigger, the LP must submit the obligatory quote [KRX-RULE-KOSDAQ-BR-KO §12-4.1; KRX-TOUR-KOSDAQ-METHOD-T7]. KOSPI's parallel rule (in KOSPI BR §20-2 — not extracted here in full) is believed to have the same 5-minute response time, but the KOSDAQ-METHOD-T7 tour explicitly states this whereas the KOSPI tour does not.

#### Suspension — 3 consecutive lowest ratings → 1 year

KOSDAQ §12-2.2.3.가 reads:

> 제12조의6에 따른 평가가 **3회 연속** 가장 낮은 등급인 경우 [그 때로부터 1년 이상 경과할 것]

Translation: "If §12-6 evaluations rate the LP at the lowest grade **3 consecutive times**, the LP is suspended for **at least 1 year** from that time" [KRX-RULE-KOSDAQ-BR-KO §12-2.2.3.가].

**KOSPI tour OPS-T7** (per [KOSPI Other Topics § LP system](../kospi/other_topics.md#liquidity-provider-lp-system)) gives "1 year suspension on **2 consecutive** lowest ratings" — flagged as operational LP-contract content. The KOSDAQ rule is **stricter** (3 consecutive) — and is in the **BR text**, not just the LP contract.

#### LP qualification

Per KOSDAQ §12-2.2:

1. The member must be a **settlement member** (결제회원, *gyeol-je-hoe-won*) with proprietary-trading authorization for stocks.
2. The member must designate an LP-business-dedicated employee.
3. None of: (a) 3-consecutive-lowest-rating LP-evaluation suspension active, (b) liquidity-provision-related criminal sanction or business-suspension order in effect.

#### Other KOSDAQ-LP rules

- **Eligible securities (§12-2.1):** stocks (주권, including foreign DRs). KOSDAQ-LP framework does **not** explicitly cover ETFs / ETNs at the BR-level — those are presumably covered separately or by the §12-2 catch-all read broadly.
- **Quotation-spread ratio (호가스프레드비율) definition (§12-4.2):** (best ask − best bid) / best bid × 100 %.
- **Quotation method (§12-5):** detailed price-construction rule for LP quotes (5-tick-band around the touch).

The 2 % spread cap, 5-minute response time, and 3-consecutive-rating suspension are the most prominent KOSDAQ-side LP deltas vs KOSPI.

### Short-term overheat (단기과열종목)

Per [KRX-RULE-KOSDAQ-BR-KO §23-2; KRX-TOUR-KOSDAQ-OPS-T6]:

- **Designation criteria** — same triple-test as KOSPI (price-rise, turnover, volatility), with the precise thresholds delegated to the KOSDAQ Enforcement Rule (R6 unresolved).
- **Designation effect.** From the day after designation, the issue trades in **single-price-only mode every 30 minutes** [KRX-TOUR-KOSDAQ-OPS-T6 explicit: "trades are executed every 30 minutes after 09:00... during the regular market session (09:00–15:30)"]. **Limit orders, market orders, and competitive-block trading orders** are allowed; **IOC and FOK conditions are not** [KRX-TOUR-KOSDAQ-OPS-T6].
- **Designation extension** — KOSDAQ-OPS-T6 says the period can be extended "by 3 (or 10) trading days when the closing price on the last day of triggering period is **20 % or higher** than the closing price of the day before the execution." The "3 or 10" framing differs from KOSPI's flat "3-day" extension at the 120 %-threshold framing in [KOSPI Other Topics § Short-term overheat](../kospi/other_topics.md#short-term-overheat). Whether the actual ER thresholds differ or the tour wording differs is unclear without R6.
- **Off-hours and block / basket / competitive-block during regular session execute normally** [KRX-TOUR-KOSDAQ-OPS-T6]: an overheat-designated issue still trades through the off-hours sessions and through block-trade routes during the regular session, just not via the standard regular-session continuous matching.

The §23-2 article structure mirrors KOSPI BR §106-2 — same designation framework, same effect of switching to §18-implemented single-price mode (KOSPI's analogue is §23 / §26-2). The 30-minute periodic single-price interval is consistent across both markets per the tour pages.

### Treasury-stock trading (KOSDAQ §10–§12, §35; K-Blox platform)

Treasury-stock acquisition / disposal by KOSDAQ-listed corporations [KRX-TOUR-KOSDAQ-EXCEPT-T6]:

- **Reporting and submission** — listed company announces resolution to KRX on resolution day; report submitted to FSC the day after.
- **K-Blox System** — KOSDAQ uses a dedicated **K-Blox** platform for treasury-stock transaction submission (analogue of KOSPI's A-Blox-related system). Application submitted from market close to 18:00 on the day prior to the bid-price submission date.
- **Period.** Within 3 months of the resolution announcement.
- **Daily quantity limits.** Within **1 % of issued shares**; the daily quantity is the **higher** of (a) 10 % of the planned acquisition / disposal quantity, (b) 25 % of the 1-month average daily trading volume retroactive to the day before the resolution.
- **Price scope** [KRX-TOUR-KOSDAQ-EXCEPT-T6]:
  - Before regular session: bid = previous close to +5 %; ask = previous close to −2 ticks.
  - During regular session: bid = ±5 ticks of (max of last-trade, best-bid); ask = ±5 ticks of (min of last-trade, best-ask).
- **No daily-price-limit override** for treasury-stock disposal via massive purchase in after-hours trading.
- **No daily-price-limit override** when FSC grants approval for investor-protection / market-stability reasons during rapid market change.
- **Treasury-stock-quotation type restrictions** [KRX-RULE-KOSDAQ-BR-KO §10] — treasury-stock orders cannot be market or conditional-limit (per the KOSDAQ ER §14.2 analogue, R6 unresolved).

KOSDAQ's K-Blox is operationally similar to KOSPI's treasury-stock workflow (which uses the KOSPI-side block-trading platform).

### Error-trade handling

Same architecture as KOSPI:

- A trade printed on KOSDAQ is **final** at the moment of match per [KRX-RULE-KOSDAQ-BR-KO §17.1]'s general rule.
- **§27 — error-trade correction by KRX:** when KRX detects a matching-process error (its own or a member's input error), KRX may correct the trade record per the Enforcement Rule [KRX-RULE-KOSDAQ-BR-KO §27]. This is a narrow, KRX-driven correction path.
- **§27-2 — mass-erroneous-trade relief by member request:** added 2015-11-04, this is the formal trade-relief mechanism for fat-finger / large-error trades. Detailed write-up in [Trading Rules § Mass-erroneous-trade relief — both markets have it](./trading_rules.md#delta-vs-kospi). Key delta from KOSPI §28-2: **KOSDAQ §27-2's eligible-security scope is narrower** — it covers only **shares, foreign DRs, and corporate-growth-investment-fund securities** (vs KOSPI's shares + foreign DRs + ETF + ETN + ELW + beneficiary certs). KOSDAQ-listed ETF / ETN errors fall outside §27-2's scope.
- **Disconnect-cancel** (§16-2) — see [Order Amendments § Detailed rules](./amendments.md#delta-vs-kospi). For mass-quotation errors from a member system failure, the disconnect-cancel facility limits forward exposure but does not retroactively undo prints.
- **System-failure / quote-flooding emergency halts** (§25-2) — see [Circuit Breakers § Detailed rules](./circuit_breakers.md#delta-vs-kospi). KRX may halt trading or change matching method when system or quote-flooding events threaten KOSDAQ system stability.

The practical implication for an execution algo: assume **no print is reversible** outside the §27 / §27-2 paths; risk-budget for fat-finger errors at the member-system pre-quote level.

## Parameters & thresholds

### Table 1 — Off-hours session matrix (KOSDAQ)

| Session                                 | Hours                           | Method                       | Price/range                                       | Order types     | Source                                |
|-----------------------------------------|---------------------------------|-------------------------------|----------------------------------------------------|-----------------|---------------------------------------|
| Off-hours closing-price (pre-open)      | 08:30–08:40 KST                 | Time priority                 | Prior day's close (fixed)                          | Limit-at-close  | [KRX-TOUR-KOSDAQ-EXCEPT-T1]           |
| Off-hours closing-price (post-close)    | 15:40–16:00 KST                 | Time priority                 | Day's close (fixed)                                | Limit-at-close  | [KRX-TOUR-KOSDAQ-EXCEPT-T1]           |
| Off-hours single-price                  | 16:00–18:00 KST                 | 12 × 10-min call auctions     | ±10 % of day's close, within daily limit            | Limit only      | [KRX-TOUR-KOSDAQ-EXCEPT-T2]           |
| Off-hours block (장개시전 / 장종료후)    | 08:00–09:00 + 15:40–18:00 KST   | Negotiated bid-ask pair       | Within daily limit                                  | Block-paired    | [KRX-TOUR-KOSDAQ-EXCEPT-T3]           |
| Off-hours basket                        | 08:00–09:00 + 15:40–18:00 KST   | Negotiated basket pair        | Within daily limit                                  | Basket-paired   | [KRX-TOUR-KOSDAQ-EXCEPT-T3]           |
| Regular-session block (장중대량매매)     | 09:00–15:30 KST                 | Negotiated bid-ask pair       | Within day's high–low range up to placement         | Block-paired    | [KRX-TOUR-KOSDAQ-EXCEPT-T3]           |
| Regular-session basket (장중바스켓매매)   | 09:00–15:30 KST                 | Negotiated basket pair        | Within day's high–low range up to placement         | Basket-paired   | [KRX-TOUR-KOSDAQ-EXCEPT-T3]           |
| Regular-session A-Blox (장중경쟁대량매매) | 09:00–15:00 KST                 | Continuous time-priority      | VWAP-based                                          | Competitive-block | [KRX-TOUR-KOSDAQ-EXCEPT-T4 — see auctions.md] |
| Off-hours A-Blox (시간외경쟁대량매매)     | 08:00–09:00 KST (pre-open only) | Continuous time-priority      | VWAP-based                                          | Competitive-block | [KRX-RULE-KOSDAQ-BR-KO §21-2]        |

### Table 2 — Block / basket / A-Blox minimum size (KOSDAQ — DELTAS vs KOSPI)

| Trade type                       | KOSDAQ Minimum                                              | KOSPI Minimum                                  | Source                              |
|----------------------------------|-------------------------------------------------------------|------------------------------------------------|-------------------------------------|
| Off-hours block                  | **KRW 50,000,000**                                          | KRW 100,000,000 (or 5,000 × lot)               | [KRX-TOUR-KOSDAQ-EXCEPT-T3]         |
| Off-hours basket                 | **KRW 200,000,000 + ≥ 5 items**                             | KRW 100,000,000 (no item-count requirement)    | [KRX-TOUR-KOSDAQ-EXCEPT-T3]         |
| Regular-session block            | KRW 50,000,000                                              | Same as off-hours block (KOSPI)                | [KRX-TOUR-KOSDAQ-EXCEPT-T3]         |
| Regular-session basket           | KRW 200,000,000 + ≥ 5 items                                 | Same as off-hours block (KOSPI)                | [KRX-TOUR-KOSDAQ-EXCEPT-T3]         |
| Regular-session A-Blox           | **KRW 200,000,000** (1-share trading unit)                  | KRW 500,000,000 (100-share trading unit)       | [KRX-TOUR-KOSDAQ-EXCEPT-T4 — see auctions.md] |

### Table 3 — Sidecar parameters (KOSDAQ — DELTA vs KOSPI)

| Parameter                                 | KOSDAQ                                                  | KOSPI                                  | Source                                  |
|-------------------------------------------|---------------------------------------------------------|----------------------------------------|-----------------------------------------|
| Reference futures                          | KOSDAQ 150 index futures (most-traded)                  | KOSPI 200 futures (most-traded)        | [KRX-RULE-KOSDAQ-BR-KO §13.1]           |
| Trigger condition                          | Futures ≥ **6 %** **AND** index ≥ **3 %** for 1 min    | Futures ≥ **5 %** for 1 min (no separate index condition) | [KRX-RULE-KOSDAQ-BR-KO §13.1]   |
| Persistence requirement                    | 1 minute (both conditions simultaneously)               | 1 minute                                | [KRX-RULE-KOSDAQ-BR-KO §13.1]           |
| Suspension duration                        | 5 minutes                                                | 5 minutes                               | [KRX-TOUR-KOSDAQ-OPS-T3]                |
| Earliest fire time (after open)            | 09:05 KST (5 min after 장개시 per §13.2)                 | (implicit — not explicitly codified)    | [KRX-RULE-KOSDAQ-BR-KO §13.2]           |
| Daily cap (latest fire time)               | 14:50 KST                                                | 14:50 KST                               | [KRX-RULE-KOSDAQ-BR-KO §13.1 proviso]   |
| CB-cancels-sidecar                          | Yes                                                      | Yes                                     | [KRX-RULE-KOSDAQ-BR-KO §13.3.3]         |
| Once-per-day cap                            | Yes                                                      | Yes                                     | [KRX-RULE-KOSDAQ-BR-KO §13.2]           |

### Table 4 — Program-trading definition (KOSDAQ — DELTA vs KOSPI)

| Aspect                                      | KOSDAQ                                                       | KOSPI                                  |
|---------------------------------------------|--------------------------------------------------------------|----------------------------------------|
| Index-arbitrage reference                    | KOSDAQ 150 / KRX 300 (per Derivatives BR)                    | KOSPI 200 (per Derivatives BR)         |
| Non-arbitrage minimum issues                 | **≥ 10 constituents of KOSDAQ Index**                        | **≥ 15 issues in KOSPI 200 stock-group** |
| Source                                       | [KRX-TOUR-KOSDAQ-OPS-T4]                                     | [KRX-RULE-KOSPI-BR-KO §2.20.2]         |

### Table 5 — LP duty (KOSDAQ — DELTAS vs KOSPI)

| Parameter                                   | KOSDAQ                                          | KOSPI                                              | Source                                      |
|---------------------------------------------|-------------------------------------------------|----------------------------------------------------|---------------------------------------------|
| Spread tightening trigger                    | Spread > **2 %** (or LP-contract ratio ≤ 2 %)   | Spread > **3 %** (or LP-contract ratio ≤ 3 %)      | [KRX-RULE-KOSDAQ-BR-KO §12-4.1]             |
| Response time                                | **Within 5 minutes** of trigger                  | Within 5 minutes (implied; not explicit in tour)   | [KRX-RULE-KOSDAQ-BR-KO §12-4.1]             |
| Suspension on lowest-rating consecutive      | **3 consecutive ratings** → ≥ 1 year suspension | 2 consecutive lowest ratings (per KOSPI tour)      | [KRX-RULE-KOSDAQ-BR-KO §12-2.2.3.가]        |
| Quotation-spread-ratio definition             | (best ask − best bid) / best bid × 100 %        | Same                                                | [KRX-RULE-KOSDAQ-BR-KO §12-4.2]             |
| Eligible securities                          | Stocks (incl. foreign DRs)                       | Stocks, ETFs, ETNs, ELWs, low-turnover stocks       | [KRX-RULE-KOSDAQ-BR-KO §12-2.1]             |

### Table 6 — Short-term overheat designation behaviour (KOSDAQ)

| Parameter                                | KOSDAQ                                                    | Source                                  |
|------------------------------------------|----------------------------------------------------------|-----------------------------------------|
| Single-price-only matching interval       | **30 minutes**                                           | [KRX-TOUR-KOSDAQ-OPS-T6]                |
| Allowed order types during overheat       | Limit, market, competitive-block (no IOC, no FOK)        | [KRX-TOUR-KOSDAQ-OPS-T6]                |
| Off-hours / block trading during overheat | Executed normally                                         | [KRX-TOUR-KOSDAQ-OPS-T6]                |
| Designation extension trigger             | Last-day close ≥ 20 % above pre-execution close → extension by 3 (or 10) trading days | [KRX-TOUR-KOSDAQ-OPS-T6] |

## Worked examples

The KOSPI worked examples — Example A (off-hours single-price auction sequence with band-binding case), Example B (sidecar trigger and resumption), Example C (short-term overheat designation cascade) — carry over to KOSDAQ with **parameter substitution**:

- For the off-hours single-price example, the ±10 % cone and the 12 × 10-min auction structure apply identically [KRX-TOUR-KOSDAQ-EXCEPT-T2]; only the daily-price-limit-band cone (60 %–400 % vs ±30 %) for newly-listed-day vs normal cases changes per market.
- For the sidecar example, the trigger arithmetic substitutes: KOSDAQ requires **futures ≥ 6 % AND index ≥ 3 %** simultaneously for 1 min, vs KOSPI's futures ≥ 5 %.
- For the short-term overheat example, the "30 minutes per single-price auction" applies on both markets; the extension-trigger phrasing differs (KOSDAQ-OPS-T6 says "20 %", KOSPI-OPS-T8 says "120 %" — the KOSDAQ tour likely means "20 % rise" while KOSPI tour means "120 % of base"; same substantive trigger, different framing).

### Example D — KOSDAQ-specific sidecar trigger

The most-traded KOSDAQ 150 futures contract opens at 1,200.00 (base price). The KOSDAQ 150 index closed yesterday at 1,150. At 13:50:

- KOSDAQ 150 futures trades at **1,128.00** (= 94 % of base, = 6 % drop). Threshold #1 met.
- KOSDAQ 150 index reads **1,114.50** (= 96.91 % of yesterday's 1,150 close, = 3.09 % drop). Threshold #2 met.

Both conditions are met simultaneously. Persistence clock starts at 13:50:00.

- **13:51:00** — both conditions still met for 1 minute → **sidecar fires** [KRX-RULE-KOSDAQ-BR-KO §13.1]. Program-sell quotations on the KOSDAQ spot market are suspended for 5 minutes.
- **13:51:00 → 13:56:00** — program-sell suspension. Program-buy quotations continue normally. Cancel and correct of suspended program-sell quotations are also held during this window [KRX-TOUR-KOSDAQ-OPS-T3].
- **13:56:00** — suspension ends; program-sell quotations resume in receipt order.

Contrast with the same scenario on KOSPI: KOSPI sidecar fires on the futures-only 5 % condition, regardless of whether the index has dropped 3 %. So a futures-spike-without-index-move scenario fires KOSPI sidecar but **does not** fire KOSDAQ sidecar — KOSDAQ's dual-condition is a stricter filter that suppresses futures-only false alarms.

### Example E — KOSDAQ LP duty trigger

A KOSDAQ-listed mid-cap stock has best bid = KRW 9,950 and best ask = KRW 10,150 (spread = 200, spread ratio = 200 / 9,950 = **2.01 %**). The LP-contract ratio for this issue is **1.8 %** (set by the LP-listed-company contract, within the 2 % cap).

- The current spread (2.01 %) exceeds the contract ratio (1.8 %) → the **LP must respond within 5 minutes** [KRX-RULE-KOSDAQ-BR-KO §12-4.1].
- Within 5 minutes, the LP submits an obligatory quote tightening the spread to within 1.8 % — e.g. a buy quote at 10,000 and/or a sell quote at 10,100 to bring the spread to ≤ 1.8 %.
- The LP-quote quantity must be at least the contract-specified minimum (typically 5 × trading lot or larger per contract).

On KOSPI, the same scenario at 2.01 % spread would not trigger LP duty — KOSPI's threshold is 3 %. KOSDAQ-listed stocks therefore experience **more frequent LP intervention** for the same spread level than KOSPI-listed stocks.

## Edge cases & open questions

- Edge case: KOSDAQ basket-trade minimum requires **≥ 5 items** on top of the KRW 200M notional [KRX-TOUR-KOSDAQ-EXCEPT-T3]. A 4-item basket totalling KRW 250M would be **rejected** as a basket trade and would have to be split into individual block trades (each ≥ KRW 50M). Algos building KOSDAQ basket flows must respect both constraints.
- Edge case: KOSDAQ sidecar's dual-condition is conjunctive ("동시에 1분간 지속"). A futures spike to 6 % without an accompanying index move ≥ 3 % does not fire KOSDAQ sidecar — significantly different from KOSPI's single-condition trigger. An index-arbitrage strategy across both markets must encode this difference into its model of sidecar-event probability.
- Edge case: KOSDAQ §13.2's explicit **09:05 earliest-fire** time means the first 5 minutes of the regular session are sidecar-immune. KOSPI's parallel rule is implicit; KOSDAQ codifies it. An algo placing program-trade orders at 09:00–09:05 KST has no sidecar-cancellation risk on KOSDAQ for that window.
- Edge case: KOSDAQ LP §12-2.1 enumerates only "주권" (stocks, including foreign DRs) as eligible securities for the LP framework. ETFs / ETNs / ELWs are not enumerated at the BR level — KOSPI's framework explicitly covers all four. Whether KOSDAQ-LPs cover KOSDAQ-listed ETFs at all (vs leaving that to the KOSPI-side LP framework via cross-market reference) is unclear from the BR text alone. R6 confirmation pending.
- Edge case: KOSDAQ-OPS-T6's "3 (or 10) trading days" extension framing differs from KOSPI-OPS-T8's "3 days" extension framing. The KOSDAQ tour's "20 %" trigger threshold also differs from KOSPI tour's "120 %" framing — both are likely two ways of expressing the same thing (last-day close at 1.2× pre-execution close = 20 % rise = 120 % level). But the "or 10" alternative on KOSDAQ may indicate a different rule for severe overheat cases. R6 / Phase 6 confirmation needed.
- Open question: The KOSDAQ K-Blox treasury-stock platform is operationally separate from KOSPI's A-Blox / treasury-stock workflow. Whether the platform-level differences affect order-routing or only operational submission timing is not detailed in [KRX-TOUR-KOSDAQ-EXCEPT-T6]. Cross-check against the KRX Member System Access Guidelines.
- Open question: KOSDAQ §27-2 mass-erroneous-trade relief excludes ETF / ETN / ELW. ELW is moot (no ELW listings on KOSDAQ); ETF / ETN are common. Whether a KOSDAQ-listed ETF / ETN fat-finger error has any post-trade relief mechanism at all (vs KOSPI which covers them under §28-2) is structurally unclear. The conservative reading: no relief; the §17.1 finality rule binds.
- Open question: KOSDAQ §13 sidecar references the "거래량이 가장 많은 종목" (most-traded contract) for the futures benchmark. On roll days, the most-traded contract may shift mid-day. KOSDAQ-OPS-T3 does not address roll-day handling explicitly; same edge case as KOSPI's sidecar most-traded-contract reference.
- Unsourced claim: [KRX-TOUR-KOSDAQ-METHOD-T7]'s "5 minutes within obligatory quote" claim is sourced to the rule (KOSDAQ §12-4.1's "5분 이내에"). The corresponding KOSPI tour [KRX-TOUR-KOSPI-OPS-T7] is silent on response time — KOSPI's analogue article in BR §20-2 likely has the same 5-minute requirement, but the explicit mention is KOSDAQ-only in the tour material. Treat the 5-minute response time as a feature both books share by rule, not just KOSDAQ.
- Unsourced claim: KOSDAQ-OPS-T6's "(or 10) trading days" extension language is unique to the KOSDAQ tour — KOSPI tour OPS-T8 doesn't have a "10-day" alternative. This may reflect a KOSDAQ-side severe-case extension that doesn't exist on KOSPI, or it may be a tour-page-specific framing. Pending R6, treat the 10-day extension as KOSDAQ-only-flagged.

## Sources

- `KRX-RULE-KOSDAQ-BR-KO` — KOSDAQ Market Business Regulation (코스닥시장 업무규정), bookid 210164370, effective 2026-04-28. Articles cited: §10–§12 (Treasury-stock trading framework), §12-2 to §12-6 (LP system — central articles for the 2 % spread cap, 5-minute response, 3-consecutive-rating suspension), §13 (Sidecar / program-trading-quote management — central article: 6 %/3 % dual-condition trigger; 09:05 earliest fire; 14:50 cutoff; CB-cancels-sidecar), §17.1 (Trade finality — referenced for error-trade discussion), §21-3 (Off-hours single-price — referenced for the limit-only carve-out), §23 (Liquidation issues — §23.2 no-price-limit-band rule), §23-2 (Short-term overheat designation), §23-3 (Per-issue trade-execution-method change — referenced for VI), §27 (Error-trade correction by KRX), §27-2 (Mass-erroneous-trade relief — narrower security scope than KOSPI §28-2; full write-up in [Trading Rules § Mass-erroneous-trade relief](./trading_rules.md#delta-vs-kospi)).
- `KRX-TOUR-KOSDAQ-EXCEPT-T1` — KRX overview "Off-hours Closing Price Trade" (KOSDAQ); English, not authoritative. Used for the off-hours closing-price parameters (08:30–08:40 / 15:30–16:00 receipt, 15:40–16:00 trading, time-priority-only matching).
- `KRX-TOUR-KOSDAQ-EXCEPT-T2` — KRX overview "Off-hours Single Price Trading" (KOSDAQ); English, not authoritative. Used for the 12 × 10-min single-price structure with random-end and the limit-only restriction.
- `KRX-TOUR-KOSDAQ-EXCEPT-T3` — KRX overview "Off-hours Block Trade" (KOSDAQ); English, not authoritative. **Sole source** for the KOSDAQ-specific block / basket minimum thresholds: KRW 50M block, KRW 200M + 5 items basket, treasury-stock-from-government no-price-limit carve-out.
- `KRX-TOUR-KOSDAQ-EXCEPT-T6` — KRX overview "Treasury stock acquisition workflow" (KOSDAQ); English, not authoritative. Used for the K-Blox platform reference, the 1 % of issued shares cap, the 25 %-of-monthly-average daily-volume formula, the 5-tick-scope bid / ask range, and the FSC-approval no-price-limit override.
- `KRX-TOUR-KOSDAQ-EXCEPT-T8` — KRX overview "Trading of Liquidation Issues" (KOSDAQ); English, not authoritative. Used for the 7-day window and 14 × 30-min single-price-auctions-per-day structure, plus the off-hours treatment (last-traded-price applies daily limits; single-price has no limits).
- `KRX-TOUR-KOSDAQ-METHOD-T7` — KRX overview "Liquidity Provider (LP)" (KOSDAQ); English, not authoritative. **Primary source** for the KOSDAQ-specific 2 %-spread-cap LP rule, the 5-minute response time, and the LP-quote minimum obligation.
- `KRX-TOUR-KOSDAQ-OPS-T3` — KRX overview "Sidecar (program-trading halt)" (KOSDAQ); English, not authoritative. Used for the 6 %/3 % dual-condition trigger language, the 5-minute suspension, the cancel / correct also held during suspension, and the 14:50 cutoff plus CB-cancels-sidecar precedence.
- `KRX-TOUR-KOSDAQ-OPS-T4` — KRX overview "Program trading disclosure" (KOSDAQ); English, not authoritative. Used for the program-trading definition: index arbitrage on KOSDAQ 150 / KRX 300 + non-arbitrage at ≥ 10 issues of the KOSDAQ Index.
- `KRX-TOUR-KOSDAQ-OPS-T6` — KRX overview "Short-term Volatility Measures (overheat)" (KOSDAQ); English, not authoritative. Used for the 30-minute single-price-only matching interval, the limit / market / competitive-block-only order-type restriction, the off-hours / block trading exception, and the "3 (or 10) trading days" extension at 20 % framing (flagged for R6 reconciliation against KOSPI tour OPS-T8's "3 days" / "120 %" framing).
