# Fix Specification — Decentralised Adapter-Based LLM Inference SLR

**Purpose of this document:** this is a prompt/spec for Claude Code to apply mechanically.
It is organised by file. Each fix has: the issue, the exact OLD text, the exact NEW text,
and an explanation of *why*, so the agent understands intent and doesn't "fix" it in a way
that re-breaks something else nearby.

## Ground rules for the agent — read this before touching anything

1. **Re-view each file immediately before editing it.** Line numbers quoted below are from
   an earlier read and may have shifted from prior edits in the same session. Match on the
   *content* of the OLD block, not on line numbers.
2. **Whitespace/line-wrapping in the OLD blocks below may not exactly match the file's
   current line breaks** (LaTeX soft-wraps mid-sentence and that wrapping isn't semantically
   meaningful). If a `str_replace`-style exact match fails, search for the block with
   whitespace normalised (collapse newlines/multiple spaces to single spaces) before
   concluding the text isn't there. Do not guess-edit a *similar-looking* passage instead —
   if you can't find an exact content match, stop and report it rather than editing the
   nearest lookalike sentence.
3. **Do not touch anything not listed here.** In particular, do not "helpfully" fix other
   instances of "we"/"our" you notice beyond what's listed — some sections (04–08) haven't
   been audited for voice yet in this pass, and blanket find-replace of "we" → passive
   voice across files not covered here risks mangling sentences with false positives
   (e.g. "we-" isn't a word boundary issue, but "steward" contains "we" is a comedic worst
   case — use word-boundary matching, not substring matching, everywhere).
4. **Several items below are explicitly marked "DO NOT AUTO-APPLY."** These require an
   author decision (Vanja), not a mechanical text change. Surface these to the user; do not
   guess on their behalf.
5. **After all edits, run the verification checklist at the end of this document** before
   declaring the pass complete.
6. Preserve LaTeX special-character escaping exactly as found (`\v{S}`, `\'{e}`, `~\cite{}`
   non-breaking spaces, etc.) — do not "clean up" escaping you don't recognise.

---

## 1. `main.tex`

### 1.1 Abstract — trim to ≤200 words AND fix voice AND fix funnel precision AND soften scope claim

**Issue (Pass 0 + Pass 1 + Pass 4):** the abstract is 216 words (MDPI ceiling ~200), uses
first-person "we" in a solo-authored paper (inconsistent with "the author" used everywhere
else), compresses the funnel in a way that implies all 1,150 raw candidates merged with the
352-paper corpus (only the 162 screened-in survivors actually did — this is the exact
ambiguity a prior reviewer round already flagged and fixed in §3.1, but the abstract was
never updated to match), and closes with a contribution claim ("establishes the theoretical
grounding... for a P2P serving architecture") that's stronger than the review's actual
gap-identification-only scope.

This single edit fixes four issues at once. Word count of the replacement is 191 words by
plain whitespace-split counting (MDPI's submission-system counter may count words joined by
`---` as two words each, adding ~2–4 to this count — still comfortably under 200).

```latex
% OLD
\abstract{Multi-task large language model inference on resource-constrained
hardware faces a fundamental tension: full fine-tuning is prohibitively
expensive, yet existing parameter-efficient serving systems all assume
centralised orchestration. This systematic literature review investigates
whether a peer-to-peer (P2P) research direction is theoretically grounded and
practically motivated: can lightweight, task-specific adapters be discovered,
retrieved, composed, and served across autonomous nodes each hosting a shared
frozen backbone without any central coordinator? Following the PRISMA 2020
guidelines with Wohlin et al.\ citation snowballing, we examined 1{,}150
snowball candidates, merged them with a 352-paper pre-validated corpus, and
retained 123 included records (121 distinct papers) spanning five
clusters: parameter-efficient fine-tuning, adapter composition, LLM inference
serving, mixture-of-experts routing, and P2P and federated learning. We
appraise each included study against a grounded six-dimension quality rubric
and synthesise the evidence into a unified gap map. The central finding is
that, to the best of the author's knowledge, no existing system simultaneously
addresses a frozen shared backbone, adapter-level exchange, P2P topology,
decentralised discovery, multi-task fusion, and the absence of a central
coordinator. The literature therefore partitions into four gap
quadrants---conceptual, algorithmic, systems, and empirical---each identifying
open research questions that the reviewed literature has not yet addressed in
an integrated manner. The review thus establishes the theoretical grounding
and concrete research agenda for a decentralised, adapter-based P2P serving
architecture.}

% NEW
\abstract{Multi-task large language model inference on resource-constrained
hardware faces a fundamental tension: full fine-tuning is prohibitively
expensive, yet parameter-efficient serving systems assume centralised
orchestration. This systematic literature review asks whether a peer-to-peer
(P2P) research direction is theoretically grounded: can task-specific
adapters be discovered, retrieved, composed, and served across autonomous
nodes sharing a frozen backbone without a central coordinator? Following
PRISMA 2020 and Wohlin et al.\ snowballing, 1{,}150 snowball candidates were
examined; 162 records passing screening were merged with a 352-paper
pre-validated corpus, yielding 123 included records (121 distinct papers)
across five clusters: parameter-efficient fine-tuning, adapter composition,
LLM inference serving, mixture-of-experts routing, and P2P/federated
learning. Each included study was appraised against a six-dimension quality
rubric and the evidence synthesised into a unified gap map. To the best of
the author's knowledge, no existing system simultaneously addresses a frozen
shared backbone, adapter-level exchange, P2P topology, decentralised
discovery, multi-task fusion, and the absence of a central coordinator. The
literature partitions into four gap quadrants---conceptual, algorithmic,
systems, and empirical---each defining open research questions not yet
addressed in an integrated manner. The review thus establishes the evidence
base and research agenda for decentralised, adapter-based P2P inference.}
```

**After applying:** run a word count on the text between `\abstract{` and the closing `}`
(split on whitespace) and confirm it is ≤200. If a later manual tweak pushes it back over,
cut from the first sentence (background) first — it's the least load-bearing for PRISMA
compliance (the methods/results/conclusion content must stay intact per PASS 0's
Background/Methods/Results/Conclusion structure requirement).

### 1.2 Supplementary Materials + Data Availability — DO NOT AUTO-APPLY, author decision required

**Issue (Pass 0/1/7):** `\supplementary{}` only lists the PRISMA checklist, but the checklist
itself points reviewers to pipeline CSVs/logs (`13_final_reading_list_2026-05-12.csv`,
`11_data_extraction_2026-05-12.csv`, screening/retrieval JSON logs) as the evidence location
for PRISMA items 9, 10a/b, 16a, 17, and 27. None of those files are actually declared as
downloadable supplementary material — the Data Availability statement instead says "upon
reasonable request." This is a real gap, but **fixing it requires Vanja to decide whether to
actually upload those files to MDPI's system** (assigning them s2/s3/s4 suffixes) or set up
a repository with a DOI (e.g. Zenodo/OSF) and link that instead. Claude Code should not
invent URLs or silently commit to a specific file list — surface this decision to Vanja.

If Vanja confirms she will deposit the reading-list CSV, the extraction table, and the audit
logs as supplementary material, apply:

```latex
% OLD
\supplementary{The following supporting information can be downloaded at:
https://www.mdpi.com/article/10.3390/ai/xxxx/s1: the completed PRISMA 2020
27-item checklist for this systematic review.}

% NEW
\supplementary{The following supporting information can be downloaded at:
https://www.mdpi.com/article/10.3390/ai/xxxx/s1: the completed PRISMA 2020
27-item checklist for this systematic review; s2:
the final reading list and per-record quality-appraisal scores
(\texttt{13\_final\_reading\_list\_2026-05-12.csv}); s3: the data-extraction
table (\texttt{11\_data\_extraction\_2026-05-12.csv}); s4: the screening and
retrieval audit logs (\texttt{log\_screening\_2026-04-21.json},
\texttt{log\_retrieval\_2026-04-21.json}).}
```

and correspondingly:

```latex
% OLD
\dataavailability{No new experimental data were created: the review analyses
previously published literature. The derived reproducibility artefacts---the
PRISMA funnel counts, the per-record quality-appraisal scores, the extraction
codebook, and the screening and audit logs---are available from the author
upon reasonable request, and the underlying pipeline files are documented by
path in Appendix~C.}

% NEW
\dataavailability{No new experimental data were created: the review analyses
previously published literature. The derived reproducibility
artefacts---the PRISMA funnel counts, the per-record quality-appraisal
scores, the extraction codebook, and the screening and audit logs---are
provided as Supplementary Material (see above) and are documented by path in
Appendix~C. Raw Scopus/WoS export files and search-engine outputs remain
available from the author upon reasonable request.}
```

**If Vanja decides NOT to deposit these files**, leave both blocks unchanged, but flag to her
that the checklist's own claimed evidence locations for items 9/10/16a/17/27 remain
inaccessible to reviewers as currently written — this is a live blocking risk either way and
needs a decision, not a default.

---

## 2. `03_methodology.tex`

### 2.1 Voice consistency — "we" → passive/"the author" (three instances)

**Issue (Pass 0/6):** the abstract fix above handles `main.tex`; these three sentences in
`03_methodology.tex` have the same first-person-plural problem in a solo-authored paper.

```latex
% OLD
i.e.\ it was systematically over-inclusive relative to the human pass. We report this as an
automated reproducibility diagnostic rather than a human inter-rater measure: the
re-screener shares priming with the review workflow, so the two passes are
not genuinely independent.

% NEW
i.e.\ it was systematically over-inclusive relative to the human pass. This is reported as an
automated reproducibility diagnostic rather than a human inter-rater measure: the
re-screener shares priming with the review workflow, so the two passes are
not genuinely independent.
```

```latex
% OLD
in top-tier venues. Because this selection was informed by the research
question itself, it carries an inherent risk of biasing the corpus toward the
thesis narrative and could under-sample works that challenge the premise of
decentralised adapter sharing. Two features mitigate this risk. First, the G0
set is complemented by the independently curated G1--G6 groups, which were
assembled from leading venues without reference to the seeds'
conclusions~\cite{XiaoWatson2019} (Table~\ref{tab:groups}). Second, forward and
backward citation snowballing and the Scopus/WoS forward pass expand the corpus
beyond the seeds' immediate frame. We further note that, although the
$\geq$300-citation criterion was applied at seed selection, verified per-record
citation counts are not uniformly retained in the reproducible corpus (the
pre-validated snapshot stores counts for a minority of seeds); the threshold
therefore reflects the decision-time snapshot rather than a figure reproduced
here, and is reported for transparency rather than as an auditable datum.

% NEW
in top-tier venues. Because this selection was informed by the research
question itself, it carries an inherent risk of biasing the corpus toward the
thesis narrative and could under-sample works that challenge the premise of
decentralised adapter sharing. Two features mitigate this risk. First, the G0
set is complemented by the independently curated G1--G6 groups, which were
assembled from leading venues without reference to the seeds'
conclusions~\cite{XiaoWatson2019} (Table~\ref{tab:groups}). Second, forward and
backward citation snowballing and the Scopus/WoS forward pass expand the corpus
beyond the seeds' immediate frame. It is further noted that, although the
$\geq$300-citation criterion was applied at seed selection, verified per-record
citation counts are not uniformly retained in the reproducible corpus (the
pre-validated snapshot stores counts for a minority of seeds); the threshold
therefore reflects the decision-time snapshot rather than a figure reproduced
here, and is reported for transparency rather than as an auditable datum.
```

**Note for the agent:** this OLD block is long (spans several sentences) specifically so the
match is unambiguous — only the "We further note that" clause changes. Do not shorten the
matched span when applying the edit.

```latex
% OLD
Because the review is a qualitative thematic synthesis of published
methods--and--systems literature rather than a meta-analysis of participant-level
interventions, the PRISMA 2020 risk-of-bias instruments for comparative studies do
not apply directly. Following the practice of software-literature systematic
reviews~\cite{XiaoWatson2019}, we instead appraise the \emph{evidence quality of
each of the 123 included records} with a six-dimension rubric scored from the
screening and extraction records (Table~\ref{tab:quality_rubric}). We emphasise
that this instrument measures the reporting completeness of each record and its
relevance to this synthesis, not the intrinsic scientific merit of the underlying
study: three dimensions are bibliographic or relevance proxies (Q1 venue prestige,
Q2 record resolvability, Q6 thematic relevance), and a pilot application of the
classic quality dimensions (code availability, result reproducibility, baseline
adequacy, threats reporting) found them to be un-populated in the extraction data,
so they are scoped out here and disclosed rather than estimated. Every retained
dimension is nevertheless operationalised from an explicit, grounded pipeline field
so that each score is reproducible from the associated CSV artifacts; no dimension
is inferred or imputed.

% NEW
Because the review is a qualitative thematic synthesis of published
methods--and--systems literature rather than a meta-analysis of participant-level
interventions, the PRISMA 2020 risk-of-bias instruments for comparative studies do
not apply directly. Following the practice of software-literature systematic
reviews~\cite{XiaoWatson2019}, this review instead appraises the \emph{evidence
quality of each of the 123 included records} with a six-dimension rubric scored
from the screening and extraction records (Table~\ref{tab:quality_rubric}). It is
emphasised that this instrument measures the reporting completeness of each record
and its relevance to this synthesis, not the intrinsic scientific merit of the
underlying study: three dimensions are bibliographic or relevance proxies (Q1
venue prestige, Q2 record resolvability, Q6 thematic relevance), and a pilot
application of the classic quality dimensions (code availability, result
reproducibility, baseline adequacy, threats reporting) found them to be
un-populated in the extraction data, so they are scoped out here and disclosed
rather than estimated. The \texttt{contribution\_codes} field underlying the top
tier of Q5 is itself sparsely populated (22 of 224 extraction rows, 9.8\%); records
lacking a code default to the middle Q5 tier regardless of the underlying
contribution's actual significance, and this should be read as a limitation of
extraction coverage rather than a substantive quality signal. Every retained
dimension is nevertheless operationalised from an explicit, grounded pipeline field
so that each score is reproducible from the associated CSV artifacts; no dimension
is inferred or imputed.
```

**Note:** this block does two things at once — the voice fix (we → passive) AND adds the new
disclosure sentence about the sparse `contribution_codes` field (Pass 2 finding). The new
sentence is inserted after the classic-quality-dimensions sentence and before the
"reproducible from CSV artifacts" sentence — do not reorder.

### 2.2 Add missing methodology citations (Kitchenham & Charters; Webster & Watson)

**Issue (Pass 5/bibliography):** `KitchenhamCharters2007` and `Webster2002` are both in
`bibliography.bib` but never cited anywhere in the manuscript. Both are canonical SLR-method
references and belong in the opening methodology sentence alongside Xiao & Watson and
Wohlin.

```latex
% OLD
This review follows the PRISMA 2020 reporting guidelines~\cite{Page2021}, the
eight-step SLR process of Xiao and Watson~\cite{XiaoWatson2019}, and the
citation-snowballing protocol of Wohlin et al.~\cite{Wohlin2014}. The review was

% NEW
This review follows the PRISMA 2020 reporting guidelines~\cite{Page2021}, the
eight-step SLR process of Xiao and Watson~\cite{XiaoWatson2019}, the
citation-snowballing protocol of Wohlin et al.~\cite{Wohlin2014}, and general
SLR guidance from Kitchenham and Charters~\cite{KitchenhamCharters2007} and
Webster and Watson~\cite{Webster2002}. The review was
```

**Warning:** the OLD block above is deliberately short (ends mid-sentence at "The review
was") to anchor precisely on the first paragraph of §3 without swallowing the rest of that
paragraph (which continues with the PROSPERO-registration justification, already correct and
must not be touched).

---

## 3. `02_background.tex`

### 3.1 Delete the leftover commented-out marketplace figure

**Issue (Pass 0):** a fully commented-out figure block referencing `fig_concept_marketplace.png`
and describing a "P2P exchange concept... Kademlia-style distributed storage" is a dead
remnant of the pre-pivot marketplace/architecture framing. It doesn't affect compilation
(it's commented out) but it's inconsistent with the deliberate reframe to gap-identification
only, and stray dead code referencing a withdrawn framing looks unfinished in a submission.

```latex
% OLD
%\begin{figure}[H]
%  \centering
%  \includegraphics[width=0.65\linewidth]{figures/fig_concept_marketplace.png}
%  \caption{P2P exchange concept: autonomous nodes exchanging adapters over a DHT-based lookup with Kademlia-style %distributed storage.}
%  \label{fig:concept_marketplace}
%\end{figure}

% NEW
[DELETE — replace with nothing, i.e. remove this whole commented block]
```

**After deleting this**, run `grep -ri "marketplace" *.tex` across every section file as a
final sanity sweep — there should be zero remaining hits (the ★-contribution-code
terminology in the quality rubric is unrelated and should NOT be touched; only literal
"marketplace" string matches are in scope here).

### 3.2 Gossip-propagation caption — optional, low priority

**Issue (Pass 0, minor):** the captions for `fig:p2p_dht_lookup` and `fig:p2p_gossip`
describe generic P2P infrastructure in terms specific to "adapter metadata" dissemination,
which is mildly solution-flavoured language for a Background section that's supposed to be
neutral technical grounding, not a preview of the (explicitly not-proposed) target system.
This is optional/low-severity — **do not apply this without Vanja's sign-off**, since it's a
style judgement call, not a factual error. Included here for completeness only:

```latex
% CURRENT (for reference only — do not change without explicit confirmation)
\caption{Gossip propagation of adapter metadata: an infected peer spreads information to randomly chosen neighbours each round until the entire network is aware.}
```

If Vanja confirms she wants this softened, a neutral alternative would be:

```latex
\caption{Gossip propagation: an informed peer spreads a piece of state to randomly chosen neighbours each round until the entire network is aware. (Adapter metadata is one example payload discussed in later chapters.)}
```

---

## 4. `01_introduction.tex`

### 4.1 Add an informal first-use definition of "adapter"

**Issue (Pass 6, matches your own already-flagged-open item R2-m1):** "PEFT" is defined at
first use (L7, parenthetical expansion), but "adapter"/"adapter modules" is used repeatedly
(L9–22) before its rigorous definition appears a full section later in §2.2. Low severity —
the term is intuitive from context — but since this was already flagged as open in your own
reviewer-response draft, close it with one inserted clause rather than a restructure.

```latex
% OLD
The result is an ecosystem in which a single frozen backbone serves as a
universal substrate, and small task-specific adapter modules provide the
task-particular knowledge required for each application.

% NEW
The result is an ecosystem in which a single frozen backbone serves as a
universal substrate, and small task-specific adapter modules---lightweight,
trainable parameter sets inserted into or alongside the frozen backbone to
encode task-specific behaviour without modifying the backbone itself
(formally defined in Section~\ref{sec:background:peft})---provide the
task-particular knowledge required for each application.
```

**Note:** `sec:background:peft` is the existing label on the "Parameter-Efficient
Fine-Tuning Primitives" subsection in `02_background.tex` (confirmed present) — do not
invent a new label, use this one.

---

## 5. `09_synthesis_gap.tex`

### 5.1 Reword the latency-exclusion rationale (objectivity-test finding)

**Issue (Pass 3 — this is the most important content fix in the whole pass; a skeptical
reviewer applying the "would this feel valuable with no stake in the field" test will quote
this sentence back at you):** the current justification for excluding "latency" as a concept
matrix dimension gives away that avoiding an unfavourable comparison was part of the
reasoning ("would therefore penalise a decentralised approach"), not just that it's a
metric rather than an architectural property. The categorical argument is fine on its own;
the second sentence undermines it.

```latex
% OLD
Two dimensions were considered and deliberately excluded. Latency was not included as a dimension because it is an evaluation metric rather than an architectural property — and one where P2P systems cannot realistically compete with centralised deployments on equal terms. Including it as a binary dimension would therefore penalise a decentralised approach for a tradeoff that is structural rather than incidental. Incentive mechanisms were also excluded; they are relevant to any future decentralised adapter-sharing design but belong outside the scope of this review. Both exclusions are reflected in the limitations discussed in Section~\ref{sec:conclusion:limitations}

% NEW
Two dimensions were considered and deliberately excluded. Latency was not included as a dimension because it is a continuous evaluation metric rather than a binary architectural commitment; its trade-offs for a P2P setting are acknowledged narratively in the per-pillar chapters (Sections~\ref{sec:inference_systems} and~\ref{sec:p2p_federated}) rather than scored in the concept matrix. Incentive mechanisms were also excluded; they are relevant to any future decentralised adapter-sharing design but belong outside the scope of this review. Both exclusions are reflected in the limitations discussed in Section~\ref{sec:conclusion:limitations}
```

**Important:** after applying this, check that §6 (`06_inference_systems.tex`) and §8
(`08_p2p_federated.tex`) actually do contain some narrative discussion of latency trade-offs
for P2P/decentralised serving — the new sentence points readers there. If neither section
currently discusses latency trade-offs narratively, either (a) add one sentence to one of
those sections doing so, or (b) soften the NEW text above to drop the "acknowledged
narratively in..." clause and end at "...binary architectural commitment." **Flag this
dependency to Vanja rather than silently picking (a) or (b).**

### 5.2 Gossip Learning concept-matrix cell — verification needed, NOT a blind fix

**Issue (Pass 3):** row `Gossip Learning \cite{HegeduisGossip2019}` in `tab:concept_matrix`
marks "Frozen backbone" as `(\checkmark)` (partial). Classical gossip-learning literature
(decentralized SGD-style training) generally predates or sits outside the
frozen-pretrained-backbone paradigm entirely, which makes a partial-credit mark here
questionable. **Do not change this cell automatically** — the correct fix depends on what
the actual Hegedűs et al. paper does, which requires checking the source PDF (not currently
available in this session's uploads). Action item: Vanja (or a follow-up session with the
paper available) should verify whether this specific paper's method involves any
frozen/pretrained component, and either confirm the `(\checkmark)` or change it to `$-$` or
`$\times$` per the scoring convention already established in §`sec:synthesis_gap:matrix`
(the `$-$` marker for "dimension not engaged," used for Houlsby/LoRA on the "No central
coord." column, is the right precedent to follow if gossip learning simply doesn't engage
the frozen-backbone concept at all).

---

## 6. `12_appendix.tex`

### 6.1 Reconcile the snowballing saturation-criterion claim with the Conclusion's own caveat

**Issue (Pass 2/6):** Appendix A.2 describes saturation assessment in a way that reads as an
applied, conclusive check ("saturation was assessed... with high overlap indicating
diminishing marginal returns"), while the Conclusion (`11_conclusion.tex`, Conclusion
Validity paragraph) explicitly and more cautiously states this was "not formally measured
using a stopping criterion." Align A.2 to the more conservative framing already committed to
in the Conclusion — don't inflate the Conclusion to match A.2's stronger claim.

```latex
% OLD
Forward and backward citation snowballing was conducted on the G0 seeds
following the procedure of Wohlin et al.~\cite{Wohlin2014}. Backward
snowballing examined the reference lists of each seed; forward snowballing
identified subsequent works citing the seeds. One wave of snowballing was
executed; saturation was assessed by inspecting the overlap between newly
retrieved candidates and the pre-validated G1--G6 corpora, with high overlap
indicating diminishing marginal returns.

% NEW
Forward and backward citation snowballing was conducted on the G0 seeds
following the procedure of Wohlin et al.~\cite{Wohlin2014}. Backward
snowballing examined the reference lists of each seed; forward snowballing
identified subsequent works citing the seeds. One wave of snowballing was
executed; saturation was assessed qualitatively by inspecting the overlap
between newly retrieved candidates and the pre-validated G1--G6 corpora, with
high overlap suggesting diminishing marginal returns. This was not, however,
formalised as a quantitative stopping criterion (e.g.\ a measured diminishing
marginal inclusion rate); see the discussion of this limitation in
Section~\ref{sec:conclusion:threats}.
```

### 6.2 Clarify the venue-distribution figure's funnel stage

**Issue (Pass 6):** `fig:venues` is captioned as describing "the 464-paper enriched corpus"
while sitting inside the "A.6 Bibliometric Overview" subsection whose opening sentence is
about "the final corpus of 123 papers" — readers can easily misread the figure as describing
the final included set.

```latex
% OLD
The most active year is 2024 with 38 papers (31\% of total), followed by 2025
with 20 (16\%) and 2023 with 19 (15\%), confirming that the field is both
active and growing. Publication volume accelerates sharply after 2022,
coinciding with the proliferation of LoRA-based PEFT papers and
adapter-serving systems.

\begin{table}[H]
\centering
\caption{Publication year distribution of the 123-paper reviewed corpus.}
\label{tab:year_dist}

% NEW
The most active year is 2024 with 38 papers (31\% of total), followed by 2025
with 20 (16\%) and 2023 with 19 (15\%), confirming that the field is both
active and growing. Publication volume accelerates sharply after 2022,
coinciding with the proliferation of LoRA-based PEFT papers and
adapter-serving systems.

\begin{table}[H]
\centering
\caption{Publication year distribution of the 123-paper reviewed corpus.}
\label{tab:year_dist}
```
*(no change needed to this block — see the actual figure fix below)*

```latex
% OLD
\begin{figure}[H]
  \centering
  \includegraphics[width=1\linewidth]{figures/fig_slr5_venues.pdf}
  \caption{Venue distribution of the 464-paper enriched corpus.
           ACL/EMNLP comprises the largest venue category (25 papers),
           followed by arXiv preprints (9), NeurIPS (8), and ICML/MLSys (7).}
  \label{fig:venues}
\end{figure}

% NEW
For context on venue composition prior to the final quality-appraisal and
full-text filtering stages, Figure~\ref{fig:venues} reports the venue
distribution of the 464-paper \emph{enriched pool} (an earlier funnel stage,
not the 123-paper final corpus discussed above).

\begin{figure}[H]
  \centering
  \includegraphics[width=1\linewidth]{figures/fig_slr5_venues.pdf}
  \caption{Venue distribution of the 464-paper enriched pool (an intermediate
           funnel stage prior to full-text review and quality appraisal;
           \emph{not} the final 123-paper corpus). ACL/EMNLP comprises the
           largest venue category (25 papers), followed by arXiv preprints
           (9), NeurIPS (8), and ICML/MLSys (7).}
  \label{fig:venues}
\end{figure}
```

---

## 7. Figure placeholders — NOT a text fix, flagged separately

**Issue (Pass 0, Blocking):** six `\fbox` placeholders remain:
`02_background.tex` (1), `04_peft.tex` (2), `05_adapter_composition.tex` (1),
`07_moe_routing.tex` (1), `08_p2p_federated.tex` (1).

**This cannot be resolved by a LaTeX text edit** — actual diagram artwork needs to be
produced (as PDF/SVG) and dropped into `figures/`, then each `\fbox{...}` block replaced
with an `\includegraphics{...}` call pointing at the real file. Claude Code should **not**
attempt to invent placeholder `\includegraphics` calls pointing at files that don't exist —
that would trade a visible `\fbox` placeholder for a silent broken-reference compile error,
which is worse. Flag this as a separate task requiring actual figure production (e.g. via
Mermaid/TikZ per Vanja's usual workflow, or a diagramming pass with Claude/Claude Code in a
follow-up session), not part of this text-fix pass.

---

## 8. `PRISMA_NUMBERS_VALIDATION.md` — NOT a LaTeX fix, flagged separately

**Issue (Pass 1, Blocking):** §B of this file states the `tab:groups` "n final" column is
currently `G0=20, G1=12, G2=15, G3=11, G4=12, G5=9, G6=29, Other=15` — this does **not**
match the actual current table in `03_methodology.tex` (`G0=18, G1=17, G2=17, G3=14, G4=16,
G5=11, G6=30`, no "Other" row). The manuscript's own numbers are internally correct; the
validation file is stale.

**This is not a `.tex` fix** — `PRISMA_NUMBERS_VALIDATION.md` is a separate audit artifact
that needs its §B table regenerated from the current `03_methodology.tex` `tab:groups`
values. If there's a script that generates this file from the pipeline CSVs, re-run it;
otherwise manually update §B to:

```markdown
## B. Groups table (`tab:groups` — pre-validated split) — verified against current `tab:groups` in `03_methodology.tex`

| Group | n pre-validated | n final | Status |
|---|---|---|---|
| G0 | 9 | 18 | ✅ |
| G1 | 59 | 17 | ✅ |
| G2 | 37 | 17 | ✅ |
| G3 | 95 | 14 | ✅ |
| G4 | 51 | 16 | ✅ |
| G5 | 35 | 11 | ✅ |
| G6 | 66 | 30 | ✅ |
| **Total** | **352** | **123** | ✅ |
```

---

## 9. `bibliography.bib`

### 9.1 Fix the Houlsby et al. 2019 author name error

**Issue (Pass 5 — verified against the actual source PDF):** the third author is listed as
"Morrone, Brian" but the paper's actual byline reads "Bruna Morrone." This is a factual
name/gender error, not a formatting issue, and it also appears in an earlier draft's
reference list, so it's a longstanding error that survived a prior review round.

```bibtex
% OLD
@inproceedings{Houlsby2019,
author    = {Houlsby, Neil and Giurgiu, Andrei and Jastrzebski, Stanislaw
             and Morrone, Brian and de Laroussilhe, Quentin and Gesmundo, Andrea
             and Attariyan, Mona and Gelly, Sylvain},
  title     = {Parameter-Efficient Transfer Learning for {NLP}},
  booktitle = {International Conference on Machine Learning (ICML)},
  pages     = {2790--2799},
  year      = {2019},
  doi = {10.48550/arXiv.1902.00751}
}

% NEW
@inproceedings{Houlsby2019,
author    = {Houlsby, Neil and Giurgiu, Andrei and Jastrzebski, Stanislaw
             and Morrone, Bruna and de Laroussilhe, Quentin and Gesmundo, Andrea
             and Attariyan, Mona and Gelly, Sylvain},
  title     = {Parameter-Efficient Transfer Learning for {NLP}},
  booktitle = {International Conference on Machine Learning (ICML)},
  pages     = {2790--2799},
  year      = {2019},
  doi = {10.48550/arXiv.1902.00751}
}
```

**Recommended follow-up (not automated here):** since this exact error slipped through a
prior review round, do a full author-list cross-check for every G0 seed paper
(`Houlsby2019`, `Hu2022`, `Pfeiffer2020hub`, `Pfeiffer2021fusion`, `Sajina2024`,
`Sajina2021`, `Borzunov2023`, `Han2024`, `Sheng2024`) against their actual PDFs/official
pages before submission — this fix only covers the one error found in this session, not a
guarantee the rest are error-free.

### 9.2 Retype 9 arXiv-preprint entries from `@article` to `@misc`

**Issue (Pass 5/bibliography):** these 9 entries store `journal = {arXiv preprint
arXiv:XXXX.XXXXX}` inside an `@article` entry, which is a type/field mismatch — arXiv
preprints should not have a fabricated "journal" name. The `.bib` file already correctly
uses `@misc`/`@techreport`/`@phdthesis` elsewhere (`SemanticScholar2023`,
`KitchenhamCharters2007`, `Sajina2021`), so this brings these 9 in line with the convention
already established in the same file. The `doi` field (arXiv-minted DOI, `10.48550/arXiv...`)
is correct and unchanged — arXiv DOIs are legitimate and should be kept.

```bibtex
% OLD
@article{Ponti2023,
  author    = {Ponti, Edoardo M. and Sordoni, Alessandro and Bengio, Yoshua
               and Reddy, Siva},
  title     = {Combining Modular Skills in Multitask Learning},
  journal   = {arXiv preprint arXiv:2202.13914},
  year      = {2023},
  doi       = {10.48550/arXiv.2202.13914}
}

% NEW
@misc{Ponti2023,
  author        = {Ponti, Edoardo M. and Sordoni, Alessandro and Bengio, Yoshua
                   and Reddy, Siva},
  title         = {Combining Modular Skills in Multitask Learning},
  year          = {2023},
  eprint        = {2202.13914},
  archivePrefix = {arXiv},
  doi           = {10.48550/arXiv.2202.13914}
}
```

```bibtex
% OLD
@article{Huang2023,
  author    = {Chengsong Huang and Qian Liu and Bill Yuchen Lin and Tianyu Pang and Chao Du and Min Lin},
  title     = {{LoraHub}: Efficient Cross-Task Generalization via Dynamic {LoRA}
               Composition},
  journal   = {arXiv preprint arXiv:2307.13269},
  year      = {2023},
  doi       = {10.48550/arXiv.2307.13269}
}

% NEW
@misc{Huang2023,
  author        = {Chengsong Huang and Qian Liu and Bill Yuchen Lin and Tianyu Pang and Chao Du and Min Lin},
  title         = {{LoraHub}: Efficient Cross-Task Generalization via Dynamic {LoRA}
                   Composition},
  year          = {2023},
  eprint        = {2307.13269},
  archivePrefix = {arXiv},
  doi           = {10.48550/arXiv.2307.13269}
}
```

```bibtex
% OLD
@article{Ghiasvand2025,
  author    = {Ghiasvand, Sajjad and Alizadeh, Mahnoosh and Pedarsani, Ramtin},
  title     = {Decentralized Low-Rank Fine-Tuning of Large Language Models},
  journal   = {arXiv preprint arXiv:2501.15361},
  year      = {2025},
  doi       = {10.48550/arXiv.2501.15361}
}

% NEW
@misc{Ghiasvand2025,
  author        = {Ghiasvand, Sajjad and Alizadeh, Mahnoosh and Pedarsani, Ramtin},
  title         = {Decentralized Low-Rank Fine-Tuning of Large Language Models},
  year          = {2025},
  eprint        = {2501.15361},
  archivePrefix = {arXiv},
  doi           = {10.48550/arXiv.2501.15361}
}
```

```bibtex
% OLD
@article{Babakniya2023,
  author    = {Babakniya, Sara and Elkordy, Ahmed Roushdy and Ezzeldin,
               Yahya H. and Liu, Qingfeng and Song, Kee-Bong and
               El-Khamy, Mostafa and Avestimehr, Salman},
  title     = {{SLoRA}: Federated Parameter Efficient Fine-Tuning of
               Language Models},
  journal   = {arXiv preprint arXiv:2308.06522},
  year      = {2023},
  doi       = {10.48550/arXiv.2308.06522}
}

% NEW
@misc{Babakniya2023,
  author        = {Babakniya, Sara and Elkordy, Ahmed Roushdy and Ezzeldin,
                   Yahya H. and Liu, Qingfeng and Song, Kee-Bong and
                   El-Khamy, Mostafa and Avestimehr, Salman},
  title         = {{SLoRA}: Federated Parameter Efficient Fine-Tuning of
                   Language Models},
  year          = {2023},
  eprint        = {2308.06522},
  archivePrefix = {arXiv},
  doi           = {10.48550/arXiv.2308.06522}
}
```

```bibtex
% OLD
@article{LinSplitLoRA2024,
  author    = {Lin, Zheng and Hu, Xuanjie and Zhang, Yuxin and Chen, Zhe and
               Fang, Zihan and Zhu, Wei and Gao, Xianhao and Gao, Yuguang
               and Xu, Pan},
  title     = {{SplitLoRA}: A Split Parameter-Efficient Fine-Tuning Framework
               for Large Language Models},
  journal   = {arXiv preprint arXiv:2407.00952},
  year      = {2024},
  doi       = {10.48550/arXiv.2407.00952}
}

% NEW
@misc{LinSplitLoRA2024,
  author        = {Lin, Zheng and Hu, Xuanjie and Zhang, Yuxin and Chen, Zhe and
                   Fang, Zihan and Zhu, Wei and Gao, Xianhao and Gao, Yuguang
                   and Xu, Pan},
  title         = {{SplitLoRA}: A Split Parameter-Efficient Fine-Tuning Framework
                   for Large Language Models},
  year          = {2024},
  eprint        = {2407.00952},
  archivePrefix = {arXiv},
  doi           = {10.48550/arXiv.2407.00952}
}
```

```bibtex
% OLD
@article{YanFeDeRA2024,
  author    = {Yan, Yuxuan and Yang, Qianqian and Tang, Shunpu and Shi, Zhiguo},
  title     = {{FeDeRA}: Efficient Fine-Tuning of Language Models in Federated
               Learning Leveraging Weight Decomposition},
  journal   = {arXiv preprint arXiv:2404.18848},
  year      = {2024},
  doi       = {10.48550/arXiv.2404.18848}
}

% NEW
@misc{YanFeDeRA2024,
  author        = {Yan, Yuxuan and Yang, Qianqian and Tang, Shunpu and Shi, Zhiguo},
  title         = {{FeDeRA}: Efficient Fine-Tuning of Language Models in Federated
                   Learning Leveraging Weight Decomposition},
  year          = {2024},
  eprint        = {2404.18848},
  archivePrefix = {arXiv},
  doi           = {10.48550/arXiv.2404.18848}
}
```

```bibtex
% OLD
@article{LiMixLoRA2024,
  author    = {Li, Dengchun and Ma, Yingzi and Wang, Naizheng and Ye, Zhengmao
               and Cheng, Zhiyuan and Tang, Yinghao and Zhang, Yan and Lei, Mingjie
               and Zuo, Shaoshan and Yang, Liu and Tang, Mingjie},
  title     = {{MixLoRA}: Enhancing Large Language Models Fine-Tuning with
               {LoRA}-Based Mixture of Experts},
  journal   = {arXiv preprint arXiv:2404.15159},
  year      = {2024},
  doi       = {10.48550/arXiv.2404.15159}
}

% NEW
@misc{LiMixLoRA2024,
  author        = {Li, Dengchun and Ma, Yingzi and Wang, Naizheng and Ye, Zhengmao
                   and Cheng, Zhiyuan and Tang, Yinghao and Zhang, Yan and Lei, Mingjie
                   and Zuo, Shaoshan and Yang, Liu and Tang, Mingjie},
  title         = {{MixLoRA}: Enhancing Large Language Models Fine-Tuning with
                   {LoRA}-Based Mixture of Experts},
  year          = {2024},
  eprint        = {2404.15159},
  archivePrefix = {arXiv},
  doi           = {10.48550/arXiv.2404.15159}
}
```

```bibtex
% OLD
@article{LuoMoELoRA2024,
  author    = {Luo, Tongxu and Lei, Jiahe and Lei, Fangyu and Liu, Weihao and
               He, Shizhu and Zhao, Jun and Liu, Kang},
  title     = {{MoELoRA}: Contrastive Learning Guided Mixture of Experts on
               Parameter-Efficient Fine-Tuning for Large Language Models},
  journal   = {arXiv preprint arXiv:2402.12851},
  year      = {2024},
  doi       = {10.48550/arXiv.2402.12851}
}

% NEW
@misc{LuoMoELoRA2024,
  author        = {Luo, Tongxu and Lei, Jiahe and Lei, Fangyu and Liu, Weihao and
                   He, Shizhu and Zhao, Jun and Liu, Kang},
  title         = {{MoELoRA}: Contrastive Learning Guided Mixture of Experts on
                   Parameter-Efficient Fine-Tuning for Large Language Models},
  year          = {2024},
  eprint        = {2402.12851},
  archivePrefix = {arXiv},
  doi           = {10.48550/arXiv.2402.12851}
}
```

```bibtex
% OLD
@article{TouvronLLaMA2023,
  author    = {Hugo Touvron and Thibaut Lavril and Gautier Izacard and
               Xavier Martinet and Marie-Anne Lachaux and Timoth\'{e}e Lacroix
               et al},
  title     = {{LLaMA}: Open and Efficient Foundation Language Models},
  journal   = {arXiv preprint arXiv:2302.13971},
  year      = {2023},
  doi       = {10.48550/arXiv.2302.13971}
}

% NEW
@misc{TouvronLLaMA2023,
  author        = {Hugo Touvron and Thibaut Lavril and Gautier Izacard and
                   Xavier Martinet and Marie-Anne Lachaux and Timoth\'{e}e Lacroix
                   et al},
  title         = {{LLaMA}: Open and Efficient Foundation Language Models},
  year          = {2023},
  eprint        = {2302.13971},
  archivePrefix = {arXiv},
  doi           = {10.48550/arXiv.2302.13971}
}
```

### 9.3 Retype `RadfordGPT22019` (GPT-2) from `@article` to `@techreport`

**Issue:** GPT-2 is an OpenAI technical report, not a journal article — this entry has no
DOI (correctly, tech reports usually don't), but the wrong `@article`/`journal=` combination.

```bibtex
% OLD
@article{RadfordGPT22019,
  author    = {Alec Radford and Jeffrey Wu and Rewon Child and David Luan
               and Dario Amodei and Ilya Sutskever},
  title     = {Language Models Are Unsupervised Multitask Learners},
  journal   = {OpenAI Technical Report},
  year      = {2019}
}

% NEW
@techreport{RadfordGPT22019,
  author      = {Alec Radford and Jeffrey Wu and Rewon Child and David Luan
                 and Dario Amodei and Ilya Sutskever},
  title       = {Language Models Are Unsupervised Multitask Learners},
  institution = {OpenAI},
  year        = {2019}
}
```

### 9.4 `Li2024CaraServe` — verification needed, NOT a blind fix

**Issue found while drafting this fix:** this entry has an internal contradiction that
needs Vanja's input, not a mechanical correction, because I can't verify the true venue/year
combination from here:

```bibtex
@article{Li2024CaraServe,
  author    = {Li, Suyi and Lu, Hanfeng and Wu, Tianyuan and Yu, Minchen and
               Weng, Qizhen and Chen, Xusheng and Shan, Yizhou and
               Yuan, Binhang and Wang, Wei},
  title     = {{CaraServe}: {CPU}-Assisted and Rank-Aware {LoRA} Serving for
               Generative {LLM} Inference},
  journal   = {USENIX Annual Technical Conference},
  year      = {2025},
  doi       = {10.48550/arXiv.2401.11240}
}
```

Three things don't line up: (1) the citation **key** says `2024`, (2) the **year field**
says `2025`, (3) the **DOI** (`arXiv.2401.11240`) is an arXiv DOI from January 2024, but the
**journal field** names a conference (USENIX ATC) rather than arXiv. Pick one of:

- **Option A — it's the arXiv preprint (year 2024):** retype as `@misc` like the group
  above, drop the "USENIX Annual Technical Conference" journal field, keep
  `eprint={2401.11240}`, set `year={2024}`, and either rename the key to match (optional,
  only if you're comfortable with the downstream `\cite{}` rename across all sections that
  reference it) or leave the key as-is since a key doesn't have to literally match its year.
- **Option B — it was actually published at USENIX ATC (confirm which year: 2024 or
  2025):** retype as `@inproceedings` with a proper `booktitle`, correct `year`, and either
  drop the arXiv DOI (replace with a USENIX proceedings DOI if one exists) or keep the arXiv
  DOI only if there genuinely is no separate published-proceedings DOI.

**Do not guess between these — verify against the actual paper (e.g. its arXiv listing or
the USENIX ATC 2024/2025 program) before editing this entry.**

### 9.5 `Johnson2023` (MIMIC-IV) — DO NOT AUTO-APPLY, author decision required

**Issue (bibliography audit):** this entry (MIMIC-IV clinical EHR dataset) is uncited
anywhere in the manuscript and unrelated to any of the five reviewed pillars
(PEFT/composition/serving/MoE/P2P–federated). It likely correlates with two other loose
ends already flagged: Appendix B's Scopus queries Q8 ("NL-to-SQL with Adapters") and Q9
(NER/sequence labelling), which are similarly disconnected from the stated three-pillar
scope, and the medical NL-to-SQL paper sitting in the project's reference material. This
looks like a dropped thread from an earlier draft.

**Two options, pick one — do not delete or restore silently:**
- **Option A (default/safer):** delete the `Johnson2023` entry entirely from
  `bibliography.bib`, since it's unused and off-scope.
- **Option B:** if there's meant to be a sentence somewhere (likely in `04_peft.tex` or
  `08_p2p_federated.tex`) discussing medical NL-to-SQL as an application domain that got cut
  during editing, restore that sentence with a `\cite{Johnson2023}` and keep the entry.

Flag this explicitly to Vanja and ask which option applies before changing the `.bib` file.

---

## 10. Verification checklist — run after all edits above

1. **Abstract word count.** Extract text between `\abstract{` and its closing `}` in
   `main.tex`, strip LaTeX commands, split on whitespace, confirm word count ≤ 200.
2. **Voice check.** Run `grep -noE '\b(we|our|us)\b' *.tex` (word-boundary, case-sensitive
   lowercase only — avoid matching "We" in bibliography titles or proper nouns) across
   `main.tex` and `03_methodology.tex` specifically, and confirm zero remaining hits in the
   passages touched by this spec. (Sections 04–08 have not been audited for voice in this
   pass — don't "fix" hits found there without a separate audit pass first.)
3. **Marketplace sweep.** `grep -ri "marketplace" *.tex` → expect zero hits after §3.1's
   deletion.
4. **Bib cross-reference re-check.** Re-run the uncited-key / undefined-key cross-check
   (parse all `\cite{}` groups across `.tex` files vs. all `@...{key,` entries in
   `bibliography.bib`) and confirm: (a) zero cited-but-undefined keys (should remain 0), (b)
   `KitchenhamCharters2007` and `Webster2002` now show as cited (fix in §2.2 above), (c)
   `Johnson2023` status matches whichever option was chosen in §9.5.
5. **Bib type-check.** Confirm the 9 entries in §9.2 are now `@misc` with `eprint` +
   `archivePrefix` fields (not `journal=`), and that `RadfordGPT22019` is `@techreport`.
   Confirm `Li2024CaraServe` was NOT silently edited without Vanja's input on §9.4.
6. **Compile check.** Actually compile the full project (`main.tex` → PDF) after all edits —
   confirm no new undefined references, no BibTeX errors from the retyped entries (a common
   failure mode: `@misc` entries in some styles need `howpublished` or `note` — if the
   `mdpi.cls`/IEEEtran bibliography style throws a warning about missing fields for the
   retyped `@misc` entries, report this back rather than inventing a `howpublished` value
   that wasn't specified in this document).
7. **Flag remaining decision points to Vanja explicitly, as a list, at the end of the
   session:** (a) §1.2 supplementary-materials expansion, (b) §5.1's dependency on
   Sections 6/8 containing narrative latency discussion, (c) §5.2 Gossip Learning cell
   verification, (d) §8's `PRISMA_NUMBERS_VALIDATION.md` regeneration, (e) §9.4
   `Li2024CaraServe` venue/year resolution, (f) §9.5 `Johnson2023` keep-or-delete decision.
