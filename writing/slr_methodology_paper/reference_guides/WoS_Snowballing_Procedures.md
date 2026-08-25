# WoS Snowballing Procedures
## PhD Thesis: Decentralized Adapter-based LLM Systems
### University of Rijeka — Faculty of Informatics and Digital Technologies


# Step-by-Step WoS Snowballing Procedures

## B.1 Overall Flow (Wohlin 2014 methodology)

```
START
  │
  ▼
[Seed Set: 69 papers in SEED_PAPERS.py]
  │
  ├─► ITERATION 1 ────────────────────────────────────────────────────────────
  │     │
  │     ├─► BACKWARD: Read reference lists of all seeds → screen → include new
  │     └─► FORWARD:  Find all papers citing seeds → screen → include new
  │
  ├─► ITERATION 2
  │     │
  │     ├─► BACKWARD: Read reference lists of NEW papers from iter 1
  │     └─► FORWARD:  Find citing papers for NEW papers from iter 1
  │
  └─► STOP when: no new inclusions in iteration N (saturation)
```

---

## B.2 BACKWARD SNOWBALLING — Step by Step

**What you are doing**: For each seed paper, collect its full reference list.
Screen each reference for relevance. Add relevant ones to your pool.

### Step 1 — Find the seed paper in WoS

Go to [webofscience.com](https://webofscience.com) → **Advanced Search** tab.

Enter the DOI in the `DO=` field:
```
DO=10.18653/v1/2021.eacl-main.39
```
Click **Search**. Open the full record by clicking the paper title.

> If no result: the paper may not be indexed in WoS (common for MLSys/OSDI papers).
> Skip to Step 1b.

### Step 1b — If DO= gives no result (arXiv-only / MLSys / OSDI papers)

Search by title words instead:
```
TI=("AdapterFusion" AND "non-destructive task composition")
```
Or by author + year:
```
AU=Pfeiffer AND PY=2021 AND TI=adapter
```

> If still not found: the paper is not in WoS. Use Semantic Scholar for its backward
> chain: go to semanticscholar.org, paste the title, open the paper, click "References".

### Step 2 — Access the paper's reference list (backward)

On the full WoS record:
1. Scroll to the bottom of the page.
2. Find the **"References"** section (also called "Cited References").
3. Click **"View all [N] references"** — a new page opens listing all citations.
4. This list IS the backward snowball: every entry is a candidate paper.

### Step 3 — Screen the reference list

For each reference in the list:
- **INCLUDE** if: peer-reviewed + intersects ≥ 2 of {PEFT, P2P, multi-task, serving, MoE, federated}
- **EXCLUDE** if: blog, thesis (unless directly relevant like Šajina 2021), application paper outside your scope
- **MAYBE** if unsure → keep, read abstract in next phase

### Step 4 — Add relevant references to Marked List

1. Check the box next to each relevant reference.
2. Click **"Add to Marked List"** (folder icon at top right).
3. WoS deduplicates entries automatically across multiple seeds.
4. Repeat Steps 1–4 for every seed paper in your current iteration.

### Step 5 — Export backward snowball results

1. Go to **Marked List** (top right folder icon).
2. Select all → **Export** → choose **BibTeX** or **Plain Text (tab-delimited)**.
3. Save with filename: `backward_iter1_YYYYMMDD.bib`

---

## B.3 FORWARD SNOWBALLING — Step by Step

**What you are doing**: Find all papers published AFTER your seed that cite it.
This is the most important direction for finding recent 2023–2026 SOTA.

### ★ METHOD 1 — "Times Cited" click (fastest, most reliable)

#### Step 1 — Open the seed's full record

```
DO=10.18653/v1/2021.eacl-main.39
```
Open the record. On the right-hand panel, find the blue **"Times Cited"** number
(e.g., "Times Cited: 1,050").

#### Step 2 — Click Times Cited

Clicking the number opens a **new results page** of every WoS-indexed paper
that has cited this work. This is your raw forward snowball pool.

#### Step 3 — Apply filters (left panel)

Narrow the results before screening:
- **Document Type** → check: Article, Proceedings Paper, Review
  → uncheck: Editorial, Correction, Retraction, Book Review
- **Publication Years** → set to: [year of seed + 1] to 2026
  Example for AdapterFusion (2021): filter PY=2022-2026
- **Research Areas** → check: Computer Science, Engineering, Telecommunications
  → uncheck: Biology, Medicine, Economics (unless combined with NLP)
- **Languages** → English only

#### Step 4 — Screen titles and abstracts

Review each remaining record:
- Read title: does it mention adapter, LoRA, PEFT, P2P, serving, MoE, federated?
- If yes: open full record, read abstract, decide INCLUDE / EXCLUDE / MAYBE
- Mark decisions with WoS labels (use the "Mark" function) or export and annotate in Zotero

#### Step 5 — Add selected papers to Marked List

Check relevant boxes → "Add to Marked List"

#### Step 6 — Export

Marked List → Export → BibTeX  
Save as: `forward_iter1_YYYYMMDD.bib`

---

### ★ METHOD 2 — Cited Reference Search (CRS) — for papers not in WoS index

Use this when the seed paper has no WoS record (MLSys, OSDI, arXiv-only).
CRS works by searching the CITATION RECORDS of all indexed papers, not the papers themselves.
Even if a paper is not indexed in WoS, papers that CITE IT may be indexed.

#### Step 1 — Go to Cited Reference Search

Top navigation bar → click **"Cited References"** tab
(next to "Advanced Search" in the main WoS menu)

#### Step 2 — Fill in the search fields

Use the DOI field — most precise method:
```
Cited DOI:  10.5555/3454287.3455530      ← Houlsby 2019 ICML
```

If no DOI match, use Author + Work:
```
Cited Author:  HOULSBY N*
Cited Work:    INT C MACHINE LEARN*      ← abbreviated proceedings title, use * wildcard
Cited Year:    2019                      ← optional; omit to catch variant citations
```

> Always use `*` wildcard after the author initial and after abbreviated titles.
> WoS stores many citation variants (e.g., "HOULSBY N" and "HOULSBY NM") —
> the wildcard catches all of them.

#### Step 3 — Get the citation variants table

Click **Search**. A table appears listing all variants of this cited reference
in the WoS citation index (different citing papers may have formatted the
citation slightly differently).

The table columns are:
- **Cited Author** | **Cited Work** | **Year** | **Volume** | **Page** | **Citing Articles**

The **Citing Articles** column shows how many WoS papers cite each variant.

#### Step 4 — Select ALL variants

This is critical: check the **"Select All"** checkbox at the top.
You want every variant, because the same paper may have been cited as:
```
HOULSBY N    INT C MACHINE LEARN   2019   97    4132     → View Record ✓
HOULSBY N    PROC ICML             2019                  → no View Record
HOULSBY NM   ARXIV                 2019                  → no View Record
```
All three point to the same paper. Select all three.

#### Step 5 — Click "See Results" / "Finish Search"

After selecting all variants, click **"See Results"** (some WoS versions label it
**"Finish Search"**). This converts the cited reference results into a standard
**document results page** showing all papers that cited your seed.

This results page is now your forward snowball pool — proceed with Steps 3–6 from Method 1.

---

### ★ METHOD 3 — Advanced Search with CI= field tag (batch forward, all seeds at once)

Use this to run forward snowballing for multiple seeds in a single query.
Requires knowing each paper's WoS Accession Number (`UT=`).

#### Step A — Get UT= accession numbers

For each seed with a WoS record, open its full record and note the UT number.
It appears in the URL and at the bottom of the record:
```
WOS:000634123400039
```
You can also retrieve it via Advanced Search:
```
DO=10.18653/v1/2021.eacl-main.39
```
→ open record → bottom → "Accession Number: WOS:XXXXXXXXXXXXXXXXXX"

#### Step B — Batch forward query

In **Advanced Search**, use the `CI=` field tag (Cites):
```
CI=WOS:000634123400039 OR
CI=WOS:000619234100007 OR
CI=WOS:000612983700040
```
This returns all papers that cite any of the listed accession numbers.

#### Step C — Add topic filter to reduce noise (optional)

```
(CI=WOS:000634123400039 OR CI=WOS:000619234100007) AND
TS=("adapter" OR "LoRA" OR "PEFT" OR "peer-to-peer" OR "mixture of experts" OR "serving")
```

#### Step D — Filter, screen, export as in Method 1 Steps 3–6.

---

## B.4 Priority Seeds for Forward Snowballing

Run forward snowballing on these 12 seeds FIRST (highest yield expected):

| Priority | Key | Reason | Method |
|----------|-----|--------|--------|
| ★★★ | Pfeiffer 2021 Fusion (EACL) | 1,050+ citations; all adapter composition papers cite this | Method 1 |
| ★★★ | Houlsby 2019 (ICML) | 5,700+ citations; all PEFT papers trace back here | Method 2 (CRS) |
| ★★★ | Pfeiffer 2020 Hub (EMNLP) | 700+ citations; all AdapterHub ecosystem papers | Method 1 |
| ★★★ | Sajina 2024 (FGCS) | Every paper citing this is directly in your prior work chain | Method 1 |
| ★★ | Fedus 2022 Switch (JMLR) | 3,800+ citations; all MoE routing papers | Method 1 |
| ★★ | Sheng 2024 SLoRA (MLSys) | 270+ citations; all adapter serving papers | Method 2 (CRS) |
| ★★ | Borzunov 2022 Petals | 200+ citations; all P2P LLM inference papers | Method 2 (CRS) |
| ★★ | Ostapenko 2024 (ICML) | Modular LoRA library; growing forward chain 2024–2026 | Method 1 |
| ★★ | Ning 2024 MoDE (NAACL) | Multi-task MoE adapter; recent, forward chain growing | Method 1 |
| ★★ | Cai 2024 MoE Survey (TKDE) | IEEE journal; forward cites = all MoE adapter papers | Method 1 |
| ★★ | Gupta 2023 P2P FL (INFOCOM) | Forward cites = all gossip-based P2P ML papers | Method 1 |
| ★★ | Koo 2024 (ACL) | Federated LoRA; forward chain = federated adapter papers | Method 1 |

---

## B.5 Handling Coverage Gaps

Some high-priority seeds are NOT indexed in WoS. Use fallbacks:

| Seed | WoS status | Fallback procedure |
|------|-----------|-------------------|
| S-LoRA (MLSys 2024) | ⚠️ Partial | CRS: `SHENG Y*` + `CONF MACH LEARN SYS*` → OR use Semantic Scholar |
| dLoRA (OSDI 2024) | ⚠️ Not indexed | Semantic Scholar: paste title → "Cited By" tab |
| Punica (MLSys 2024) | ⚠️ Partial | CRS: `CHEN L*` + cited DOI `10.5555/...` |
| DeltaZip (EuroSys 2023) | ✅ ACM DL | Method 1 or Method 2 with `DO=10.1145/3552326.3587438` |
| Han 2024 TMLR | ✅ WoS (ESCI) | Method 1 direct |

---

## B.6 Screening Worksheet (print or copy per iteration)

```
Iteration: ___    Direction: FORWARD / BACKWARD    Date: ___________
Seed paper: ________________________________________

Raw hits from WoS: ______
After Document Type filter: ______
After Year filter: ______
After Research Area filter: ______

Papers screened by title: ______
  → INCLUDE (2+ pillars): ______
  → EXCLUDE: ______
  → MAYBE (read abstract): ______

After abstract screening:
  → Final INCLUDE: ______
  → Final EXCLUDE: ______

New papers not already in SEED_PAPERS.py: ______
Added to Marked List: YES / NO
Export filename: ______________________________
```

---

## B.7 Iteration Log (thesis appendix table)

| Iter | Direction | Seeds used | WoS raw | After filters | After title screen | After abstract | New inclusions | Cumulative total |
|------|-----------|-----------|---------|---------------|--------------------|----------------|----------------|-----------------|
| 0 | — | 69 (SEED_PAPERS.py) | — | — | — | — | 69 | 69 |
| 1 | Backward | G0 (9 papers) | | | | | | |
| 1 | Forward | ★★★ seeds (4) | | | | | | |
| 2 | Backward | New from iter 1 | | | | | | |
| 2 | Forward | New from iter 1 | | | | | | |
| 3 | Both | New from iter 2 | | | | | | |

**Stop condition**: New inclusions = 0 OR 3 full iterations completed.

---

*Version 1.0 — April 2026*
*Methodology: Wohlin (2014) — DOI: 10.1145/2601248.2601268*
*WoS CRS documentation: Clarivate Analytics (2024)*
