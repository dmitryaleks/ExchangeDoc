---
title: "Trading Rules & Matching (KOSPI)"
markets: [KOSPI]
last_reviewed: 2026-04-30
sources:
  - KRX-RULE-KOSPI-BR-KO
  - KRX-RULE-KOSPI-BR-ENFORCE-KO
  - KRX-TOUR-KOSPI-METHOD-T3
  - KRX-TOUR-KOSPI-OPS-T6
  - KRX-TOUR-KOSPI-TRUST-T1
---

> See also: [Trading Rules (KOSDAQ)](../kosdaq/trading_rules.md), [Order Types (KOSPI)](./order_types.md), [Auctions (KOSPI)](./auctions.md), [Price Ranges (KOSPI)](./price_ranges.md), [Comparison](../common/comparison.md).

## Summary

- KRX matches all on-exchange trades by individual competitive auction (개별경쟁매매, *gae-byeol gyeong-jaeng mae-mae*) — single-price (단일가매매) for the five auction events listed in §23.1, and continuous (복수가매매) at all other times during the regular session [KRX-RULE-KOSPI-BR-KO §22.1, §23, §24]. The detailed matching mechanics are documented in [Auctions (KOSPI)](./auctions.md).
- Default matching priority is **price-then-time** [KRX-RULE-KOSPI-BR-KO §22.2]. A buy market quotation is deemed to sit at 상한가 (*sang-han-ga*; the daily upper price limit) and a sell market at 하한가 (*ha-han-ga*; lower limit) for *price-priority* purposes, making them equal to limits resting at those limits — but execution prices and fill semantics still differ [KRX-RULE-KOSPI-BR-KO §22.2.1].
- Time priority is suspended at the upper/lower price limit for opening, market-resumption, and individual-resumption single-price auctions only — orders at the limit are deemed simultaneous (동시호가, *dong-si-ho-ga*) and allocated by **quantity priority** in three passes per Enforcement Rule §34 [KRX-RULE-KOSPI-BR-KO §22.3]. The closing single-price auction does **not** carry this carve-out — time priority continues to apply.
- Trade types are defined by settlement timing: 보통거래 (*bo-tong geo-rae*; T+2) for ordinary share trades, plus 당일결제거래 (*dang-il gyeol-je geo-rae*; T+0) and 익일결제거래 (*ik-il gyeol-je geo-rae*; T+1) for narrow special cases — all unspecified securities default to T+2 보통거래 [KRX-RULE-KOSPI-BR-KO §7].
- Members must run pre-quote risk checks (호가 사전통제, *ho-ga sa-jeon-tong-je*) covering account, security, quantity, price, stop-price, type, margin, and HSA-ID validity before any quotation reaches the Exchange system [KRX-RULE-KOSPI-BR-KO §11-2; KRX-RULE-KOSPI-BR-ENFORCE-KO §12-2]. The Exchange publishes a 10-deep order book during continuous trading and a 3-deep order book plus expected matching price (예상체결가, *ye-sang che-gyeol-ga*) during single-price auction receipt windows [KRX-TOUR-KOSPI-OPS-T6].

## Detailed rules

### Trade types and settlement timing

Article 7 of the Business Regulation defines three categories of trade by settlement-day offset [KRX-RULE-KOSPI-BR-KO §7.1]:

1. **당일결제거래 (T+0)** — settled the same day. Used for narrow rule-specified cases (e.g. block-trade and basket-trade settlement variants).
2. **익일결제거래 (T+1)** — settled the next trading day.
3. **보통거래 (T+2)** — the default; settled two trading days after the trade. Holidays are excluded from the day-count [KRX-RULE-KOSPI-BR-KO §7.2].

Unless the Enforcement Rule specifies otherwise for a particular security or trade-type, **every listed-securities trade defaults to T+2 보통거래** [KRX-RULE-KOSPI-BR-KO §7.4]. KRX may shift the settlement date when natural disaster, war, sudden economic change, or system failure prevents normal settlement [KRX-RULE-KOSPI-BR-KO §7.3].

### Quotation flow — receipt, recording, pre-quote control

A member submits a quotation by inputting it into the Exchange system on a per-account basis, with proprietary and customer flow segregated and buy/sell separated [KRX-RULE-KOSPI-BR-KO §9.1]. The Exchange records each accepted quotation in receipt order, immediately, in the system [KRX-RULE-KOSPI-BR-KO §14.1]. Receipt order is the input sort key for everything downstream — time priority under §22.2.2 reads from this record.

Before a quotation reaches the Exchange system, the member must run a **pre-quote conformance check** (호가 사전통제) per [KRX-RULE-KOSPI-BR-KO §11-2.1]. The Enforcement Rule §12-2 enumerates the mandatory check items [KRX-RULE-KOSPI-BR-ENFORCE-KO §12-2]:

1. **Account fields** — account number; account type (proprietary / consigned).
2. **Security fields** — ticker code; whether the security is suspended from trading per §26, §49, the Listing Regulation, or the Disclosure Regulation.
3. **Quantity fields** — trading-lot conformance (§33); per-quotation quantity limit (§14.1.3); LP-quote quantity limit (§31-6.4-5); treasury-stock quantity limit (§57.1.3); debt-securities quantity limits (§14.1.4).
4. **Price fields** — tick conformance (§32.2); daily price-limit conformance (§20); short-sale price restriction (§14.1.1, §14.1.2-3); LP-quote price restriction (§20-5.1); treasury-stock price restriction (§35.5, §39.1).
5. **Stop-price fields** *(added 2025-02-27)* — stop-price within the daily price-limit band (§14.1.2-4.a); stop-price on a tick (§14.1.2-4.b).
6. **Quotation-type fields** — type permitted for the security category (§10.1); per-type × per-situation restrictions (§14.2).
7. **Margin fields** — consignment-margin requirements (§89); ELW basic-deposit (§87-2).
8. **HSA fields** — for high-speed-algorithmic-trading-flagged quotations: HSA account registration (§104-3.3); HSA ID match between the registered account and the input field.
9. **Market-administration fields** — KRX-imposed restrictions per consigner or per security.
10. **Other fields** — anything the member deems necessary.

The member must submit the quotation immediately after the pre-quote check passes [KRX-RULE-KOSPI-BR-KO §11-2.2]. A quotation that fails any check is not transmitted to the Exchange.

The pre-quote check is **bypassed** when the member uses a member-securities-terminal (회원증권단말기, *hoe-won jeung-gwon dan-mal-gi*) — i.e. a directly-attached emergency input device used when the normal member-system has failed [KRX-RULE-KOSPI-BR-KO §9.4].

### Cancellation, correction, and disconnect-cancel

Cancellation and correction apply only to the unfilled portion of an existing quotation [KRX-RULE-KOSPI-BR-KO §13.1]. The behavioral rules are documented in [Order Types — Cancellation and correction](./order_types.md#cancellation-and-correction-of-quotations); this section adds two trading-rules-specific items:

- **Disconnect-cancel (접속해제 호가취소, *jeop-sok-hae-je ho-ga chwi-so*)** — when the member-system loses its connection to the Exchange system, the member may pre-register a "disconnect-cancel" rule that triggers a bulk cancel of a defined range of quotations on disconnect [KRX-RULE-KOSPI-BR-KO §13-2.1]. The member nominates the rule in advance via the procedure in the Enforcement Rule §17-2; on disconnection the Exchange applies the cancel automatically. (Re-enrolled in 2022-12-07 as part of the post-2022 algorithmic-trading framework.)
- **Halt-period quotations** — quotations submitted during a market-wide halt (§6), individual-issue halt (§25, §26, §49, §50, §107), or disclosure-driven halt are not given effect — but a **cancel** quotation submitted during the halt is honored [KRX-RULE-KOSPI-BR-ENFORCE-KO §13.1.1]. So a member can clean up its book during a halt even though no new resting orders are accepted.

### Order priority — the §22 hierarchy

Article 22 of the Business Regulation is the matching-priority spec. The hierarchy has three levels, in order:

1. **Price priority** [KRX-RULE-KOSPI-BR-KO §22.2.1].
   - A lower-priced ask outranks a higher-priced ask.
   - A higher-priced bid outranks a lower-priced bid.
   - **Market-vs-limit equivalence at price limits:** A buy market quotation is deemed to sit at the daily upper price limit (상한가) for price-priority purposes — equal to a buy limit at 상한가. A sell market quotation is deemed at the daily lower price limit (하한가) — equal to a sell limit at 하한가. (This is a price-*priority* equivalence only; the actual *execution price* of a market order is computed separately per §23.3 / §24.2 — see [Auctions § Limit-orders-vs-market-orders](./auctions.md#order-priority-and-same-price-tie-breaking) and the worked example in [Price Ranges § Limit orders vs market orders at price limits](./price_ranges.md#limit-orders-vs-market-orders-at-price-limits).)
2. **Time priority** [KRX-RULE-KOSPI-BR-KO §22.2.2]. Among same-price quotations (and among multiple market quotations on the same side), the earlier-received quotation outranks the later. Receipt time is the system-recorded time per §14.1.
3. **동시호가 quantity priority — narrow carve-out** [KRX-RULE-KOSPI-BR-KO §22.3]. When the matching price of a single-price auction is set **at the daily upper or lower price limit**, time priority is *suspended* for orders at that limit. Those orders are deemed simultaneous (동시호가) and allocated by quantity-priority per Enforcement Rule §34 (see *Quantity allocation* below).

The §22.3 carve-out applies **only to** the single-price auctions of items 1–3 of §23.1 — opening price (시가), market-wide-resumption first price, and individual-issue-resumption first price. The closing single-price (item 4) and the trade-execution-method-change first price (item 5) **do not** trigger §22.3, and time priority continues to apply at the limit.

For the special case of stop-limit quotations: once activated, a stop-limit's time priority for §22.2.2 uses its **original receipt time**, not the activation moment [KRX-RULE-KOSPI-BR-ENFORCE-KO §15-2.2]. See [Order Types § Stop-limit activation](./order_types.md#stop-limit-activation).

### Quantity allocation at price limits

When §22.3 applies, the Enforcement Rule §34 sets a three-pass quantity-priority allocation that proceeds from the largest-quantity order to the smallest [KRX-RULE-KOSPI-BR-ENFORCE-KO §34]:

1. **First pass** — to each eligible order: up to **100 × the trading lot** (매매수량단위).
2. **Second pass** — to each eligible order with remaining unfilled balance: **half** of that remaining balance, rounded to the trading-lot grain.
3. **Third pass** — the residual quantity flows to the same priority sequence (largest order first) until the matched quantity is exhausted.

The fully worked example with KRW 20,150 upper-limit allocation is in [Auctions § Example B — quantity allocation at the upper price limit](./auctions.md#example-b-quantity-allocation-at-the-upper-price-limit).

### Matching algorithms — single-price and continuous

The single-price (§23) and continuous (§24) matching algorithms are documented in detail in [Auctions (KOSPI)](./auctions.md). The trading-rules-specific notes:

- **Single-price (§23.4):** finds the equilibrium where cumulative ask quantity = cumulative bid quantity. All orders strictly inside the price (asks below, bids above) fill in full; at the equilibrium price, one side fills entirely, the other fills to the matching quantity in §22 priority order. Tie-break for multiple matching prices: closeness to the previous price (직전의 가격 / 기세), with sub-rules for above/below/within the matching range [KRX-RULE-KOSPI-BR-KO §23.5].
- **Continuous (§24.1, §24.3):** triggered by a price-overlap (lowest ask ≤ highest bid). The trade prints at the price of the **earlier-entered order** (선행호가, *seon-haeng-ho-ga*; "leading quote") — i.e. the resting order's price, not the incoming order's price [KRX-RULE-KOSPI-BR-KO §24.3]. Worked examples in [KRX-TOUR-KOSPI-METHOD-T3] (incoming bid takes the resting ask price; incoming sell takes the resting bid price; etc.) — which mirror §24.3.

The leading-quote rule is the practical interpretation of §22.2.2's time-priority for continuous trading: the resting order's time wins, so its price becomes the print.

### Self-match prevention

Self-match-prevention (자전거래방지조건) is available as a quotation condition only to high-speed-algorithmic traders (HSA) who share an HSA ID across the two opposite-side quotations [KRX-RULE-KOSPI-BR-ENFORCE-KO §13-2]. Three sub-modes are member-selectable: cancel-the-older, cancel-the-newer, cancel-the-matchable-quantity-each-side. See [Order Types § Quotation conditions](./order_types.md#quotation-conditions-ioc-fok-self-match-prevention) for the detail.

The trading-rules-specific notes:

- The mechanism is **active only during continuous matching** (§24); it is suspended during 단일가매매 single-price auctions and during 동시호가 simultaneous-quotation matching at price limits [KRX-RULE-KOSPI-BR-ENFORCE-KO §13-2.2].
- When SMP and IOC are both attached to a quotation, **SMP runs first** [KRX-RULE-KOSPI-BR-ENFORCE-KO §13-2.3]. So an HSA-tagged IOC that would have self-matched is cancelled-by-SMP before its IOC condition fires.
- SMP is **not** the same as a member-side wash-trade prevention. The Exchange enforces only HSA-ID-keyed prevention; non-HSA traders rely on member-side cancel-then-replace logic, and the only rule-level enforcement of self-trading prohibition is the conduct-rule in the FSC's Market Misconduct Notice (not the trading rule).

### Lot size, quote-quantity unit, and tick

The lot, quote-quantity, and tick schedules are documented in [Price Ranges § Tick size, quote-quantity unit, and trading lot](./price_ranges.md#tick-size-and-quote-quantity-unit). Trading-rules-specific notes:

- The trading lot (매매수량단위) is the granularity at which a *trade* is sized; the quote-quantity unit (호가수량단위, *ho-ga su-ryang dan-wi*) is the granularity at which a *quotation* is sized [KRX-RULE-KOSPI-BR-ENFORCE-KO §32.1, §33.1]. For nearly all securities the two are 1 share / 1 cert / 1 unit; only ELWs differ — they may be quoted in single certs but trade in lots of 10 [KRX-RULE-KOSPI-BR-ENFORCE-KO §33.1.5-2].
- KRX may temporarily adjust the trading lot when quote flooding (호가폭주, *ho-ga-pok-ju*) threatens system load; any adjustment is pre-announced [KRX-RULE-KOSPI-BR-ENFORCE-KO §33.3, §33.5].
- Member pre-quote checks must reject a quotation whose quantity is not a multiple of the trading lot (§12-2.3.a) and whose price is not on a tick (§12-2.4.a). These rejections happen at the member system; they never reach the Exchange.

### Algorithmic and high-speed-algorithmic trading

Article 2 of the Business Regulation defines two categories of automated trading [KRX-RULE-KOSPI-BR-KO §2.21–2.22]:

- **Algorithmic trading (알고리즘거래, *al-go-ri-jeum geo-rae*)** — rule-based investment decision and quotation generation/submission performed by an automated system without human intervention, for any security other than those excluded by the Enforcement Rule.
- **High-speed algorithmic trading (고속 알고리즘거래)** — algorithmic trading where (a) the consigner's dedicated order system is owned or directly controlled by the consigner, **and** (b) the order system is housed inside the member's data-center building [KRX-RULE-KOSPI-BR-KO §2.22.1–.2]. This is the KRX colocation framework.

A high-speed algorithmic trader (고속 알고리즘거래자) must register with KRX under §104-3 before submitting any HSA-tagged quotation [KRX-RULE-KOSPI-BR-KO §2.23]. Registered HSA IDs are checked at member-side pre-quote conformance (§12-2.7) and again at the Exchange. SMP (§13-2) is available only to HSA-registered traders.

### Quotation-information disclosure (depth-of-book)

KRX publishes the depth-of-book on a real-time basis during quotation receipt hours [KRX-TOUR-KOSPI-OPS-T6]:

- **Continuous trading:** **10 levels** of best bids and best asks, with the quantity at each level. Disclosure runs continuously during the regular session.
- **Single-price auction (during the receipt window):** **3 levels** of best bids and best asks, with the quantity at each level, **plus** an expected matching price (예상체결가, *ye-sang che-gyeol-ga*) and expected matching quantity. The full 10-level cumulative totals were withdrawn 2002-09-30 in favor of the EAP figure.
- **Opening auction receipt window (08:30–09:00):** disclosure begins **10 minutes after** the receipt window opens — i.e. 08:40 KST — to prevent gaming on early-arrived orders [KRX-TOUR-KOSPI-OPS-T6].

The 10-deep depth applies only to the standard continuous order book. A-Blox order books are not published — only a per-security buy/sell-existence indicator is disclosed (see [Auctions § A-Blox](./auctions.md#a-blox-auction-based-block-trade)).

### Member-customer order channels

Members may accept consigned orders through three channels [KRX-TOUR-KOSPI-TRUST-T1]:

1. **Written orders** — paper order slip signed by the consigner at a branch.
2. **Phone orders** — telephone, telegram, or fax; the member prepares and signs an order slip and may also record the call as evidence.
3. **Electronic communication (home trading / HTS)** — consigner submits via PC/mobile; the order is transmitted directly into the member's order-management system without member personnel handling it.

After execution, the member must immediately notify the consigner by phone or electronic communication [KRX-TOUR-KOSPI-TRUST-T1]. These channel rules are operational background; they do not affect the matching priority or settlement timing inside KRX.

## Parameters & thresholds

### Trade types

| Trade type           | Korean              | Settlement offset | Default for                                               | Source                          |
|----------------------|---------------------|------------------:|-----------------------------------------------------------|---------------------------------|
| 당일결제거래          | dang-il gyeol-je    |              T+0  | Specific block / basket variants per Enforcement Rule     | [KRX-RULE-KOSPI-BR-KO §7.1.1]   |
| 익일결제거래          | ik-il gyeol-je      |              T+1  | Specific securities per Enforcement Rule                  | [KRX-RULE-KOSPI-BR-KO §7.1.2]   |
| 보통거래              | bo-tong geo-rae     |              T+2  | All listed-securities trades unless otherwise specified   | [KRX-RULE-KOSPI-BR-KO §7.1.3, §7.4] |

### §22 priority levels

| Level | Rule                                                       | Article                                  |
|-------|------------------------------------------------------------|------------------------------------------|
| 1     | Price priority (lower ask / higher bid wins)               | [KRX-RULE-KOSPI-BR-KO §22.2.1]           |
| 1a    | Market = limit-at-limit for price priority only            | [KRX-RULE-KOSPI-BR-KO §22.2.1 proviso]   |
| 2     | Time priority among same-price (and among markets)         | [KRX-RULE-KOSPI-BR-KO §22.2.2]           |
| 3     | 동시호가 quantity priority — single-price auction at limit, items 1–3 of §23.1 only | [KRX-RULE-KOSPI-BR-KO §22.3; -ENFORCE §34] |

### Quotation-information disclosure

| Phase                              | Levels disclosed (each side)         | Extra fields                          | Disclosure starts        | Source                           |
|------------------------------------|--------------------------------------|---------------------------------------|--------------------------|----------------------------------|
| Continuous trading                 | 10 best                              | Total per side                        | At session start         | [KRX-TOUR-KOSPI-OPS-T6]          |
| Single-price auction (receipt)     | 3 best                               | Expected matching price + quantity    | Throughout receipt window| [KRX-TOUR-KOSPI-OPS-T6]          |
| Opening single-price (08:30–09:00) | 3 best                               | Expected matching price + quantity    | 08:40 (10 min delay)     | [KRX-TOUR-KOSPI-OPS-T6]          |
| A-Blox                             | 0                                    | Buy/sell-existence indicator only     | n/a                      | [KRX-TOUR-KOSPI-EXCEPT-T4 — see auctions.md] |

## Worked examples

### Example A — continuous matching with three resting orders

(Adapted from [KRX-TOUR-KOSPI-METHOD-T3] Example 1. Tick size assumed KRW 100.)

The book before the new ask arrives:

| Asks | Price (KRW) | Bids |
|-----:|------------:|-----:|
|      |      10,600 |      |
|      |      10,500 |      |
| ② 200 |     10,400 |      |
|      |      10,300 | ① 200 |
| ③ 200 |     10,200 |      |

Asks ② (10,400) and ③ (10,200) are both willing to sell. Bid ① (10,300) is willing to buy. There is a price overlap: ask ③ (10,200) ≤ bid ① (10,300). The trade matches at the **price of the earlier-entered order** [KRX-RULE-KOSPI-BR-KO §24.3] — bid ① arrived before ask ③, so the print is at **KRW 10,300**, ① with ③, 200 shares.

Note: the leading-quote rule is what gives §24 its time-priority effect. If the same orders arrived in a different sequence (ask ③ first, then bid ①), the print would have been at KRW 10,200 instead — bid ① would be the incoming, ask ③ the resting, leading price = ask's 10,200.

### Example B — pre-quote control rejecting a malformed stop-limit

A member's pre-quote system receives a buy stop-limit with stop price KRW 10,005 and limit price KRW 10,010 on an ordinary share whose tick at this band is KRW 10. The pre-quote check runs through §12-2's items in order [KRX-RULE-KOSPI-BR-ENFORCE-KO §12-2]:

1. Account, security, quantity all valid.
2. Price (10,010) — on a tick (10,010 ÷ 10 = 1,001), passes §12-2.4.a.
3. Daily price-limit — assume base price 9,000, upper limit 11,700, lower limit 6,300. 10,010 inside the band → §12-2.4.b passes.
4. **Stop-price (10,005) — not on a tick (10,005 ÷ 10 = 1,000.5).** Fails §12-2.4-2.b ([KRX-RULE-KOSPI-BR-ENFORCE-KO §14.1.2-4.b]).

The member rejects the quotation; nothing is sent to the Exchange. The consigner sees a rejection from the member's order-management system, not from KRX. This is the design intent of §11-2 — surface input errors at the member, not at the venue.

### Example C — disclosure timing on the opening auction

A passive participant watching the opening auction receipt window (08:30–09:00 KST) sees:

- 08:30:00 — receipt window opens; quotations begin to arrive. **No depth-of-book data is published yet** [KRX-TOUR-KOSPI-OPS-T6].
- 08:40:00 — depth-of-book disclosure begins. The first published snapshot shows 3 best bids and 3 best asks (each with quantity), plus the expected matching price (예상체결가) and expected matching quantity computed from the orders received in the first 10 minutes.
- 08:40:00 → 09:00:00 — the disclosure refreshes in real time as new orders arrive and as cancels/corrects modify the book.
- 09:00:00 → up to 30 s — random-end window per [KRX-RULE-KOSPI-BR-ENFORCE-KO §35.1] (see [Auctions § Random-end mechanism](./auctions.md#random-end-mechanism)). Disclosure continues to refresh during the random extension.
- 09:00:00 + random-end-tick — auction clears; the matching price prints; continuous trading begins; the order book switches to 10-deep disclosure.

The 10-minute disclosure delay at the opening (but **not** at any of the other single-price events of §23.1) is the only KRX disclosure-curtain in the regular session.

## Edge cases & open questions

- Edge case: §22.3's quantity-priority carve-out applies only to **single-price auctions** of items 1–3 of §23.1 (opening, market-resumption, individual-resumption) when the matching price equals 상한가 or 하한가. If the matching price is *one tick inside* the limit, time priority continues to apply — even though many participants may have been queued at the limit during the receipt window. The mode switch is binary on the matching-price-equals-limit condition.
- Edge case: §22.3 does not list the closing single-price auction (§23.1.4). Implication: a closing auction that prints at the upper limit does **not** trigger 동시호가 — time priority continues. This is asymmetric with the opening auction, where the same outcome would invoke quantity priority. Verify the practical effect by reviewing closing-call execution audits before relying on a particular fill model.
- Edge case: The 10-minute disclosure curtain at the opening auction (08:30–08:40) applies only to the public depth-of-book feed. Members continue to see their own resting quotations and can adjust them; the curtain hides the *aggregate* book from the consumer feed, not the private-order view. Algorithms that condition on the public expected-matching-price feed must therefore wait until 08:40 to receive a usable signal.
- Edge case: The member-side pre-quote check (§11-2) runs synchronously before transmission, but the Enforcement Rule §12-2's emergency-input proviso (§9.4) explicitly bypasses it when the member uses a 회원증권단말기. So in a member-system-failure scenario, the pre-quote control is *off* — the Exchange's own input-validation (§14) becomes the only gate. Members operating with both normal and emergency channels should cross-check that any rejection logic encoded only in pre-quote is also encoded server-side.
- Open question: §13-2.3's SMP-then-IOC ordering is well-defined, but the rule does not specify the ordering when SMP and FOK are both attached. Treating SMP as first-applied (consistent with §13-2.3) implies that if SMP cancels part of the quotation, the surviving FOK condition would test fillability against the *remaining* quantity. Verify against the FSC implementation guide before designing HSA strategies that combine SMP and FOK.
- Open question: §104-3 HSA registration (referenced but not extracted here) gates SMP eligibility. Whether a non-HSA member's algorithmically-generated quotations can be tagged as 알고리즘거래 (BR §2.21) without HSA registration — and what reporting obligations apply — is in §104-2 (referenced from §104-3) and not yet pulled into this document.
- Unsourced claim: [KRX-TOUR-KOSPI-OPS-T6] notes that the "expansion to 10 stage preferential offer price" was effective 2002-01-02 and the "publication of expected agreed price" was added 2002-09-30. The rulebook does not preserve these historical dates. Treat as overview color.

## Sources

- `KRX-RULE-KOSPI-BR-KO` — KOSPI Market Business Regulation (유가증권시장 업무규정, *yu-ga-jeung-gwon si-jang eom-mu gyu-jeong*), bookid 210200859, effective 2026-04-28. Articles cited: §2 (Definitions, including 알고리즘거래 and 고속 알고리즘거래), §7 (Trade types and settlement offsets), §9 (Quotation methods, including emergency input), §11-2 (Member pre-quote control), §13 (Cancel and correct), §13-2 (Disconnect-cancel), §14 (Recording in receipt order), §22 (Priority — price, time, 동시호가 carve-out), §23 (Single-price auction — referenced for §22.3 scope), §24 (Continuous matching — leading-quote rule), §104-3 (HSA-trader registration — referenced).
- `KRX-RULE-KOSPI-BR-ENFORCE-KO` — KOSPI BR Enforcement Rule (유가증권시장 업무규정 시행세칙, *yu-ga-jeung-gwon si-jang eom-mu gyu-jeong si-haeng se-chik*), bookid 210203562, effective 2026-04-28. Articles cited: §12-2 (Pre-quote check items — full enumerated list), §13 (Quotation effect — halt-period cancel-only behavior), §13-2 (Self-match-prevention; SMP-before-IOC ordering), §14 (Input restrictions — referenced for §12-2 cross-checks), §15-2 (Stop-limit time-priority retention — referenced for §22.2.2 interaction), §32 (Quote-quantity unit and tick), §33 (Trading lot), §34 (Quantity allocation at price limits — three-pass algorithm), §35 (Single-price receipt windows including random-end — referenced).
- `KRX-TOUR-KOSPI-METHOD-T3` — KRX overview "Execution Method for Continuous Trading"; English, not authoritative. Used for the leading-quote-price worked example (Example A) and the descriptive framing of §24.3.
- `KRX-TOUR-KOSPI-OPS-T6` — KRX overview "Publication of Quotation Information"; English, not authoritative. Used for the depth-of-book disclosure parameters (10-deep continuous, 3-deep auction + EAP), and for the 08:40 disclosure-start at the opening auction (10-minute curtain).
- `KRX-TOUR-KOSPI-TRUST-T1` — KRX overview "Method of consigning order"; English, not authoritative. Used for the member-customer order-channel summary (written / phone / HTS) and the post-execution notification requirement.
