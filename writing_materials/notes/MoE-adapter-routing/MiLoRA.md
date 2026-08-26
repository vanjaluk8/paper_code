## Meta
- **Citation:** Zhang et al. (2024) MiLoRA: Efficient Mixture of Low-Rank Adaptation for Large Language Models
- **Venue:** ArXiv preprint (October 2024)
- **Tags:** `MoE-routing` `LoRA` `multi-task` `adapter-composition`
- **Thesis sections:** §7.x (MoE routing)

## Key Findings
1. MiLoRA proposes a multiple LoRA expert setup per transformer layer. Experts are small and can be swapped at inference.
2. The router adaptively selects the best LoRA combination for each input, inscreasing performance on multiple tasks simultaneously.
3. Uses a regularisation penalty to maintain expert diversity.

## Routing / Gating Mechanism
- Each token is routed to one expert (Top-1) via a lightweight gating network.
- Router is trained jointly with the model via backpropagation through the gating function.
- Diversity is encouraged through a penalty term in the loss function.

## Relevance to Thesis
- Very relevant to adapter selection and composition — single task fine-tuning with multiple small expert modules.
- Top-1 routing reduces inference overhead compared to dense MoE, which may be beneficial in resource-constrained P2P.

## Limitations / Gaps
- Load-balancing loss across experts may introduce training instability.
- Router centralised and bound to the model — no distribution across peers.