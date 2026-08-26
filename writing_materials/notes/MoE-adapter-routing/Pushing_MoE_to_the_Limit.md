## Meta
- **Citation:** Li et al. (2023) Pushing Mixture of Experts to the Limit: Extremely Parameter Efficient Fine-Tuning
- **Venue:** ArXiv preprint (September 2023)
- **Tags:** `MoE-routing` `parameter-efficiency` `scaling`
- **Thesis sections:** §7.x (MoE routing)

## Key Findings
1. Shows that MoE-based PEFT can operate at extremely small parameter budgets when using sparse gating with fine-grained expert definition.
2. Proposes more aggressive expert pruning and routing strategies that maintain performance at very low parameter counts.
3. Demonstrates that dense-to-sparse expert allocation (freezing base + tiny expert pool) achieves strong performance.

## Routing / Gating Mechanism
- Top-1 or top-2 experts per token are selected by a router.
- Expert capacity is constrained so that load across experts stays balanced.
- Routing choice penalises expert imbalance via load-balancing loss.

## Relevance to Thesis
- Highly relevant to token-level adapter selection across the P2P network — load balancing and sparse selection are critical for P2P performance.
- The extreme parameter efficiency is key for heterogeneous edge systems.

## Limitations / Gaps
- Routing overhead scales with the number of experts.
- Focused on single-device routing — no P2P or decentralised routing considerations.