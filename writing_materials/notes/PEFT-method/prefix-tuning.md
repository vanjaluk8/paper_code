## Meta
- **Citation:** Li, X. & Liang, P. (2021). Prefix-Tuning: Optimizing Continuous Prompts for Generation. *ACL*.
- **Venue:** ACL
- **Tags:** Prefix-Tuning, Continuous Prompts, PEFT, Conditional Generation
- **Thesis sections:** §4.4 Prefix Tuning, §5.1 PEFT for Generation

## Key Findings
1. Prefix-tuning: prepend learnable, continuous vectors (prefix) to transformer layers to condition generation without fine-tuning underlying LM.
2. Outperforms full fine-tuning in low-data regime (<1K examples) and matches full fine-tune in large data regime (all 12 tasks).
3. Can be applied to BART and GPT-2 style models.
4. Prefix technique: train a small MLP to produce prefix parameters for more stable learning.
5. Only adds 0.1% - 5% of original model size depending on prefix length.
6. Enables separate per-task prefixes while reusing frozen base model.

## Relevance to Thesis
- Showcases a form of "soft prompt" adapter that is independently shareable and task-specific.
- Directly relevant for adapter marketplace: each task-specific prefix is cheap: 20-200 tokens.
- The separate per-task independent prefix concept maps well to marketplace: each seller provides their prefix (adapter) for their task.

## Limitations / Gaps
- Prefix cannot be easily mixed across tasks without additional training.
- Prefix lengths scale with transformer layers optimally: prefix longer than 100 tokens doesn't show improvement.
- "Conditional generation" only for autoregressive LM; discriminator tasks not evaluated.