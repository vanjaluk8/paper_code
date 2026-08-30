# MDPI Submission Checklist & Reference

> **Target journal:** MDPI *AI* — `\documentclass[ai,...]` (see `main.tex:6`)
> **Tracked against:** the core MDPI package shared across titles (Sustainability, Technologies, Publications, Stats, AI, Information, ...).
> **Status legend:** ✅ Ready · 🟡 Partial / needs action · ⬜ To do · ➖ Not applicable (N/A)

---

## 1. Core Manuscript Files

### 1.1 Main manuscript (LaTeX source + compiled PDF)
MDPI does not accept free-form formatting — the manuscript must use the official MDPI LaTeX (or Word) template. **If LaTeX: both the source files AND a compiled PDF must be submitted.**

| Item | Status | Location / Notes |
|---|---|---|
| `main.tex` (master) | ✅ | `writing/mdpi_paper/main.tex` — uses `Definitions/mdpi.cls` |
| Section sources | ✅ | `writing/mdpi_paper/sections/01…12_appendix.tex` |
| LaTeX template (`Definitions/`) | ✅ | `mdpi.cls`, `mdpi.bst`, `mdpi_apacite.*`, `mdpi_chicago.*`, `journalnames.tex`, `logo-*.eps` |
| Bibliography | ✅ | `writing/mdpi_paper/bibliography.bib` |
| **Compiled PDF** | ✅ | `main.pdf` compiles cleanly (66 pages, no undefined refs/citations). Still need to zip `.tex` source, `sections/`, `Definitions/`, `bibliography.bib`, and the PDF together. |

### 1.2 Required front-matter & back-matter sections
All must already be present inside the manuscript body (MDPI checks these on submission).

| Section | Present? | Location / Notes |
|---|---|---|
| Title | ✅ | `main.tex` (`\Title{...}`) |
| Author list | ✅ | `\Author{Vanja Luk ...}` — single author |
| Affiliations | ✅ | `\address{...}` (University of Rijeka, FDIT) |
| ORCID | ✅ | `\orcidauthorA{0009-0009-8142-6890}` |
| Abstract | ✅ | `\abstract{...}` (~200 words, single paragraph) |
| Keywords | ✅ | `\keyword{...}` (9 terms) |
| Introduction | ✅ | `sections/01_introduction.tex` |
| Materials & Methods (→ Methodology) | ✅ | `sections/03_methodology.tex` (PRISMA 2020 + snowballing) |
| Results (→ Results & Synthesis) | ✅ | `sections/04_peft` … `09_synthesis_gap` |
| Discussion / Conclusions | ✅ | `sections/11_conclusion.tex` |
| Supplementary Materials | ✅ | `\supplementary{...}` in `main.tex` |
| Acknowledgments | ✅ | `\acknowledgments{Not applicable.}` |
| Author Contributions | ✅ | `\authorcontributions{...}` |
| Conflicts of Interest | ✅ | `\conflictsofinterest{...}` |
| References | ✅ | `\bibliography{bibliography}` |

> Template note: this SLR uses a methodology/Results framing rather than a literal *Materials and Methods*–*Results* split; MDPI accepts the SLR-specific section set. Section headings should be reconciled against the journal's *AI* Instructions for Authors on final read-through.

### 1.3 Cover letter — REQUIRED for every submission
| Item | Status | Notes |
|---|---|---|
| Cover letter | ✅ | Drafted at `cover_letter.md` (significance, novelty, fit to *AI* scope). |
| Suggested referees | 🟡 | Placeholder rows in `cover_letter.md` — names/affiliations still need to be filled in (or section removed if *AI* doesn't require them). |

---

## 2. Figures, Data & Supplementary Material

### 2.1 Figures ZIP archive
MDPI wants **all figures in a single ZIP**, high resolution — min **1000 px** width/height or **≥300 dpi**; TIFF/JPEG/EPS/PDF preferred.

| Item | Status | Notes |
|---|---|---|
| Figures (PDF) | ✅ | **15 in-manuscript figures** in `figures/` (11 pre-existing + 4 newly generated) plus the graphical abstract (`fig_ga.pdf`, separate SUSY upload, not in-manuscript) |
| **Package into single ZIP** | ⬜ | Not yet zipped. Include every figure referenced in the manuscript. |
| Resolution check | ✅ | All figures are vector PDFs (resolution-independent, ≥1000 px at any reasonable rendering). |

**Figures referenced and present** (all in `figures/`):

**Pre-existing (11):**
- `fig_concept_peft_paradigm.pdf`, `fig_peft_adapter_types.pdf`, `fig_houlsby_adapter_figure.pdf`
- `fig_p2p_dht_lookup.pdf`, `fig_p2p_gossip.pdf`, `fig_gap_quadrant.pdf`
- `fig_slr1_prisma_flow.pdf`, `fig_slr_quality_bands.pdf`
- `fig_slr6_tier_breakdown.pdf`, `fig_slr5_venues.pdf`, `fig_slr3_year_distribution.pdf`

**Newly generated & linked (4) — built as HTML/CSS/SVG source, rendered to vector PDF via headless Chrome:**
- `fig_peft_taxonomy.pdf` (source `fig_peft_taxonomy.html`) — PEFT families taxonomy (section 4, `\label{fig:peft_types}`)
- `fig_adapterfusion.pdf` (source `fig_adapterfusion.html`) — AdapterFusion fusion layer (section 5, `\label{fig:adapterfusion}`)
- `fig_switch_transformer.pdf` (source `fig_switch_transformer.html`) — Switch Transformer Top-1 routing (section 7, `\label{fig:switch_transformer}`)
- `fig_petals.pdf` (source `fig_petals.html`) — Petals collaborative inference (section 8, `\label{fig:petals}`)

### 2.2 Graphical Abstract (GA)
| Item | Status | Notes |
|---|---|---|
| Graphical Abstract | ✅ | `figures/fig_ga.pdf` rendered from `figures/ga.html` via headless Chrome. Not wired into `main.tex` (GA is a separate SUSY upload, not an in-manuscript figure). |

### 2.3 Original / uncropped images (integrity verification)
| Item | Status | Notes |
|---|---|---|
| Original unadjusted images | ➖ | Not an experimental/biomedical study — not applicable for this SLR unless the journal still requests source figures. |

### 2.4 Supplementary data & depositions
| Item | Status | Notes |
|---|---|---|
| Supplementary files packaged | ✅ | `\supplementary{}` in `main.tex` now lists S1 (PRISMA 2020 checklist) and S2 (`quality_appraisal_scored.csv`) explicitly. |
| PRISMA 2020 checklist (S1) | ✅ | `supplementary/PRISMA_2020_checklist.md` — referenced as download in `\supplementary{}` |
| Raw datasets / extended tables (S2) | ✅ | `quality_appraisal_scored.csv` (123 rows, six-dimension rubric) — now wired in as S2. |
| **Sequence/database depositions + accession numbers** | ➖ | No new sequences/databases generated — review of published literature. |
| Datasets/repo links in Data Availability | 🟡 | `\dataavailability{...}` now points to `slr_engine` (public) + `papers_code` at `https://github.com/vanjaluk8/papers_code` — **this papers_code URL is a placeholder** (marked `%TODO` in `main.tex`); confirm/replace with the final public repo URL before submission. |

### 2.5 Combined file size cap
| Item | Status | Notes |
|---|---|---|
| Total submission ≤ **120 MB** | ✅ | Current figures total ~1.5 MB — well under cap even with GA + supplementary + compiled PDF. |

---

## 3. Ethics & Authorship Declarations

| Item | Status | Notes |
|---|---|---|
| **Author approval** — all co-authors approve content & confirm they read Instructions for Authors | ✅ | Single author (V.L.) — self-approval; declare in SUSY. |
| Informed consent (identifiable patient/participant info) | ➖ | Review of published literature — `\informedconsent{Not applicable.}` already set. |
| Publication ethics / research ethics / **IRB** statements | ✅ | `\institutionalreview{Not applicable.}` set. |
| Copyright & conflict-of-interest declaration | ✅ | `\conflictsofinterest{Not applicable.}` set. |
| **ARRIVE checklist** (animal research) | ➖ | No animal studies — applies only to some journals (e.g., *Information*); N/A here. |

---

## 4. Final Pre-Flight Checklist (before clicking Submit in SUSY)

- [x] Compile the manuscript and read the PDF end-to-end — `main.pdf` compiles cleanly via `latexmk -pdf` (TinyTeX, reinstalled to TL2026 + missing packages installed), 66 pages, no undefined refs/citations left.
- [ ] Reconcile section headings with the target journal's Instructions for Authors.
- [ ] Finalize & upload the **compiled PDF** + LaTeX source zip.
- [x] Write and attach the **cover letter** — drafted at `cover_letter.md`; referee names still placeholders.
- [x] Resolve all 4 `\fbox` figure placeholders — replaced with `\includegraphics`; the 4 schematic PDFs were actually missing from disk despite being referenced, now built as HTML/SVG (`fig_*.html`) and rendered to vector PDF via headless Chrome.
- [ ] Zip all **figures** into a single archive; vector PDFs — no resolution concern.
- [x] Create **Graphical Abstract** — `fig_ga.pdf` rendered from `ga.html`.
- [x] Decide which files become **Supplementary S1/S2** — S1 = PRISMA checklist, S2 = `quality_appraisal_scored.csv`; wired into `\supplementary{}`.
- [ ] Confirm `\dataavailability` repo link for `papers_code` — currently a placeholder URL, swap for the real one before submission.
- [ ] Complete all **declarations in the SUSY form** (ethics, authorship, copyright, COI) — finalized, not just in the manuscript.
- [ ] Verify **total upload size ≤ 120 MB** — figures are ~1.5 MB, well under cap.
- [ ] For single-author paper: confirm author-approval step in SUSY is satisfied.

---

## Reference — the three MDPI requirement buckets (quick recall)

**A. Core manuscript:** template-formatted manuscript (Word or LaTeX + compiled PDF); all front/back matter sections; mandatory cover letter (significance, novelty, fit; possibly 4–5 suggested referees).

**B. Figures/data/supplementary:** figures Packaged as one high-res ZIP (≥1000 px / ≥300 dpi; TIFF/JPEG/EPS/PDF); Graphical Abstract; unadjusted source images if requested; supplementary data + sequence/database accession numbers; total ≤ 120 MB.

**C. Ethics/authorship:** co-author approval + reading of Instructions for Authors; informed consent where identifiable info; publication/research-ethics, copyright, authorship & COI statements; ARRIVE checklist for animal work.
