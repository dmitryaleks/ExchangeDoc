---
title: "Price Ranges & Tick Sizes (KOSPI)"
markets: [KOSPI]
last_reviewed: 2026-04-30
sources:
  - KRX-RULE-KOSPI-BR-KO
  - KRX-RULE-KOSPI-BR-ENFORCE-KO
  - KRX-TOUR-KOSPI-BASIC-T5
  - KRX-TOUR-KOSPI-BASIC-T6
  - KRX-TOUR-KOSPI-METHOD-T6
---

> See also: [Price Ranges & Tick Sizes (KOSDAQ)](../kosdaq/price_ranges.md), [Auctions (KOSPI)](./auctions.md), [Order Types (KOSPI)](./order_types.md), [Comparison](../common/comparison.md).

## Summary

- The daily price for shares, ETFs, ETNs, foreign DRs, and beneficiary certificates is bounded to ±30 % of the base price (기준가격, *gi-jun-ga-gyeok*) — the upper bound is 상한가 (*sang-han-ga*) and the lower bound is 하한가 (*ha-han-ga*) [KRX-RULE-KOSPI-BR-KO §20.1–20.2].
- The default base price is the previous trading day's closing price, rounded up to the nearest tick when needed; corporate actions adjust the base price to a theoretical equivalent [KRX-RULE-KOSPI-BR-ENFORCE-KO §30.1.1, §30.1.4–30.1.6].
- Tick size (호가가격단위, *ho-ga-ga-gyeok dan-wi*) is a 7-band schedule running from KRW 1 (price < 2,000) to KRW 1,000 (price ≥ 500,000) [KRX-RULE-KOSPI-BR-ENFORCE-KO §32.2].
- Trading lot (매매수량단위, *mae-mae su-ryang dan-wi*) is 1 share for ordinary shares, ETFs, ETNs, and most certificates; 10 certs for ELWs [KRX-RULE-KOSPI-BR-ENFORCE-KO §33.1].
- Two important exceptions to the ±30 % rule: newly-listed common shares trade in a +300 % / –60 % band on day 1 (60 %–400 % of base), and liquidation issues (정리매매종목, *jeong-ri mae-mae jong-mok*) trade with no price limit [KRX-RULE-KOSPI-BR-ENFORCE-KO §31.3; KRX-RULE-KOSPI-BR-KO §20.3].

## Detailed rules

### Daily price limit

For shares (주권, *ju-gwon*), foreign DRs (외국주식예탁증권, *oe-guk ju-sik ye-tak jeung-gwon*), ETFs (상장지수집합투자기구 집합투자증권, *sang-jang-ji-su jip-hap-tu-ja-gi-gu jip-hap-tu-ja jeung-gwon*), ETNs (상장지수증권, *sang-jang-ji-su jeung-gwon*), and beneficiary certificates (수익증권, *su-ik jeung-gwon*), the quoted price must satisfy [KRX-RULE-KOSPI-BR-KO §20.1]:

> 하한가 ≤ price ≤ 상한가

with [KRX-RULE-KOSPI-BR-KO §20.2]:

> 가격제한폭 (*ga-gyeok-je-han-pok*; the price-limit band) = base price × 0.3, with any fraction below the tick-size at the base-price level rounded down.

Upper and lower limits are then computed and rounded onto the tick grid at the *new* price level [KRX-RULE-KOSPI-BR-ENFORCE-KO §31.1]:

- 상한가 = base + band, rounded **down** to the nearest tick.
- 하한가 = base − band, rounded **up** to the nearest tick.
- If base = the smallest tick (KRW 1), the lower limit is also KRW 1.

For leveraged ETFs and ETNs whose unit value is geared to the underlying by a fixed multiple (positive or negative), the band is multiplied by the absolute value of the multiple [KRX-RULE-KOSPI-BR-KO §20.2; KRX-RULE-KOSPI-BR-ENFORCE-KO §31.2.2]. Multiples of absolute value < 1 do not get multiplied (the band uses the plain 0.3 formula).

The ±30 % rule does not apply to:

- Liquidation issues (정리매매종목) [KRX-RULE-KOSPI-BR-KO §20.3].
- ELWs (주식워런트증권, *ju-sik wo-reon-teu jeung-gwon*), subscription right certificates (신주인수권증서, *sin-ju-in-su-gwon jeung-seo*), and subscription right warrants (신주인수권증권, *sin-ju-in-su-gwon jeung-gwon*) [KRX-TOUR-KOSPI-BASIC-T5].

### Base price (기준가격)

The base price for the trading day is set per [KRX-RULE-KOSPI-BR-ENFORCE-KO §30.1]. The default rule is the previous day's closing price (전일종가, *jeon-il jong-ga*); when that price is not on a tick, it is rounded up to the nearest tick. If no trade occurred on the previous day, the previous day's *base* price is used [KRX-RULE-KOSPI-BR-ENFORCE-KO §30.1.1].

Several special cases override the default:

- **Newly listed issues** [KRX-RULE-KOSPI-BR-ENFORCE-KO §30.1.2]:
  - Common shares & foreign DRs — base is computed per Annex 1-4 (in practice the public offering price, per [KRX-TOUR-KOSPI-BASIC-T6]).
  - Transfers from KOSDAQ — last KOSDAQ closing price (or its base if no close).
  - ETFs — most recent published base per the Capital Markets Act §238.6.
  - ETNs — per-security indicative value per Listing Regulation §149-3.2.4.
  - Other beneficiary certificates — issue/sale price at the most recent offering.
- **Issues using the opening-price-base method** (시가기준가종목, *si-ga gi-jun-ga jong-mok*) [KRX-RULE-KOSPI-BR-ENFORCE-KO §30.1.3]: the day's first trade price (determined by the day's opening single-price auction per [KRX-RULE-KOSPI-BR-KO §37.1]) becomes the base. If no first price is determined by session close, an evaluation price (평가가격, *pyeong-ga ga-gyeok*) per Annex 1 is used.
- **Merger-listed issues** [KRX-RULE-KOSPI-BR-ENFORCE-KO §30.1.3-2] — base computed from the merger ratio applied to the predecessor's last close.
- **Ex-dividend / ex-rights issues** [KRX-RULE-KOSPI-BR-ENFORCE-KO §30.1.4]: Annex 2 formulas apply.
- **ETFs/ETNs with declared cash distribution** [KRX-RULE-KOSPI-BR-ENFORCE-KO §30.1.5]: prior close minus per-unit distribution.
- **Stock splits and reverse splits** [KRX-RULE-KOSPI-BR-ENFORCE-KO §30.1.6]: prior close × split (or merge) ratio.

When a base price computed by formula does not land on a tick, sub-cents are dropped and the result is rounded up to the nearest tick [KRX-RULE-KOSPI-BR-ENFORCE-KO §30.3].

### Tick size and quote-quantity unit

Tick size — formally 호가가격단위 (the minimum price increment at which an order can be placed) — runs in 7 bands for ordinary shares, foreign DRs, subscription right certificates, subscription right warrants, and beneficiary certificates [KRX-RULE-KOSPI-BR-ENFORCE-KO §32.2.1]. ETFs and ETNs follow a 2-band schedule [KRX-RULE-KOSPI-BR-ENFORCE-KO §32.2.2]. ELWs (stock warrants — 주식워런트증권, *ju-sik wo-reon-teu jeung-gwon*) are flat at KRW 5 [KRX-RULE-KOSPI-BR-ENFORCE-KO §32.2.3]. The full schedules are in *Parameters & thresholds* below.

The quote-quantity unit (호가수량단위, *ho-ga su-ryang dan-wi*) — the granularity at which an order quantity may be specified — is 1 share for ordinary shares, 1 share for ETFs, and 1 cert for foreign DRs, ETNs, subscription rights, ELWs, and beneficiary certificates [KRX-RULE-KOSPI-BR-ENFORCE-KO §32.1].

### Trading lot

The trading lot (매매수량단위) — the granularity at which a *trade* (not just a quote) is sized — matches the quote-quantity unit for almost everything: 1 share / 1 cert / 1 unit [KRX-RULE-KOSPI-BR-ENFORCE-KO §33.1]. The single exception is ELWs, which trade in lots of 10 certs even though they may be quoted in single certs [KRX-RULE-KOSPI-BR-ENFORCE-KO §33.1.5-2].

KRX may adjust the trading lot when quote flooding (호가폭주, *ho-ga-pok-ju*) causes a system-load risk; any adjustment must be pre-announced [KRX-RULE-KOSPI-BR-ENFORCE-KO §33.3, §33.5].

### Special-case price limits

Two cases override the default ±30 % band:

- **Newly listed common shares — day-1 only** [KRX-RULE-KOSPI-BR-ENFORCE-KO §31.3; KRX-TOUR-KOSPI-BASIC-T6]:
  - Upper limit: base × 3.0 (effectively a +300 % limit).
  - Lower limit: base × 0.4 (effectively a –60 % limit).
  - Combined: the day-1 trading band is **60 %–400 %** of the base price.
- **Long-market-closure resumption / extraordinary market situations** [KRX-RULE-KOSPI-BR-ENFORCE-KO §31.2.1]: KRX may set a different price-limit band on the first trading day after a long closure or in any other extraordinary market situation.

### Limit orders vs market orders at price limits

When the limit price of a limit order coincides with 상한가 or 하한가, the limit order and an equivalent-side market order are deemed equal in price priority [KRX-RULE-KOSPI-BR-KO §22.2.1; KRX-TOUR-KOSPI-METHOD-T6]:

- A **buy market order** is deemed to sit at 상한가, treated as having the same price priority as a buy limit at 상한가.
- A **sell market order** is deemed to sit at 하한가, treated as having the same price priority as a sell limit at 하한가.

Despite the price-priority equivalence, the *execution* differs by quantity and arrival order [KRX-TOUR-KOSPI-METHOD-T6]:

- In a single-price auction with sufficient counter-party quantity, both fill at the same price.
- In a single-price auction where the counter-party quantity is smaller, the market order fills at a *better* internal price (the matched counter-party's limit), while a limit-at-limit fills at its own limit price — so the market order is more advantageous.
- In continuous trading, the difference depends on time priority: if the limit-at-limit was already in the book when the market order arrived, both fill at the same price; if the market order arrives first, it can match against an inbound limit-at-limit at a better internal price.

See *Worked examples* below.

## Parameters & thresholds

### Tick size schedule (호가가격단위)

For ordinary shares, foreign DRs, subscription right certificates, subscription right warrants, and beneficiary certificates [KRX-RULE-KOSPI-BR-ENFORCE-KO §32.2.1]:

| Price band (KRW)              | Tick (KRW) |
|-------------------------------|-----------:|
| under 2,000                   |          1 |
| 2,000 – under 5,000           |          5 |
| 5,000 – under 20,000          |         10 |
| 20,000 – under 50,000         |         50 |
| 50,000 – under 200,000        |        100 |
| 200,000 – under 500,000       |        500 |
| 500,000 and above             |      1,000 |

For ETFs and ETNs [KRX-RULE-KOSPI-BR-ENFORCE-KO §32.2.2]:

| Price band (KRW) | Tick (KRW) |
|------------------|-----------:|
| under 2,000      |          1 |
| 2,000 and above  |          5 |

For ELWs (주식워런트증권): flat 5 KRW [KRX-RULE-KOSPI-BR-ENFORCE-KO §32.2.3].

### Trading lot (매매수량단위)

| Instrument                                          | Trading lot |
|-----------------------------------------------------|------------:|
| Ordinary share (주권)                                |     1 share |
| Foreign DR (외국주식예탁증권)                         |      1 cert |
| ETF unit (상장지수집합투자기구 집합투자증권)          |     1 share |
| ETN (상장지수증권)                                   |      1 cert |
| Subscription right certificate (신주인수권증서)      |      1 cert |
| Subscription right warrant (신주인수권증권)          |      1 cert |
| ELW (주식워런트증권)                                 |     10 cert |
| Beneficiary certificate (수익증권)                   |      1 unit |

Source: [KRX-RULE-KOSPI-BR-ENFORCE-KO §33.1].

### Daily price-limit band

| Issue category                            | Upper             | Lower             | Source                                       |
|-------------------------------------------|-------------------|-------------------|----------------------------------------------|
| Default (shares, DRs, ETFs, ETNs, etc.)   | base × 1.30       | base × 0.70       | [KRX-RULE-KOSPI-BR-KO §20.2]                |
| Leveraged ETF/ETN, multiple ≥ 1 (×*k*)    | base × (1 + 0.30·k) | base × (1 − 0.30·k) | [KRX-RULE-KOSPI-BR-KO §20.2]              |
| Leveraged ETF/ETN, multiple < 1           | base × 1.30       | base × 0.70       | [KRX-RULE-KOSPI-BR-ENFORCE-KO §31.2.2]       |
| Newly listed common share — day 1         | base × 4.00 (+300%) | base × 0.40 (−60%) | [KRX-RULE-KOSPI-BR-ENFORCE-KO §31.3]        |
| Liquidation issue (정리매매종목)           | unlimited         | unlimited (down to KRW 1 minimum tick) | [KRX-RULE-KOSPI-BR-KO §20.3]   |
| Long-closure resumption / extraordinary   | per KRX notice    | per KRX notice    | [KRX-RULE-KOSPI-BR-ENFORCE-KO §31.2.1]       |
| ELW, subscription rights / warrants       | none              | none              | [KRX-TOUR-KOSPI-BASIC-T5]                    |

The upper-limit calculation rounds **down** to the nearest tick at the new price level; the lower-limit calculation rounds **up** [KRX-RULE-KOSPI-BR-ENFORCE-KO §31.1].

### Base-price determination — selected cases

| Case                                                  | Base price                                                              | Source                                       |
|-------------------------------------------------------|-------------------------------------------------------------------------|----------------------------------------------|
| Default (existing listed issue)                       | Previous day's closing price (전일종가) — round up to tick if needed     | [KRX-RULE-KOSPI-BR-ENFORCE-KO §30.1.1]       |
| No trade on previous day                              | Previous day's base price                                               | [KRX-RULE-KOSPI-BR-ENFORCE-KO §30.1.1]       |
| Newly listed common share                             | Public offering price (per Annex 1-4)                                   | [KRX-RULE-KOSPI-BR-ENFORCE-KO §30.1.2.a]     |
| Transfer from KOSDAQ                                  | Last KOSDAQ closing price (or KOSDAQ base if no close)                  | [KRX-RULE-KOSPI-BR-ENFORCE-KO §30.1.2.b]     |
| Stock split / reverse split                           | Previous close × split-or-merge ratio                                   | [KRX-RULE-KOSPI-BR-ENFORCE-KO §30.1.6]       |
| Ex-dividend / ex-rights                               | Per Annex 2 formula                                                     | [KRX-RULE-KOSPI-BR-ENFORCE-KO §30.1.4]       |
| ETF / ETN with declared cash distribution             | Previous close − per-unit distribution                                  | [KRX-RULE-KOSPI-BR-ENFORCE-KO §30.1.5]       |
| Issue under opening-price-base method (시가기준가종목) | First trade of the day; or evaluation price if no first trade by close  | [KRX-RULE-KOSPI-BR-ENFORCE-KO §30.1.3]       |

## Worked examples

### Example A — daily price limit calculation

(From [KRX-TOUR-KOSPI-BASIC-T5].)

Base price = KRW 9,980. The price-limit band per [KRX-RULE-KOSPI-BR-KO §20.2]:

1. 9,980 × 0.3 = KRW 2,994.
2. The tick size at the base-price level (≥ 5,000 < 20,000) is KRW 10. Round 2,994 down to a multiple of 10 → KRW 2,990.
3. 상한가 = 9,980 + 2,990 = KRW 12,970 (already on tick).
4. 하한가 = 9,980 − 2,990 = KRW 6,990 (already on tick).

If the upper limit had not landed on a tick, it would have been rounded **down** to the nearest valid tick at the price level of the upper limit, per [KRX-RULE-KOSPI-BR-ENFORCE-KO §31.1].

### Example B — newly-listed common share, day 1

A common share lists on KOSPI with base price = KRW 10,000 (the public offering price, per [KRX-TOUR-KOSPI-BASIC-T6]). Day-1 limits per [KRX-RULE-KOSPI-BR-ENFORCE-KO §31.3]:

- 상한가 = 10,000 × 3 = +30,000 added → 10,000 + 30,000 = KRW 40,000.
- 하한가 = 10,000 × 0.4 = 4,000 subtracted → 10,000 − 4,000 = KRW 6,000.
- Day-1 trading band: KRW 6,000 to KRW 40,000 (60 %–400 % of the base).

From day 2 the issue reverts to the default ±30 % band [KRX-RULE-KOSPI-BR-KO §20.2].

### Example C — limit-at-limit vs market order in a single-price auction

(Adapted from [KRX-TOUR-KOSPI-METHOD-T6] Case 2.)

Auction state on the bid side (assume tick = KRW 100):

| Asks |  Price  | Bids |
|-----:|--------:|-----:|
|      |  11,500 | 200 (limit at upper limit, OR market order — both deemed equal) |
|      |  10,600 |      |
|      |  10,550 |      |
|  100 |  10,500 | (deemed price for market) |
|  100 |  10,450 |      |
| (last)| 10,000 |      |

The 200 buy quantity at the upper limit is matched against 100 of available asks. The execution price differs depending on how the buy was placed [KRX-TOUR-KOSPI-METHOD-T6]:

- If the 200 was a **buy limit order at 11,500**, the execution price is **KRW 11,500** (the limit's own price — the "price of the larger-quantity order" rule).
- If the 200 was a **buy market order**, the execution price is **KRW 10,500** (the matched ask's limit price).

So at the limit, a market order is *more advantageous* than a limit-at-limit, by 1,000 KRW per share in this example — even though §22 considers them equal in price priority. (In a continuous auction, this advantage exists only when the market order arrives *before* the counter-party limit; see [KRX-TOUR-KOSPI-METHOD-T6] Cases 3 & 4.)

## Edge cases & open questions

- Edge case: §31.1's rounding rules are asymmetric — upper rounds down, lower rounds up. Both directions narrow the band relative to the unrounded ±30 % calculation. A caller computing "upper" as `floor(base × 1.3, tick)` must use the tick at the *upper-limit price level*, not the base-price level. The ±30 % multiplier itself uses the base-price tick (per §20.2's "tick at the base price level"). Two different ticks in a single calculation — easy to get wrong.
- Edge case: For a leveraged ETF/ETN with multiple absolute value < 1 (i.e. a partial-leverage product), §31.2.2 explicitly restores the plain 0.3 multiplier rather than scaling down — so a 0.5x product still has a ±30 % band, not ±15 %. Verify the reading against any English KRX guidance before publishing.
- Edge case: §30.1.1's "round up to nearest tick" applies when the previous close falls between ticks. This can happen after corporate-action recalculations — but the *previous close* itself is reported on a tick, so off-tick closes only arise from formula-derived prices (§30.1.4–.6). A subsequent §30.1.1 base-price recovery (e.g. the day after a split) carries the rounded-up tick, not the formula's exact value.
- Open question: §20.3 says liquidation issues "have no price limit" but does not relax the smallest-tick floor of §31.1 (which sets 하한가 = KRW 1 if base = KRW 1). Implication: a liquidation issue can trade arbitrarily high but not below KRW 1. Verify against the Listing Regulation (§9, referenced in §20.3) to confirm.
- Open question: ELWs and subscription rights are excluded from the ±30 % rule per [KRX-TOUR-KOSPI-BASIC-T5], but the rulebook §20.1 enumerates *included* securities as "shares, foreign DRs, ETFs, ETNs, beneficiary certificates" — ELWs and subscription rights are conspicuously absent. The exclusion is therefore by omission rather than by explicit carve-out. Cross-check against any ELW-specific provisions in the rulebook before relying on "no limit".
- Open question: The 60 %–400 % day-1 band for newly listed common shares (§31.3) was added 2023-04-12. Whether the same band applies to newly-listed-via-merger or transfer-from-KOSDAQ issues is not fully clear from §31.3 alone — those cases use different base-price formulas (§30.1.2.b, §30.1.3-2) and the rule may default back to ±30 % from day 1. Verify before treating any non-IPO new listing as a 60–400 % day-1 candidate.
- Unsourced claim: [KRX-TOUR-KOSPI-BASIC-T5] gives a historical price-limit progression (4.6 % avg pre-1995 → 6 % → 8 % → 12 % → 15 % → 30 %) — overview color, not preserved in the rulebook. Treat as background only.

## Sources

- `KRX-RULE-KOSPI-BR-KO` — KOSPI Market Business Regulation (유가증권시장 업무규정, *yu-ga-jeung-gwon si-jang eom-mu gyu-jeong*), bookid 210200859, effective 2026-04-28. Articles cited: §20 (Daily Price Limit Band), §21 (Tick / Quote / Trading-Lot Units — delegates to Enforcement Rule), §22.2.1 (priority for market vs limit at limit), §37.1 (newly-listed first-price method, referenced).
- `KRX-RULE-KOSPI-BR-ENFORCE-KO` — KOSPI BR Enforcement Rule (유가증권시장 업무규정 시행세칙, *yu-ga-jeung-gwon si-jang eom-mu gyu-jeong si-haeng se-chik*), bookid 210203562, effective 2026-04-28. Articles cited: §30 (Base Price — full set of cases including newly listed, transfer, ETF, ETN, splits, distributions, opening-price-base), §31 (Price-Limit Band — tick rounding, special-situation overrides, day-1 newly-listed +300 %/-60 %), §32 (Quote-Quantity Unit and Tick Size — full schedules), §33 (Trading Lot — full schedule including the ELW 10-cert exception).
- `KRX-TOUR-KOSPI-BASIC-T5` — KRX overview "Daily Price Limits"; English, not authoritative. Used for the worked-example base 9,980 calculation; for the historical price-limit progression (flagged as background); for the explicit list of products excluded from the ±30 % rule (ELW, subscription rights, subscription warrants).
- `KRX-TOUR-KOSPI-BASIC-T6` — KRX overview "Base Price"; English, not authoritative. Used for the public-offering-price = day-1 base mapping for newly listed shares, and for the descriptive language around the opening-price-base method.
- `KRX-TOUR-KOSPI-METHOD-T6` — KRX overview "Limit Orders at Daily Price Limits vs Market Orders"; English, not authoritative. Used for the limit-vs-market worked example (Example C) and the priority-equivalence-but-execution-difference framing.
