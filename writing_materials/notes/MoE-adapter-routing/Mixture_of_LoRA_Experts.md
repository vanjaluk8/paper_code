## Meta
- **Citation:** Yang et al. (2024) Mixture of LoRA Experts for Multi-task Learning
- **Venue:** ArXiv preprint (April 2024)
- **Tags:** `MoE-routing` `LoRA` `multi-task`
- **Thesis sections:** §7.x (MoE routing)

## Key Findings
1. The work proposes a mixture of LoRA experts for multi-task learning, where each expert is a distinct LoRA weight set combined through routing.
2. Demonstrates that the composition of specialised LoRA modules yields better generalisation across tasks than monolithic training.
3. The router learns per-task routing probabilities to select relevant experts at inference.

## Routing / Gating Mechanism
- A router takes the input embedding and produces a weighted sum of LoRA expert outputs.
- Can be either soft routing (weighted average) or hard routing (top-k selection).
- Routing decisions depend on input task or token.

## Relevance to Thesis
- The ability to select per-instance expert composition is useful for predicting adapter quality across the P2P network.
- How task assignment is integrated into expert routing informs P2P discovery design.

## Limitations / Gaps
- Downstream task defined fixed; assumes known tasks before deployment.
- Router and experts need centralised training — adaptation to new tasks is not straightforward.