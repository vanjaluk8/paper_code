## Meta
- **Citation:** Zhang et al. (2025) When MoE Meets LLMs: Parameter Efficient Fine-tuning for Multi-task Medical Applications
- **Venue:** ACM (2024)
- **Tags:** `MoE-routing` `multi-task` `fine-tuning` `LoRA` `MoE` `medical-NLP`
- **Thesis sections:** §7.x (MoE routing)

## Key Findings
1. Applies an MoE-LoRA setup to the medical domain where different medical tasks (e.g., named entity recognition, question answering) are served by shared + expert LoRA modules.
2. Achieves multi-task medical NLP performance superior to per-task fine-tuning at a fraction of the parameter count.
3. Router uses both task ID (if known) and input token embeddings to allocate experts — partially task-aware, partially input-aware.

## Routing / Gating Mechanism
- Employs a transformer-based router that combines global (task-based) and local (token-based) routing scores.
- Top-2 experts selected per layer per token.
- Expert capacity is capped to ensure latency remains low.

## Relevance to Thesis
- Demonstrates domain-specific MoE routing applicable to multi-task medical NLP, which is relatable to P2P adapter composition for different domains in a network.
- Suggests how peer adapters for diverse domains can be routed.

## Limitations / Gaps
- Requires pre-defined tasks and a central model update process.
- Constructed for the medical domain — generalisation to broader tasks not evaluated.
- Not distributed or P2P — central training and inference only.