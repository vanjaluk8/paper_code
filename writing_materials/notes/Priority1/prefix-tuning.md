## Meta
- **Citation:** Li, X. L. & Liang, P. (2021). Prefix-Tuning: Optimizing Continuous Prompts for Generation. *ACL*.
- **Venue:** ACL 2021
- **Tags:** Prefix-Tuning, Continuous Prompts, PEFT, Conditional Generation, Adapter, Soft Prompt

## Key Findings
1. Prefix-tuning prepends learnable continuous vectors ("prefix") to transformer layer inputs, conditioning generation without fine-tuning the base LM.
2. Matches full fine-tuning performance in high-data regimes and outperforms it in low-data settings (<1K examples).
3. Applied to BART and GPT-2; effective across table-to-text, summarization, and LM tasks.
4. Prefix parameters are generated via a small MLP, which acts as a hyper-network for more stable learning.
5. Only adds 0.1%-5% of the original model parameters depending on prefix length (20-200 tokens).
6. Enables separate per-task prefixes while keeping the base model frozen — ideal for multi-task inference.

## Relevance to Thesis (Specifically Mentioned Thesis Gap: §4.5 Adapter-Based Inference)
- Prefix-tuning demonstrates a form of "soft prompt" adapter that is independently shareable and task-specific.
- Each prefix is cheap (20-200 tokens of embedding size) and independent — maps directly to marketplace: each seller provides their prefix (adapter) for their task.
- Multi-prefix composition is possible: combine prefix vectors from different tasks.

## Key Metrics / Results
- Prefix length: optimal at 100-200 tokens for prefix tuning.
- 0.1%-5% total parameters added.
- BART prefix: 0.17M parameters (around 200 tokens each transformer layer).

## Limitations / Gaps
- Prefix cannot be easily mixed across tasks without additional training.
- Prefix lengths longer than 200 tokens show no improvement.
- Primarily studied for autoregressive/decode transformers — BERT-like encoder- and decoder-only evaluation.
- Prefix for each layer → transmitter cost scales with number of layers.

## Relevance to Thesis Sections
- §4.4 Prefix Tuning
- §5.1 PEFT for Generation
- §4.5 Multi-task modular architectures