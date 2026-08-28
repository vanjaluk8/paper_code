# MDPI Submission — Handoff / Next Steps

> **Purpose:** Everything still to do before submitting to MDPI *AI* journal (SUSY portal).
> Written so you can continue on another machine. All paths are relative to
> `writing/mdpi_paper/` unless stated. The companion repo is `slr_engine` (sibling checkout).

**Status legend:** ⬜ To do · 🟡 Partial · ✅ Done (in previous session)

---

## ✅ Already done (do NOT redo)

- All **4 figure placeholders** (`\fbox{...}`) replaced with `\includegraphics{...}` in:
  `04_peft.tex`, `05_adapter_composition.tex`, `07_moe_routing.tex`, `08_p2p_federated.tex`
- **4 schematic figures generated** and linked: `fig_peft_taxonomy.pdf`, `fig_adapterfusion.pdf`,
  `fig_switch_transformer.pdf`, `fig_petals.pdf`
- **Graphical abstract created** → `figures/fig_ga.pdf` (source `figures/ga.html`) — optional but recommended
- **PRISMA flow diagram replaced** → `figures/fig_slr1_prisma_flow.pdf` (source `figures/prisma.html`),
  now includes the **19 UNCERTAIN** side box that resolves the `972−791=181≠162` arithmetic
- **Bibliography.bib fixed** (5 edits: 4× `et al`→`and others`, removed 1 spurious DOI)
- **PRISMA 2020 checklist corrected** → `supplementary/PRISMA_2020_checklist.md` (Item 8,6,16b,7,5,18 + 14,21,16a)
- **PRISMA numbers validated** → `supplementary/PRISMA_NUMBERS_VALIDATION.md`

---

## ⬜ The 3 mandatory gaps (must do before clicking Submit)

### 1. Cover letter — REQUIRED
- Not yet written. Explain: significance, novelty (P2P adapter-based inference survey), fit to *AI* scope.
- Confirm whether *AI* wants **suggested referees** (some MDPI titles ask for 4–5 names in the letter).
- Save as `cover_letter.md` (or .pdf) in this folder.

### 2. Compiled PDF
- **No TeXLive on current machine.** Compile `main.tex` on Overleaf or a system with TeXLive (`pdflatex`/`latexmk` with MDPI `mdpi.cls` template, which is already bundled in `Definitions/`).
- Read the PDF end-to-end: check figure numbering, references resolve, no broken build.
- Zip the LaTeX source package: `main.tex` + `sections/` + `Definitions/` + `bibliography.bib` + the compiled PDF.

### 3. Figures ZIP
- Package ALL figures into one ZIP (all in `figures/`, 17 vector PDFs — resolution-independent, ≥1000 px / ≥300 dpi requirement satisfied). Name e.g. `figures.zip`.

---

## 🟡 Decisions / confirmations still open

- **Graphical abstract format:** `fig_ga.pdf` exists. If the journal wants PNG/JPEG/TIFF, export from `ga.html`.
- **Which files = Supplementary S1/S2:**
  - S1 = PRISMA 2020 checklist (`supplementary/PRISMA_2020_checklist.md`) — already referenced in `\supplementary{}`.
  - Optional extra: `quality_appraisal_scored.csv` (Item 18 source data, currently in `figures/`).
- **Data availability statement** (`\dataavailability` in `main.tex`): currently says public release deferred until after examination. **Verify MDPI accepts a private/deferred repo link** — may need to point to the public `slr_engine` GitHub (`github.com/vanjaluk8/slr_engine`) instead.
- **Pipeline CSVs NOT needed for submission.** The PRISMA checklist references files that live in the companion `slr_engine` repo (e.g. `13_final_reading_list_2026-05-12.csv`, `S1_prevalidated_corpus.csv`). These are audit/traceability artifacts, **not** submission uploads. Do not hunt for them inside `papers_code` — they are in the `slr_engine` repo.

---

## ⬜ Final pre-flight checklist (SUBMIT gate)

- [ ] Compile `main.tex` → read PDF end-to-end → fix any LaTeX warnings/broken refs
- [ ] Reconcile section headings with *AI* Instructions for Authors
- [ ] Write cover letter (significance, novelty, fit to scope; referee confirm)
- [ ] Zip LaTeX source + compiled PDF
- [ ] Zip all figures into one archive (`figures.zip`)
- [ ] Export graphical abstract to required format (or keep PDF)
- [ ] Finalize supplementary S1/S2 assignment + upload
- [ ] Fix `\dataavailability` repo links to something live/acceptable to MDPI
- [ ] Complete all SUSY form declarations (ethics, authorship, copyright, COI)
- [ ] Verify total upload ≤ 120 MB (figures ~1.5 MB, comfortable)
- [ ] Single-author approval step in SUSY

---

## Quick reference (other machine)

```bash
# Compile (on a machine with TeXLive / or Overleaf)
latexmk -pdf -interaction=nonstopmode main.tex

# Zip figures
cd writing/mdpi_paper && zip -r figures.zip figures

# Verify all referenced figures exist (should list 17 PDFs, all linked)
ls figures/*.pdf
```
