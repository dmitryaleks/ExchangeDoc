---
title: "Short Selling (KOSDAQ)"
markets: [KOSDAQ]
last_reviewed: 2026-05-01
sources:
  - KRX-RULE-KOSDAQ-BR-KO
  - KRX-TOUR-KOSDAQ-EXCEPT-T7
---

> See also: [Short Selling (KOSPI)](../kospi/short_selling.md), [Order Types (KOSDAQ)](./order_types.md), [Trading Rules (KOSDAQ)](./trading_rules.md), [Comparison](../common/comparison.md).

**Delta file.** KOSDAQ short-selling substance is **substantively identical** to KOSPI: same FSCMA §180 framework (naked prohibited, covered allowed), same 8-case "deemed-not-short" carve-out list, same four-step member duty cycle (identify / verify / refuse / flag), same deemed-verification opt-out path with 120-day breach reset, same uptick rule with the uptick-exception (must be above the immediately preceding price; may be at it if the immediately preceding price was an uptick), same 40/80/120-day post-management escalation matrix with the same KRW 5억 / 10억 thresholds. The deltas are: (1) **article-numbering remap** (KOSDAQ §9-2/§9-3/§9-4 vs KOSPI §17/§18/§18-2); (2) **§9-2.1.3.나 narrower scope** — KOSDAQ uses "corporate-growth-investment-fund collective-investment securities" (added 2026-03-04) where KOSPI §17.1.3.b uses "ETFs"; (3) **§9-3.2 LP-hedging exemptions cross-reference KOSPI BR §20-2** (since ELWs only list on KOSPI; KOSDAQ-side LPs hedging KOSDAQ ETFs face a possible rule gap — see *Detailed rules § Delta vs KOSPI*); (4) granular Enforcement-Rule items (per-quotation pre-quote check articles, KRX-discretionary restriction details) cannot be cited authoritatively until R6 resolves. This file points to the [KOSPI write-up](../kospi/short_selling.md) for shared content.

## Summary

- The Capital Markets Act (FSCMA) §180 defines short selling (공매도, *gong-mae-do*) in two forms: **naked short** (무차입공매도, *mu-cha-ip gong-mae-do*) — prohibited — and **covered short** (차입공매도, *cha-ip gong-mae-do*) — allowed subject to flagging-and-verification + uptick rule [KRX-TOUR-KOSDAQ-EXCEPT-T7; KRX-RULE-KOSDAQ-BR-KO §9-2].
- **§9-2 carve-outs:** 8 cases of "deemed-not-short" sales (purchase-not-yet-settled, rights exercise / new issue / stock dividend, third-party-custody verified, ETF additional issuance / redemption, DR-deposit-contract termination, lent-securities-return-confirmed, off-exchange delivery, post-close-buy-agreement same-day) [KRX-RULE-KOSDAQ-BR-KO §9-2.1].
- **§9-2 four-step member duty cycle:** identify (consigner declaration), verify (borrow contract + settlement feasibility), refuse (if settlement risk), flag (to KRX at receipt and submission) [KRX-RULE-KOSDAQ-BR-KO §9-2.2 / §9-2.3].
- **§9-2.4 deemed-verification opt-out path:** consigner written undertaking + member system-block = deemed verification; if breached, the member must perform the full verification cycle for **120 days** following the breach discovery [KRX-RULE-KOSDAQ-BR-KO §9-2.4].
- **§9-3 uptick rule:** covered short must price **above the immediately preceding price**; may price **at** it if that price was an uptick relative to the next-prior price. 8-case categorical exemption list mirroring KOSPI §18.2 [KRX-RULE-KOSDAQ-BR-KO §9-3].
- **§9-4 post-management escalation:** **40 / 80 / 120 trading days** of mandatory pre-deposit (사전납부, *sa-jeon-nap-bu*) for naked-short violators, parameterized over (violation days × cumulative violation amount), with KRW 5억 / 10억 thresholds — **identical numeric matrix to KOSPI §18-2.4** [KRX-RULE-KOSDAQ-BR-KO §9-4].

## Detailed rules

For full prose on the FSCMA §180 framework, the four-step member duty cycle, the deemed-verification opt-out path, the uptick rule and its exception, the eight categorical exemptions, the post-management escalation by tier, and the FSC-level reporting/disclosure obligations under FSCMA §180-2 / §180-3, see [KOSPI § Detailed rules](../kospi/short_selling.md#detailed-rules). The KOSDAQ articles map directly:

| KOSDAQ BR article | KOSPI BR article | Topic                                                              |
|-------------------|------------------|--------------------------------------------------------------------|
| §9-2              | §17              | Short-sale quotation restriction (naked-prohibited; 8-case carve-outs; 4-step member duties; deemed-verification path) |
| §9-2.1            | §17.1            | 8-case "deemed-not-short" carve-out list                            |
| §9-2.2 / §9-2.3   | §17.2 / §17.3    | Member duty cycle: identify, verify, refuse, flag                    |
| §9-2.4            | §17.4            | Deemed-verification opt-out + 120-day breach reset                   |
| §9-3              | §18              | Uptick rule (must price above immediately preceding price; uptick-exception); §9-3.2 = §18.2 categorical exemptions |
| §9-4              | §18-2            | Post-management — 40/80/120-day pre-deposit escalation matrix       |

### Delta vs KOSPI

#### §9-2.1.3.나 narrower scope — corporate-growth-investment-fund securities, not ETFs

KOSDAQ §9-2.1.3.나 reads:

> "**상장된 기업성장집합투자기구 집합투자증권의 추가발행에 따라 받게 될 집합투자증권의 매도**" *(open issue 2026-03-04)*

Translation: "Sale of corporate-growth-investment-fund collective-investment securities to be received from additional issuance." The 2026-03-04 amendment (added in lockstep with the §2.21 definition of corporate-growth-investment-fund securities) replaces an older ETF-style carve-out.

KOSPI §17.1.3.b reads:

> "Selling additional ETF units to be received from issuer."

So:

- **KOSDAQ §9-2.1.3.나:** scope = corporate-growth-investment-fund collective-investment securities (a KOSDAQ-only security class — they don't list on KOSPI).
- **KOSPI §17.1.3.b:** scope = ETF additional issuance.

ETF additional-issuance carve-out on KOSDAQ moves to a **different sub-paragraph** of §9-2.1.3 — likely §9-2.1.3.다 (which references "법 제234조에 따른 상장지수집합투자기구 집합투자증권... 환매청구에 따라 받게 될 상장증권의 매도", *sale of listed securities to be received via ETF redemption*). So the §17.1.3.b ETF-issuance carve-out on KOSPI maps to §9-2.1.3.다 on KOSDAQ (ETF-redemption-resale only) plus the existing carve-outs that already cover ETF additional issuance via the §234-route. The two markets reach the same effective coverage but via different sub-paragraph allocations.

For an execution algo, the practical effect is unchanged — both markets allow ETF-related sales to be classified as not-short. The structural difference matters only when citing the exact article number for compliance purposes.

#### §9-3.2 LP-hedging exemptions cross-reference KOSPI BR §20-2

KOSDAQ §9-3.2.5 / 6 / 6-2 / 7 enumerate uptick-rule exemptions for LP-hedging cases. The wording explicitly references **KOSPI's** §20-2 LP framework rather than KOSDAQ's own §12-2 LP framework:

- §9-3.2.5: "유가증권시장에 상장된 주식워런트증권에 대하여 「유가증권시장 업무규정」 제20조의2제1항에 따라 유동성공급호가를 제출하는 회원이..." — **KOSPI-market ELW LPs** hedging by selling KOSDAQ-side basic stock.
- §9-3.2.6: "상장지수집합투자기구 집합투자증권에 대하여 「유가증권시장 업무규정」 제20조의2제1항에 따라 유동성공급호가를 제출하는 회원이..." — **KOSPI-market ETF LPs** hedging by selling KOSDAQ-side basic stock.
- §9-3.2.6-2: "상장지수증권에 대하여 「유가증권시장 업무규정」 제20조의2제1항에 따라 유동성공급호가를 제출하는 회원이..." — **KOSPI-market ETN LPs** hedging by selling KOSDAQ-side basic stock.
- §9-3.2.7: 파생상품시장 §83 derivatives market-makers hedging by selling KOSDAQ-side basic stock.

This cross-market structure makes sense for **ELWs** (which only list on KOSPI — KOSDAQ has no ELWs) and partially for **ETFs / ETNs** (most ETFs / ETNs are KOSPI-listed; KOSDAQ has some). But KOSDAQ-listed ETFs are LP-supported by **KOSDAQ-side LPs registered under KOSDAQ BR §12-2 to §12-6**, not KOSPI BR §20-2. The §9-3.2.6 exemption may **not** apply to a KOSDAQ-LP hedging a KOSDAQ-listed ETF.

There are two possible readings:

- **Strict reading:** §9-3.2.6 applies only to KOSPI-LP hedging (per the explicit "유가증권시장 업무규정 제20조의2" reference). KOSDAQ-LP hedging KOSDAQ-listed ETFs is not exempt under §9-3.2.6 — KOSDAQ-LP short hedges face the §9-3.1 uptick rule.
- **Broader reading:** the §9-3.2.6 reference to "ETF LPs" is intended to cover both KOSPI- and KOSDAQ-side LPs equivalently; the KOSPI cross-reference is a drafting artefact from when KOSDAQ had no LP framework of its own. This reading would mean KOSDAQ ETF LPs are also exempt.

The KOSDAQ tour [KRX-TOUR-KOSDAQ-EXCEPT-T7] does not disambiguate. The conservative compliance posture is the strict reading: a KOSDAQ-LP hedging by selling underlying KOSDAQ stock should **not** rely on the §9-3.2.6 exemption without explicit KRX guidance. Phase 6 freshness audit should clarify with KRX market administration.

#### §9-2.4 deemed-verification path — same 120-day breach reset as KOSPI

KOSDAQ §9-2.4 reads:

> 제3항에도 불구하고 회원이 위탁자로부터 차입공매도 주문을 제출하지 아니한다는 확약을 받고 해당 위탁자 계좌에 대해 차입공매도 주문이 제출되지 않도록 전산조치를 한 경우에는 제2항제1호나목에 따른 확인을 이행한 것으로 본다. 다만, 위탁자가 해당 계좌에서 공매도를 한 경우 회원은 그 사실을 안 날의 다음 매매거래일부터 **120일간** 제3항의 방법으로 제2항제1호나목에 따른 확인을 하여야 한다.

Translation: a consigner who provides written confirmation that no short orders will be submitted, plus a member-side system-level block, is treated as having satisfied the verification requirement. If the consigner subsequently breaches the no-short undertaking, the member must perform the full verification cycle for **120 trading days** from the day after the breach is discovered. **Identical to KOSPI §17.4** in both substance and the 120-day duration.

#### §9-3.1 uptick rule and uptick exception — verbatim parallel to KOSPI §18.1

KOSDAQ §9-3.1 reads:

> 회원이 차입공매도를 하거나 그 위탁을 받아 호가를 제출하는 경우에는 직전의 가격 이하의 가격으로 호가할 수 없다. 다만, 직전의 가격이 그 직전의 가격(직전의 가격과 다른 가격으로서 가장 최근에 형성된 가격을 말한다)보다 높은 경우에는 직전의 가격으로 호가할 수 있다.

Translation: "A covered short shall not be quoted at a price equal to or below the immediately preceding price. Provided that, where the immediately preceding price is higher than the price formed before it, a covered short may be quoted at the immediately preceding price." Same wording as KOSPI §18.1 — the proviso for the uptick exception is identical. Same minimum-permitted-short-price logic; same mid-price comparator (per [KRX-TOUR-KOSDAQ-EXCEPT-T7] confirming the rule applies the same way as KOSPI).

#### §9-4 escalation matrix — identical numeric thresholds to KOSPI §18-2.4

KOSDAQ §9-4.4 enumerates the same 3-tier escalation:

- **Tier 1 (40 days):** 1 day × 5억–10억; or 2–4 days × ≤ 5억 cumulative.
- **Tier 2 (80 days):** 1 day × > 10억; or 2–4 days × 5억–10억; or 5+ days × ≤ 5억.
- **Tier 3 (120 days):** 2–4 days × > 10억; or 5+ days × > 5억.

The KOSDAQ §9-4.2 carve-out (added 2026-01-28) excludes certain entities subject to FSCMA §208-7.2.1.라 measures from the §9-4.1 verification-on-settlement-day requirement. KOSPI's §18-2 likely has a parallel 2026-01-28 amendment; cross-check at Phase 6.

#### KRX-discretionary covered-short restriction

KOSPI §17.6 enables KRX-discretionary covered-short restriction for short-sale-overheat issues and FSC-designated issues. The KOSDAQ analogue is in §9-2 paragraphs not extracted in this document's source pull (KOSDAQ §9-2 has additional paragraphs ⑤ and beyond covering KRX-discretionary measures). The substance is believed to mirror KOSPI §17.6 verbatim — both books delegate the precise overheat-designation criteria to the Enforcement Rule (R6 unresolved on KOSDAQ side). Phase 6 audit should re-pull the full KOSDAQ §9-2 to confirm.

## Parameters & thresholds

### Table 1 — KOSDAQ §9-2.1 "deemed-not-short" carve-outs

Per [KRX-RULE-KOSDAQ-BR-KO §9-2.1]:

| #     | Carve-out                                                                                                                                | Article                                |
|-------|-------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------|
| 1     | Selling already-purchased listed securities, within the purchased quantity, before the settlement date                                    | [KRX-RULE-KOSDAQ-BR-KO §9-2.1.1]       |
| 2     | Selling rights-acquired stocks (CB / EB / BW exercise; capital increase; stock dividend) when listing-by-settlement-date is feasible      | [KRX-RULE-KOSDAQ-BR-KO §9-2.1.2]       |
| 3a    | Selling securities held at a third-party custodian (not the broker)                                                                       | [KRX-RULE-KOSDAQ-BR-KO §9-2.1.3.가]    |
| 3b    | Selling **corporate-growth-investment-fund** securities to be received from additional issuance *(added 2026-03-04; KOSPI uses "ETF" here at §17.1.3.b)* | [KRX-RULE-KOSDAQ-BR-KO §9-2.1.3.나]  |
| 3c    | Selling listed securities to be received via ETF (상장지수집합투자기구 집합투자증권) redemption                                                | [KRX-RULE-KOSDAQ-BR-KO §9-2.1.3.다]    |
| 3d    | Selling listed shares acquired upon DR-deposit-contract termination                                                                       | [KRX-RULE-KOSDAQ-BR-KO §9-2.1.3.라]    |
| 3e    | Selling lent securities whose return is confirmed                                                                                         | [KRX-RULE-KOSDAQ-BR-KO §9-2.1.3.마]    |
| 3f    | Selling securities to be delivered under an off-exchange trade or other contract                                                          | [KRX-RULE-KOSDAQ-BR-KO §9-2.1.3.바]    |
| 3g    | Selling DRs to be acquired by depositing eligible underlying securities                                                                   | [KRX-RULE-KOSDAQ-BR-KO §9-2.1.3.사]    |
| 3h    | Selling securities the consigner has agreed to buy in the post-close off-hours session of the same day                                    | [KRX-RULE-KOSDAQ-BR-KO §9-2.1.3.아]    |

### Table 2 — KOSDAQ §9-3.2 uptick rule exemptions

Per [KRX-RULE-KOSDAQ-BR-KO §9-3.2]:

| #     | Exemption category                                                                                                                       | Article                                |
|-------|-------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------|
| 1     | Index arbitrage — selling stock-basket against index futures/options                                                                      | [KRX-RULE-KOSDAQ-BR-KO §9-3.2.1]       |
| 1-2   | Single-stock arbitrage — selling underlying against single-stock futures/options                                                          | [KRX-RULE-KOSDAQ-BR-KO §9-3.2.1의2]    |
| 3     | DR-vs-original arbitrage                                                                                                                  | [KRX-RULE-KOSDAQ-BR-KO §9-3.2.3]       |
| 5     | **KOSPI-market ELW LP hedging** — KOSPI-market LP for ELW (per KOSPI BR §20-2.1) sells KOSDAQ-side underlying short                       | [KRX-RULE-KOSDAQ-BR-KO §9-3.2.5]       |
| 6     | **KOSPI-market ETF LP hedging** — KOSPI-market LP for ETF (per KOSPI BR §20-2.1) sells KOSDAQ-side underlying short                       | [KRX-RULE-KOSDAQ-BR-KO §9-3.2.6]       |
| 6-2   | **KOSPI-market ETN LP hedging** — KOSPI-market LP for ETN (per KOSPI BR §20-2.1) sells KOSDAQ-side underlying short                       | [KRX-RULE-KOSDAQ-BR-KO §9-3.2.6-2]     |
| 7     | Derivatives market-maker hedging — sells KOSDAQ-side underlying to hedge derivative-position                                              | [KRX-RULE-KOSDAQ-BR-KO §9-3.2.7]       |

KOSDAQ §9-3.2.2 / 2-2 / 2-3 / 4 / 4-2 were deleted in various amendments (most recently 2021-03-08). The current 7-effective-exemption list aligns with the substance of KOSPI §18.2's 8-case list (8 = 7 + 7-2 KOSPI's ETN-LP-hedging which is split into a separate sub-item; KOSDAQ inlines this under §9-3.2.6-2).

### Table 3 — KOSDAQ §9-4.4 post-management escalation (identical to KOSPI §18-2.4)

Pre-deposit period for naked-short violators, by violation days × cumulative amount over the last 6 months [KRX-RULE-KOSDAQ-BR-KO §9-4.4]:

|                                | ≤ KRW 5 억 (≤ 500 M)  | KRW 5 억 < x ≤ 10 억 (500 M – 1 B) | > KRW 10 억 (> 1 B) |
|--------------------------------|:--------------------:|:------------------------------:|:------------------:|
| **1 day**                      |          —           |        **40 days**             |    **80 days**     |
| **2–4 days**                   |    **40 days**       |        **80 days**             |   **120 days**     |
| **5+ days**                    |    **80 days**       |       **120 days**             |   **120 days**     |

Identical numeric matrix to KOSPI §18-2.4. Same definition of 매도일수 (*mae-do-il-su*; violation days within 6-month look-back) and 누적매도금액 (*nu-jeok mae-do-geum-aek*; cumulative violation amount).

The §9-4.2 amendment (added 2026-01-28) carves out FSCMA §208-7.2.1.라 entities from the §9-4.1 settlement-day verification — a drafting parallel of the KOSPI §18-2 amendment landed on the same date.

## Worked examples

The KOSPI worked examples — Example A (uptick rule on a downtick day; minimum permitted short = next tick above last), Example B (uptick rule under the uptick exception; short permitted at the touch), Example C (escalation tier upgrade from tier 1 → tier 2 → tier 3) — all carry over to KOSDAQ unchanged because §9-3.1 / §9-4.4 mirror KOSPI §18.1 / §18-2.4 verbatim. See [KOSPI § Worked examples](../kospi/short_selling.md#worked-examples).

### Example D — KOSDAQ-specific cross-market hedging exemption

A KOSPI-listed ETF tracks the KOSDAQ 150 index. The ETF's KOSPI-side LP holds long inventory of the ETF and wants to hedge by short-selling underlying KOSDAQ-150-constituent stocks on KOSDAQ.

- The KOSPI-side LP submits a covered-short on KOSDAQ-listed stock X (a KOSDAQ 150 constituent).
- The standard KOSDAQ §9-3.1 uptick rule would normally apply: short must price above last-trade.
- §9-3.2.6 explicitly exempts "ETFs ... LPs registered under KOSPI BR §20-2.1 ... selling underlying basic stock" — the KOSPI-LP-on-KOSDAQ-underlying case [KRX-RULE-KOSDAQ-BR-KO §9-3.2.6].
- The covered-short on KOSDAQ stock X is therefore **uptick-rule-exempt**; the short may be priced at or below the immediately preceding price.

Contrast: a KOSDAQ-listed ETF LP (registered under KOSDAQ BR §12-2) doing the same hedge faces the strict-vs-broad-reading question for §9-3.2.6. Until clarified, KOSDAQ-LP hedging by selling KOSDAQ-side underlying short should plan for the standard uptick rule.

## Edge cases & open questions

- Edge case: KOSDAQ §9-2.1.3.나 carves out *corporate-growth-investment-fund* securities; KOSPI §17.1.3.b carves out *ETFs*. Both lists provide ETF-related coverage but via different sub-paragraphs (KOSDAQ's ETF coverage moves to §9-2.1.3.다 redemption-resale). This is a drafting structural delta with no material substantive effect, but compliance audits cross-referencing carve-out sub-paragraphs by index will mismatch.
- Edge case: KOSDAQ §9-3.2 LP-hedging exemptions explicitly reference **KOSPI BR §20-2** (the KOSPI LP framework). KOSDAQ has its own LP framework at §12-2 to §12-6 (see [Order Types § Detailed rules](./order_types.md#detailed-rules)). KOSDAQ-side LPs hedging KOSDAQ-listed ETFs are likely **not** covered by §9-3.2.6's strict reading — verify with KRX before relying on a KOSDAQ-LP uptick exemption.
- Edge case: The 2026-01-28 §9-4.2 carve-out for FSCMA §208-7.2.1.라 entities is a recent amendment. Whether the KOSPI §18-2 has a parallel 2026-01-28 amendment is not yet pulled — Phase 6 audit should cross-check.
- Edge case: KOSDAQ-OPS-T7 KRX-tour does not enumerate the §9-2.1 carve-outs by reference number, only by description. Treating the tour as the source of carve-out enumeration (rather than the BR text) misses the §9-2.1.3.나 corporate-growth-investment-fund language — algorithmic-trading-compliance code should anchor on the BR sub-paragraph references, not the tour summary.
- Edge case: The §9-3.1 uptick rule's "직전의 가격" reference, like KOSPI's, is believed to include mid-price prints (per the parallel KOSPI tour treatment). KOSDAQ tour does not state this explicitly; cross-check at R6 / Phase 6.
- Open question: KOSDAQ §9-2 paragraphs ⑤ and beyond (KRX-discretionary covered-short restriction, FSC-designation following) are not pulled in this document's source extract. The substance is believed to mirror KOSPI §17.6 / §17.7 / §17.8 verbatim, but the precise paragraph numbering and the cross-reference structure to FSC notices need confirmation.
- Open question: The §9-3.2.6 / 6-2 cross-market LP-hedging exemption references KOSPI BR §20-2 explicitly. As KOSDAQ-listed ETF / ETN LP framework matures (KOSDAQ has its own LP framework since 2007-10-12), whether §9-3.2.6 will be amended to reference both §20-2 (KOSPI) and §12-2 (KOSDAQ) — or whether KOSDAQ-LP hedging will remain non-exempt — depends on regulatory direction. Phase 6 audit should re-check.
- Unsourced claim: [KRX-TOUR-KOSDAQ-EXCEPT-T7] mentions "regular session block trading is exempt from uptick" — same as KOSPI's tour. The rule path for block-trade short exemption is via the §9-2.1 carve-outs / §9-3.2 categorical exemptions rather than a standalone "block-trade" exemption; treat the tour's framing as approximate.

## Sources

- `KRX-RULE-KOSDAQ-BR-KO` — KOSDAQ Market Business Regulation (코스닥시장 업무규정), bookid 210164370, effective 2026-04-28. Articles cited: §9-2 (Short-sale quotation restriction — central article: §9-2.1 8-case carve-outs with §9-2.1.3.나 corporate-growth-investment-fund language added 2026-03-04; §9-2.2 / §9-2.3 four-step member duty cycle; §9-2.4 deemed-verification opt-out path with 120-day breach reset; KRX-discretionary restriction in paragraphs ⑤+ not yet extracted), §9-3 (Covered-short price restriction — uptick rule with uptick exception at §9-3.1; 7-case categorical exemption list at §9-3.2 with KOSPI BR §20-2 cross-references for LP-hedging cases), §9-4 (Post-management — 40/80/120-day pre-deposit escalation matrix at §9-4.4 with same numeric thresholds as KOSPI §18-2.4; §9-4.2 carve-out for FSCMA §208-7.2.1.라 entities added 2026-01-28).
- `KRX-TOUR-KOSDAQ-EXCEPT-T7` — KRX overview "Limit to short sale" (KOSDAQ); English, not authoritative. Used for: the FSCMA §180 naked-vs-covered framing (substantively identical to KOSPI's tour), the 8-case carve-out narrative, the uptick-rule-with-uptick-exception explanation, and the categorical exemption summary (index arbitrage / stock arbitrage / ETF arbitrage / DR arbitrage / ETF sale / share-warrant-LP / ETF-LP / derivatives-market-organizer hedging — matching the §9-3.2 list). External references: FSCMA §180 (statute), FSCMA §180-2 (short-sale balance reporting), FSCMA §180-3 (short-sale public disclosure) — same statute ladder as KOSPI.
