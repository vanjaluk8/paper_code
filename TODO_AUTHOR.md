# TODO_AUTHOR.md

Flat list of every `% TODO-AUTHOR` marker left in the manuscript source, per
Phase 4 of `REVISION_PROMPT.md`. One marker found (searched all of
`sections/*.tex` for the literal string).

## `sections/05_adapter_composition.tex:47`

```latex
% TODO-AUTHOR [C-2]: IA$^3$ is named but never cited anywhere in the manuscript.
% Add its originating reference (Liu et al., "Few-Shot Parameter-Efficient
% Fine-Tuning is Better and Cheaper than In-Context Learning", NeurIPS 2022) to
% bibliography.bib and \cite it here -- not added automatically per the rule
% against introducing citations from the agent's own knowledge of the literature.
```

**Context:** §5.2 (`sec:adapter_composition:...`) names IA$^3$ as one of the
methods the unified Adapters library supports, but no reference is attached
to it anywhere in the manuscript, and IA$^3$'s originating paper is not in
`bibliography.bib`.

**Why not fixed automatically:** the suggested reference (Liu et al., NeurIPS
2022) is asserted from general knowledge of the PEFT literature, not verified
against a primary source the way every other citation fix in this revision
was (see `OPEN_QUESTIONS.md`'s citation-integrity section for the standard
applied elsewhere: quote the paper, don't assert from memory). Adding an
unverified citation would violate the same rule that governed every other
citation decision in this revision.

**What you need to do:** confirm the correct originating paper for IA$^3$
(Infused Adapter by Inhibiting and Amplifying Inner Activations), add a
`bibliography.bib` entry for it with a verified DOI/arXiv ID, and add a
`\cite{}` at its first mention in `sections/05_adapter_composition.tex`.
Once done, delete the `TODO-AUTHOR` comment block.
