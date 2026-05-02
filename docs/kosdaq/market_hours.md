---
title: "Market Hours (KOSDAQ)"
markets: [KOSDAQ]
last_reviewed: 2026-05-01
sources:
  - KRX-RULE-KOSDAQ-BR-KO
  - KRX-TOUR-KOSDAQ-OPS-T1
---

> See also: [Market Hours (KOSPI)](../kospi/market_hours.md), [Comparison](../common/comparison.md).

**Delta file.** KOSDAQ market-hours rules are substantively **identical** to KOSPI: same regular-session window (09:00–15:30 KST), same intraday-competitive-block carve-out (09:00–15:00), same off-hours sub-windows (08:00–09:00 pre-open + 15:30–18:00 post-close), and the same holiday categories. This file points to the [KOSPI write-up](../kospi/market_hours.md) for shared content and records the KOSDAQ-side citations + the small structural / wording differences.

## Summary

- **Regular session** trades 09:00–15:30 KST [KRX-RULE-KOSDAQ-BR-KO §4.3.1] — identical to KOSPI.
- **Intraday competitive-block** receipt closes 30 min before 장종료 (*jang-jong-ryo*; 15:00 KST) per [KRX-RULE-KOSDAQ-BR-KO §4.3.1 + §19-3] — identical to KOSPI.
- **Off-hours sessions:** pre-open 08:00–09:00 (with 시간외종가매매 (*si-gan-oe jong-ga mae-mae*; off-hours closing-price) at 08:30–08:40); post-close 15:40–18:00 (with closing-price 15:40–16:00 and 시간외단일가매매 (*si-gan-oe dan-il-ga mae-mae*; off-hours single-price) 16:00–18:00) [KRX-RULE-KOSDAQ-BR-KO §4.3.2; KRX-TOUR-KOSDAQ-OPS-T1] — same windows as KOSPI.
- **Holidays:** Saturdays, Government Office holidays, Workers' Day (May 1), end-of-year 1 day, plus discretionary days [KRX-RULE-KOSDAQ-BR-KO §5] — substantively identical to KOSPI; ordering of the list differs, see *Delta vs KOSPI* below.
- **Authority to alter hours:** KRX may temporarily change trading hours under system-failure / market-administration grounds [KRX-RULE-KOSDAQ-BR-KO §4.4] — identical to KOSPI.

## Detailed rules

For full prose on regular-session anchors, off-hours session breakdown, and the quotation-receipt-window concept, see [KOSPI § Detailed rules](../kospi/market_hours.md#detailed-rules). KOSDAQ uses the same 장개시 (*jang-gae-si*; session-open) and 장종료 (*jang-jong-ryo*; session-close) anchors, defined identically [KRX-RULE-KOSDAQ-BR-KO §2.14, §2.15].

### Delta vs KOSPI

The substantive trading-hours content matches KOSPI; the deltas are structural rather than parametric:

- **Off-hours section structure.** KOSPI splits the off-hours session into a brief mention in BR §4 + a fuller catalogue in BR §33 (listing the five off-hours trading types: closing-price, single-price, competitive block, block, basket). **KOSDAQ inlines** the off-hours timing directly inside §4.3.2, with cross-references to §20 (off-hours closing-price) and §21-3 (off-hours single-price) for type-specific details. The KOSDAQ BR has no §33 for off-hours-types; that section number is used for account-setup rules instead.
- **Holiday list ordering.** KOSPI BR §5 lists holiday categories as: (1) public holidays, (2) Workers' Day, (3) Saturdays, (4) Dec 31, (5) discretionary. KOSDAQ BR §5 lists: (1) Saturdays, (2) public holidays, (3) Workers' Day, (4) end-of-year 1 day, (5) discretionary. The substance is identical; the wording on the year-end day is also slightly different — KOSPI says "December 31" with an explicit shift rule; KOSDAQ says "연말의 1일간" (*yeon-mal-ui il-il-gan*; "one day at year-end") with a parenthetical that holidays and Saturdays are excluded from the day-count, which produces the same effective shift behaviour.
- **Market-types list (§4.1).** KOSDAQ §4.1 enumerates additional market types not present on KOSPI: 신주인수권증권시장 (*sin-ju-in-su-gwon-jeung-gwon si-jang*; pre-emptive subscription-warrant market), 신주인수권증서시장 (*sin-ju-in-su-gwon-jeung-seo si-jang*; pre-emptive subscription-right-certificate market), and 기업성장집합투자기구 집합투자증권시장 (*gi-eop-seong-jang ji-pap-tu-ja-gi-gu ji-pap-tu-ja-jeung-gwon si-jang*; corporate-growth investment-fund collective-investment-securities market — added 2026-03-04). These run inside the same regular-session timing as the equity market.
- **Quotation receipt windows.** KOSPI sources the granular receipt windows (e.g. 08:30 = 30 min before 장개시; 15:30–16:00 receipt for post-close closing-price; 16:00–18:00 receipt for off-hours single-price) from the **KOSPI Enforcement Rule §11**. The **KOSDAQ Enforcement Rule (시행세칙) is not yet archived** (R6 — see PROJECT_IMPLEMENTATION.md). KOSDAQ-side receipt-window granularity in this file is sourced from the [KRX-TOUR-KOSDAQ-OPS-T1] tour table, which exactly matches the KOSPI Enforcement Rule §11 windows. Treat the windows as authoritative-by-equivalence pending R6 resolution; flag any KOSDAQ-specific divergence at Phase 6 freshness audit.

## Parameters & thresholds

All times in 24-hour KST. All windows match KOSPI; see [KOSPI table](../kospi/market_hours.md#parameters-thresholds) for the same data with KOSPI Enforcement Rule citations.

| Session                                                  | Quotation receipt | Trading       | Source                                    |
|----------------------------------------------------------|------------------:|--------------:|-------------------------------------------|
| Regular session                                          | 08:30–15:30       | 09:00–15:30   | [KRX-RULE-KOSDAQ-BR-KO §4.3.1; KRX-TOUR-KOSDAQ-OPS-T1] |
| Regular session — intraday competitive block             | 09:00–15:00       | 09:00–15:00   | [KRX-RULE-KOSDAQ-BR-KO §4.3.1 + §19-3]    |
| Pre-open off-hours — closing-price trading               | 08:30–08:40       | 08:30–08:40   | [KRX-RULE-KOSDAQ-BR-KO §4.3.2.가 + §20; KRX-TOUR-KOSDAQ-OPS-T1] |
| Pre-open off-hours — block / basket / competitive block  | 08:00–09:00       | 08:00–09:00   | [KRX-RULE-KOSDAQ-BR-KO §4.3.2.가; KRX-TOUR-KOSDAQ-OPS-T1] |
| Post-close off-hours — closing-price trading             | 15:30–16:00       | 15:40–16:00   | [KRX-RULE-KOSDAQ-BR-KO §4.3.2.나 + §20; KRX-TOUR-KOSDAQ-OPS-T1] |
| Post-close off-hours — single-price (call) auction       | 16:00–18:00       | 16:00–18:00   | [KRX-RULE-KOSDAQ-BR-KO §4.3.2.나 + §21-3; KRX-TOUR-KOSDAQ-OPS-T1] |
| Post-close off-hours — block / basket trading            | 15:40–18:00       | 15:40–18:00   | [KRX-RULE-KOSDAQ-BR-KO §4.3.2.나; KRX-TOUR-KOSDAQ-OPS-T1] |

The 15:30–15:40 receipt-only buffer for post-close closing-price trading is reported by [KRX-TOUR-KOSDAQ-OPS-T1] and matches the KOSPI buffer (the same 10-minute pre-trade gap that KOSPI sources from BR Enforcement Rule §11.2.b(1) — see [KOSPI § Edge cases](../kospi/market_hours.md#edge-cases-open-questions)).

## Worked examples

Behaviour mirrors KOSPI — see [KOSPI § Worked examples](../kospi/market_hours.md#worked-examples). The three reject-pattern examples (08:25 KST regular-session order, 15:35 KST off-hours-single-price order, 15:05 KST intraday-competitive-block order) all apply identically to KOSDAQ because the receipt windows are identical.

## Edge cases & open questions

- Edge case: KOSDAQ shares the KOSPI 15:30–15:40 receipt-only buffer for post-close closing-price trading. Until R6 (KOSDAQ Enforcement Rule archive) is resolved, this buffer is sourced only from the tour page; the analogue of KOSPI Enforcement Rule §11.2.b(1) cannot be cited directly.
- Edge case: KOSDAQ §4.3.1 inline phrasing — "오전 9시부터 오후 3시 30분(제18조제1항제2호의 장종료시의 가격을 결정하는 경우에는 오후 3시 30분 이후 당해 가격이 결정되는 시점)까지" — extends the formal end of the regular session past 15:30 *for the limited purpose of fixing the closing price*. This matches KOSPI §4.3.1 phrasing; the implication is that closing-price determination (single-price auction) can clear marginally after 15:30 wall-clock, but no new orders are received after 15:30. The same interpretation applies to KOSPI.
- Edge case: KOSDAQ §4.3.2.나 inline phrasing — "오후 3시 40분부터 오후 6시(최종 가격을 결정하는 경우에는 오후 6시 이후 당해 가격이 결정되는 시점)까지" — applies the same closing-clear extension to the post-close off-hours single-price session. So the *final* off-hours single-price clear may print marginally after 18:00 wall-clock without new orders being accepted.
- Edge case: KOSDAQ §4.1.5 (corporate-growth investment-fund collective-investment-securities market) was added effective 2026-03-04. Its trading hours fall under the same §4.3 timing as the equity market. Whether it has separate receipt-window rules will be visible in the Enforcement Rule once R6 is resolved.
- Open question: The discretionary market-administration day in §5.5 is structurally the same on KOSPI and KOSDAQ; in practice the two markets are typically halted together (a single KRX system event halts both books). Confirm whether there's a regulatory carve-out for KOSDAQ-only halts at Phase 6 freshness audit.

## Sources

- `KRX-RULE-KOSDAQ-BR-KO` — KOSDAQ Market Business Regulation (코스닥시장 업무규정, *ko-seu-dak si-jang eom-mu gyu-jeong*), bookid 210164370, effective 2026-04-28. Articles cited: §2.14 (장개시 anchor), §2.15 (장종료 anchor), §4 (Market division and trading hours; §4.1 market-types list, §4.3 trading-time table inlining off-hours), §5 (Holidays — five categories), §19-3 (Intraday competitive-block reference), §20 (Off-hours closing-price reference), §21-3 (Off-hours single-price reference).
- `KRX-TOUR-KOSDAQ-OPS-T1` — KRX overview "Trading Hours" (KOSDAQ); English, not authoritative. Used for the granular per-trade-type receipt-window table that would normally come from the KOSDAQ Enforcement Rule (R6 unresolved).
