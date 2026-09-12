# TODO_AUTHOR.md

All 5 `% TODO-AUTHOR` markers flagged during Phase 4 of `REVISION_PROMPT.md`
have been resolved (author-confirmed sources, network-verified against
primary sources, citations restored). None remain in `sections/*.tex`.

## `sections/05_adapter_composition.tex` — IA$^3$ (`C-2`)

Resolved: `LiuIA3_2022` (Liu et al., "Few-Shot Parameter-Efficient
Fine-Tuning is Better and Cheaper than In-Context Learning," NeurIPS 2022,
arXiv:2205.05638) added to `bibliography.bib`, cited at IA$^3$'s first
mention. Verified via the arXiv API that this is IA$^3$'s originating paper.

## `sections/04_peft.tex` §4.1 and §4.3 — intrinsic dimensionality (`E-2`)

Resolved: `Aghajanyan2021Intrinsic` (Aghajanyan, Zettlemoyer, Gupta,
"Intrinsic Dimensionality Explains the Effectiveness of Language Model
Fine-Tuning," ACL-IJCNLP 2021, DOI `10.18653/v1/2021.acl-long.568`) added
to `bibliography.bib`. §4.1's lower-dimensional-subspace claim now cites
it directly (verified the paper's own abstract states pre-trained models
have very low intrinsic dimension — matches the claim). §4.3's occurrence
(the paragraph attributing this to `ZengExpressive2024`) was left as
removed, per the marker's own guidance that no replacement claim was
required once §4.1 carries the correct citation.

## `sections/02_background.tex` §2.3 and `sections/09_synthesis_gap.tex` §9.4 — gossip O(log N) (`E-6`)

Resolved: `KarpRumor2000` (Karp, Schindelhauer, Shenker, Vöcking,
"Randomized Rumor Spreading," FOCS 2000, DOI `10.1109/SFCS.2000.892324`)
added to `bibliography.bib`, cited at both occurrences. Chosen over the
alternative candidate (Pittel 1987) because its own result is stated in
the same terms as the manuscript's claim — "...rounds ... with high
probability" — a near-exact phrase match, confirmed by reading the paper
directly (author's choice among the two verified candidates).
