## Meta
- **Citation:** Pfeiffer, J., et al. (2021). MAD-G: Multilingual Adapter Generation for Efficient Cross-Lingual Transfer.
- **Venue:** Findings of EMNLP 2021
- **Tags:** `adapter-composition` `cross-lingual` `hypernetwork`
- **Thesis sections:** §4.2 (cross-lingual adapter composition)

## Key Findings
1. MAD-G extends MAD-X by introducing a hypernetwork to generate adapters for unseen target languages without any training data in those languages.
2. Train language adapters for a set of source languages (e.g., English, German, French), then use a hypernetwork conditioned on language embeddings to generate new language adapters for target languages.
3. Achieves cross-lingual transfer to languages not seen during language adapter training, outperforming adapter stacking-based approaches on zero-shot cross-lingual tasks.
4. The hypernetwork learns to interpolate between known language adapter parameter spaces.

## Composition Method
- Language adapter generation is continuous: the hypernetwork maps language embeddings to adapter weights.
- For inference: generated target-language adapter + source task adapter stacked together through the base layers.
- This enriches the MAD-X paradigm: instead of training adapters for each language separately, MAD-G generates them on the fly.

## Relevance to Thesis
- Hypernetwork-based generation is a key technique for scaling adapter availability without training per-task adapters for each language/task.
- Inspires potential "adapter synthesis" in P2P settings: you could generate adapters for new peers/tasks using learned generation from known adapters.
- Directly relevant to cross-lingual transfer approaches in §4.

## Limitations / Gaps
- Hypernetwork generation assumes a stable relationship between language embeddings and adapter parameters.
- Not directly tested on multi-task multi-adapter routing/composition.
- Does not address decentralized discovery or routing of adapters.