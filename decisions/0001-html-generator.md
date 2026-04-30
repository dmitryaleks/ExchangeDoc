# ADR 0001 — HTML site generator

- **Status:** Accepted
- **Date:** 2026-04-30
- **Plan task:** PROJECT_IMPLEMENTATION.md §0.5
- **Decided by:** user, 2026-04-30.
- **Decision summary:** Option A — MkDocs Material, pinned to current major version,
  built-in offline search, no interactive embeds in docs.

---

## 1. What we're choosing

The tool that turns `docs/*.md` + `docs/images/` + `docs/index.yaml` into a static HTML
site under `site/`, with a pastel light theme and a pastel dark theme.

## 2. Hard requirements

These are non-negotiable per `PROJECT.md` and the implementation plan:

1. **Static output.** No server runtime needed to serve the site.
2. **Two themes:** pastel light (default) and pastel dark, user-toggleable in the header,
   choice persisted client-side.
3. **Reads `docs/index.yaml`** as the source of truth for sidebar order and per-page
   metadata. We are not maintaining a second nav config in the generator's native format.
4. **Renders per-page metadata** from frontmatter: market badge (KOSPI / KOSDAQ / both),
   `last_reviewed` date, source links resolving to `docs/sources/INVENTORY.md`.
5. **Full-text search** across all topic pages, working without any backend.
6. **Reproducible build** from a clean checkout via a single command.

## 3. Soft preferences

These bias the choice but won't kill an option that misses one:

- Python ecosystem alignment (project already has `main.py`).
- Small dependency tree — this is a docs project, not a SaaS frontend.
- Theming via plain CSS, not React component overrides.
- Plain Markdown over MDX. We don't need JSX inside docs.

## 4. Options considered

### A. MkDocs Material *(Python)*

Mature Python doc generator with a polished default theme.

- **Theming:** built-in light/dark with palette toggle is one config block. Pastel palette
  via `extra_css` overrides — straightforward.
- **Sidebar from `index.yaml`:** mkdocs reads `nav` from `mkdocs.yml`. We'd write a tiny
  `tools/gen_nav.py` that reads `docs/index.yaml` and emits `mkdocs.yml`'s `nav` section
  before each build. ~30 lines of glue. `index.yaml` stays the source of truth.
- **Frontmatter:** Material reads frontmatter natively for `title`, `description`. Custom
  fields (`markets`, `last_reviewed`, `sources`) need a small `mkdocs_hooks.py`
  (`on_page_context`) to surface them in the page template.
- **Search:** built in (`search` plugin), client-side, indexed at build. No work.
- **Per-page metadata UI:** override `partials/page.html` to render the market badge,
  `last_reviewed` date, and source links in the page header.
- **Effort to first working build:** ~half a day.
- **Risks:** template overrides can drift across Material versions; pin the version.

### B. Docusaurus *(React / Node)*

React-based doc generator from Meta. Excellent navigation and search, polished defaults.

- **Theming:** built-in light/dark switcher. Pastel palettes via Infima CSS variables.
- **Sidebar from `index.yaml`:** Docusaurus reads `sidebars.js`. Same trick: a build
  step generates `sidebars.js` from `docs/index.yaml`. Doable.
- **Frontmatter:** rich support, custom fields surfaceable via swizzled components.
- **Search:** Algolia DocSearch (hosted, free for open source) or local search plugin.
  Local plugin is fine for a private project.
- **Per-page metadata UI:** swizzle `DocItem/Layout` — this means committing React
  components into the repo. Heavier than CSS overrides.
- **Effort to first working build:** ~1 day, more if pastel theme work is detailed.
- **Risks:** Node + npm + React toolchain for a docs project that doesn't need any of
  React's runtime features. Heaviest dependency tree of the options.

### C. Astro Starlight *(Astro / Node)*

Newer, very fast, MDX-native. Light/dark built in; theming via CSS variables.

- **Theming:** built-in light/dark + custom palette via `theme.css`. Clean.
- **Sidebar from `index.yaml`:** Starlight uses an `astro.config.mjs` `sidebar:` block
  or auto-generation from folder structure. Same generate-from-yaml step applies.
- **Frontmatter:** fully supported; custom fields surfaceable in component overrides
  (Astro `.astro` components, simpler than React swizzling).
- **Search:** built in (Pagefind), client-side, very fast.
- **Per-page metadata UI:** override `PageFrame.astro` or similar — straightforward
  if you know Astro syntax.
- **Effort to first working build:** ~1 day for someone fluent in Astro; ~2 if not.
- **Risks:** smallest community of the three frameworks; less Stack Overflow surface
  area; Astro idioms are still evolving.

### D. Custom Python static generator

A small `tools/build.py` that reads `docs/index.yaml`, renders each `.md` with
`python-markdown` (or `mistune`) + Jinja2 templates, writes static HTML, and emits a
`search-index.json` for client-side `lunr.js`.

- **Theming:** write two CSS files. Total control over the pastel palette.
- **Sidebar from `index.yaml`:** native — no glue code, just iterate the YAML.
- **Frontmatter:** parse it ourselves with `python-frontmatter`. Custom fields render
  exactly as we want, no plugin/hook plumbing.
- **Search:** ship `lunr.js` (~30 KB) + a build step that walks the rendered HTML and
  produces an index. Maybe 50 lines of code.
- **Per-page metadata UI:** trivially exact — we own the templates.
- **Effort to first working build:** ~2–3 days of focused work for a clean MVP.
- **Risks:** **maintenance is on us.** No upstream theme upgrades; we own
  accessibility, mobile responsiveness, print stylesheets, and any future site features.
  This is the option where we'll get the bug reports.

### E. Custom Node static generator

Same as D but Node-based (`markdown-it` + `nunjucks` or similar). No advantage over D
given the project already has Python; introduces a Node toolchain. Mentioned for
completeness; not recommended further.

## 5. Comparison at a glance

| Criterion                                    | A. MkDocs Material | B. Docusaurus | C. Astro Starlight | D. Custom Python |
|----------------------------------------------|:------------------:|:-------------:|:------------------:|:----------------:|
| Reads `index.yaml` as source of truth        | via build step     | via build step| via build step     | natively         |
| Theming effort (pastel)                      | low (CSS)          | medium (CSS+swizzle) | low (CSS)    | low (CSS, ours)  |
| Search built-in                              | yes                | yes (plugin)  | yes (Pagefind)     | DIY (lunr.js)    |
| Custom frontmatter fields in UI              | template override  | React swizzle | Astro override     | trivial          |
| Dependency weight                            | small (Python)     | large (Node + React) | medium (Node) | smallest         |
| Effort to first working build                | ~½ day             | ~1 day        | ~1–2 days          | ~2–3 days        |
| Long-term maintenance burden                 | low                | medium        | medium             | high             |
| Aligns with existing Python in repo          | yes                | no            | no                 | yes              |
| Risk of "fighting the framework"             | low–medium         | medium        | medium             | none             |

## 6. Recommendation

**Pick MkDocs Material (Option A).** It hits every hard requirement, the half-day to
first working build is the lowest of the four, theming is a CSS file, and the
`index.yaml`-as-source-of-truth requirement is solved by ~30 lines of glue. Long-term
we get free upstream improvements (accessibility, mobile, search quality) without
having to maintain them ourselves.

The tradeoff vs. the custom Python generator is real: with Material we accept that
some per-page rendering goes through their template system and we have to learn (a
little of) it. With a custom generator we'd write less novel CSS but more boilerplate
and own every future bug. For a small docs project that wants to stay focused on
*content*, paying that template-system tax is worth it.

## 7. Conditions that would flip the recommendation

If any of these turn out to be true, reconsider:

- **The pastel theme requires layout changes Material doesn't support cleanly.** If
  we end up swizzling more than the page header and the sidebar, the maintenance
  cost of template overrides starts to rival writing a custom generator. → switch to D.
- **We want MDX-style interactive components inside docs** (e.g. live tick-size
  calculators, embedded VI threshold visualisers). Material won't do that; Docusaurus
  or Astro will. → switch to B or C.
- **`index.yaml` evolves into something Material can't represent in `nav`** (e.g.
  dynamic per-market filtering, multiple parallel orderings). → switch to D, where we
  control rendering directly.

## 8. Consequences if Option A is chosen

Affects subsequent plan tasks:

- **0.4** — `Makefile` / `tasks.py` targets:
  - `build` runs `python tools/gen_nav.py && mkdocs build`
  - `serve` runs `python tools/gen_nav.py && mkdocs serve`
  - `lint` runs a Markdown linter (`pymarkdown` or `markdownlint-cli`) over `docs/`
- **5.1** — scaffold `mkdocs.yml` template + `tools/gen_nav.py`.
- **5.2** — implement two pastel palettes via `docs/_extra.css` and Material's
  `palette:` config; toggle uses Material's built-in theme switcher.
- **5.5** — page-header partial override to render market badge, `last_reviewed`,
  and source links from frontmatter.
- **New dependency:** `mkdocs`, `mkdocs-material`, `pyyaml`. Pin versions in a
  `requirements.txt`.

## 9. Resolved questions

Answered by user on 2026-04-30:

1. **Generator:** Option A (MkDocs Material).
2. **Versioning:** pin to MkDocs Material's current major version. Capture the exact
   pinned versions in `requirements.txt` during task 0.4.
3. **Search backend:** Material's built-in offline search. No Algolia, no external
   search service.
4. **Interactive embeds:** not on the roadmap. Plain Markdown rendering is sufficient;
   we will not introduce MDX or any framework that supports embedded JS components.

## 10. Locked-in implementation contract

Following from §8 + the answers above, the Phase 5 implementation must conform to:

- **Build entry-point:** `python tools/gen_nav.py && mkdocs build`
- **Serve entry-point:** `python tools/gen_nav.py && mkdocs serve`
- **Source of truth for nav:** `docs/index.yaml` → consumed by `tools/gen_nav.py` →
  emits the `nav:` block of `mkdocs.yml`. `mkdocs.yml` is a generated artefact for the
  `nav` section; non-`nav` parts of `mkdocs.yml` are hand-maintained.
- **Theme config:** Material's `palette` with two entries — pastel-light (default) and
  pastel-dark — with the toggle exposed in the header.
- **Pastel palette:** implemented in `docs/_extra.css`, referenced from
  `mkdocs.yml`'s `extra_css`.
- **Custom frontmatter rendering:** `mkdocs_hooks.py` `on_page_context` hook surfaces
  `markets`, `last_reviewed`, and `sources` to the page template; a `partials/`
  override renders the page-header badge + metadata block.
- **Search:** Material's bundled `search` plugin, no extra plugins, no external index.
- **Pinned dependencies** (exact versions captured in 0.4): `mkdocs`,
  `mkdocs-material`, `pyyaml`. Pin to current major version; renovate manually.
