## Meta
- **Citation:** Houlsby, N., et al. (2019). Parameter-Efficient Transfer Learning for NLP. *ICML*.
- **Venue:** ICML
- **Tags:** Adapters, PEFT, Transfer Learning, Bottleneck Adapters
- **Thesis sections:** §4.1 Bottleneck Adapters, §4.5 Adapter Architecture and Training

## Key Findings
1. Introduces bottleneck adapter modules placed after each transformer sub-layer (attention and FFN).
2. Bottleneck: down-project (ff → d) then up-project (d → ff); non-linearity in the bottleneck.
3. Only 3-5% of original parameters (depending on bottleneck size) are tuned per new task.
4. Acoustic results across 26 tasks: adapters match full fine-tune accuracy while being parameter efficient.
5. Adapters for each task learned sequentially; then froze warm-start that pre-adapts only final adapter for new small tasks.

## Relevance to Thesis
- Bottleneck adapters are the primary architecture. Adapter-sharing across tasks corresponds to transmitting these compact bottleneck weight matrices.
- Bottleneck dimension d controls all task-specific capacity — similar to rank for LoRA.
- Sequential training technique (train one adapter per task, then freeze) maps directly to marketplace concept where each adapter is its own task.

## Limitations / Gaps
- Bottleneck adapters still add inference overhead (extra forward pass through adapter) — decoder for attention sublayer.
- Requires shared base model for all tasks: all participants must use the same frozen backbone.
- Adapter training must be sequential across tasks.