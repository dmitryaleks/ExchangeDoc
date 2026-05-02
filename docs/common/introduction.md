---
title: "Introduction"
markets: [KOSPI, KOSDAQ]
last_reviewed: 2026-05-02
sources: []
---

# Introduction

This site is a reference for the **microstructure of the KOSPI and KOSDAQ equity markets** operated by the Korea Exchange (KRX) — sufficient to inform execution-algorithm design and pre-trade compliance. It is organized by topic, with one chain of pages per market, plus a [cross-market comparison](./comparison.md) for quick lookup.

## Scope

In scope:

- **KOSPI Market** — KRX's main board for large-cap and mid-cap listings.
- **KOSDAQ Market** — KRX's growth / smaller-cap board.

Out of scope (per `PROJECT.md`):

- Nextrade.
- ATS / PTS.
- Derivatives markets.

When a topic page references derivatives (e.g. sidecar, CB-linked-derivatives halt, derivatives-expiry-day VI tightening), the referenced rules live on the spot side; the derivatives side is mentioned only as far as it interacts with the spot trading rules.

## Reading paths

- **Cross-market diff first.** If you have already read the topic on one market and want to know how the other market diverges, jump to [Comparison](./comparison.md).
- **Algo-design checklist.** [Comparison § Top-level — what is materially different](./comparison.md#0-top-level-what-is-materially-different) is a 17-row punch list of all the parameter-level divergences between the two markets that an execution algo must encode separately.
- **Topic chains.** Each market has 10 topic pages: market hours, auctions, price ranges, order types, trading rules, amendments, volatility interruption, circuit breakers, short selling, and other topics. Use the sidebar to navigate.

## Authoritative sources

The Korean-language **Business Regulation** (업무규정) and **Enforcement Rule** (시행세칙) are the authoritative sources. English KRX overview tour pages are used for narrative framing and operational color but are **not authoritative**.

The KOSDAQ Enforcement Rule was not located on the KRX Legal Portal during the source-discovery phase (project risk **R6**) — KOSDAQ-side parameter values flagged with R6 are sourced from KRX overview tour pages and are believed to mirror the corresponding KOSPI Enforcement Rule articles, pending the KOSDAQ Enforcement Rule archive. Phase 6 freshness audit will reconcile these.

## Conventions

- Korean terms appear with their original Hangul plus *romanization* and an English gloss on first use within a page; subsequent uses drop the romanization.
- All times are in Korea Standard Time (KST, UTC+9) unless otherwise stated.
- Citations use bracketed source IDs from [`docs/sources/INVENTORY.md`](../sources/INVENTORY.md), e.g. `[KRX-RULE-KOSPI-BR-KO §22]`.
- The *Edge cases & open questions* section at the end of each topic page records ambiguities, pending verifications, and historical-only claims that should not be relied upon for current-day execution.

## Reading the per-page header

Each topic page carries a YAML frontmatter block:

- `title` — page title.
- `markets` — `[KOSPI]`, `[KOSDAQ]`, or `[KOSPI, KOSDAQ]` (cross-market pages).
- `last_reviewed` — ISO date of the most recent freshness pass on this page.
- `sources` — source-inventory IDs cited on the page.

Phase 5.5 of the project plan adds a rendered metadata banner at the top of each page surfacing this frontmatter as a market badge, last-reviewed date, and clickable source-inventory links. Until that lands, the frontmatter is the canonical metadata reference.
