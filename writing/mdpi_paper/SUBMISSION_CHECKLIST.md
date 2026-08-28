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
| **Compiled PDF** | ⬜ | Not present on disk. Must be compiled from source before upload. Zip the `.tex` source, `sections/`, `Definitions/`, `bibliography.bib`, and the PDF together. |

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
| Cover letter | ⬜ | **Not yet written.** Must explain significance, novelty, and fit to *AI* journal scope. |
| Suggested referees | ⬜ | Field-specific — confirm whether *AI* requires them; some legacy MDPI guidelines want 4–5 named referees in the letter. |

---

## 2. Figures, Data & Supplementary Material

### 2.1 Figures ZIP archive
MDPI wants **all figures in a single ZIP**, high resolution — min **1000 px** width/height or **≥300 dpi**; TIFF/JPEG/EPS/PDF preferred.

| Item | Status | Notes |
|---|---|---|
| Figures (PDF) | ✅ | **15 figures total** in `figures/` (11 pre-existing + 4 newly generated) |
| **Package into single ZIP** | ⬜ | Not yet zipped. Include every figure referenced in the manuscript. |
| Resolution check | ✅ | All figures are vector PDFs (resolution-independent, ≥1000 px at any reasonable rendering). |

**Figures referenced and present** (all in `figures/`):

**Pre-existing (11):**
- `fig_concept_peft_paradigm.pdf`, `fig_peft_adapter_types.pdf`, `fig_houlsby_adapter_figure.pdf`
- `fig_p2p_dht_lookup.pdf`, `fig_p2p_gossip.pdf`, `fig_gap_quadrant.pdf`
- `fig_slr1_prisma_flow.pdf`, `fig_slr_quality_bands.pdf`
- `fig_slr6_tier_breakdown.pdf`, `fig_slr5_venues.pdf`, `fig_slr3_year_distribution.pdf`

**Newly generated & linked (4):**
- `fig_peft_taxonomy.pdf` — PEFT families taxonomy (section 4, `\label{fig:peft_types}`)
- `fig_adapterfusion.pdf` — AdapterFusion fusion layer (section 5, `\label{fig:adapterfusion}`)
- `fig_switch_transformer.pdf` — Switch Transformer Top-1 routing (section 7, `\label{fig:switch_transformer}`)
- `fig_petals.pdf` — Petals collaborative inference (section 8, `\label{fig:petals}`)

### 2.2 Graphical Abstract (GA)
| Item | Status | Notes |
|---|---|---|
| Graphical Abstract | ⬜ | Not created. Optional but recommended — high-quality PNG/JPEG/TIFF. Could reuse the gap-quadrant or concept figure as a basis. |

### 2.3 Original / uncropped images (integrity verification)
| Item | Status | Notes |
|---|---|---|
| Original unadjusted images | ➖ | Not an experimental/biomedical study — not applicable for this SLR unless the journal still requests source figures. |

### 2.4 Supplementary data & depositions
| Item | Status | Notes |
|---|---|---|
| Supplementary files packaged | 🟡 | `supplementary/` holds PRISMA 2020 checklist + PRISMA numbers/summary MDs. Need to confirm these are what will be attached as S1. |
| PRISMA 2020 checklist (S1) | ✅ | `supplementary/PRISMA_2020_checklist.md` — referenced as download in `\supplementary{}` |
| Raw datasets / extended tables | 🟡 | `quality_appraisal_scored.csv` lives in `figures/`; decide whether to attach as supplementary data. |
| **Sequence/database depositions + accession numbers** | ➖ | No new sequences/databases generated — review of published literature. |
| Datasets/repo links in Data Availability | ✅ | `\dataavailability{...}` points to `papers_code` (private) + `slr_engine` (public GitHub). **Action:** confirm repo is public / accessible before submission (currently `dataavailability` says public release deferred until after examination — verify this is acceptable to MDPI). |

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

- [ ] Compile the manuscript and read the PDF end-to-end (orphan sections, figure numbering, references resolve, no LaTeX warnings that break build). **No LaTeX engine on this machine — compile on Overleaf or a system with TeXLive.**
- [ ] Reconcile section headings with the target journal's Instructions for Authors.
- [ ] Finalize & upload the **compiled PDF** + LaTeX source zip.
- [ ] Write and attach the **cover letter** (significance, novelty, fit to journal scope; confirm referee requirement).
- [x] Resolve all 4 `\fbox` figure placeholders — replaced with `\includegraphics` and generated schematic PDFs.
- [ ] Zip all **figures** into a single archive; vector PDFs — no resolution concern.
- [ ] Create **Graphical Abstract** (PNG/JPEG/TIFF).
- [ ] Decide which files (PRISMA checklist, quality scoring CSV, etc.) become **Supplementary S1/S2** and attach.
- [ ] Confirm `\dataavailability` repo links are live/accessible as stated (private repo currently deferred — verify MDPI policy accepts this).
- [ ] Complete all **declarations in the SUSY form** (ethics, authorship, copyright, COI) — finalized, not just in the manuscript.
- [ ] Verify **total upload size ≤ 120 MB** — figures are ~1.5 MB, well under cap.
- [ ] For single-author paper: confirm author-approval step in SUSY is satisfied.

---

## Reference — the three MDPI requirement buckets (quick recall)

**A. Core manuscript:** template-formatted manuscript (Word or LaTeX + compiled PDF); all front/back matter sections; mandatory cover letter (significance, novelty, fit; possibly 4–5 suggested referees).

**B. Figures/data/supplementary:** figures Packaged as one high-res ZIP (≥1000 px / ≥300 dpi; TIFF/JPEG/EPS/PDF); Graphical Abstract; unadjusted source images if requested; supplementary data + sequence/database accession numbers; total ≤ 120 MB.

**C. Ethics/authorship:** co-author approval + reading of Instructions for Authors; informed consent where identifiable info; publication/research-ethics, copyright, authorship & COI statements; ARRIVE checklist for animal work.
