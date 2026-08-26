## Meta
- **Citation:** (2023). Adapters: A Unified Library for Parameter-Efficient and Modular Transfer Learning.
- **Venue:** Pre-print (arXiv:2311.11077)
- **Tags:** `adapter-composition` `library` `framework`
- **Thesis sections:** §2 (background), §4 (implementation), §8 (tooling)

## Key Findings
1. Introduces Adapters library that provides a standardized interface for all major PEFT methods (adapters, LoRA, prefix tuning, IA^3) integrated with HuggingFace Transformers.
2. Supports linear composition methods like adapter stacking, addition, averaging, concatenation, gated combinations.
3. Integrates with AdapterFusion and provides out-of-the-box fusion setup.
4. Modular approach enables zero-shot mixing of independently trained adapters.

## Composition Method
- The library supports multiple composition types: 'linear' (sequential stacking), 'addition' (parallel sum), 'average' (mean of adapters), 'cat' (concatenation), 'split' (invertible adapters).
- Fusion composition: gated combination of adapters with learnable fusion weights.
- Supports sequential integration of multiple adapters, and 'parallel' inference using multiple heads of adapters.

## Relevance to Thesis
- The Adapters library is the most practical implementation of modular, composable PEFT; directly aligned with the implementation orientation for P2P marketplace.

## Limitations / Gaps
- Composition capabilities are limited to linear combination and simple heuristics; no routing across adapters.
- Does not support runtime/dynamic selection among adapter heads.
- Lacks mechanisms for decentralized routing, selection, and fault tolerance.