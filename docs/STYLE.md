# Style Guide — Exchange Analysis docs

This guide is the per-file template, the formatting conventions, and the
citation rules for every Markdown file under `docs/`. Stick to it so the HTML
site (Phase 5) can render uniformly, the Phase 6 audits stay tractable, and
diffs stay readable.

If a rule here conflicts with a need you actually have, prefer the rule and
raise the conflict in `PROJECT_IMPLEMENTATION.md` §6 (Risks & Open Questions).

---

## 1. File metadata (frontmatter)

Every topic file (under `kospi/`, `kosdaq/`, `common/`) starts with YAML
frontmatter:

```yaml
---
title: "Volatility Interruption (KOSPI)"
markets: [KOSPI]            # one or both of: KOSPI, KOSDAQ
last_reviewed: 2026-04-30   # ISO date; update on every substantive edit
sources:                    # IDs from docs/sources/INVENTORY.md
  - KRX-BR-2024-09
  - KRX-EN-VI-NOTICE-2025-02
---
```

The frontmatter is the source of truth for that file's metadata. The
corresponding entry in `docs/index.yaml` must agree (same `title`, `markets`,
`last_reviewed`, `sources`). The Phase 6 audit greps for divergence.

`README.md` files in subfolders do not need frontmatter.

---

## 2. Per-topic file template

After the frontmatter, every topic file uses these H2 sections, in this order.
Sections may be empty (write `None known.`), but they must all be present so
the site renderer doesn't have to guess.

```markdown
## Summary

3–5 bullet points an execution-algo developer needs to know. No prose
paragraphs in this section.

## Detailed rules

The full normative description. Use H3 subheadings to group related rules.
Every "must / shall / may not / is prohibited" sentence carries an inline
citation (see §5).

## Parameters & thresholds

All numeric values in tables (see §6). One row per parameter. If the topic
has no numeric parameters, write `Not applicable.`

## Worked examples

Optional. Use when a rule is easier to read as a scenario than as prose.
Diagrams go here too — see §8 for image conventions.

## Edge cases & open questions

Anything ambiguous, contested, or unsourced. Each item is a bullet starting
with one of: `Edge case:`, `Open question:`, or `Unsourced claim:`.

## Sources

Bullet list of source-inventory IDs cited in the file, each with the URL
fetched at archival time. See §5.
```

---

## 3. Heading levels

- `H1` is reserved for the file title and is rendered from frontmatter — do
  not write a `# Title` line in the body.
- Use `H2` for the template sections in §2 above.
- Use `H3` for sub-rules within "Detailed rules".
- Do not go below `H4`. If you need deeper nesting, split the topic.

---

## 4. Voice, tone, language

- Third person, declarative, present tense. *"The market opens at 09:00 KST."*
- No marketing language ("seamless", "robust"). No first person ("we", "our").
- Prefer short sentences. One claim per sentence makes citation easier.
- English is the working language. Quote Korean only when (a) the rule's
  authoritative wording is in Korean and (b) the wording is load-bearing for
  a numeric threshold or a definition. In that case use the format in §10.
- Avoid abbreviations on first use. Spell out then parenthesise:
  *"Volatility Interruption (VI)"*, *"Korea Composite Stock Price Index
  (KOSPI)"*. After that, the abbreviation is fine.
- **Korean terms — first-occurrence rule.** When a Korean term appears in a
  topic file, give both its Revised Romanization (italicized) and an English
  translation/equivalent on its **first occurrence in that file**. Two formats:
  - Term has a clean English equivalent: `English term (한국어, *romanization*)`
    — e.g. `Regular Session (정규시장, *jeong-gyu si-jang*)`.
  - Term is being introduced as Korean terminology with no clean English
    equivalent: `한국어 (*romanization*) — definition` — e.g.
    `장개시 (*jang-gae-si*) — start of the Regular Session`.

  Subsequent uses in the same file may use the English term alone (or the
  bare Korean when it's idiomatic in rulebook context). Do not repeat the
  romanization+translation on every occurrence. Use Revised Romanization (RR),
  the official ROK government standard since 2000 — not McCune-Reischauer
  or Yale.

---

## 5. Citations

**Every numeric threshold and every normative statement carries a citation.**
Phase 6 will fail an audit that finds an unsourced claim.

Citation syntax — inline, at the end of the sentence, before the period:

```markdown
The daily price limit is ±30 % of the base price [KRX-BR-2024-09 §4.2].
```

Rules:

- The bracketed token is a **source ID** from `docs/sources/INVENTORY.md`,
  optionally followed by a section reference (`§4.2`, `Art. 12`, `p. 47`).
- One sentence may carry multiple citations: `[A §1; B §3]`.
- If you cannot find a primary source, the claim does not go in "Detailed
  rules". It goes in "Edge cases & open questions" prefixed with
  `Unsourced claim:`.
- The "Sources" section at the end of the file lists every cited ID once,
  with the archived URL and fetch date pulled from `INVENTORY.md`.
- Do not paraphrase from memory. If the source is in Korean and you used a
  translation, cite the Korean source ID and add `(translated)` after the
  reference.

---

## 6. Tables

- Use GitHub-flavoured pipe tables.
- Put units in the **column header**, not in each cell.
- Right-align numeric columns, left-align text columns.
- Always include a header row. Always cite the source in a final column or in
  a footnote-style line directly under the table.
- Keep one row per logical parameter; do not merge cells.

Example:

```markdown
| Parameter            | KOSPI | KOSDAQ | Unit | Source             |
|----------------------|------:|-------:|------|--------------------|
| Daily price limit    |    30 |     30 | %    | [KRX-BR-2024-09 §4.2] |
| Tick size (≥ 200,000) |   500 |    500 | KRW  | [KRX-BR-2024-09 §3.1] |
```

If a table is wider than ~6 columns, split it or move it to a dedicated
"Parameters" subsection.

---

## 7. Units, numbers, time, dates

- **Currency:** `KRW` (ISO 4217). Format with thousands separators:
  `1,000,000 KRW`. Do not use `₩` in tables (alignment issues); use `KRW`.
- **Percent vs basis points:** prefer `%` for thresholds ≥ 0.1 %. Use `bps`
  only when the source itself uses bps. Never mix in the same table.
- **Time of day:** 24-hour, suffix `KST`. Example: `15:20 KST`. Always
  include `KST`, even when context seems obvious — the docs are read
  cross-timezone.
- **Durations:** explicit units. `2 minutes`, not `2m` or `2'`.
- **Dates:** ISO `YYYY-MM-DD`. Example: `2026-04-30`.
- **Numbers:** thousands separators (commas). Decimals with `.`. Don't write
  `30%` — write `30 %` (space before unit) for readability, except when
  quoting a source verbatim.

---

## 8. Images & diagrams

- Stored in `docs/images/`, named `{topic}_{short_description}.{ext}` —
  lowercase, underscores. See `docs/images/README.md`.
- Reference with relative paths: `![alt text](../images/auctions_kospi_random_end.svg)`.
- Alt text is required and must describe the image content, not just label it.
- Prefer SVG for diagrams, PNG for screenshots.
- Captions go directly underneath in italics:
  `*Figure 1: KOSPI closing call auction with random end window.*`
- Every screenshot of a source page must have the corresponding source
  archived in `docs/sources/`.

---

## 9. Market callouts (KOSPI vs KOSDAQ)

Files under `kospi/` and `kosdaq/` are implicitly market-scoped — no callout
needed. Use callouts only inside `common/` files where a passage applies to
just one market. Format:

```markdown
> **KOSPI only** — listed companies on the KOSPI Market are subject to
> the additional rule that … [SOURCE-ID §x].

> **KOSDAQ only** — for KOSDAQ-listed securities, the threshold is …
> [SOURCE-ID §y].
```

Do **not** use callouts to make general remarks ("note that …"). Reserve them
for genuine market-scoped divergences. Anything else goes in the body prose
or in "Edge cases & open questions".

---

## 10. Quoting Korean text

Use this format when the Korean wording is load-bearing:

```markdown
> 정규시장의 매매거래시간은 09:00부터 15:30까지로 한다.
>
> *Translation:* Regular session trading hours are from 09:00 to 15:30.
> [KRX-BR-2024-09-KO §2.1] (translated)
```

The Korean original is the authoritative quote; the English line is marked
*Translation:* in italics. Cite the Korean source ID, not the English one.

---

## 11. Cross-references

- Link between topic files with relative Markdown links:
  `[Auctions (KOSPI)](../kospi/auctions.md)`.
- Anchor links use the auto-generated slug from the H2 heading:
  `[see Parameters & thresholds](#parameters-thresholds)`.
- Always link the KOSPI ↔ KOSDAQ counterparts at the top of "Detailed rules"
  (or in a single line right after the Summary):

  ```markdown
  > See also: [Auctions (KOSDAQ)](../kosdaq/auctions.md), [Comparison](../common/comparison.md).
  ```

The Phase 6 cross-link audit checks that every topic links to its
counterpart and to the comparison page.

---

## 12. Lists, code, miscellany

- Use `-` for unordered lists (not `*`), for diff stability.
- Use ordered lists (`1.`, `2.`) only when order matters.
- Inline code: backticks for parameter names, identifiers, and field names
  used in protocols (`OrdQty`, `LeavesQty`).
- Block code fences for any multi-line example; tag the language
  (` ```yaml`, ` ```text`).
- One blank line before and after every heading, list, table, and code
  block. The site builder is forgiving; humans aren't.

---

## 13. What not to put in topic files

- Implementation notes about the algo project itself — those belong in
  source-code repos or design docs, not the documentation database.
- Speculation about why a rule exists, unless the source explicitly says so.
- Links to non-archived sources. If it's worth citing, archive it in
  `docs/sources/` first.
- Information about Nextrade, ATS / PTS, or derivatives markets (out of scope
  per `PROJECT.md`).

---

## 14. Pre-commit checklist (per file)

Before marking a topic task `[x]` in `PROJECT_IMPLEMENTATION.md`:

- [ ] Frontmatter present and matches `docs/index.yaml`.
- [ ] All six template sections present (§2).
- [ ] Every numeric or normative claim has an inline citation (§5).
- [ ] Tables follow §6 layout.
- [ ] Units follow §7.
- [ ] Cross-link to counterpart market is present (§11).
- [ ] `last_reviewed` updated to today's date.
- [ ] All cited source IDs exist in `docs/sources/INVENTORY.md`.
