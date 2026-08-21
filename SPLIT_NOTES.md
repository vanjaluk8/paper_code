# SPLIT_NOTES — how the two-repo split works (read before diving in)

**Date:** 2026-08-21 · **Original combined repo:** `litreview-peft-p2p-adapters`
(local only; its rewritten history was **not** force-pushed).

The original monorepo was split into **two fresh repos** (no history surgery —
both began with clean initial commits of the current working tree):

| Repo | Role | Path to clone |
|---|---|---|
| **`slr-engine`** | Snowballing/search/screening/extraction/PRISMA/figures pipeline (code) | sibling checkout, `slr_engine/` |
| **`slr-literature`** (this repo) | Manuscripts (`writing/`), curated corpus & methodology (`papers_repo/`), PRISMA package | `./` |

---

## Why this split
The manuscript reports numbers and figures that the pipeline (`slr-engine`) generates.
The goal is a clean "**code** vs **literature/materials**" separation:
- `slr-engine` = the tooling (self-contained, runnable).
- `slr-literature` = curated corpus + the manuscripts + the audited PRISMA evidence.

## The curated-corpus coupling (important nuance)

The pipeline **does** depend on curated inputs (`G0_seed_papers.md` + `G1–G6_*.csv`).
To keep `slr-engine` runnable on its own, those inputs are **snapshotted** into
**`slr-engine/slr_engine/snowballing/data/`** (~576 KB).

- **Canonical** curated corpus lives here, in **`papers_repo/`**.
- The `data/` **snapshot** in `slr-engine` is the machine input for the pipeline.
- Keep them in sync: update `papers_repo/` → re-sync `slr-engine/.../data/`.

## Provenance line
`slr-engine` (runs pipeline → emits `snowball_output/*.csv` + `assets/figures/*.pdf`)
→ this repo consumes those outputs (figures copied to `writing/.../figures/`, numbers
reported in the manuscript and `PRISMA_NUMBERS_VALIDATION.md`).

## Things that were excluded from git (stay local / in Zotero)
- `**/pdfs/**` and `**/*.pdf` — reference PDF libraries (`validation/pdfs/`,
  `writing_materials/pdfs/`, `papers_repo/*.pdf`). Large, not source-of-truth.
- Figure PDFs in `writing/.../figures/` — regenerable from `slr-engine`
  (`python -m app.visualise`).
- `*_data_extraction_*.csv` — pipeline-derived; kept local.
- `.env`, `.venv`, `__pycache__/`, `*.pyc`.

## Known quirks carried over (cleanup candidates, not this split's scope)
1. **Two files with a literal `"` + fullwidth `～` in their names:**
   `writing/slr_methodology_paper/{validation,writing_materials}/notes/MoE-routing/switch-transformers.md</～DSML～"`.
   They are tracked and valid but awkward in git shell operations — consider renaming
   to `switch-transformers.md` when convenient.
2. Some **`reports/PHASE*.md`** audit records reference the old combined layout
   (`slr_engine/snowballing/...`). They are **historical records** — left as-is;
   the manuscript/PRISMA *live* docs were updated to the new layout.
3. `writing/slr_methodology_paper/validation/generate_validation.py` reads the audited
   `13_final_reading_list` from this repo's `writing_materials/` and the pipeline
   intermediate `S7b_...` from the sibling `slr-engine` checkout (path updated for the split).

## Still pending (from the earlier MDPI revision plan)
The manuscript's PRISMA package (`PRISMA_2020_checklist.md`, `PRISMA_summary`,
`PRISMA_NUMBERS_VALIDATION.md`) and the MDPI-revision checklist have **open items** —
refer to the `MDPI_revision_execution_plan.md` / the audit `reports/` for what remains
(e.g. placeholder figures, quality-appraisal §3.3, checklist title/figure# fixes).
