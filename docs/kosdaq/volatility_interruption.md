---
title: "Volatility Interruption (KOSDAQ)"
markets: [KOSDAQ]
last_reviewed: 2026-05-01
sources:
  - KRX-RULE-KOSDAQ-BR-KO
  - KRX-TOUR-KOSDAQ-OPS-T7
  - KRX-TOUR-KOSDAQ-OPS-T5
---

> See also: [Volatility Interruption (KOSPI)](../kospi/volatility_interruption.md), [Circuit Breakers (KOSDAQ)](./circuit_breakers.md), [Auctions (KOSDAQ)](./auctions.md), [Trading Rules (KOSDAQ)](./trading_rules.md), [Comparison](../common/comparison.md).

**Delta file.** KOSDAQ standard VI substance is **identical to KOSPI**: same Dynamic / Static split, same per-method-change architecture, same rate categories (3 % / 6 % continuous + 2 % / 4 % closing + 1 % derivatives-expiry; 10 % Static), same 2-minute cool-off, same exclusions (liquidation / overheat / new-listing-day / cascading / small-stock-3-tick filter), same CB-cancels-VI and VI-blocks-VI overlap precedence, same SMP-before-VI ordering, same 10-min disclosure-curtain. The deltas are: (1) **article-numbering remap** (KOSDAQ §23-3 vs KOSPI §26-2; KOSDAQ ER analogue of KOSPI ER §41-2 unresolved per R6); (2) on KOSDAQ, the **typical equity** (non-KOSPI200 constituent) sits in the **6 %** Dynamic continuous bucket — KOSPI's 3 % bucket essentially does not apply to KOSDAQ-listed common shares; (3) **KOSDAQ has an additional price-disparity cooling-off mechanism** for preferred / new / SIC stocks at ≥ 200 % base-price divergence — this is **KOSDAQ-specific** and not part of the §23-3 VI framework. This file points to the [KOSPI write-up](../kospi/volatility_interruption.md) for shared VI content.

## Summary

- KOSDAQ implements two VI mechanisms — **Dynamic VI** (동적VI) and **Static VI** (정적VI) — via the per-issue trade-execution-method change rule [KRX-RULE-KOSDAQ-BR-KO §23-3; KRX-TOUR-KOSDAQ-OPS-T7]. Substance and parameters are believed to mirror the KOSPI Enforcement Rule §41-2 verbatim; KOSDAQ Enforcement Rule (R6) not yet archived.
- **Dynamic VI rates** [KRX-TOUR-KOSDAQ-OPS-T7]: 3 % / 2 % / 3 % for KOSPI200 constituents (and ETFs / ETNs linked to KOSPI200 / 100 / 50, KRX100, inverse, bond indices); **6 % / 4 % / 6 % for all other shares** including typical KOSDAQ equity (sector, foreign, commodity, leveraged products fall into the 6 % bucket too). Closing-call rates are reduced by ~33 %; derivatives-expiry-day closing-call further tightens to **1 %** for derivative-underlying constituents (KOSPI 200, KOSTAR / KOSDAQ 150, sector index, single-stock-future / option underlyings).
- **Static VI** is **10 %** of the last single-price-determined price for all eligible categories [KRX-TOUR-KOSDAQ-OPS-T7], applied during continuous + opening single-price + closing single-price (not during off-hours single-price).
- **Cool-off:** 2-minute single-price call auction; in continuous mode, switch from continuous to single-price; in single-price mode, extend the receipt window. Random-end does not apply to VI resumption auctions.
- **Exclusions** [KRX-TOUR-KOSDAQ-OPS-T7]: scheduled-for-delisting issues (= liquidation issues 정리매매종목) and short-term overheat issues are explicitly carved out by the tour; full §41-2.4 exclusion list (liquidation, overheat, abnormal-rise, investment-warning, low-liquidity / preferred-share single-price, newly-listed listing-day, within-day halt resumption, cascading VI suppression, small-stock 3-tick filter, KRX discretion) is believed to apply on KOSDAQ as on KOSPI.
- **KOSDAQ-only addition — price-disparity cooling-off** for preferred / new / securities-investment-company stocks: when the issue's base price is ≥ **200 %** of a comparable price (common-stock base for preferred; common-stock base for new; net-asset-value for SIC), and the issue is designated or about-to-be-designated as a price-surged stock, KRX imposes a **3-trading-day trading halt** [KRX-TOUR-KOSDAQ-OPS-T5]. Repeated rounds apply the same trigger cycle. This is **separate** from the §23-3 VI framework — it is a long-window 3-day halt rather than a 2-minute cool-off.

## Detailed rules

For full prose on the Dynamic / Static distinction, the per-method-change architecture (continuous → single-price; or extend the existing single-price window), the 2-minute cool-off, the SMP → VI evaluation order of operations, the CB-cancels-VI and VI-blocks-VI precedence rules, and the exhaustive exclusion list with worked examples, see [KOSPI § Detailed rules](../kospi/volatility_interruption.md#detailed-rules). The KOSDAQ articles map directly:

| KOSDAQ BR article | KOSPI BR article | Topic                                                             |
|-------------------|------------------|-------------------------------------------------------------------|
| §23-3             | §26-2            | Per-issue trade-execution-method change — parent VI article (Dynamic at §23-3.1.1, Static at §23-3.1.2) |
| §18               | §23              | Single-price auction — referenced as the matching method during VI cool-off |
| §23-2             | §106-2           | Short-term overheat designation — referenced for the overheat exclusion |
| §26               | §25              | Index-level CB — referenced for CB precedence (covered in [Circuit Breakers (KOSDAQ)](./circuit_breakers.md)) |

KOSDAQ §23-3.1 enumerates two cases that mirror KOSPI §26-2.1 word-for-word:

1. §23-3.1.1 — *"정규시장의 매매거래시간(시가 결정시를 제외한다) 및 시간외시장(시간외단일가매매에 한한다)의 매매거래시간 중에 해당 호가 접수시점의 직전의 가격을 기준으로 세칙에서 정한 비율 이상 상승 또는 하락하는 경우"* — Dynamic VI: tentative price moves ≥ ER-set rate from "the immediately preceding price" (직전의 가격, *jik-jeon-ui ga-gyeok*).
2. §23-3.1.2 — *"정규시장의 매매거래시간 중에 해당 호가 접수시점의 직전의 가격(제18조에 따라 단일가격에 의한 개별경쟁매매의 방법으로 결정된 가격에 한하며, 시가 결정시에는 당일의 기준가격을 말한다)을 기준으로 세칙에서 정한 비율 이상 상승 또는 하락하는 경우"* — Static VI: tentative price moves ≥ ER-set rate from "the last single-price-determined price (or the day's base price before the opening determines)."

### Delta vs KOSPI

#### Effective rate buckets — KOSDAQ stocks land in the 6 % bucket

The KOSPI rate split (3 % for KOSPI 200 constituent shares, 6 % for "other shares") implies, on KOSDAQ, that **virtually all common-equity issues fall into the 6 % bucket**. KOSPI 200 is by definition a KOSPI-listed-issue index, so a KOSDAQ-listed common share is not a KOSPI 200 constituent. The KOSDAQ tour [KRX-TOUR-KOSDAQ-OPS-T7] preserves the same rate-table structure with the same labels, but the practical outcome is:

- **KOSDAQ common shares (KOSDAQ 150 constituents and others alike):** 6 % continuous / 4 % closing / 6 % off-hours.
- **KOSDAQ-listed ETFs / ETNs tracking KOSPI 200 / 100 / 50, KRX 100, inverse, or debt indices** (rare in practice — most KOSPI 200 ETFs are KOSPI-listed): 3 % / 2 % / 3 %.
- **KOSDAQ-listed ETFs / ETNs tracking KOSDAQ 150, sector / foreign / commodity indices, or with leverage |k| > 1:** 6 % / 4 % / 6 %.

Note that **KOSDAQ 150 itself is not in the 3 % bucket** per the KOSDAQ tour table — KOSDAQ-150-tracking ETFs sit in the 6 % bucket. The 1 % derivatives-expiry tightening, by contrast, **does** apply to KOSDAQ 150 (= "KOSTAR index" historically) constituents on the closing call of the derivatives-expiry day per the tour footnote — so KOSDAQ-150-constituent common shares get the 1 % cone on the closing call of KOSPI 200 / KOSDAQ 150 futures-options expiry days, even though their continuous rate is 6 %.

For an execution algo, this means:

- A simple "VI rate = 3 % if KOSPI 200 else 6 %" classifier is correct for KOSDAQ as a fallback.
- The derivatives-expiry-day closing-call tightening must be evaluated against the KOSDAQ 150 constituent set, not just the KOSPI 200 set.
- A typical KOSDAQ name with intraday volatility ~5 % will still fire Dynamic VI (5 % > the 6 % rule? **no — 5 % < 6 %**, so no Dynamic VI fires). Re-checking: with the 6 % rate, a 5 % move from the immediately preceding trade does **not** fire Dynamic VI — KOSDAQ Dynamic VI is **less sensitive** than KOSPI 200's 3 % cone, mirroring the typical higher-volatility profile of small-cap KOSDAQ issues.

#### KOSDAQ-only — Price-disparity cooling-off for preferred / new / SIC stocks (3-day halt)

[KRX-TOUR-KOSDAQ-OPS-T5] — titled "VI for preferred / new stocks (price-disparity cooling-off)" — describes a separate trading-halt mechanism not part of the §23-3 VI framework:

> If the base prices of preferred stocks, new stocks and securities investment companies are **200 % or higher** than the each price in comparison (base price of common stocks for preferred stocks; base price of common stocks for new stocks; their net asset values for securities investment companies) **and** preferred stocks, new stocks and securities investment companies are already designated or about to be designated the next day as price-surged stocks → **3 days of trading halt**.

Continuation behavior:

- After the 3-day halt is lifted, **if the price-divergence is still ≥ 200 % from the new comparable price** computed 3 trading days after lift-off **and** the issue rises ≥ 20 % over those 3 days → **another 3-day halt**.
- The cycle repeats until the divergence falls below 200 %.

Exceptions:

- Stock-split / reverse-split / spin-off / merger-after-spin-off / merger-between-listed-corporations: **between 4 to 2 trading days before the deadline for stock-certificate submission**, the divergence rule is suspended.
- Ex-dividend / ex-rights: **between 4 to 2 trading days before the base date**, the divergence rule is suspended.

This is **KOSDAQ-only** — KOSPI does not have a parallel 3-day-halt mechanism for preferred / new / SIC stocks at the 200 % divergence threshold. The KOSPI §41-2.4.2-4 exclusion list does carve out "preferred-share single-price issues (§56-4.1)" from VI, but the KOSPI mechanism for those is a single-price-only trading mode, not a 3-day halt.

For an execution algo running across both markets, this means:

- A KOSDAQ preferred share trading at >2× its common-share base price, especially during a price-surge designation window, can disappear from the order book for 3 trading days at a time. A passive-resting strategy must be aware of this — orders survive the halt but cannot fill until trading resumes.
- The exception windows around corporate-action submission deadlines (4 to 2 days before) and ex-dates need calendar-aware filtering before relying on price-disparity-halt timing.
- The KOSDAQ Enforcement Rule analogue of this rule has not yet been pulled — R6 unresolved. Numeric thresholds (200 %, 20 %, 4-to-2 day windows) are flagged for re-verification at R6 / Phase 6.

#### Derivatives-expiry tightening — also covers KOSDAQ 150 constituents

The KOSPI §41-2.1 proviso 2 reduces the closing-call dynamic rate to 1 % for the underlying assets of equity-related derivatives on the last trading day of those derivatives. The KOSDAQ tour footnote 1 confirms the **same 1 % rate** applies on KOSDAQ for "constituents of KOSPI200, **KOSTAR index** [= KOSDAQ 150], Sector indices, underlying stock of individual stock futures and options" [KRX-TOUR-KOSDAQ-OPS-T7]. So the derivatives-expiry-day tightening is a cross-market concept anchored on the underlying-stock side, not the listing-side: a KOSDAQ-150 constituent gets 1 % on its KOSDAQ closing call, just as a KOSPI 200 constituent gets 1 % on its KOSPI closing call.

The "KOSTAR" naming in the KOSDAQ tour is historical — the index was renamed from "KOSTAR" to "KOSDAQ 150" in 2015. Treat the two names as synonymous in this rule context.

#### Exclusions — abbreviated tour list vs full ER list

The KOSDAQ tour [KRX-TOUR-KOSDAQ-OPS-T7] enumerates only two exclusions:

> Issues scheduled to be delisted and temporary overheated issues

This is a tour-page abbreviation. The full §41-2.4 exclusion list — liquidation, overheat, abnormal-rise single-price, investment-warning, low-liquidity / preferred-share single-price, newly-listed listing-day (since 2021-10-18), within-day halt resumption, cascading VI suppression, small-stock 3-tick filter, KRX discretion — is believed to apply on KOSDAQ verbatim because the §23-3 framework delegates to the Enforcement Rule for the exclusion-set definition. KOSDAQ ER (R6) not yet archived; treat all 10 KOSPI exclusions as applicable until R6 confirms otherwise.

## Parameters & thresholds

### Table 1 — VI rates by category and session (KOSDAQ)

Per [KRX-TOUR-KOSDAQ-OPS-T7]:

| Category                                                                 | Continuous (09:00–15:20) | Closing call (15:20–15:30) | Off-hours single-price (16:00–18:00) | Source                              |
|--------------------------------------------------------------------------|-------------------------:|---------------------------:|-------------------------------------:|-------------------------------------|
| Dynamic — KOSPI 200 constituent shares (KOSPI-listed only — rare on KOSDAQ books) |             3 %   |                       2 %  |                              3 %     | [KRX-TOUR-KOSDAQ-OPS-T7]            |
| Dynamic — Underlying of derivatives products on derivatives-expiry-day closing call (KOSPI 200, KOSDAQ 150 / KOSTAR, sector indices, single-stock-derivative underlyings) | n/a |                       1 %  |                              n/a     | [KRX-TOUR-KOSDAQ-OPS-T7 fn. 1]      |
| Dynamic — Other shares (= virtually all KOSDAQ-listed common equity)     |                    6 %   |                       4 %  |                              6 %     | [KRX-TOUR-KOSDAQ-OPS-T7]            |
| Dynamic — ETF / ETN linked 1× (incl. inverse) to KOSPI 200 / 100 / 50, KRX 100, debt indices |        3 %   |                       2 %  |                              3 %     | [KRX-TOUR-KOSDAQ-OPS-T7]            |
| Dynamic — Other ETF / ETN (KOSDAQ 150-tracking, sector, foreign, commodity, leveraged) |             6 %   |                       4 %  |                              6 %     | [KRX-TOUR-KOSDAQ-OPS-T7]            |
| Static — all eligible (vs last single-price-determined price)            |                   10 %   |                      10 %  |                              n/a     | [KRX-TOUR-KOSDAQ-OPS-T7]            |

Static VI is not applied during off-hours single-price (16:00–18:00).

### Table 2 — KOSDAQ-only price-disparity cooling-off

Per [KRX-TOUR-KOSDAQ-OPS-T5]:

| Parameter                                | Value                                                       | Source                              |
|------------------------------------------|-------------------------------------------------------------|-------------------------------------|
| Trigger                                   | Issue base price ≥ **200 %** of comparable price            | [KRX-TOUR-KOSDAQ-OPS-T5]            |
| Comparable price (preferred shares)      | Common-stock base price                                     | [KRX-TOUR-KOSDAQ-OPS-T5]            |
| Comparable price (new stocks)            | Common-stock base price                                     | [KRX-TOUR-KOSDAQ-OPS-T5]            |
| Comparable price (SIC = securities investment company) | Net asset value                                | [KRX-TOUR-KOSDAQ-OPS-T5]            |
| Eligibility precondition                  | Issue is designated or about-to-be-designated as a price-surged stock | [KRX-TOUR-KOSDAQ-OPS-T5]   |
| Halt duration                             | **3 trading days**                                          | [KRX-TOUR-KOSDAQ-OPS-T5]            |
| Continuation cycle                        | After lift-off, if divergence ≥ 200 % and price rises ≥ 20 % over the next 3 trading days, another 3-day halt | [KRX-TOUR-KOSDAQ-OPS-T5] |
| Exception window — corporate actions       | 4 to 2 trading days before stock-certificate submission deadline | [KRX-TOUR-KOSDAQ-OPS-T5]      |
| Exception window — ex-dividend / ex-rights | 4 to 2 trading days before the base date                    | [KRX-TOUR-KOSDAQ-OPS-T5]            |

### Table 3 — Reference prices

| VI type    | Phase                                  | Reference price                                                  | Source                                                |
|------------|----------------------------------------|------------------------------------------------------------------|-------------------------------------------------------|
| Dynamic    | Before opening print                   | Day's base price (기준가격)                                       | [KRX-TOUR-KOSDAQ-OPS-T7]                              |
| Dynamic    | After opening print, intraday          | Immediately preceding trade price (직전의 가격)                   | [KRX-RULE-KOSDAQ-BR-KO §23-3.1.1]                     |
| Static     | Before opening print                   | Day's base price                                                  | [KRX-TOUR-KOSDAQ-OPS-T7]                              |
| Static     | After opening print                    | Most recent single-price-determined price                         | [KRX-RULE-KOSDAQ-BR-KO §23-3.1.2]                     |

### Table 4 — Action and timing

| Mechanism            | Trigger condition (tentative price vs reference)            | Action                                                       | Duration                       |
|----------------------|--------------------------------------------------------------|---------------------------------------------------------------|--------------------------------|
| VI from continuous   | |Δ| ≥ rate × reference                                       | Switch to single-price (§18) for the §35.1.4 receipt window  | 2 minutes                      |
| VI from single-price | |Δ| ≥ rate × reference                                       | Extend single-price participation window by 2 minutes        | 2 minutes (additional)         |
| Random-end on resumption | n/a                                                      | None — VI auctions do not carry the §35.1 random-end          | n/a                            |

Source for the duration: [KRX-TOUR-KOSDAQ-OPS-T7] ("orders received for 2 minutes are matched by a single price auction"); KOSDAQ ER analogue of KOSPI ER §41-2.3 / §35.1.4 unresolved (R6).

## Worked examples

### Example A — Dynamic VI on a typical KOSDAQ stock (6 % rate)

A non-KOSDAQ-150 KOSDAQ-listed stock has last traded at **KRW 50,000** at 13:30. At 13:31 a buy-market quote sweeps the book, generating a tentative match price of **KRW 53,500**. The KOSDAQ Dynamic VI rate for "Other shares" in continuous mode is **6 %**.

- Trigger threshold: 50,000 × 1.06 = 53,000. Tentative 53,500 ≥ 53,000 → **Dynamic VI fires** [KRX-RULE-KOSDAQ-BR-KO §23-3.1.1].
- Action: continuous → single-price call for 2 minutes [KRX-RULE-KOSDAQ-BR-KO §23-3 + §18].
- Receipt window: 13:31–13:33. All orders received in the window participate.
- At 13:33 the call clears at, say, **KRW 52,700**. Continuous trading resumes immediately. The "last single-price-determined price" for Static VI now becomes 52,700.

Contrast with KOSPI Example A: a KOSPI 200 constituent uses 3 %, so the same 7 % move at 13:31 would have fired KOSPI 200 Dynamic VI at much smaller absolute moves. The 6 % vs 3 % rate split makes typical KOSDAQ Dynamic VI events **less frequent** per unit of absolute price move than KOSPI 200 events.

### Example B — Static VI is the same 10 % everywhere

A KOSDAQ stock opens at **KRW 10,000** at 09:00. By 11:00 the price has drifted upward via small Dynamic-VI-not-firing trades to a tentative print of **KRW 11,050**. Dynamic VI compares to the immediately preceding price (≈ 10,990) — Δ = 60 = 0.55 % — does not fire (well under 6 %). Static VI compares to the last single-price-determined price (10,000):

- Static threshold: 10,000 × 1.10 = 11,000. Tentative 11,050 ≥ 11,000 → **Static VI fires**.
- Action: switch to single-price for 2 minutes.
- At 11:02 the call clears at, say, **KRW 11,020**. The new "last single-price-determined price" becomes 11,020 — Static VI's next threshold is 11,020 × 1.10 = 12,122.

Same outcome as KOSPI Example B because Static VI's 10 % rate is identical across markets. The dynamics of cumulative-drift detection are unchanged on KOSDAQ.

### Example C — KOSDAQ-only preferred-share price-disparity cooling-off

A KOSDAQ-listed preferred share has base price **KRW 100,000**. The corresponding common share's base price is **KRW 40,000**. The preferred is trading at base price = 250 % of common (= 100,000 / 40,000), and the issue is on the price-surge designation list. Per [KRX-TOUR-KOSDAQ-OPS-T5]:

- Divergence ≥ 200 % → preconditions met.
- KRX imposes a **3-trading-day halt** on the preferred share.
- During the halt, no quotations match for the preferred (passive resting orders survive but do not fill).
- After the 3-day lift-off, on each successive 3-trading-day window: if the divergence is still ≥ 200 % **and** the preferred has risen ≥ 20 % over those 3 days, another 3-day halt fires.
- The cycle continues until the divergence drops below 200 % for a full 3-day window without a 20 %+ surge.

This is the **only** KOSDAQ mechanism that produces a multi-day issue-level halt outside the index-level CB framework; KOSPI does not have a parallel mechanism (KOSPI carves out preferred-share single-price issues from VI but does not impose multi-day halts at the 200 % divergence threshold).

## Edge cases & open questions

- Edge case: KOSDAQ tour [KRX-TOUR-KOSDAQ-OPS-T7] uses "KOSPI200 constituents" as a row label even though no KOSPI 200 stock is KOSDAQ-listed. This row is operationally defined for ETF / ETN linkage, not for direct equity classification on KOSDAQ. A KOSDAQ-stock-row reader of the tour table should always pick the "Others stocks" row (6 % / 4 % / 6 %) for equity issues.
- Edge case: KOSDAQ 150 constituents are **not** in the 3 % rate bucket per the tour table — they sit in the 6 % bucket alongside other KOSDAQ stocks. But on derivatives-expiry days, the KOSDAQ-150-constituent rate **is** tightened to 1 % for the closing call (per the tour footnote). So a KOSDAQ-150 constituent sees 6 % continuous → 4 % closing on most days, and 6 % continuous → 1 % closing on the second-Thursday of each KOSPI 200 / KOSDAQ 150 derivatives delivery month.
- Edge case: The KOSDAQ-only price-disparity cooling-off [KRX-TOUR-KOSDAQ-OPS-T5] is a tour-page-only source — the corresponding article in the KOSDAQ Business Regulation has not been pinpointed. The KOSDAQ §23 chapter handles 정리매매종목, 단기과열종목, and 시장감시규정 referrals; the price-disparity 3-day-halt may be in the §25 / §26 area (individual-issue trading halts) or in the §50 area (market-administration). Cross-check at R6 / Phase 6.
- Edge case: The KOSDAQ-only price-disparity rule's 4-to-2-day exception window for corporate actions creates a calendar-aware suspension band. An algo holding a passive bid on a preferred share during the rule's exception window must still respect the underlying corporate-action timing — the halt is suspended, not the trade-affecting corporate action itself.
- Edge case: KOSDAQ §23-3 applies to "주권, 외국주식예탁증권 및 기업성장집합투자기구 집합투자증권" (shares, foreign DRs, and corporate-growth-investment-fund securities — added 2026-03-04). KOSPI §26-2 has "주권, 외국주식예탁증권, 상장지수집합투자기구 집합투자증권, 상장지수증권 등" (shares, foreign DRs, ETFs, ETNs, etc.). The KOSDAQ §23-3 enumeration is narrower; KOSDAQ-listed ETFs / ETNs presumably get VI via the Enforcement Rule's ER §41-2.1.2 analogue rather than §23-3 directly. Cross-check at R6.
- Open question: The KOSDAQ Enforcement Rule analogue of KOSPI ER §41-2.4.2-5 (newly-listed-on-listing-day VI exclusion, added 2021-10-18) is not yet citable. KOSDAQ-METHOD-T4 establishes that newly-listed KOSDAQ stocks trade in a 60 %–400 % day-1 band — which in itself implies VI cannot meaningfully fire on day 1, since the 6 % continuous threshold sits well inside the 60 %–400 % range. But whether the explicit exclusion is in the KOSDAQ ER mirroring KOSPI's needs R6 confirmation.
- Open question: KOSDAQ-OPS-T5 is dated by the project tour fetch (2026-04-30) but the rule itself may have been amended without the tour reflecting the change. The "KOSTAR" historical naming and the tour's preserved 200 %/20 %/3-day cycle parameters suggest the tour was last updated some years ago. Phase 6 freshness audit should reconcile against the latest KRX press releases on price-disparity-halt thresholds.

## Sources

- `KRX-RULE-KOSDAQ-BR-KO` — KOSDAQ Market Business Regulation (코스닥시장 업무규정), bookid 210164370, effective 2026-04-28. Articles cited: §18 (Single-price auction — referenced as the matching method during VI cool-off), §23-2 (Short-term overheat designation — referenced for the overheat exclusion), §23-3 (Per-issue trade-execution-method change — the parent VI article: §23-3.1.1 Dynamic, §23-3.1.2 Static), §26 (Index-level CB — referenced for CB precedence; full coverage in [Circuit Breakers (KOSDAQ)](./circuit_breakers.md)).
- `KRX-TOUR-KOSDAQ-OPS-T7` — KRX overview "Volatility Interruption (VI)" (KOSDAQ); English, not authoritative. Used for the rate-table by category and session, the Dynamic / Static framing matching KOSPI, the 2-minute cool-off duration, the applied-session list, the 1 % derivatives-expiry footnote (which extends the tightening to KOSPI 200 + KOSTAR / KOSDAQ 150 + sector + single-stock-derivative underlyings), the no-daily-cap-on-VI-events claim, and the CB-cancels-VI / VI-blocks-VI overlap rules.
- `KRX-TOUR-KOSDAQ-OPS-T5` — KRX overview "VI for preferred / new stocks (price-disparity cooling-off)" (KOSDAQ); English, not authoritative. **Sole source** for the KOSDAQ-only 200 %-divergence + 3-day-halt mechanism for preferred / new / SIC stocks, the 20 %-rise continuation cycle, and the corporate-action / ex-date exception windows (4 to 2 trading days before submission deadline / base date). The corresponding KOSDAQ Business Regulation article has not yet been pinpointed; flagged for R6 / Phase 6 audit.
