## Meta
- **Citation:** Jin et al. (2025) Sparser Mixture-of-Adapters with Cross-Layer Generalization
- **Venue:** NAACL 2025
- **Tags:** `MoE-routing` `cross-layer` `sparsity` `shared-experts`
- **Thesis sections:** §7.x (MoE routing)

## Key Findings
1. Proposes a cross-layer parameter sharing scheme for MoE adapters where expert modules can be shared across layers rather than having separate experts per layer.
2. Demonstrates that cross-layer sharing improves parameter efficiency while maintaining performance.
3. Sparser Top-k selection further reduces compute by routing to fewer experts without loss.

## Routing / Gating Mechanism
- Employs a sparse gating mechanism where each layer's router selects top-k experts from a pool shared across layers.
- Cross-layer weight sharing reduces the number of expert parameters needed.
- Routing decisions are per token and per layer.

## Relevance to Thesis
- Demonstrates parameter-sharing across layers for MoE adapters — potentially relevant for constrained environments in P2P setups.
- Cross-layer routing could inspire how adapter modules are shared across peers.

## Limitations / Gaps
- Evaluation only on encoder-only and relatively small LLMs (BERT and GPT-2 families), leaving scaling behaviour in larger LMs underexplored.
- Shared expert pool may cause negative interference between layers/tasks.