# TODO_AUTHOR.md

Flat list of every `% TODO-AUTHOR` marker left in the manuscript source, per
Phase 4 of `REVISION_PROMPT.md`. 5 markers found (searched all of
`sections/*.tex` for the literal string), all concerning missing or
uncertain citations that could not be added without introducing a reference
from the agent's own knowledge of the literature.

## `sections/05_adapter_composition.tex:47`

```latex
% TODO-AUTHOR [C-2]: IA$^3$ is named but never cited anywhere in the manuscript.
% Add its originating reference (Liu et al., "Few-Shot Parameter-Efficient
% Fine-Tuning is Better and Cheaper than In-Context Learning", NeurIPS 2022) to
% bibliography.bib and \cite it here -- not added automatically per the rule
% against introducing citations from the agent's own knowledge of the literature.
```

**Context:** §5.2 names IA$^3$ as one of the methods the unified Adapters
library supports, but no reference is attached to it anywhere, and IA$^3$'s
originating paper is not in `bibliography.bib`.

**What you need to do:** confirm the correct originating paper for IA$^3$,
add a `bibliography.bib` entry with a verified DOI/arXiv ID, and add a
`\cite{}` at its first mention. Delete the marker once done.

## `sections/04_peft.tex:24` (E-2)

```latex
% TODO-AUTHOR [E-2]: the following sentence attributed the lower-dimensional-subspace
% observation to Zeng et al. (ZengExpressive2024), but that paper is about LoRA's
% representational/expressive capacity (whether a rank-r adapter can exactly represent
% a target model), not the empirical intrinsic-dimensionality claim below -- confirmed
% by reading the paper's own abstract, which states its scope explicitly excludes
% optimisation. The reviewer's suggested correct source is Aghajanyan et al. 2021
% ("Intrinsic Dimensionality Explains the Effectiveness of Language Model Fine-Tuning",
% ACL 2021), which is absent from bibliography.bib and this corpus -- not added here
% per the rule against introducing citations from the agent's own literature knowledge.
% If you confirm Aghajanyan et al. 2021 is the intended source, add it to
% bibliography.bib and restore a \cite{} here.
```

**Context:** §4.1's sentence attributing the PEFT-motivating
low-dimensionality observation to a specific formalising paper. The false
attribution to `ZengExpressive2024` has been removed and the sentence
reworded to an unattributed general statement; it currently carries no
citation at all.

**What you need to do:** confirm whether Aghajanyan et al. 2021 is the
intended source (or a different paper); add the bib entry and `\cite{}`.

## `sections/04_peft.tex:136` (E-2)

```latex
% TODO-AUTHOR [E-2]: this paragraph attributed a gradient-manifold/intrinsic-dimensionality
% result to Zeng et al. (ZengExpressive2024) and called it "established earlier" than LoRA --
% chronologically impossible on its face, since that paper is from 2024 and cites LoRA
% (2021/2022) as prior work it builds on. Confirmed by reading the paper directly: its
% actual subject is LoRA's expressive/representational capacity (a rank threshold for
% exact representability of a target model), and it explicitly states "This excludes
% other aspects such as optimization" -- it contains no gradient-manifold claim at all.
% Zeng et al.~\cite{ZengExpressive2024} is a genuine, later theoretical result about
% LoRA's expressive power and may still be worth citing accurately elsewhere in this
% section; it does not support the claim that was here. The reviewer's suggested
% correct source for the deleted claim is Aghajanyan et al. 2021, absent from
% bibliography.bib -- not added here per the rule against introducing citations from
% the agent's own literature knowledge.
```

**Context:** §4.3 previously claimed LoRA's theoretical basis was
"established earlier" by Zeng et al. — a 2024 paper that postdates LoRA and
does not contain the claimed result. The whole paragraph asserting this was
removed (see `CHANGELOG.md` / `OPEN_QUESTIONS.md` E-2 for detail); nothing
currently fills the gap left by its removal.

**What you need to do:** if you want to keep a "LoRA's effectiveness has a
theoretical basis in prior intrinsic-dimensionality work" claim in this
paragraph's place, confirm the correct source (Aghajanyan et al. 2021 is the
reviewer's candidate) and add it. Otherwise no further action is needed —
the surrounding paragraphs already flow without this claim.

## `sections/02_background.tex:136` (E-6)

```latex
% TODO-AUTHOR [E-6]: the O(log N) round-complexity claim below was previously attributed
% to Ormandi et al. (OrmandyGossip2013), but that paper (an ML ensemble-voting method,
% "Gossip Learning with Linear Models on Fully Distributed Data") contains no such result --
% confirmed by a full-text search of the paper for "O(log", "log N", and "rounds with high
% probability" (zero matches). This is a real, classical epidemic/rumour-spreading bound
% (e.g. Demers et al. 1987; Karp et al. 2000; Pittel 1987) but the citation for it is not
% currently in bibliography.bib -- not added here per the rule against introducing citations
% from the agent's own literature knowledge. Please add the correct source and restore a
% \cite{} here.
```

**Context:** §2.3's general statement that gossip protocols achieve
network-wide dissemination in O(log N) rounds — a real, well-established
result, just not from the citation that was previously attached to it.

**What you need to do:** add the correct classical source (the comment
suggests candidates: Demers et al. 1987, Karp et al. 2000, or Pittel 1987 —
confirm which, if any, is the one you intend) to `bibliography.bib` and
`\cite{}` it here.

## `sections/09_synthesis_gap.tex:259` (E-6, second occurrence)

```latex
% TODO-AUTHOR [E-6]: same citation issue as Sec 2.3 -- OrmandyGossip2013 does not
% contain an O(log N) round-complexity result (verified by full-text search); the
% correct classical source is not yet in bibliography.bib.
```

**Context:** §9.4's gap statement repeats the same uncited O(log N) claim in
a different location (an open-question framing about gossip-based adapter
metadata dissemination). Same fix as above — once you add the correct
citation for the Background-section occurrence, add it here too.
