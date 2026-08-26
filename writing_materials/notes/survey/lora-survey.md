## Meta
- **Citation:** Wang, Z., et al. (2024). A survey on LoRA of large language models. *Frontiers of Computer Science*.
- **Venue:** Frontiers of Computer Science
- **Tags:** LoRA Survey, LLM, Parameter-Efficient Fine-tuning
- **Thesis sections:** §4.2 LoRA, §4.6 Multi-task Integration

## Key Findings
1. Comprehensive LoRA modifications: LoRA-Vec, MOELoRA, LoRA-FA, AdaLoRA, Delta-LoRA.
2. Variants: specific shapes (LoRA (192:19); LoRA vs others integration)
3. Dynamic low-rank adaptation improvements (DyLoRA, Incretera) train alone, AdaLoRA adapts mid-training.
4. Multi-task LoRA: integrate multiple LoRAs into single one via: sum, batch, product, task-structure.
5. Mention specialized hardware/software optimization.

## Relevance to Thesis
- Covers all recent LoRA variants as candidates for the adapter marketplace.
- Multi-task LoRA integration strategies of discussion: product adapter soup — directly concerning the merger direction operation for market route.

## Limitations / Gaps
- Does not cover: P2P adapter deployment, adaptation across boundaries of P2P sharing, latency/bang with adapter selection.
- Very recent publications only (2023-2024 main) — LoRA variants for training — not serving.
- No system-level cost evaluation for frequent adapter switching.