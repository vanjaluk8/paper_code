# Phase 0 — Reconnaissance Findings Report (pre-submission cleanup)

Project root (confirmed): `writing/mdpi_paper/` with `main.tex`, `sections/` (11 files),
`Definitions/` (mdpi.cls etc.), `figures/` (10 PDFs), `bibliography.bib` (147 entries).
No edits applied in this phase.

---

## Item 1 — Raw audit/log files: all present in the repo

Every file referenced in `12_appendix.tex` exists locally (under the snowball engine /
papers_repo, not inside `mdpi_paper/`):

| Referenced file | Actual location |
|---|---|
| `log_screening_2026-04-21.json` | `slr_engine/snowballing/snowball_output/` |
| `log_retrieval_2026-04-21.json` | `slr_engine/snowballing/snowball_output/` |
| `S7b_abstract_reviewed_final.csv` | `slr_engine/snowballing/snowball_output/` |
| `13_final_reading_list_2026-05-12.csv` | `slr_engine/snowballing/snowball_output/` and `writing/slr_methodology_paper/writing_materials/` |
| `08_zotero_ready_2026-05-02.ris` | `slr_engine/snowballing/snowball_output/` |
| `*_scopus_venue*`, `*_wos_venue*` | `M3_scopus_venue_validation_2026-05-11.csv`, `M4_wos_venue_validation_2026-05-11.txt` |
| `*forward_wos*`, `*FORWARD_SCOPUS*` | `M2_forward_wos_2026-05-08.txt`, `MANUAL_FORWARD_SCOPUS_0805.csv` |

Ground truth was taken from `S7b`, the final reading list, and the group CSVs.

---

## Item 2 — Corpus count: **"352" is correct, the table's "351" is wrong (G0 off by one)**

**Ground truth (S7b screening pool = PREVALIDATED + SEED directions):**

| Group | S7b pool | Methodology tab:groups |
|---|---|---|
| G0 | **9** | **8** ← mismatch |
| G1 | 59 | 59 |
| G2 | 37 | 37 |
| G3 | 95 | 95 |
| G4 | 51 | 51 |
| G5 | 35 | 35 |
| G6 | 66 | 66 |
| **Total** | **352** | **351** |

- G0 = **9** is independently confirmed by both `G0_seed_papers.md` (9 paper bullets) and
  S7b (SEED direction = 9).
- Every G1–G6 value in the methodology table matches the S7b screening pool exactly.
- **Conclusion:** the appendix's repeated "352-paper pre-validated corpus (G0–G6)"
  (`A.5` line 110, `C.1` line 622) is **correct**. The **methodology `tab:groups`
  is the one that is wrong** — its G0 is listed as 8 (should be 9), dragging the total
  to 351. Correcting G0 → 9 makes the total **352** and reconciles the whole document.
- Note: the raw group CSVs (G0–G6 = 9/62/42/98/56/46/77 = **386**) hold *more* records
  than the screening pool, because they are the pre-resolution group lists; the S7b
  PREVALIDATED+SEED counts are the authoritative numbers that actually entered
  abstract review, and they equal **352**.

**Action flagged (not yet applied):** change `03_methodology.tex` line 42 `G0 … 8` → `9`
and line 57 Total `351` → `352` (only if you agree 352 is the intended figure; the
appendix and PRISMA narrative already use 352).

---

## Item 3 — Abstract-review timeline: two inconsistencies in Table C.1 (and one resolved)

**Ground truth from S7b (552 records):**
- Abstract decisions: **214 KEEP / 338 SKIP** (A.7's Table 5 is correct for the 552 pool).
- Split by forward source:
  - `G_SNOW_F` (manual 05-08 forward, Scopus 74 + WoS 14 = 88): **12 KEEP / 76 SKIP**
  - `G0`-forward (Semantic-Scholar 04-21 forward on seeds): 86 records, 21 KEEP / 65 SKIP
  - PREVALIDATED (G1–G6): 343 records, 160 KEEP / 183 SKIP
  - BACKWARD + SEED: 26 + 9 records, 12 KEEP / 9 KEEP
- Cross-check: 214 = 12 (G_SNOW_F) + 202 (everything else); 338 = 76 + 262. ✓

### C.1 row "2026-04-28 | 464 → 214 KEEP; 338 SKIP" — **numbers belong to the wrong input**
214 + 338 = **552**, but the row's input column says **464**. The abstract review at
04-28 covered only the 464 enriched records; the 88 forward records were added **later**
(05-08) and contributed 12 KEEP / 76 SKIP on top. Decomposing the 552 totals:

- **04-28 abstract review (464 input): 202 KEEP / 262 SKIP** (202+262 = 464)
- **05-08 forward additions (88 input): 12 KEEP / 76 SKIP**
- **Combined 552: 214 KEEP / 338 SKIP**

The C.1 04-28 row therefore shows the **combined 552 totals against the pre-forward 464
input**. The row should read **464 → 202 KEEP; 262 SKIP** (or be reworded to indicate the
214/338 apply to the combined pool). The prose in §A.7 is itself correct ("across all 552
records").

### C.1 row "2026-05-02 | 214 KEEP → 387 queued" — **output exceeds input with DEFER = 0**
§A.7 states DEFER = 0, yet this row lists 214 KEEP in and **387 queued** out. With no
DEFER and no stated new records at this row, output cannot exceed input. Even adding the
later 88 forward records only reaches 302, not 387. **387 is unaccounted for.** The final
row ("387 queued → 123 final") depends on it. Either 387 is a typo, or the queue count
intentionally included something not described (e.g. borderline Tier-2/3 reads pulled
back in for re-check). This needs the author's source diary to resolve; it cannot be
derived from the CSVs.

### Verified consistent
- 05-08 forward row ("88 added → 12 KEEP; 76 SKIP") matches S7b `G_SNOW_F` **exactly**.
- 08_zotero_ready has **214** entries = KEEP count. ✓
- Final reading list has **123** rows = "123 final". ✓

**Actions flagged (not yet applied):** fix C.1 04-28 row (464 → 202/262); investigate/flag
the 214→387 step.

---

## Item 4 — Bibliography: 29 unused entries, all deliberately orphaned (per source log)

All 118 distinct `\cite` keys used across sections resolve; **29** bib entries are unused —
exactly the 29 named. The source project's `uncited_papers.txt` (in
`slr_methodology_paper/latex_folder/`) explains **every one**: they were intentionally
left uncited as content subsumed by cited works, out of scope, or unreadable.

Classification (all confirmed by membership in `13_final_reading_list_2026-05-12.csv`):

| Key | In final reading list? | Classification |
|---|---|---|
| BaiFedHetero2024 | Y | corpus paper, never discussed in MDPI text → delete or cite |
| BaziotisMultilingual2022 | Y | corpus paper → delete or cite |
| ByunFedRank2024/2025 | Y | corpus paper → delete or cite |
| CacciaMultiHead2022 | Y | corpus paper → delete or cite |
| ErmisMemory2022 | Y | corpus paper → delete or cite |
| FlinkLoRASwitch2025 | Y | corpus paper → delete or cite |
| FriedmanSingleDataset2021 | Y | corpus paper → delete or cite |
| Gabrielsson2024 | Y | corpus paper → delete or cite |
| GuptaSymbiosis2025 | Y | corpus paper → delete or cite |
| Iliakopoulou2024 | Y | corpus paper → delete or cite |
| KimClientCustomized2023 | Y | corpus paper → delete or cite |
| KuangFederatedScope2023 | Y | corpus paper → delete or cite |
| LinFedNLP2022 | Y | corpus paper → delete or cite |
| LiuBeyond2023 | Y | corpus paper → delete or cite |
| LuSEA2026 | Y | corpus paper → delete or cite |
| SuiFedED2020 | Y | corpus paper → delete or cite |
| WuFedBiOT2024 | Y | corpus paper → delete or cite |
| WuFedSurvey2025 | Y | corpus paper → delete or cite |
| YangFedLoraSurvey2025 | Y | corpus paper → delete or cite |
| ZhangHMI2025 | Y | corpus paper → delete or cite |
| ZhangITIF2023 | Y | corpus paper → delete or cite |
| ZhaoPrototype2023 | Y | corpus paper → delete or cite |
| AbdullahLlama2025 | Y (DOI match) | corpus paper (survey) → delete or cite |
| GaoDLoRA2024 | Y (DOI match) | corpus paper → delete or cite |
| Jaiswal2025 | Y (DOI match) | corpus paper → delete or cite |
| Xue2026 (MuxTune) | Y (title match) | corpus paper → delete or cite |
| **Johnson2023 (MIMIC-IV)** | N | **genuine background ref** — cited in source `10_poc.tex`, which was **dropped** in MDPI; orphaned because §9 PoC was cut. Keep for future PoC section or delete |
| **KitchenhamCharters2007** | N | **genuine methodology ref** — cited in source `03_methodology.tex`; MDPI rewrite dropped the citation → **candidate to re-instate** in Methodology |
| **Webster2002** | N | **genuine methodology ref** — same as Kitchenham; **candidate to re-instate** |

**Bottom line:** 26 are corpus papers dropped from MDPI text (safely deletable — they were
never meant to appear). `Johnson2023` is a background/dataset ref orphaned by the cut
PoC section. `KitchenhamCharters2007` and `Webster2002` are legitimately-cited
methodology works in the source that lost their citations during the MDPI rewrite — worth
**re-instating a citation** in the Methodology section rather than deleting.

**Actions flagged (not yet applied):** decide per class — delete the 26 corpus-only
entries (or add citations if you reconsider any), re-instate Kitchenham/Webster citations,
and decide Johnson2023 (keep for a future PoC).

---

## Item 5 — Abbreviations table gaps (GPU, CPU, KV-cache, SGMV, NF4 confirmed + extended)

Frequently used all-caps tokens **not in `\abbreviations{}`** (count = occurrences in
body text):

**Confirmed gaps (define in text, used 3+ times):**
| Token | n | Where defined in body |
|---|---|---|
| **GPU** | 31 | — (used plainly) |
| **CPU** | 14 | — |
| **KV-cache** | 4 | 06:41 (expanded as "KV-cache") |
| **SGMV** | 2 | 06:52 "(SGMV, Segmented Gather Matrix-Vector)"; reused 09:51 |
| **NF4** | 2 | 04:152 "4-bit NormalFloat (NF4)"; reused 04:159 |

**Recommended adds (technical terms, high frequency, no table entry):**
| Token | n | Notes |
|---|---|---|
| **NLU** | 17 | Natural Language Understanding |
| **GLUE** | 23 | benchmark name — commonly kept out; your call |
| **SOTA** | 6 | state-of-the-art |
| **ML** | 7 | Machine Learning |
| **WoS** | 18 | Web of Science |

**Deliberately excluded (not needed in table):** model names (BERT, GPT, T5, RoBERTa),
venue names (ACL, EMNLP, ICML, NeurIPS, MLSys), MAD-X, BBH, NER, GB, SQL, arXiv, and
search-query tokens from the appendix (TITLE-ABS, TS, KEY, BA, PY — these are Scopus/WoS
field codes, not abbreviations the reader needs defined).

`PEFT, LoRA, P2P, DHT, MoE, FL, LLM, NLP, HBM, API, FFN, MHA, SVD, IID, DP, PRISMA, SLR, RQ, SQ`
are already present and fine.

**Actions flagged (not yet applied):** add rows for **GPU, CPU, KV-cache, SGMV, NF4**
(minimum — matches your own list), and optionally NLU / SOTA / ML / WoS / GLUE.

---

## Summary of findings (nothing edited)

| # | Finding | Location(s) affected | Priority |
|---|---|---|---|
| 2 | 351 should be 352 — methodology `tab:groups` G0=8 → 9 | `03_methodology.tex:42,57` | High (factual) |
| 3a | C.1 04-28 row shows 552 totals against 464 input | `12_appendix.tex:626` | High (factual) |
| 3b | "214 → 387 queued" output>input with DEFER=0 | `12_appendix.tex:628` | Medium (needs source) |
| 4 | 26 corpus-only unused bib entries + 3 back/meth refs | `bibliography.bib` | Medium |
| 5 | GPU, CPU, KV-cache, SGMV, NF4 (+ NLU/SOTA/ML/WoS) missing | `main.tex` `\abbreviations{}` | Low/Medium |

Phase 1 items 6 (grammar), 7 (DOI), 8 (ISO-4), 9 (conclusion sentence) are scoped for the
next phase. All of the above are **reported only**; awaiting your go-ahead before applying.
