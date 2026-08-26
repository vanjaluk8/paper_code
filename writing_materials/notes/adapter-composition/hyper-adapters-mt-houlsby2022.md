## Meta
- **Citation:** Houlsby, N. et al. (2022). Multilingual Machine Translation with Hyper-Adapters.
- **Venue:** (Pre-print, arXiv:2205.10835)
- **Tags:** `adapter-composition` `multilingual` `hypernetworks`
- **Thesis sections:** §4.2 (multi-lingual), §8 (potentially)

## Key Findings
1. Hyper-Adapters extend hypernetworks to generate language-specific adapters for machine translation, enabling zero-shot cross-lingual transfer to unseen languages.
2. A hypernetwork generates the adapter weights for each language, conditioned on a learned language embedding.
3. Achieves comparable translation quality to MAD-X's language-specific adapter stacking but uses a more parameter-efficient single hypernetwork that generates weights on the fly.
4. Supports up to 100 languages without retraining per language.

## Composition Method
- Generates adapter parameters dynamically per language via a hypernetwork conditioned on language embeddings.
- The hypernetwork is shared across all languages, so this is a generative/extern parameterization of adapters.
- Composition across languages is implicit: the hypernetwork learns to interpolate in the language embedding space.

## Relevance to Thesis
- Dynamic parameter generation could be extended to generate adapters for unseen tasks in a P2P setting.
- Not directly applicable to composing adapters, but analogous scenario in decentralized P2P tasks.

## Limitations / Gaps
- The hypernetwork requires training on the available languages and may not generalize to entirely unseen task types (novel domains beyond languages).
- Still focused on a centralized training setup.