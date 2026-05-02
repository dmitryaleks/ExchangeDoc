---
title: "Price Ranges & Tick Sizes (KOSDAQ)"
markets: [KOSDAQ]
last_reviewed: 2026-05-01
sources:
  - KRX-RULE-KOSDAQ-BR-KO
  - KRX-TOUR-KOSDAQ-BASIC
  - KRX-TOUR-KOSDAQ-METHOD-T2
  - KRX-TOUR-KOSDAQ-METHOD-T3
  - KRX-TOUR-KOSDAQ-METHOD-T4
---

> See also: [Price Ranges & Tick Sizes (KOSPI)](../kospi/price_ranges.md), [Auctions (KOSDAQ)](./auctions.md), [Order Types (KOSDAQ)](./order_types.md), [Comparison](../common/comparison.md).

**Delta file.** KOSDAQ price-range substance is **identical to KOSPI**: same ±30 % daily band, same 60 %–400 % day-1 newly-listed band, same 7-band tick-size schedule, same base-price formulas including the corporate-action / split / ex-dividend / cash-distribution cases, same opening-price-base method, and the same priority equivalence (with execution divergence) for limit-at-limit vs market orders. The deltas are structural — article numbering and the §14.1 security-enumeration scope — plus an R6 citation gap. This file points to the [KOSPI write-up](../kospi/price_ranges.md) for shared content.

## Summary

- Daily price band is **±30 %** of the base price (기준가격, *gi-jun-ga-gyeok*); 상한가 (*sang-han-ga*; upper limit) and 하한가 (*ha-han-ga*; lower limit) are the band edges [KRX-RULE-KOSDAQ-BR-KO §14.1–14.2; KRX-TOUR-KOSDAQ-METHOD-T2].
- Tick size (호가가격단위, *ho-ga-ga-gyeok dan-wi*) follows the identical KOSPI 7-band schedule (KRW 1 below 2,000 → KRW 1,000 at and above 500,000) [KRX-TOUR-KOSDAQ-BASIC]. The KOSDAQ Business Regulation §15 delegates the tick / quote-quantity / trading-lot units to the Enforcement Rule (R6 unresolved — see PROJECT_IMPLEMENTATION.md).
- Trading lot (매매수량단위, *mae-mae su-ryang dan-wi*) is **1 share / 1 certificate** for all instruments per [KRX-TOUR-KOSDAQ-BASIC]. The ELW 10-cert lot exception that exists on KOSPI applies only to KOSPI-listed ELWs — KOSDAQ does not have a parallel ELW listing, so the exception is moot here.
- Newly-listed common share day-1 band is **60 %–400 %** of the base price (= public offering price); from day 2 the issue reverts to the default ±30 % band [KRX-TOUR-KOSDAQ-METHOD-T4]. Identical to KOSPI.
- Liquidation issues (정리매매종목, *jeong-ri mae-mae jong-mok*) trade with no price limit per [KRX-RULE-KOSDAQ-BR-KO §23.2]. Identical to KOSPI.

## Detailed rules

For full prose on the band-calculation arithmetic, the up / down asymmetric tick-rounding (上한가 rounds down, 下한가 rounds up at the new-price-level tick), the corporate-action base-price formulas, the opening-price-base method, the limit-at-limit vs market-order priority-equivalence-but-execution-divergence rule, and the leveraged ETF / ETN multiplier scaling, see [KOSPI § Detailed rules](../kospi/price_ranges.md#detailed-rules). The KOSDAQ articles map directly:

| KOSDAQ BR article | KOSPI BR article | Topic                                                    |
|-------------------|------------------|----------------------------------------------------------|
| §14               | §20              | Daily price-limit band — ±30 % default + extraordinary override |
| §15               | §21              | Tick / quote-quantity / trading-lot units (delegated to Enforcement Rule) |
| §17.2.1           | §22.2.1          | Limit-at-limit vs market order — same price priority      |
| §23.2             | §20.3            | Liquidation issues — no price-limit band                  |

KOSDAQ Enforcement Rule article numbers for the granular cases (base-price formula in Annex 1-4, tick-size schedule, day-1 +300 % / -60 % band, opening-price-base 1 KRW–300 % auction band) cannot be cited authoritatively until R6 resolves. KOSDAQ-METHOD-T4 explicitly references "Annex 1-4 of the Enforcement Rules of the KOSDAQ Market Business Regulation," confirming that the KOSDAQ Enforcement Rule exists and has the same Annex structure as KOSPI.

### Delta vs KOSPI

#### Article-numbering remap

The KOSPI BR uses §20 / §21 for price-limit and tick-size; the KOSDAQ BR uses **§14 / §15** for the same content. Inside the KOSDAQ BR, all cross-references use the §14 / §15 numbering.

#### §14.1 enumerated-securities scope (narrower than KOSPI §20.1)

KOSDAQ §14.1 explicitly applies the price-limit band to "**주권, 외국주식예탁증권 및 기업성장집합투자기구 집합투자증권**" (*ju-gwon, oe-guk ju-sik ye-tak jeung-gwon mit gi-eop-seong-jang ji-pap-tu-ja-gi-gu ji-pap-tu-ja-jeung-gwon*; shares, foreign DRs, and corporate-growth-investment-fund collective-investment securities — added 2026-03-04). KOSPI §20.1 also lists ETFs (상장지수집합투자기구 집합투자증권), ETNs (상장지수증권), and beneficiary certificates (수익증권) explicitly. The KOSDAQ §14.1 enumeration is narrower:

- **Implication for KOSDAQ ETF / ETN price-limit band.** KOSDAQ-listed ETFs and ETNs are governed by the KOSDAQ Enforcement Rule (R6 unresolved) rather than the BR §14.1 enumeration. The substance is believed to be the same ±30 % default band with the same leverage-multiplier scaling, but this cannot yet be authoritatively cited. Cross-check at R6 resolution.
- **Implication for §14.3 extraordinary override.** §14.3 ("시장상황급변 등 세칙이 정하는 경우에는 호가의 가격제한폭을 달리 정할 수 있다"; *si-jang sang-hwang geup-byeon deung se-chik-i jeong-ha-neun gyeong-u-e-neun ho-ga-ui ga-gyeok-je-han-pok-eul dal-li jeong-hal su it-da*; "in cases of abrupt market change or other situations as defined by the Enforcement Rule, the price-limit band may be set differently") matches KOSPI §20.4 verbatim. Same authority, same Enforcement-Rule delegation, same scope.

#### Day-1 newly-listed band (identical, but tour-sourced)

KOSDAQ tour [KRX-TOUR-KOSDAQ-METHOD-T4] confirms the **60 %–400 %** day-1 band with the public offering price as the base (per Annex 1-4 of the Enforcement Rule). The 30 s random-end of the opening single-price auction also applies to the newly-listed first-price determination [KRX-TOUR-KOSDAQ-METHOD-T4]. The tour notes that the historical "Opening Price Method" (시가기준가종목 — first-trade-becomes-base) is no longer applied to typical IPOs after the FSC's "Measures to Improve soundness of IPO Market"; it remains in use for capital-reduction relistings, listing-change-after-spin-off, and similar where a theoretical price cannot be calculated [KRX-TOUR-KOSDAQ-METHOD-T4]. Same regime as KOSPI.

#### Liquidation-issue carve-out (identical wording)

KOSDAQ §23.2 — "정리매매종목에는 호가의 가격제한폭을 두지 아니한다" — matches KOSPI §20.3 word-for-word in its core directive. The 7-day liquidation window with 14 × 30-min single-price auctions per day is set in the KOSDAQ Enforcement Rule (R6 unresolved); KOSPI's analogue is in Enforcement Rule §56. See [KOSPI Other Topics § Liquidation issues](../kospi/other_topics.md#liquidation-issues) for the operational mechanics.

## Parameters & thresholds

### Tick-size schedule (KOSDAQ)

Per [KRX-TOUR-KOSDAQ-BASIC], for ordinary shares (formal authority pending R6 resolution):

| Price band (KRW)              | Tick (KRW) |
|-------------------------------|-----------:|
| under 2,000                   |          1 |
| 2,000 – under 5,000           |          5 |
| 5,000 – under 20,000          |         10 |
| 20,000 – under 50,000         |         50 |
| 50,000 – under 200,000        |        100 |
| 200,000 – under 500,000       |        500 |
| 500,000 and above             |      1,000 |

**Identical to KOSPI 7-band schedule.** ETF / ETN / ELW-specific schedules are not enumerated in the KOSDAQ tour; on KOSPI the ETF / ETN schedule is a 2-band (KRW 1 / KRW 5) and ELWs are flat at KRW 5 [KRX-RULE-KOSPI-BR-ENFORCE-KO §32.2.2, §32.2.3]. KOSDAQ ETF / ETN schedules are believed to be the same structure but cannot be authoritatively cited until R6 resolves.

### Trading lot (매매수량단위)

| Instrument                              | Trading lot |
|-----------------------------------------|------------:|
| Ordinary share (주권)                    |     1 share |
| Foreign DR (외국주식예탁증권)             |      1 cert |
| ETF / ETN (KOSDAQ-listed)                |     1 share / 1 cert |
| Subscription right cert / warrant        |      1 cert |
| Corporate-growth-investment-fund security |     1 unit |

Source: [KRX-TOUR-KOSDAQ-BASIC] ("Trading lots in KOSDAQ market is 1 share (1 certificate)"); R6 confirmation pending. KOSDAQ does not list ELWs separately, so the KOSPI 10-cert ELW lot exception does not arise here.

### Daily price-limit band

| Issue category                                     | Upper                | Lower                | Source                                                                |
|----------------------------------------------------|----------------------|----------------------|-----------------------------------------------------------------------|
| Default (shares, foreign DRs, investment-fund securities) | base × 1.30   | base × 0.70          | [KRX-RULE-KOSDAQ-BR-KO §14.1–14.2]                                    |
| ETFs / ETNs (KOSDAQ-listed)                        | base × 1.30 (default) | base × 0.70 (default) | KOSDAQ Enforcement Rule analogue (R6 unresolved); per [KRX-TOUR-KOSDAQ-METHOD-T2] same 30 % calculation |
| Newly-listed common share — day 1                  | base × 4.00 (+300 %)  | base × 0.40 (–60 %)   | [KRX-TOUR-KOSDAQ-METHOD-T4]                                           |
| Liquidation issue (정리매매종목)                    | unlimited            | unlimited (down to KRW 1 minimum tick) | [KRX-RULE-KOSDAQ-BR-KO §23.2]                          |
| Long-closure resumption / extraordinary            | per KRX notice       | per KRX notice       | [KRX-RULE-KOSDAQ-BR-KO §14.3]                                         |

The upper-limit calculation rounds **down** to the nearest tick at the new price level; the lower-limit calculation rounds **up**. Same asymmetric rounding as KOSPI; per [KRX-TOUR-KOSDAQ-METHOD-T2] the band is computed at the base-price-level tick, and any residual sub-tick is dropped before the upper / lower addition.

### Base-price determination — selected cases

Per [KRX-TOUR-KOSDAQ-METHOD-T3] (with R6 ER citations pending):

| Case                                                  | Base price                                                              |
|-------------------------------------------------------|-------------------------------------------------------------------------|
| Default (existing listed issue, traded yesterday)      | Previous day's closing price                                            |
| No trade on previous day                              | Previous day's special quotation if better than base — lowest sell or highest buy quote; otherwise previous day's base price |
| Newly listed common share                             | Public offering price (per Enforcement Rule Annex 1-4)                  |
| Stock split / reverse split                           | Previous close × split-or-merge ratio (round up to tick)                 |
| Ex-rights — capital increase with consideration       | [(cum-right price × pre-issue shares) + (issue price × allotted shares)] / post-issue shares |
| Ex-rights — capital increase without consideration    | Same formula with issue price = 0                                        |
| Ex-dividend                                           | (cum-dividend price × pre-issue shares) / post-issue shares; only for issuers that disclosed a stock-dividend plan |
| Mutual-fund cash distribution resumption              | If per-share distribution < last price of T−2: subtract; else: orders accepted from KRW 1 to T−2 last price as the reopening band |
| Issue under opening-price-base method                 | Day's first single-price-auction trade; if no trade by close, evaluation price per Annex 1 |

Same case structure and same formulas as KOSPI [KRX-RULE-KOSPI-BR-ENFORCE-KO §30].

## Worked examples

### Example A — daily price limit calculation (KOSDAQ)

(From [KRX-TOUR-KOSDAQ-METHOD-T2], adapted.)

Base price = KRW 9,940. Per [KRX-RULE-KOSDAQ-BR-KO §14.2]:

1. 9,940 × 0.3 = KRW 2,982.
2. The tick at the base-price level (≥ 5,000 < 20,000) is KRW 10. Round 2,982 down to KRW 2,980.
3. 상한가 = 9,940 + 2,980 = KRW 12,920 (already on tick).
4. 하한가 = 9,940 − 2,980 = KRW 6,960 (already on tick).

The same calculation against a base of KRW 9,980 (KOSPI tour example) yields band 2,990 → upper 12,970 / lower 6,990. The two examples confirm the algorithm is identical; only the base inputs differ between the tours.

### Example B — newly-listed common share, day 1 (KOSDAQ)

A common share lists on KOSDAQ with public offering price = KRW 10,000 (so base = KRW 10,000 per [KRX-TOUR-KOSDAQ-METHOD-T4]). Day-1 limits per [KRX-TOUR-KOSDAQ-METHOD-T4] ("Within the range of 60 % and 400 % based on the base price"):

- Upper-band amount = 10,000 × 3 = 30,000 → 상한가 = 10,000 + 30,000 = **KRW 40,000** (= 400 % of base).
- Lower-band amount = 10,000 × 0.4 = 4,000 → 하한가 = 10,000 − 4,000 = **KRW 6,000** (= 60 % of base).
- Day-1 trading band: **KRW 6,000 to KRW 40,000** (60 %–400 % of base).

The asymmetric language "+300 % / −60 %" describes the *band amounts* (upper-band 3× base; lower-band 0.4× base), not the floor / ceiling levels — the trading band itself is 60 %–400 % of base. From day 2 the issue reverts to the default ±30 % band [KRX-RULE-KOSDAQ-BR-KO §14.2]. Same arithmetic and same outcome as the [KOSPI Example B](../kospi/price_ranges.md#example-b-newly-listed-common-share-day-1).

### Example C — limit-at-limit vs market order

The KOSPI worked example in [KOSPI § Worked examples](../kospi/price_ranges.md#example-c-limit-at-limit-vs-market-order-in-a-single-price-auction) carries over to KOSDAQ unchanged because KOSDAQ §17.2.1 (price-priority equivalence at limit) mirrors KOSPI §22.2.1.

## Edge cases & open questions

- Edge case: KOSDAQ §14.1 narrower enumeration vs KOSPI §20.1 means KOSDAQ-listed ETF / ETN price-limit citations need the KOSDAQ Enforcement Rule. Until R6 resolves, treat KOSDAQ ETF / ETN ±30 % bands as inferred-by-tour rather than authoritatively cited.
- Edge case: §31.3-equivalent rule reads as "+300 % upper / −60 % lower" in KRX language but the actual band-amount formula is upper-band = 3× base and lower-band = 0.4× base — yielding floor / ceiling at 60 % / 400 % of base. The asymmetric "0.4 multiplier" on the lower side describes the *band amount subtracted*, not the floor level. Easy to mis-read on a first pass; both the KOSPI and KOSDAQ tour pages (and the corresponding worked examples) use the "60 %–400 % of base" framing.
- Edge case: The KOSDAQ-tour 7-band tick schedule [KRX-TOUR-KOSDAQ-BASIC] is presented for ordinary shares. Whether the schedule applies to ETF / ETN (KOSPI uses a 2-band schedule for those) or to corporate-growth-investment-fund securities (added 2026-03-04, no parallel on KOSPI) is not stated in the tour. R6 resolution is needed for these ETF / ETN-specific tick schedules and for the new investment-fund security class.
- Edge case: The KOSDAQ-METHOD-T4 tour confirms the 30 s random-end of the opening auction also applies to newly-listed first-price determination — same as KOSPI Enforcement Rule §67-2. The KOSDAQ analogue article in the Enforcement Rule cannot yet be cited (R6).
- Open question: KOSDAQ §23.2's "no price-limit band for liquidation issues" inherits the same minimum-tick floor (KRW 1) as KOSPI — but the smallest-tick floor is set by §15-delegated Enforcement-Rule article and cannot be cited authoritatively until R6 resolves. Practical effect is unchanged: a KOSDAQ liquidation issue cannot trade below KRW 1.
- Open question: The §14.3 extraordinary-situation override has been used by KOSPI in the past (e.g. 2020-03-13 limited-tick widening during COVID volatility, 2022-09-30 short-sale-restriction lift). Whether KOSDAQ has a parallel set of historical invocations should be cross-checked before any historical-data analysis that depends on which days the band was non-standard.
- Open question: The 2026-03-04 addition of "기업성장집합투자기구 집합투자증권" (corporate-growth-investment-fund collective-investment securities) to KOSDAQ §14.1 is novel — these securities don't exist on KOSPI. Whether they have any special price-limit treatment (e.g. tighter or looser than ±30 %, or different base-price formula for the fund-NAV anchor) is not visible in the BR text alone. Cross-check the Enforcement Rule and the Listing Regulation at R6 / Phase 6.

## Sources

- `KRX-RULE-KOSDAQ-BR-KO` — KOSDAQ Market Business Regulation (코스닥시장 업무규정), bookid 210164370, effective 2026-04-28. Articles cited: §14 (Daily price-limit band — ±30 %, narrower §14.1 enumeration than KOSPI §20.1; §14.3 extraordinary override delegated to Enforcement Rule), §15 (Tick / quote-quantity / trading-lot units — fully delegated to Enforcement Rule), §17.2.1 (price priority for market vs limit at limit), §23.2 (No price-limit band for liquidation issues).
- `KRX-TOUR-KOSDAQ-BASIC` — KRX overview "Basic Facts about Trading System" (KOSDAQ); English, not authoritative. Used for the 7-band tick-size schedule (matching KOSPI verbatim) and the 1-share / 1-cert trading-lot statement.
- `KRX-TOUR-KOSDAQ-METHOD-T2` — KRX overview "Base Price" (KOSDAQ); English, not authoritative. Used for the 30 % price-limit calculation language and the worked-example base 9,940 → band 2,980 calculation.
- `KRX-TOUR-KOSDAQ-METHOD-T3` — KRX overview "Calculation of Base Prices" (KOSDAQ); English, not authoritative. Used for the corporate-action base-price formulas (split, ex-dividend, ex-rights with / without consideration, mutual-fund cash distribution resumption) — all matching the KOSPI Enforcement Rule §30 case structure.
- `KRX-TOUR-KOSDAQ-METHOD-T4` — KRX overview "Trading of newly listed stocks" (KOSDAQ); English, not authoritative. Used for the 60 %–400 % day-1 band, the public-offering-price-as-base mapping, and the historical context that the older opening-price-base method was deprecated for typical IPOs by FSC measure but retained for capital-reduction-relisting and listing-change-after-spin-off cases. Explicitly references Annex 1-4 of the KOSDAQ Enforcement Rule (which exists but is not yet archived — R6).
