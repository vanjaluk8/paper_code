# SLR Methodology Outline
## Search Strategy and Study Selection

**For:** Systematic Literature Review — Decentralised Adapter-Based LLM Systems  
**Thesis:** P2P Multi-Task NLP Inference Using PEFT Adapters over a Shared Frozen Transformer Backbone  
**Affiliation:** University of Rijeka, Faculty of Informatics and Digital Technologies  
**Governing framework:** PRISMA 2020 \citep{Page2021}; Snowballing procedure \citep{Wohlin2014}  

---

## Alignment with PDF Guidelines

| PDF requirement (Research Methodology in IS/CS) | Status in pipeline |
|---|---|
| Comprehensive pre-planned strategy (systematic review definition) | ✅ Fully automated, reproducible pipeline |
| State database(s) used explicitly | ✅ Added to PRISMA summary (search date + DB list) |
| Define and report inclusion/exclusion criteria in a table | ✅ Added to PRISMA summary as formal I/E table |
| Snowballing procedure: backward + forward (Wohlin 2014) | ✅ Implemented via Semantic Scholar API |
| Three-step: leading venues → backward → forward (Jalali & Wohlin 2012) | ✅ G0 seeds are top-venue foundational papers |
| Title → abstract → full-text screening (PRISMA flow) | ✅ Three-layer title screen + abstract review step |
| Seed selection rationale (why these papers?) | ✅ G0_seed_papers.md documents criteria per paper |
| Search date prominently recorded | ✅ Added to PRISMA summary header |
| PRISMA flow diagram | ✅ fig_slr1_prisma_flow.png (extends with abstract review) |
| Venue/source quality assessment | ✅ `venue_quality` column (top_venue / peer_reviewed / preprint / unknown) |
| Enrichment source traceability | ✅ `enrichment_sources` column records acl / semantic_scholar / openalex per paper |
| WoS role clarified | ✅ WoS used for citation-count enrichment only, not as snowball source (corrected from earlier draft) |
| Pre-validated corpus filter bypass clarified | ✅ G1–G6 bypass both year and domain filters (manual curation is the quality gate) |
| Language filter | ⚠️ No mechanical filter — English coverage is implicit in source database indexing |
| Iterative saturation | ⚠️ Single snowball wave performed; saturation assessed manually via G1–G6 overlap |

---

## Suggested Section Heading

> **§3.2 Search Strategy and Study Selection**

*(or, if part of a broader methods chapter:)*

> **§3 Research Methodology — Systematic Literature Review Protocol**

---

## Paragraph-by-Paragraph Outline with Draft Text

---

### ¶1 — Review type and governing framework

This study adopts a **Systematic Literature Review (SLR)** methodology, defined as a
comprehensive pre-planned strategy for locating, critically appraising, analysing, and
synthesising existing research pertinent to a clearly formulated research question
\citep{Moher2009}. The review follows the **PRISMA 2020** reporting guidelines
\citep{Page2021}, which structure the process into four stages: *Identification*,
*Screening*, *Eligibility*, and *Inclusion*. The thesis design question is:

> *How can lightweight task-specific adapters be discovered, fetched, composed, and served
> across a P2P network of nodes sharing a single frozen transformer backbone, with minimal
> latency and without centralised orchestration?*

The SLR operationalises this question as:

> *What methods have been proposed for decentralised, adapter-based multi-task inference
> over a shared frozen transformer backbone, and what are the open research gaps?*

The review synthesises three intersecting fields: parameter-efficient fine-tuning (PEFT)
and adapter architectures; distributed and peer-to-peer (P2P) machine learning systems;
and multi-task large language model (LLM) serving and inference. This three-pillar
framing directly drives the corpus design: Groups G1–G2 cover PEFT and adapter
composition; Groups G3, G6 cover decentralised and federated learning; Groups G4–G5
cover inference systems and MoE routing. The coverage of all three pillars is a
necessary precondition for positioning the thesis contributions (§3.X below).

---

### ¶2 — Seed paper selection and pre-validated corpus

The search was anchored on a set of **nine foundational seed papers** (Group G0), selected
on the basis of three criteria: (*i*) direct relevance to at least two of the three core
themes (PEFT/adapters; distributed/P2P systems; multi-task LLM serving); (*ii*) high
citation impact (≥ 300 citations at time of selection); and (*iii*) publication in a
top-tier venue (ICML, ICLR, NeurIPS, ACL/EMNLP/EACL, MLSys, or a Scopus Q1 journal).
These seeds span the three pillars of the thesis: adapter architectures
\citep{Houlsby2019, Hu2022, Pfeiffer2020hub, Pfeiffer2021fusion}, multi-task P2P learning
\citep{Sajina2024}, P2P LLM inference \citep{Borzunov2023}, PEFT surveys \citep{Han2024},
and multi-tenant serving \citep{Sheng2024}.

In parallel, **six thematically focused pre-validated corpora** (Groups G1–G6) were
assembled by manual curation of leading publication venues, covering:

| Group | Theme | *n* pre-validated | *n* in final list | Thesis section(s) | SLR coverage |
|-------|-------|------------------:|------------------:|-------------------|---|
| G0 | Foundational seeds (PEFT · P2P · serving) | 9 | 20 | §3.2–3.3 · §5.1–5.2 · §6.2–6.3 | 🟢 Strong |
| G1 | PEFT methods beyond adapters and LoRA | 62 | 12 | §3.4 | 🔴 Critical gap |
| G2 | Adapter composition for multi-task NLP | 46 | 15 | §4.1–4.3 | 🔴 Critical gap |
| G3 | Decentralised and P2P machine learning systems | 112 | 11 | §6.1–6.4 | 🔴 Critical gap |
| G4 | Adapter multiplexing for efficient LLM inference | 64 | 12 | §5.1–5.3 | 🟡 Medium |
| G5 | Routing and mixture-of-experts for modular PEFT | 69 | 9 | §7.1–7.3 | 🔴 Critical gap |
| G6 | Federated PEFT for transformer NLP | 91 | 29 | §6.1 · §6.4 | 🟡 Medium |
| Other | Manual additions (Scopus/WoS forward snowball) | — | 15 | cross-cutting | — |
| **Total** | | **444** | **123** | | |

These corpora were treated as pre-screened inclusions and merged with the snowball output
prior to the enrichment stage. Because G1–G6 papers were assembled through targeted
manual curation (source: Undermind AI-assisted search against leading venues), they bypass
both the year filter and the automated domain-relevance filter applied to snowballed
candidates. Their relevance was established during curation, not re-assessed
programmatically.

---

### ¶3 — Citation snowballing procedure

Forward and backward citation snowballing was conducted on the G0 seeds following the
procedure of \citet{Wohlin2014}. Backward snowballing examined the reference lists of
each seed paper; forward snowballing identified subsequent works citing the seeds. One
wave of snowballing was executed; saturation was assessed manually by reviewing the
overlap between newly retrieved candidates and the pre-validated G1–G6 corpora
(high overlap indicated diminishing returns).

Snowballing was performed programmatically via the **Semantic Scholar Academic Graph API**
\citep{SemanticScholar}, supplemented by the **Scopus** (Elsevier) and **ACL Anthology**
engines to capture venue-specific corpora not fully indexed by Semantic Scholar. The
**Web of Science Starter API** was used in a post-hoc enrichment role — appending WoS
accession numbers and citation counts to already-retrieved records — rather than as a
source of new candidates. The search was executed on **[DATE — inserted automatically from
pipeline log]**.

In total, 1,150 raw records were retrieved across both directions; after deduplication
by DOI and Semantic Scholar paper identifier, **41 unique new records** remained for
screening (1,109 duplicates removed).

---

### ¶4 — Inclusion and exclusion criteria

Records were assessed against the following pre-defined criteria, applied consistently
across all screening stages:

| Criterion | Inclusion | Exclusion |
|-----------|-----------|-----------|
| **Publication year** | ≥ 2021 | < 2021 |
| **Language** | English (implicit — source databases index predominantly English-language works; no mechanical language filter was applied) | Non-English works not surfaced by the APIs |
| **Document type** | Peer-reviewed conference paper, journal article, or arXiv preprint with ≥ 1 citation | Blog posts, grey literature, software documentation, workshop papers without proceedings |
| **Minimum topical relevance** | Addresses ≥ 1 of: (a) PEFT / adapters (LoRA, bottleneck adapters, prefix/prompt tuning); (b) distributed / P2P / federated ML systems; (c) multi-task LLM serving or inference | Exclusively covers unrelated domains (CV, audio, RL) with no NLP or systems angle |
| **Tier 1 (highest priority)** | Covers all three themes jointly | — |
| **Abstract availability** | Accessible via API or pre-validated corpus | No accessible metadata and no resolvable DOI |

> **Note on year cutoff:** Pre-2021 foundational works (e.g., Houlsby et al. 2019, Hu et
> al. 2022) are included via the pre-validated G0–G6 corpora, which were assembled by
> manual curation and bypass the year filter. The year 2021 was chosen as the lower bound
> for snowballed records because the confluence of LoRA \citep{Hu2022} and widespread
> large-scale transformer deployment marks the practical onset of the PEFT-at-scale era
> addressed by this thesis.

---

### ¶5 — Screening procedure (PRISMA: Identification → Screening)

Title screening was applied to all **1,008 unique records** entering the pipeline (41
snowballed + the merged pre-validated corpus). Screening was performed in three layers:

- **Layer 1 — hard exclusions:** Records published before 2021 were excluded
  automatically. No minimum citation threshold was applied (disabled by default).
- **Layer 2 — keyword scoring:** Titles were scored against four pre-defined term sets —
  *PEFT/adapters*, *LLM/transformers*, *systems/serving*, and *distributed/P2P/federated*
  — using exact substring matching (term-set version 1.0). Records matching ≥ 2 term sets
  were auto-included (INCLUDE); records matching exactly one non-LLM term set were queued
  for triage (REVIEW); LLM-only matches and zero-match records were excluded.
- **Layer 3 — LLM triage:** The 21 REVIEW-queue records were submitted to a large
  language model (Claude claude-haiku-4-5-20251001, Anthropic) for title- and venue-level
  classification, resolving each to INCLUDE, EXCLUDE, or UNCERTAIN. UNCERTAIN records
  were retained for manual inspection.

**Screening outcomes:**

| Decision | N |
|----------|--:|
| INCLUDE (auto) | 162 |
| REVIEW (manual triage) | 21 |
| EXCLUDE | 825 |
| **Total screened** | **1,008** |

This screening procedure is reproducible and fully audited: keyword term sets, decision
counts, and per-seed breakdowns are recorded in `log_screening_<date>.json` (SHA-256
checksums retained for traceability).

---

### ¶6 — Enrichment and tier classification (PRISMA: Eligibility)

All records passing title screening were enriched with full abstracts and keyword metadata
via the Semantic Scholar batch API and OpenAlex. A relevance filter subsequently removed
records classified as off-topic (domain mismatch or malformed title), and low-citation
arXiv preprints lacking a Tier 1 topic signal were deprioritised (moved to a separate file
for potential rescue). The remaining **517 records** were classified into three tiers based
on combined title, abstract, and keyword signal:

| Tier | Criteria | *n* | % |
|------|----------|----:|--:|
| **Tier 1** | PEFT + distributed/P2P + LLM serving (all three) | 108 | 20.9% |
| **Tier 2** | Two of the three themes | 163 | 31.5% |
| **Tier 3** | Foundational or tangential (one theme) | 246 | 47.6% |
| **Total** | | **517** | |

**Venue quality of the 517-paper corpus:**

| Venue quality | *n* | % |
|---------------|----:|--:|
| Top-tier venue (CORE A\* / Scopus Q1) | 66 | 12.8% |
| Peer-reviewed (other conference or journal) | 209 | 40.4% |
| Preprint (arXiv, no published venue) | 219 | 42.4% |
| Unknown / missing venue | 23 | 4.4% |

Tiers serve as a reading-priority guide: all three tiers are retained in the corpus, with
Tier 1 papers receiving full reads, Tier 2 selective reads, and Tier 3 abstract-level
assessment \citep[following the three-pass method of][]{Keshav2007}.

---

### ¶7 — Abstract-level review (PRISMA: Eligibility → Inclusion)

Following the three-pass reading model of \citet{Keshav2007} — in which the first pass
(title, abstract, section headings, five Cs) is used to decide whether a paper warrants
further reading — an abstract-level review was conducted across all 517 records. To
improve decision consistency and reduce reviewer fatigue across a corpus of this size,
each abstract was accompanied by an AI-generated suggestion produced by Claude Sonnet
(Anthropic), providing a one-sentence paper summary, a one-sentence relevance note, and a
KEEP / SKIP / DEFER recommendation grounded in the three core themes of the review. The
AI suggestion was strictly advisory; all final decisions were made by the human reviewer.

Papers were classified as:

| Decision | Meaning |
|----------|---------|
| **KEEP** | Included in the Zotero reference corpus for full-text reading |
| **SKIP** | Excluded at abstract level (out of scope confirmed) |
| **DEFER** | Retained for closer inspection before final inclusion/exclusion |

KEEP and DEFER papers were exported to **Zotero** via RIS format for full-text reading.
The AI suggestion and human decision are both recorded in the audit file
(`08_abstract_reviewed_<date>.csv`) to support inter-rater reproducibility checks.

> **Full-text review** (reading, quality assessment, and synthesis) constitutes the
> ongoing phase of the review following corpus construction.

---

### ¶8 — PRISMA reporting and reproducibility

The complete PRISMA 2020 flow (Figure X) traces records through all stages:

```
Retrieved (raw)           n = 1,150
After deduplication       n =    41  (snowballed new; + 444 pre-validated)
After title screening     n =   162  (auto-INCLUDE + manual triage promotions)
After enrichment/filter   n =   517
After abstract review     n = [KEEP]  (to be filled after ¶7 is complete)
```

The pipeline, audit logs (SHA-256 checksums per file), term-set versions, and AI model
identifiers are archived alongside the thesis supplementary materials. All intermediate
CSVs and JSON logs are version-controlled in the project repository, enabling full
re-execution from any stage.

---

### ¶9 — Corpus design and contribution alignment

The six thematic groups (G1–G6) were not assembled arbitrarily; each group was designed to provide the evidentiary base for one or more specific thesis contributions, as mapped below. This alignment ensures that the SLR scope is co-extensive with the claimed contribution space and that every novel claim can be grounded in a documented gap in the reviewed literature.

| Contribution | Type | Description | Evidence group(s) | Thesis section |
|---|---|---|---|---|
| **★A1** | Algorithmic | Adapter discovery protocol — DHT + capability embeddings | G3 · G4 | §8.3 → §1.5 |
| **★R1** | Representation | Adapter capability embeddings for task-agnostic similarity | G2 · G5 | §7.3 → §8.1 |
| **★R2** | Representation | Adapter behavioural fingerprints from probe-set outputs | G2 · G4 | §4.3 → §8.1 |
| **★S1** | Systems | P2P adapter marketplace framework architecture | G3 · G4 | §5 · §8 |
| **★S2** | Systems | Adapter gossip / exchange protocol | G3 · G6 | §6 · §8 |
| **★T2** | Theoretical | Reuse bounds under heterogeneous data distributions (non-IID) | G3 · G6 | §6.1 → §8.3 |
| **★M2** | Architecture | Decentralised AdapterFusion without central coordinator | G2 · G5 | §4.2 · §7.2 → §8.2 |
| **★C2** | Conceptual | Adapters as atomic units of knowledge exchange in P2P systems | G0–G6 all | §8.1 |

The **coverage dashboard** below (derived from the 123-paper final reading list) identifies which thesis sections are well-served by the corpus and which retain gaps requiring targeted reading of priority papers:

| Pillar | G-groups | Final list (*n*) | Status | Priority items still needed |
|--------|----------|----------------:|--------|---|
| PEFT & adapter architecture | G0 · G1 · G2 | 47 | 🔴 Critical: §3.4 empty | QLoRA, Prefix Tuning, HyperFormer, AdaLoRA |
| Adapter composition | G2 | 15 | 🔴 Critical: §4.3 empty | Ponti 2023, LoraHub, AdapterSoup, Ostapenko 2024 |
| Inference systems | G4 | 12 | 🟡 Medium: §5.3 partial | Punica, dLoRA, CaraServe |
| P2P / federated learning | G3 · G6 | 40 | 🔴 Critical: §6.1 empty | FedAvg (McMahan 2017), FedProx (Li 2020), FLamby |
| MoE & adapter routing | G5 | 9 | 🔴 Critical: §7.1–7.2 empty | Switch Transformers, SiRA, MoDE, Expert Choice |
| Synthesis | cross-cutting | — | 🟡 §8 partially drafted | — |

The four critical gaps (§3.4, §4.3, §6.1, §7.1–7.2) correspond directly to the 🔴 Empty sections in the thesis outline. Closing these gaps is the primary objective of the full-text reading phase; all priority papers are present in the 123-paper final reading list or in the Appendix B snowball log as Priority 1 items.

---

### ¶10 — Thesis outline alignment

The SLR is organised concept-centrically following the framework of \citet{Webster2002}, with each literature chapter (§3–§8 of the thesis) corresponding to one or two thematic G-groups. Figure X (Literature Map, `fig_literature_map.png`) visualises the mapping from G-groups to thesis sections and to the novel contribution space. The four stages of the PRISMA flow (Figure Y, `fig_slr1_prisma_flow.png`) trace how the 1,150 raw records were refined to the 123-paper reading pool that provides this evidentiary base.

The thesis sections follow a deliberate ordering: §3 (PEFT) and §4 (adapter composition) establish the atomic units of knowledge; §5 (inference systems) and §6 (P2P/federated learning) establish the network substrate; §7 (MoE routing) provides the algorithmic selection mechanism; §8 (synthesis) integrates all prior sections into the unified gap statement that motivates the novel contributions (★A1, ★S1, ★R1, ★R2, ★T2, ★M2).

---

## Key Citations (Harvard / LaTeX \citep)

| Reference | Use in paragraph |
|-----------|-----------------|
| \citep{Moher2009} — Moher et al., PRISMA statement | ¶1 review framework |
| \citep{Page2021} — Page et al., PRISMA 2020 | ¶1 reporting guidelines |
| \citep{Wohlin2014} — Wohlin, Guidelines for snowballing | ¶3 procedure |
| \citep{Jalali2012} — Jalali & Wohlin, DB search vs snowballing | ¶3 three-step approach |
| \citep{Keshav2007} — Keshav, How to read a paper | ¶6 tier rationale, ¶7 abstract review |
| \citep{SemanticScholar} — Semantic Scholar API | ¶3 tool |
| \citep{Houlsby2019} — Houlsby et al., Adapter PEFT | ¶2 G0 seed |
| \citep{Hu2022} — Hu et al., LoRA | ¶2 G0 seed, ¶4 year cutoff note |
| \citep{Pfeiffer2020hub} — Pfeiffer et al., AdapterHub | ¶2 G0 seed |
| \citep{Pfeiffer2021fusion} — Pfeiffer et al., AdapterFusion | ¶2 G0 seed |
| \citep{Sajina2024} — Šajina et al., Multi-task P2P | ¶2 G0 seed |
| \citep{Borzunov2023} — Borzunov et al., Petals | ¶2 G0 seed |
| \citep{Han2024} — Han et al., PEFT survey | ¶2 G0 seed |
| \citep{Sheng2024} — Sheng et al., S-LoRA | ¶2 G0 seed |
| \citep{Webster2002} — Webster & Watson, Analysing past to prepare for the future | ¶10 concept-centric organisation |

---

## Remaining gaps / items to address before submission

1. **Fill in the search date** in ¶3 — now auto-populated in `PRISMA_summary_<date>.md`
   header field `Search executed:`.

2. **Abstract review count is final:** KEEP=214, SKIP=338, DEFER=0 (resolved 2026-05-02).
   Fill in ¶8 KEEP count with 214.

3. **Inter-rater check** — for a rigorous SLR, consider having a second reviewer spot-
   check a sample (e.g., 10%) of SKIP decisions from the abstract review. The AI
   suggestion column in `S7b_abstract_reviewed_final.csv` can serve as a first-pass surrogate.

4. **Quality assessment table** — the PDF guidelines (Box 3.2 / Box 3.4) suggest assessing
   credibility of sources. The `venue_quality` column now provides a machine-readable
   proxy. Consider adding a short paragraph noting that top-tier peer-reviewed works are
   prioritised in synthesis, with preprints used where no published version exists.
   Current corpus: Scopus=101 (82%), arXiv=18 (15%), other=4 (3%).

5. **Close coverage gaps before submission** — four thesis sections are currently 🔴 Empty
   and all have priority papers already in `S8_final_reading_list.csv`:
   - **§3.4** (Advanced PEFT variants): read QLoRA, Prefix Tuning, HyperFormer, AdaLoRA
   - **§4.3** (Modular composition): read Ponti 2023, LoraHub, AdapterSoup, Ostapenko 2024
   - **§6.1** (Federated foundations): read FedAvg (McMahan 2017), FedProx (Li 2020)
   - **§7.1–7.2** (MoE + adapter routing): read Switch Transformers, SiRA, MoDE

6. **Add \citet{Webster2002}** to the Key Citations table — referenced in ¶10 for the
   concept-centric organisation rationale.

7. **Update figures** after reading phase by re-running:
   ```bash
   cd snowballing
   python -m app.prisma
   python -m app.visualise
   ```
   This regenerates `PRISMA_summary.md` and all SLR figures including fig9 (G-group
   breakdown by tier).

---

## Code–outline alignment log (resolved)

| Issue | Resolution |
|---|---|
| `screen.py` `year_cutoff` default was 2017 | Fixed to 2021 in function signature |
| `prisma.py` Stage 3 said "one reviewer" | Updated to reflect LLM triage; auto-populates counts from `log_screening_*.json` |
| WoS described as snowballing source | Corrected in ¶3: WoS is enrichment/verification only |
| Pre-validated papers said to go through domain filter | Corrected in ¶2: they bypass both year and domain filters |
| English language criterion had no code equivalent | Clarified in ¶4 I/E table as implicit (database-level coverage) |
| Iterative saturation criterion | Corrected in ¶3: one-wave snowball, saturation assessed manually |
| Enrichment source traceability | Added `enrichment_sources` column (acl / semantic_scholar / openalex) in `enrich_and_filter._merge()` |
