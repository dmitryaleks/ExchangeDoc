---
title: "Short Selling (KOSPI)"
markets: [KOSPI]
last_reviewed: 2026-04-30
sources:
  - KRX-RULE-KOSPI-BR-KO
  - KRX-RULE-KOSPI-BR-ENFORCE-KO
  - KRX-TOUR-KOSPI-OPS-T5
---

> See also: [Short Selling (KOSDAQ)](../kosdaq/short_selling.md), [Order Types (KOSPI)](./order_types.md), [Trading Rules (KOSPI)](./trading_rules.md), [Comparison](../common/comparison.md).

## Summary

- The Capital Markets Act (FSCMA) §180 defines short selling (공매도, *gong-mae-do*) in two forms: **naked short** (무차입공매도, *mu-cha-ip gong-mae-do*) — selling listed securities the seller does not own — and **covered short** (차입공매도, *cha-ip gong-mae-do*) — selling with intent to settle via borrowed securities [KRX-TOUR-KOSPI-OPS-T5; KRX-RULE-KOSPI-BR-KO §17].
- **Naked short is prohibited** in Korea. **Covered short is allowed** subject to a strict per-quotation flagging-and-verification regime and to a tick-test-style price restriction [KRX-RULE-KOSPI-BR-KO §17.1, §17.2; FSCMA §180].
- The **uptick rule** [KRX-RULE-KOSPI-BR-KO §18.1] requires a covered-short quotation to be priced **above the immediately preceding price**. Exception: if the immediately preceding price was an uptick (i.e. higher than the price before it), the short may be priced **at** the immediately preceding price. Eight categorical exemptions cover index/single-stock arbitrage, ETF/ETN unit sales, DR-vs-original arbitrage, and various liquidity-provider / market-maker hedging cases [KRX-RULE-KOSPI-BR-KO §18.2].
- A member receiving a sell order must (a) **identify** whether it is a short, (b) **verify** the borrow contract and settlement feasibility, (c) **flag** the order to KRX, and (d) **refuse** the order if settlement risk is identified [KRX-RULE-KOSPI-BR-KO §17.2.1, §17.2.2]. A consigner may opt out of short selling via a member-system block [KRX-RULE-KOSPI-BR-KO §17.4].
- KRX runs a **post-management escalation** for naked-short violators [KRX-RULE-KOSPI-BR-KO §18-2]. When a member or KRX detects a customer making naked-short trades, the customer is required to **pre-deposit sale securities** for **40, 80, or 120 trading days** depending on the number of violation days and cumulative violation amount (5억 / 10억 KRW thresholds).

## Detailed rules

### Naked vs covered short — the FSCMA §180 framework

The FSCMA §180 carves the universe of short sales into two types [KRX-TOUR-KOSPI-OPS-T5]:

- **Naked short (무차입공매도)** — sale of listed securities without owning them and without a borrow.
- **Covered short (차입공매도)** — sale with intent to settle via borrowed securities (margin or securities-lending transactions).

The same article also enumerates situations that **do not count as short selling**, even though the seller does not currently own the securities — the regulatory premise is that the seller will own the securities by the settlement date with no possibility of settlement failure [KRX-RULE-KOSPI-BR-KO §17.1; KRX-TOUR-KOSPI-OPS-T5]. The KOSPI BR mirrors the FSCMA carve-outs. The full list is in *Parameters & thresholds* — Table 1 below.

### Member duties on receiving a sell order

When a member receives a sell order from a consigner, the rule cycle is [KRX-RULE-KOSPI-BR-KO §17.2.1, §17.2.2]:

1. **Identify** whether the order is a short sale by querying the consigner [KRX-RULE-KOSPI-BR-KO §17.2.1.a]. If the consigner is an officer or employee of the issuer, this status must also be flagged.
2. **Verify** that the order is a covered short — confirm the borrow contract and confirm settlement feasibility [KRX-RULE-KOSPI-BR-KO §17.2.1.b, §17.3]. Verification methods are: written, phone/fax/email, or electronic communication; records retained per the Enforcement Rule.
3. **Refuse** the order if the member identifies any settlement risk [KRX-RULE-KOSPI-BR-KO §17.2.1.c].
4. **Flag** to KRX that the order is a covered short — both at consigner-receipt and at quotation-submission [KRX-RULE-KOSPI-BR-KO §17.2.1.d, §17.2.2].

A simplification path is provided by §17.4 [KRX-RULE-KOSPI-BR-KO §17.4]: a consigner who has provided written confirmation that they will not submit short orders, **and** for whose account the member has installed a system-level block, is treated as having satisfied the verification requirement. If the consigner subsequently breaches the no-short undertaking, the member must perform the full verification cycle for **120 days** following the day the breach is discovered.

### Uptick rule (가격제한, *ga-gyeok-je-han*)

A covered-short quotation is subject to the price-restriction rule of [KRX-RULE-KOSPI-BR-KO §18.1]:

> A covered short shall not be quoted at a price equal to or below the immediately preceding price. Provided that, where the immediately preceding price is higher than the price formed before it, a covered short may be quoted at the immediately preceding price.

In execution-algo terms:

- The **default rule** is "must price strictly above the last trade." This is a **plus-tick** test (sometimes called an uptick in tour material — but the rule allows pricing at the last trade only when there has been an uptick, so the strict version is "no minus-tick").
- The **uptick exception**: if last_trade_price > previous_trade_price (an uptick has just occurred), the short may price *at* last_trade_price, not strictly above. The rule's design intent is that an uptick already absorbs a sell-side preference and may be hit by a short without artificial pressure.

The reference price comparator extends to **mid-price** (중간가) — the OPS-T5 tour explicitly states "the last traded price (including mid-price)" [KRX-TOUR-KOSPI-OPS-T5]. So a midpoint-quotation print also acts as a 직전의 가격 (*jik-jeon-ui ga-gyeok*) for uptick-rule purposes.

#### Uptick rule exemptions

[KRX-RULE-KOSPI-BR-KO §18.2] lists eight categorical exemptions where a covered short may be priced at or below the immediately preceding price:

1. **Index arbitrage** — selling the constituent stock-basket against a futures or options position on that index (under detailed criteria in the Enforcement Rule).
2. **Single-stock arbitrage** — selling the underlying against a single-stock futures or options position on that underlying.
3. **ETF unit sales** — selling shares of a listed ETF.
4. **ETN sales** — selling listed ETN units.
5. **DR-original arbitrage** — selling DRs against the underlying original shares (or vice versa) for arbitrage.
6. **ELW-LP hedging** — when a liquidity provider for stock warrants (주식워런트증권, *ju-sik wo-reon-teu jeung-gwon*) sells the underlying stock to hedge its ELW inventory.
7. **ETF-LP hedging** — when an ETF liquidity provider sells underlying stocks to hedge ETF inventory.
7-2. **ETN-LP hedging** — when an ETN liquidity provider sells underlying stocks to hedge ETN inventory.
8. **Derivatives market-maker hedging** — when a derivatives-market market maker (per Derivatives Market Business Regulation §83) sells underlying stocks to hedge a futures or options position acquired in market-making.

[KRX-TOUR-KOSPI-OPS-T5] also mentions "regular session block trading" as exempt — this is covered indirectly by the §17.6 carve-out for the various block-trade variants, not by §18.2.

The exemptions also tie into the order-type-eligibility matrix: a covered-short subject to the §18 price restriction cannot use a market or conditional-limit quotation [KRX-RULE-KOSPI-BR-ENFORCE-KO §14.2.1.a; see Order Types (KOSPI) — Per-session and per-issue restrictions](./order_types.md#per-session-and-per-issue-restrictions). Best-counterparty (최유리) and best-same-side (최우선) limits face the same restriction unless explicitly carved out.

### KRX-discretionary covered-short restriction

[KRX-RULE-KOSPI-BR-KO §17.6] gives KRX power to restrict covered short for [KRX-RULE-KOSPI-BR-KO §17.6.1]:

- Issues whose **price decline rate and covered-short concentration** meet criteria set by the Enforcement Rule (the "short-sale overheat" framework).
- [§17.6.2] Issues that the **FSC has designated** as needing covered-short restriction for market-stability or fair-pricing reasons.

When KRX restricts covered short on an issue, the §18.2 categorical exemptions may still apply if the Enforcement Rule explicitly says so [KRX-RULE-KOSPI-BR-KO §17.6 proviso]. The Enforcement Rule procedure for KRX-discretionary restriction is referenced in §17.8 (delegation) and operationalized through the FSC's market-stability notice framework.

### Post-management — escalation tiers (§18-2)

When a customer is found to have made a naked-short trade, the member is required to apply pre-deposit verification for an escalating duration based on severity [KRX-RULE-KOSPI-BR-KO §18-2.4]. The metrics:

- **매도일수 (*mae-do-il-su*; violation days)** — number of days the customer made naked-short trades within the last 6 months.
- **누적매도금액 (*nu-jeok mae-do-geum-aek*; cumulative violation amount)** — total notional value of the naked-short trades.

The escalation matrix is in *Parameters & thresholds* — Table 3 below. Briefly:

- 40-day pre-deposit period for the lightest tier (1 day, KRW 5억–10억; or 2–4 days, ≤ KRW 5억).
- 80-day for the middle tier (1 day > KRW 10억; or 2–4 days, KRW 5억–10억; or 5+ days, ≤ KRW 5억).
- 120-day for the heavy tiers (2–4 days > KRW 10억; or 5+ days > KRW 5억).

The pre-deposit ("매도증권의 사전납부", *mae-do-jeung-gwon-ui sa-jeon-nap-bu*) requirement means the customer must transfer the sale securities into the member's account *before* the order is accepted — eliminating the borrow-then-sell mechanic for the duration. Pre-deposit applies for any covered-short order from that customer for the escalation period.

The same escalation applies, mutatis mutandis, when the FSC reports a customer for breach of the FSCMA §180-2 (short-sale balance reporting) or §180-3 (short-sale public disclosure) obligations [KRX-RULE-KOSPI-BR-KO §18-2.5].

### Record retention and KRX inquiry

Members must record and retain short-sale-related verification data for **at least 3 years**, per FSC notice referenced from [KRX-TOUR-KOSPI-OPS-T5] and operationalized via [KRX-RULE-KOSPI-BR-KO §17.7]. KRX may request short-sale records from members at any time for market-administration purposes [KRX-RULE-KOSPI-BR-KO §17.7].

The Enforcement Rule also requires bulk-cancel records to be retained for **10 years** [KRX-RULE-KOSPI-BR-ENFORCE-KO §17-2.3] — see [Order Amendments § Bulk cancel](./amendments.md#bulk-cancel). The 3-year vs 10-year asymmetry is a recurring quirk in KRX retention rules.

### Reporting and disclosure obligations (FSCMA §180-2, §180-3)

Beyond the trade-level rules in BR §17–§18, the FSCMA imposes two reporting obligations on short-sellers, governed by the FSC and the FSS:

- **Short-sale balance reporting (FSCMA §180-2)** — large-position holders of short positions must report their balances to the FSC. Detailed thresholds and timing are set by FSC notice; not in the KRX rulebook.
- **Short-sale public disclosure (FSCMA §180-3)** — significant short positions must be publicly disclosed. Again FSC-governed; the KRX rulebook only references compliance with these obligations for §18-2 escalation purposes.

These FSC-level obligations are external to the trade-execution rules covered by KRX. An execution-algo strategy that involves significant short positions must comply with both the KRX trading rules (this document) and the FSC's reporting/disclosure framework.

## Parameters & thresholds

### Table 1 — What does NOT count as short selling

Per [KRX-RULE-KOSPI-BR-KO §17.1] (mirroring FSCMA §180.1 carve-outs):

| #     | Carve-out                                                                                                                                | Article                              |
|-------|-------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------|
| 1     | Selling already-purchased listed securities, within the purchased quantity, before the settlement date                                    | [KRX-RULE-KOSPI-BR-KO §17.1.1]       |
| 2     | Selling rights-acquired stocks (CB / EB / BW exercise; capital increase; stock dividend) when listing-by-settlement-date is feasible      | [KRX-RULE-KOSPI-BR-KO §17.1.2]       |
| 3a    | Selling securities held at a third-party custodian (not the broker)                                                                       | [KRX-RULE-KOSPI-BR-KO §17.1.3.a]     |
| 3b    | Selling additional ETF units to be received from issuer                                                                                   | [KRX-RULE-KOSPI-BR-KO §17.1.3.b]     |
| 3c    | Selling underlying stocks to be received via ETF redemption                                                                               | [KRX-RULE-KOSPI-BR-KO §17.1.3.c]     |
| 3d    | Selling listed shares acquired upon DR-deposit-contract termination                                                                       | [KRX-RULE-KOSPI-BR-KO §17.1.3.d]     |
| 3e    | Selling lent securities whose return is confirmed                                                                                         | [KRX-RULE-KOSPI-BR-KO §17.1.3.e]     |
| 3f    | Selling securities to be delivered under an off-exchange trade or other contract                                                          | [KRX-RULE-KOSPI-BR-KO §17.1.3.f]     |
| 3g    | Selling DRs to be acquired by depositing eligible underlying securities                                                                   | [KRX-RULE-KOSPI-BR-KO §17.1.3.g]     |
| 3h    | Selling securities the consigner has agreed to buy in the post-close off-hours session of the same day                                    | [KRX-RULE-KOSPI-BR-KO §17.1.3.h]     |

### Table 2 — Uptick rule exemptions

Per [KRX-RULE-KOSPI-BR-KO §18.2]:

| #     | Exemption category                                                                                | Article                              |
|-------|----------------------------------------------------------------------------------------------------|--------------------------------------|
| 1     | Index-arbitrage stock-basket sales (vs index futures/options)                                      | [KRX-RULE-KOSPI-BR-KO §18.2.1]       |
| 2     | Single-stock-arbitrage underlying sales (vs single-stock futures/options)                          | [KRX-RULE-KOSPI-BR-KO §18.2.2]       |
| 3     | ETF unit sales                                                                                      | [KRX-RULE-KOSPI-BR-KO §18.2.3]       |
| 3-2   | ETN sales                                                                                           | [KRX-RULE-KOSPI-BR-KO §18.2.3-2]     |
| 4     | DR-vs-original arbitrage sales                                                                      | [KRX-RULE-KOSPI-BR-KO §18.2.4]       |
| 5     | ELW liquidity-provider quotes                                                                       | [KRX-RULE-KOSPI-BR-KO §18.2.5]       |
| 6     | ELW LP hedging — selling underlying to hedge ELW inventory                                         | [KRX-RULE-KOSPI-BR-KO §18.2.6]       |
| 7     | ETF LP hedging — selling underlying to hedge ETF inventory                                         | [KRX-RULE-KOSPI-BR-KO §18.2.7]       |
| 7-2   | ETN LP hedging — selling underlying to hedge ETN inventory                                          | [KRX-RULE-KOSPI-BR-KO §18.2.7-2]     |
| 8     | Derivatives market-maker hedging — selling underlying to hedge futures/options inventory            | [KRX-RULE-KOSPI-BR-KO §18.2.8]       |

### Table 3 — Post-management escalation (§18-2.4)

Pre-deposit period for naked-short violators, by violation days × cumulative amount over the last 6 months:

|                                | ≤ KRW 5 억 (≤ 500 M)  | KRW 5 억 < x ≤ 10 억 (500 M – 1 B) | > KRW 10 억 (> 1 B) |
|--------------------------------|:--------------------:|:------------------------------:|:------------------:|
| **1 day**                      |          —           |        **40 days**             |    **80 days**     |
| **2–4 days**                   |    **40 days**       |        **80 days**             |   **120 days**     |
| **5+ days**                    |    **80 days**       |       **120 days**             |   **120 days**     |

Source: [KRX-RULE-KOSPI-BR-KO §18-2.4]. Tier-1 is the lightest escalation; tier-3 is the heaviest. The pre-deposit rule applies to any covered-short order from that customer for the duration, regardless of subsequent compliance.

The OPS-T5 tour [KRX-TOUR-KOSPI-OPS-T5] gives a simpler, older summary ("breach twice or more in 6 months OR ≥KRW 1 billion / day → 30 days documentation"). The current rule is materially stricter and is parameterized over the joint-distribution of (days × amount) rather than a single-threshold OR.

### Table 4 — Member-side verification methods (§17.3.2)

| Method                                                                       | Source                                |
|------------------------------------------------------------------------------|---------------------------------------|
| Written (paper)                                                              | [KRX-RULE-KOSPI-BR-KO §17.3.2.a]      |
| Phone, telegraph, fax, email                                                 | [KRX-RULE-KOSPI-BR-KO §17.3.2.b]      |
| Computer / electronic communication                                          | [KRX-RULE-KOSPI-BR-KO §17.3.2.c]      |
| **Member-side block + customer no-short undertaking (deemed verification)**  | [KRX-RULE-KOSPI-BR-KO §17.4]          |

The §17.4 deemed-verification path is the operating mode for retail accounts whose holders never short. It is the only path that does not require per-order verification.

## Worked examples

### Example A — uptick rule on an ordinary downtick day

Last three trade prints on KOSPI 200 stock X:

- 13:00:00 — KRW 50,000 (no relevant prior reference for our example).
- 13:01:00 — KRW 49,950 (down from 50,000).
- 13:02:00 — KRW 49,900 (down from 49,950 — current 직전의 가격).

Member submits a covered-short for stock X at 13:02:30. Per §18.1, the short cannot be priced at or below KRW 49,900. The 13:02:00 print (49,900) was not an uptick — it was lower than the 13:01:00 price of 49,950 — so the proviso does not apply. Minimum permitted short price: **49,950** (one tick above 49,900) [KRX-RULE-KOSPI-BR-KO §18.1].

The same short submitted to KRX as a regular limit at KRW 49,900 would be **rejected** at the member's pre-quote control [KRX-RULE-KOSPI-BR-ENFORCE-KO §12-2.4.c]. To execute at the touch, the member must wait for either an uptick or for one of the §18.2 exemptions to apply.

### Example B — uptick rule under the uptick exception

Last three prints:

- 13:00:00 — KRW 50,000.
- 13:01:00 — KRW 49,950 (downtick).
- 13:02:00 — KRW 50,000 (uptick relative to 13:01:00).

At 13:02:30 the member submits a covered-short. The 직전의 가격 is 50,000; the price-before-that is 49,950. 50,000 > 49,950 → uptick has occurred. Per the §18.1 proviso, the short **may be priced at KRW 50,000** (not strictly above) [KRX-RULE-KOSPI-BR-KO §18.1 proviso].

This is the design feature that distinguishes the KRX rule from the historical US rule: KRX permits pricing at the touch only when the touch was just established by an uptick, not as a default.

### Example C — escalation tier upgrade

Customer Z, over the last 6 months, has been identified by member or KRX as having made naked-short trades on:

- 2026-02-14 — KRW 700 million notional (1 day, > 5억 but < 10억).
- 2026-03-19 — KRW 200 million notional (2 days now, cumulative 9억).
- 2026-04-15 — KRW 800 million notional (3 days now, cumulative 17억).

Looking up [KRX-RULE-KOSPI-BR-KO §18-2.4] Table 3 with **3 violation days × cumulative > 10억**: tier-3 — **120-day pre-deposit** required. The escalation runs from the day after the member is informed by KRX, for 120 trading days. During the period, customer Z's covered-short orders are accepted only when the sale securities are pre-deposited at the member.

If a fourth violation occurs at day 60 of the 120-day escalation, no upgrade is possible (tier 3 is already the maximum). The 120-day clock does not reset on subsequent violations within the period — but if violations continue past the 120-day end, a fresh tier-3 escalation begins (subject to the same 6-month look-back window).

## Edge cases & open questions

- Edge case: §17.4's "deemed verification" path is conditional on a system-level block. The rule says "if the member modified the computer program to block short-selling order from the account" — but the modification is a one-time member-side action. If the member's system has a bug or a bypass, the deemed-verification claim collapses. The conservative interpretation is that the block must be tested and audited; the rule is silent on testing requirements.
- Edge case: §18.1's "직전의 가격" reference includes mid-price prints per [KRX-TOUR-KOSPI-OPS-T5]. So a midpoint trade between two regular trades shifts the uptick-rule reference. An algorithm submitting a short shortly after a midpoint print therefore must use the midpoint as the comparator, not the most recent regular-limit print.
- Edge case: §18.2's exemption #3 (ETF unit sales) applies to *the ETF unit itself*, not to the underlying basket. So a sell-short on an ETF unit is uptick-exempt; a sell-short on an underlying constituent (without an arbitrage-or-hedging context) is not. Members operating multi-leg arbitrage strategies must classify each leg separately.
- Edge case: The §18-2 escalation runs on a 6-month rolling look-back. A customer that completed a 120-day escalation at day 0 and was clean from day 1 to day 121 still has the prior violations counted toward a fresh escalation if a new violation occurs at day 122 — the look-back window does not exclude the prior escalation's underlying violations until 6 months have passed since the violation date.
- Open question: BR §17.6 enables KRX-discretionary covered-short restriction for short-sale-overheat issues, but the precise criteria are delegated to the Enforcement Rule §17.8 (referenced) — which I have not extracted in this document. The OPS-T5 tour does not describe these criteria. Verify against KRX market-administration notice for the current overheat-designation thresholds and the duration of restrictions.
- Open question: The FSCMA §180.3 gives the FSC power to **suspend covered short** entirely for fixed periods. As of this document's review date (2026-04-30), the operative status of any FSC-imposed covered-short suspension is not confirmed. Algorithmic strategies that depend on short execution must check the FSC's current notice before relying on the §17.2 covered-short permission.
- Open question: §17.1.1's "결제일 전" (before settlement date) carve-out is bound by the T+2 settlement default [KRX-RULE-KOSPI-BR-KO §7]. So a sell-then-buy strategy executed within the same settlement window is exempted from the short-selling regime. But the carve-out scope when settlement is shifted (e.g. T+0 or T+1 trade types per §7.1) is not explicit. Verify against the Capital Markets Act §180 implementing notice for non-T+2 settlement scenarios.
- Unsourced claim: [KRX-TOUR-KOSPI-OPS-T5]'s "regular session block trading is exempt from uptick" is not directly enumerated in §18.2's eight categories. The tour's claim is consistent with §17.6's carve-out for the various block-trade variants but the rule path is operational, not a categorical §18.2 exemption. Treat the tour's framing as approximate; consult §17.6 for precise scope.
- Unsourced claim: The OPS-T5 tour's "30 days documentation requirement on ≥KRW 1 billion / day breaches" is **outdated**. The current rule [KRX-RULE-KOSPI-BR-KO §18-2.4] is parameterized over the (days × amount) joint distribution and ranges 40 / 80 / 120 days. The tour appears to predate the 2018-12-05 / 2026-01-28 amendments to §18-2 — treat the tour's escalation as historical and rely on Table 3 above for current rules.

## Sources

- `KRX-RULE-KOSPI-BR-KO` — KOSPI Market Business Regulation (유가증권시장 업무규정, *yu-ga-jeung-gwon si-jang eom-mu gyu-jeong*), bookid 210200859, effective 2026-04-28. Articles cited: §7 (Trade types and settlement timing — referenced for the §17.1.1 carve-out), §17 (Short-sell quotation restrictions — central article: §17.1 carve-outs (8 cases), §17.2 covered-short member duties, §17.3 verification methods, §17.4 deemed-verification path with 120-day breach reset, §17.6 KRX-discretionary restriction, §17.7 KRX inquiry power, §17.8 ER delegation), §18 (Uptick rule — §18.1 plus-tick test with uptick exception, §18.2 eight categorical exemptions, §18.3 ER delegation), §18-2 (Post-management — §18-2.1 settlement-day verification, §18-2.4 escalation matrix to 40/80/120 days, §18-2.5 FSCMA §180-2/§180-3 breach treatment).
- `KRX-RULE-KOSPI-BR-ENFORCE-KO` — KOSPI BR Enforcement Rule (유가증권시장 업무규정 시행세칙, *yu-ga-jeung-gwon si-jang eom-mu gyu-jeong si-haeng se-chik*), bookid 210203562, effective 2026-04-28. Articles cited: §12-2.4.c (Pre-quote control for short-sale price restriction — referenced), §14.1.2-2 (Short-sale price-restriction input prohibitions for newly-listed issues — referenced), §14.2.1.a (Market and conditional-limit prohibition for price-restricted short — referenced), §17-2.3 (10-year bulk-cancel record retention — referenced for retention-asymmetry note), §17.8 (ER delegation for §17.6 KRX-discretionary covered-short restriction — referenced; not extracted).
- `KRX-TOUR-KOSPI-OPS-T5` — KRX overview "Concept of Short Selling"; English, not authoritative. Used for: the FSCMA §180 naked-vs-covered framing, the FSCMA §180 carve-out narrative, the four-step member-duty cycle (identify / verify / mark / refuse), the consigner-opt-out path, the uptick-rule including the mid-price comparator, the regular-session block-trade exemption claim (flagged as approximate), the 3-year retention claim, and the (now-outdated) "30-day documentation on ≥KRW 1 B/day breach" pre-§18-2 escalation summary (flagged as historical). External references: FSCMA §180 (statute — Capital Markets Act, the parent statute for KRX short-sale rules); FSCMA §180-2 (short-sale balance reporting); FSCMA §180-3 (short-sale public disclosure); FSC market-stability notices for covered-short suspension. These FSCMA articles are statute, not KRX rules; they are operative-by-reference and not archived in the source inventory.
