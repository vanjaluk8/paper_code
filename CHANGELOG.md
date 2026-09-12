# CHANGELOG.md

Every edit made during the peer-review revision (`REVISION_PROMPT.md`),
grouped by work package. Each entry: item ID(s), file(s)/line range, one-line
rationale, and class (**MECHANICAL** / **DATA**). DATA edits cite the script
that produced the number. Full git history is in this repo; this file is the
audited summary requested by Phase 4.

Pre-revision, unrelated: `aaaa3b6` fixed an unclosed `\emph{}` brace in
`sections/03_methodology.tex` that was blocking the LaTeX build entirely —
a pure syntax bug, not part of the reviewer response.

---

## Phase 1 — MECHANICAL

### WP-1 — cross-references and build hygiene (`0618068`)
- **C-1** — `sections/12_appendix.tex`: Appendix C's four `\subsection*{}`
  headings had no manual numbering (unlike every sibling appendix
  subsection), so `\ref{}` to them rendered as garbage
  ("Appendix C.0.0.22", "§C.0.0.20"). Added "C.1"–"C.4" to the heading text
  and replaced the four broken `\ref{app:db_queries:*}` call sites
  (`sections/03_methodology.tex`, `sections/11_conclusion.tex`,
  `sections/12_appendix.tex`) with the working section-level label plus a
  literal "§ C.3"/"§ C.4" suffix. **MECHANICAL**
- **C-6** — `sections/09_synthesis_gap.tex`: narrowed a claim that both the
  latency and incentive-mechanism exclusions "are reflected in the
  limitations discussed in Section 10.4" — Section 10.4 only discusses
  incentives, not latency. **MECHANICAL**
- **Minor #31** — `sections/04_peft.tex`: closed an unbalanced parenthesis
  in the BitFit sentence. **MECHANICAL**

### WP-2 — duplication (`2826e46`)
- **D-1** — removed three duplicate figures: `fig:peft_paradigm` (Sec 6,
  reused Figure 1's image), `fig:dht_lookup` (Sec 8.6, reused Figure 3's
  image), `fig:gossip` (Sec 8.2, reused Figure 4's image) — replaced with
  cross-references to the originals. None were redrawn with new content;
  flagged for the author's judgement in the commit message. **MECHANICAL**
- **C-3** — `sections/04/05/06/07/08_*.tex`: the sentence "The … findings of
  this section are consolidated … in Section 9.1" appeared verbatim 5
  times; kept the first (Sec 4), deleted the other 4. **MECHANICAL**
- **C-4** — `sections/08_p2p_federated.tex`: cut the Sec 8.6 Kademlia
  description (already given in Sec 2.3) to a cross-reference. **MECHANICAL**
- **C-5** — `sections/02_background.tex`: Figure 1's caption claimed an
  "adapter exchange via shared repositories" element the figure doesn't
  contain (verified by rendering the PDF directly) — corrected the caption.
  **MECHANICAL**

### WP-3 — terminology and abbreviations (`b4f281e`)
- **C-2** — defined SLO, IA³, CORE A*, Scopus Q1 on first use; extended the
  Abbreviations list (`main.tex`) with SLO, IA³, SGMV, NF4, MBC, GLUE, BBH.
  **MECHANICAL**
- **Minor #28** — "Wohlin et al."→"Wohlin" (5 instances, confirmed
  single-authored against `bibliography.bib`); "Chen et al."→"Chen" (the
  single-authored `ChenFlashServe2025`); "Mahabadi et al."→"Karimi Mahabadi
  et al." at both occurrences, plus fixed the bib `author` field for both
  entries. **MECHANICAL**
- **E-4 (naming half)** — disambiguated "MOELoRA (Liu et al.)" vs "MoELoRA
  (Luo et al.)" at every occurrence including Table 7. **MECHANICAL**
  (the *substantive* E-4 question — whether the two claims attributed to
  Liu et al. are accurate — is answered in `OPEN_QUESTIONS.md`: both
  CONTRADICTED)
- **Minor #32** — replaced the one located instance of "to the best of the
  author's knowledge" with "within the 123-record corpus" (§8.3).
  **MECHANICAL**

### WP-4 — reference-list formatting (`6b4e6f9`, `2041554`)
- **Minor #40** — normalised ref [29]'s non-standard `note` field to a
  `doi` field; removed the CaraServe/Toppings explanatory note from ref
  [7] (already stated in running prose, so not duplicated as a footnote).
  **MECHANICAL**
- Documented the arXiv-DOI-first convention as a `bibliography.bib` header
  comment, per author decision on the 40-vs-2 DOI-format inconsistency
  reported alongside the fix. **MECHANICAL** (documentation only)

### WP-5 — abstract (`77d5af7`, superseded by `4c9af87`)
- Trimmed the concept-matrix dimension list to free room for the required
  discovery-route clause; placeholder later replaced with the verified
  82.1/11.4/6.5% split once WP-6 computed it. Final abstract: 193 words.
  **MECHANICAL**

---

## Phase 2 — DATA

### WP-6 — seed-origin attribution, Table 5 (`4c9af87`) — P1-2
- **Script:** `verify/wp6_seed_origin_route_split.py`
- **Finding:** Houlsby (2019) and LoRA (Hu et al. 2022) are 2 of the 9 G0
  seed papers, each present as 2 rows (arXiv + Scopus) attributed by group
  label to G2/G1 rather than G0 — 4 rows total, previously counted inside
  "targeted retrieval" (105) instead of as seed-origin.
- **Corrected:** targeted retrieval 105→**101**, seed-origin 4→**8**,
  snowball unchanged at 14. Sum still 123.
- **Files:** `sections/03_methodology.tex` (Table 5 + §3.2 prose), `main.tex`
  (abstract route-split clause). **DATA**

### WP-7 — 19 UNCERTAIN records' disposition (`6244cff`) — P1-3
- **Script:** `verify/wp7_uncertain_disposition.py`
- **Finding:** `log_screening_2026-04-21.json`'s `llm_screening` field shows
  the 19 UNCERTAIN records dropped at title screening, absent from both the
  162 final-INCLUDE and 791 final-EXCLUDE tallies — consistent with Figure
  5's account, contradicting two other passages in Appendix A.
- **Files:** `sections/12_appendix.tex` (2 passages rewritten to agree),
  `figures/prisma.html` + regenerated `figures/fig_slr1_prisma_flow.pdf`
  (rescue-file wording fix). **DATA**

### WP-8 — Table 7 Public column, Pillar-4 denominator (`bcd035e`) — P1-4, C-8
- **Script:** `verify/wp8_table7_public_column.py`
- **Finding:** Ostapenko row read "No" in the table body but "Unknown" in
  the caption/§3.4.1 — script parses the table body directly and confirms
  the fix (26/1/2/4 now matches exactly). Pillar 4 has 7 rows, not 3, per a
  direct parse.
- **Files:** `sections/03_methodology.tex` (1 cell + 2 prose passages).
  **DATA**

### WP-9 — appraisal over 120 distinct studies; gross records (`1e3aebd`) — P1-5, P1-7
- **Script:** `verify/wp9_appraisal_n_and_totals.py`
- **Finding:** 3 duplicate-identity record pairs are NOT scored identically
  (LoRA 8/8 matches, Houlsby 5/6 and CaraServe/Toppings 7/6 don't) — the
  "duplicates scored identically, mean unaffected" defence doesn't hold.
  Recomputed mean/SD/bands over the 120-distinct-study subset (author's
  chosen rule: keep the arXiv-keyed record for LoRA/Houlsby, the
  peer-reviewed record for CaraServe/Toppings).
- **Corrected:** mean 6.04→**6.03**, SD 2.00→**2.01**, bands
  13/61/47/2→**13/59/46/2**.
- **Files:** `sections/03_methodology.tex` (Sec 3.4 prose + Figure 6
  caption), `figures/fig_slr_quality_bands.pdf` (regenerated, script:
  `verify/wp9_regen_fig_slr_quality_bands.py`), `main.tex` (`\supplementary{}`
  description). Also added the P1-7 gross-records-identified sentence
  (1,658) to §3.1. **DATA**

### WP-11 — Figure A3 population mismatch (`c94a3bd`) — D-2
- **Script:** `verify/wp11_figure_a3_venue_population.py`
- **Finding:** the figure's rendered pie chart reads "123 total" and its
  bars exactly match the 123-record final corpus (verified by recomputing
  venue counts from `13_final_reading_list_2026-05-12.csv`), not the
  464-record enriched pool the old caption claimed.
- **Files:** `sections/12_appendix.tex` (caption + preceding sentence
  rewritten; no figure regeneration needed, the image was already correct).
  **DATA**

### WP-12 — Boolean recall of the final corpus (`ace12f6`) — Major #10
- **Script:** `verify/boolean_recall.py`
- **Result:** **104 of 123 (84.6%)** final records are returned by at least
  one of the 20 Scopus/WoS Boolean queries (59 by DOI, 45 by title only).
  Full per-record table and the 19 non-recalled records in
  `verify/boolean_recall.md`.
- **No manuscript prose written** — per task instructions, the number and
  table are the deliverable; the interpretive paragraph is the author's to
  write. **DATA**

### WP-13 — inclusion-route defect (`8fc5372`, `1e61c8e`) — P1-1, Blocking 2
- **Script:** `verify/wp13_inclusion_route_membership.py`
- **Finding:** all 123 final records — both the 70 tagged
  `review_source=fulltext` and the 53 tagged `abstract-2nd-pass` — have
  `in_fulltext_queue_Q9=1` and `in_extraction_E11=1` in
  `pipeline_unified.csv`. `review_source` is an internal workflow tag, not
  a membership boundary; the 224→101→123 arithmetic is valid for all 123.
- Also checked the 173 DEFER records (0 reach final; 1 unexpectedly has
  `in_extraction_E11=1`) and found a secondary anomaly (2 of the 34 manual
  top-up records have `in_fulltext_queue_Q9=1`, contradicting the
  manuscript's own source-comment claim that none do) — both flagged, not
  silently corrected.
- Added `entered_eligibility` to `snowball_output/pipeline_unified.csv`
  (evidence-derived: identical to the existing `in_extraction_E11` flag).
- **Files:** `sections/03_methodology.tex` (§3.2 rewritten, **author-approved
  wording**, see commit `1e61c8e`), `figures/prisma.html` + regenerated
  `figures/fig_slr1_prisma_flow.pdf` (INCLUDED box wording, also
  author-approved). **DATA**

### WP-14 — extended verification scripts — all P1-* relations
- **Location:** the sibling `mdpi_slr_engine` repository (where
  `verify_prisma_counts.py` / `verify_quality_appraisal.py` actually live),
  commit `a7ed994`.
- Extended `verify_prisma_counts.py` from 40 to **62** passing checks:
  added the WP-6 route split, per-group Table 3 tallies, UNCERTAIN
  disposition, WP-13 membership check, and 173-DEFER check.
- Extended `verify_quality_appraisal.py` from 19 to **36** passing checks:
  added the WP-9 120-distinct-study mean/SD/band computation and the WP-8
  Table 7 Public-column/Pillar-4 tally (against
  `artifact_availability_verified.csv`, the source-of-truth behind Table
  7's Public column).
- Added `manuscript_repo_snowball_output_dir()` / `manuscript_repo_figures_dir()`
  resilience fallbacks to `verify_common.py`, pointing at this repo's
  `snowball_output/`/`figures/` directories.
- Added `verification_fixtures/` to `mdpi_slr_engine`'s `.gitignore` — it
  was untracked but not ignored, meaning a careless `git add -A` there
  would have committed restricted vendor data (citation counts, abstracts)
  that repo's own licence rules forbid distributing.
- Saved run outputs mirrored into this repo's
  `snowball_output/verification_runs/`. **DATA**

---

## Data files recovered / added

- `chore(data)` commit `cba36ea`: added `11_data_extraction_2026-05-12.csv`,
  `11_MANUAL_SCOPUS_export_1105.csv`, `11_MANUAL_WOS_export_1105.txt`,
  `MANUAL_FORWARD_SCOPUS_0805.csv`, `M1_forward_wos_2026-05-08.txt` to
  `snowball_output/` — files the Data Availability statement already
  claimed were version-controlled here but were absent; also carved a
  `.gitignore` exception for the extraction CSV (previously blanket-excluded
  by a `*_data_extraction_*.csv` rule).

---

## Major #21 — citation DOI corrections (not an E-item, found during the
## systematic citation-verification pass)

- `5dca50f`: `MahabadiCompacter2021`'s DOI pointed at a non-existent arXiv ID
  (2110.16277); corrected to the verified real ID (2106.04647).
- `b8ec5b7`: `Ostapenko2024` and `Fedus2022` both cited fabricated-looking
  `10.5555/...` DOIs (404 on doi.org, no Crossref record); corrected both to
  their real, verified arXiv DOIs.
- All three are **MECHANICAL, network-verified identifier corrections** —
  author/title/venue were already correct; only the DOI digits were wrong.

**Process disclosure:** `5dca50f` was committed autonomously by a background
research subagent (launched to do primary-source PDF verification for the
E-items) before it stalled partway through its task. The fix itself was
independently re-derived and verified correct in this session before the
commit's existence was discovered; it was not reverted, since the change is
factually correct, but the commit was made without the normal review-before-
commit step this revision otherwise followed throughout. See
`OPEN_QUESTIONS.md`'s "Process note" section for the full account, including
the duplicate/less-accurate scaffolding files that subagent also produced
(discarded) before stalling.

---

## Phase 3 — AUTHOR report

`OPEN_QUESTIONS.md` — primary-source-verified findings for all `E-1`…`E-15`,
`S-1`…`S-4`, `N-1`, `N-3`; scaffolding for Blocking 5, Major 11, Major 18,
Major 20, Major 21. See that file for full detail; not duplicated here since
it makes no manuscript edits.
