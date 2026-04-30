# Exchange Analysis — KOSPI & KOSDAQ Microstructure

Documentation project covering Korean equity market microstructure (KOSPI and
KOSDAQ) for the purpose of designing execution algorithms. See `PROJECT.md`
for scope and `PROJECT_IMPLEMENTATION.md` for the phase plan.

The published site is generated from Markdown under `docs/` plus
`docs/index.yaml` (the sidebar source-of-truth) using **MkDocs Material** —
see `decisions/0001-html-generator.md` for the rationale.

## Generating and serving the documentation

### 1. Prerequisites

- Python 3.10+ on `PATH`.
- A virtual environment in `./.venv` (already present in this repo).

### 2. Install pinned dependencies

Activate the venv, then install:

```bash
# Windows (Git Bash / cmd)
.venv\Scripts\activate
python tasks.py install
```

```bash
# macOS / Linux
source .venv/bin/activate
python tasks.py install
```

This installs `mkdocs`, `mkdocs-material`, `pyyaml`, and `pymarkdownlnt` at
the versions pinned in `requirements.txt`.

### 3. Serve locally with live-reload

```bash
python tasks.py serve
```

Then open <http://localhost:8000/>. Edits to any `.md` file under `docs/`
trigger a rebuild and a browser refresh.

The `serve` task first runs `tools/gen_nav.py`, which reads `docs/index.yaml`
and rewrites the `nav:` block of `mkdocs.yml` (between the
`# === BEGIN/END GENERATED NAV ===` sentinels). Entries in `index.yaml` that
point at not-yet-written files are skipped with a stderr warning, so the
build keeps working while the docs tree is partial.

If you change `docs/index.yaml` while `serve` is running, re-run
`python tasks.py gen-nav` to regenerate the nav block — `mkdocs serve` will
then pick up the updated `mkdocs.yml`.

### 4. Build a static site

```bash
python tasks.py build
```

Produces a self-contained static site under `./site/`. Open
`site/index.html` directly, or serve the directory with any static file
server (e.g. `python -m http.server -d site 8000`). The `site/` directory is
gitignored.

`--strict` is intentionally not used during day-to-day builds because
forward-references to not-yet-written counterpart pages emit expected
warnings. It will be re-enabled at the Phase 6.5 freeze gate.

### 5. Other tasks

```bash
python tasks.py --list           # list available tasks
python tasks.py lint             # lint all Markdown under docs/
python tasks.py gen-inventory    # regenerate docs/sources/INVENTORY.md
python tasks.py gen-nav          # regenerate the nav block only
python tasks.py clean            # remove ./site/
```
