---
title: "Market Hours (KOSPI)"
markets: [KOSPI]
last_reviewed: 2026-04-30
sources:
  - KRX-RULE-KOSPI-BR-KO
  - KRX-RULE-KOSPI-BR-ENFORCE-KO
  - KRX-TOUR-KOSPI-BASIC-T1
---

> See also: [Market Hours (KOSDAQ)](../kosdaq/market_hours.md), [Comparison](../common/comparison.md).

## Summary

- KOSPI regular trading session is 09:00–15:30 KST [KRX-RULE-KOSPI-BR-KO §4.3].
- Quotation receipt for the regular session begins 30 minutes before the open, i.e. 08:30 KST [KRX-RULE-KOSPI-BR-ENFORCE-KO §11.1].
- Off-hours sessions run before (08:00–09:00) and after (15:30–18:00) the regular session, with distinct sub-windows per off-hours trading type [KRX-RULE-KOSPI-BR-ENFORCE-KO §11.2].
- Markets close on Saturdays, public holidays per the Government Office Holidays Regulation, Workers' Day (May 1), December 31, and any day the Exchange designates [KRX-RULE-KOSPI-BR-KO §5].
- KRX may temporarily change trading hours and quotation receipt windows when system failures or market-administration needs require it [KRX-RULE-KOSPI-BR-KO §4.3 proviso; KRX-RULE-KOSPI-BR-ENFORCE-KO §8].

## Detailed rules

### Regular session

The KOSPI Stock Market is divided into a Regular Session (정규시장, *jeong-gyu si-jang*) and an Off-hours Session (시간외시장, *si-gan-oe si-jang*) [KRX-RULE-KOSPI-BR-KO §4.2]. The Regular Session trades from 09:00 to 15:30 KST [KRX-RULE-KOSPI-BR-KO §4.3]. Two anchor points defined by the rules drive most other timing references:

- 장개시 (*jang-gae-si*) — start of the Regular Session, 09:00 KST.
- 장종료 (*jang-jong-ryo*) — end of the Regular Session, 15:30 KST.

These terms are used by reference throughout the Business Regulation and Enforcement Rule whenever sub-session boundaries are defined.

### Off-hours session

The Off-hours Session is composed of five distinct trade types, each with its own receipt window [KRX-RULE-KOSPI-BR-KO §33]:

1. 시간외종가매매 (*si-gan-oe jong-ga mae-mae*) — off-hours closing-price trading (post-only, plus a pre-open variant).
2. 시간외단일가매매 (*si-gan-oe dan-il-ga mae-mae*) — off-hours single-price (call-auction) trading (post-open only).
3. 시간외경쟁대량매매 (*si-gan-oe gyeong-jaeng dae-ryang mae-mae*) — off-hours competitive block trading (pre-open only).
4. 시간외대량매매 (*si-gan-oe dae-ryang mae-mae*) — off-hours block trading.
5. 시간외바스켓매매 (*si-gan-oe ba-seu-ket mae-mae*) — off-hours basket trading.

Receipt windows for each type are set by the Enforcement Rule [KRX-RULE-KOSPI-BR-ENFORCE-KO §11.2] — see *Parameters & thresholds* below.

### Quotation receiving hours

A quotation (호가, *ho-ga*) may only be submitted during the receipt window applicable to the session it targets [KRX-RULE-KOSPI-BR-KO §10.1]. The Business Regulation delegates the specific windows to the Enforcement Rule [KRX-RULE-KOSPI-BR-KO §10.2]. The Enforcement Rule sets [KRX-RULE-KOSPI-BR-ENFORCE-KO §11.1]:

- **Regular session:** from 30 minutes before 장개시 until 장종료, i.e. 08:30–15:30 KST. *Exception:* for intraday competitive block trading (장중경쟁대량매매, *jang-jung gyeong-jaeng dae-ryang mae-mae*), the receipt window is from 장개시 until 30 minutes before 장종료, i.e. 09:00–15:00 KST.
- **Pre-market off-hours and post-market off-hours:** trade-type-specific windows (see *Parameters & thresholds*).

### Holidays and non-trading days

KRX does not conduct trading on any of the following days [KRX-RULE-KOSPI-BR-KO §5]:

1. Public holidays defined by the Regulation on Holidays of Government Offices (관공서의공휴일에관한규정, *gwan-gong-seo-ui gong-hyu-il-e gwan-han gyu-jeong*).
2. Workers' Day (근로자의 날, *geun-ro-ja-ui nal*), May 1.
3. Saturdays.
4. December 31. If December 31 falls on a public holiday or Saturday, the immediately preceding trading day is closed instead.
5. Any other day on which an abrupt change (or expected abrupt change) in economic conditions occurs, or which the Exchange deems necessary for market administration.

Settlement is T+2; member firms must complete settlement with KRX (acting as central counterparty) by 16:00 KST on T+2 [KRX-TOUR-KOSPI-BASIC-T1].

### Authority to change hours

The Exchange may temporarily alter trading hours when system failures or market-administration concerns require it; the procedure is set by the Enforcement Rule [KRX-RULE-KOSPI-BR-KO §4.3 proviso; KRX-RULE-KOSPI-BR-ENFORCE-KO §8]. When trading hours are altered, the Exchange may also alter the corresponding quotation receipt windows [KRX-RULE-KOSPI-BR-ENFORCE-KO §11.2].

## Parameters & thresholds

All times in 24-hour KST.

| Session                                                  | Quotation receipt | Trading       | Source                                       |
|----------------------------------------------------------|------------------:|--------------:|----------------------------------------------|
| Regular session                                          | 08:30–15:30       | 09:00–15:30   | [KRX-RULE-KOSPI-BR-KO §4.3; -ENFORCE-KO §11.1] |
| Regular session — intraday competitive block             | 09:00–15:00       | 09:00–15:00   | [KRX-RULE-KOSPI-BR-ENFORCE-KO §11.1]         |
| Pre-open off-hours — closing-price trading               | 08:30–08:40       | 08:30–08:40   | [KRX-RULE-KOSPI-BR-ENFORCE-KO §11.2.a(1)]    |
| Pre-open off-hours — block / basket / competitive block  | 08:00–09:00       | 08:00–09:00   | [KRX-RULE-KOSPI-BR-ENFORCE-KO §11.2.a(2)]    |
| Post-close off-hours — closing-price trading             | 15:30–16:00       | 15:40–16:00   | [KRX-RULE-KOSPI-BR-ENFORCE-KO §11.2.b(1); KRX-TOUR-KOSPI-BASIC-T1] |
| Post-close off-hours — single-price (call) auction       | 16:00–18:00       | 16:00–18:00   | [KRX-RULE-KOSPI-BR-ENFORCE-KO §11.2.b(2)]    |
| Post-close off-hours — block / basket trading            | 15:40–18:00       | 15:40–18:00   | [KRX-RULE-KOSPI-BR-ENFORCE-KO §11.2.b(3)]    |

The trading-window column above for the post-close closing-price trade shows 15:40 (not the receipt-window start of 15:30); the 10-minute receipt-only gap between 15:30 and 15:40 is reported by the KRX overview tour [KRX-TOUR-KOSPI-BASIC-T1] but is not itself spelled out in §11. See *Edge cases & open questions*.

## Worked examples

- **An order placed at 08:25 KST targeting the regular-session open** is rejected: the 08:30 receipt window has not yet started [KRX-RULE-KOSPI-BR-ENFORCE-KO §11.1].
- **An off-hours single-price trade order placed at 15:35 KST** is rejected: the 16:00–18:00 single-price window has not yet opened [KRX-RULE-KOSPI-BR-ENFORCE-KO §11.2.b(2)]. To trade in the post-close window, the order must be placed at or after 16:00.
- **An intraday competitive block order placed at 15:05 KST** is rejected: although the regular session is still open, the competitive-block receipt window closed at 15:00 [KRX-RULE-KOSPI-BR-ENFORCE-KO §11.1 exception].

## Edge cases & open questions

- Edge case: For post-close closing-price trading, the receipt window starts at 15:30 (immediately at 장종료) but the trading window per the tour starts at 15:40 [KRX-TOUR-KOSPI-BASIC-T1]. The Enforcement Rule §11.2.b(1) sets receipt as "from 장종료시 until 16:00" but does not separately gate trading inside that window. The 10-minute pre-trade buffer is not visible in the rule text we have archived; it likely reflects a system-level batching of orders before matching. Verify against KRX-RULE-KOSPI-BR-ENFORCE-KO §51 (시간외종가매매 specifics) before publishing v1.0.
- Edge case: §11.1's regular-session quotation receipt explicitly extends to 장종료 (15:30), but the Business Regulation §10.1 prohibits quotations outside receipt windows. A quotation submitted at 15:30:00 KST is at the boundary — confirm whether 장종료 is inclusive or exclusive in the rule. (Practical effect: order placed at 15:30:00.000 may be rejected by some systems and accepted by others.)
- Open question: Article 5 lists Saturdays separately from "public holidays per the Government Holidays Regulation". For days that are *both* a Saturday and a public holiday, no shifting rule applies — but Dec 31 has an explicit shift rule when it lands on a public holiday or Saturday. Are there other date-shifting rules elsewhere in the Enforcement Rule that affect the trading calendar (e.g. for split sessions on the last trading day of the year)? Not visible in the articles we have extracted.
- Edge case: The "30 minutes before 장종료" cutoff for intraday competitive block trading is 15:00 KST. This is a hard cutoff for *receipt* of new orders; it does not preclude the matching of already-received orders during the remaining 30 minutes [KRX-RULE-KOSPI-BR-ENFORCE-KO §11.1].

## Sources

- `KRX-RULE-KOSPI-BR-KO` — KOSPI Market Business Regulation (유가증권시장 업무규정, *yu-ga-jeung-gwon si-jang eom-mu gyu-jeong*), bookid 210200859, effective 2026-04-28. Articles cited: §4 (Market Division and Trading Hours), §5 (Holidays), §10 (Quotation Receiving Hours — high-level), §33 (Off-hours Trading types).
- `KRX-RULE-KOSPI-BR-ENFORCE-KO` — KOSPI BR Enforcement Rule (유가증권시장 업무규정 시행세칙, *yu-ga-jeung-gwon si-jang eom-mu gyu-jeong si-haeng se-chik*), bookid 210203562, effective 2026-04-28. Articles cited: §8 (Trading Hours Changes), §11 (Quotation Receiving Hours — specifics), §51 (Off-hours Closing-Price Trading specifics, referenced).
- `KRX-TOUR-KOSPI-BASIC-T1` — *General Procedures of Trading* (KRX English overview), language English, not authoritative. Used only for cross-referencing the 15:40 trading-window start in the post-close closing-price session and for the T+2/16:00 settlement deadline.
