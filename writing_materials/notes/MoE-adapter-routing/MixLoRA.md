## Meta
- **Citation:** Wang et al. (2024) MixLoRA: Enhancing Large Language Models Fine-Tuning with LoRA Mixtures
- **Venue:** ArXiv preprint (April 2024)
- **Tags:** `MoE-routing` `LoRA` `mixture-of-experts`
- **Thesis sections:** §7.x (MoE routing)

## Key Findings
1. MixLoRA augments the MoE structure by injecting both LoRA and a lightweight gating network into transformer layers while keeping the backbone frozen.
2. Each transformer layer hosts its own set of LoRA experts + a router — mixed across queries.
3. Uses a contrastive regularisation between experts to encourage specialisation and reduce redundancy.

## Routing / Gating Mechanism
- MixLoRA uses a soft routing method where the gating layer computes weighted averages over experts rather than strict top-k selection.
- Gradients to the router flow continuously, allowing more stable training.
- Contrastive clustering of experts for diverse expertise across different attention heads.

## Relevance to Thesis
- Provides a method for multi-expert composition via learnable mixing weights.
- Relevant for combining adapters from different sources in a P2P system.

## Limitations / Gaps
- All experts reside on same device — no protocol for distributing experts across the network.
- Soft mixing means all experts are always used to some degree; this may not be efficient for P2P contexts.