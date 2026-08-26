## Meta
- **Citation:** Ben Zaken, E., Sabri, H., Mehta, A., & Belinkov, Y. (2022). BitFit: Simple Parameter-efficient Fine-tuning for Transformer and Beyond. *ACL*.
- **Venue:** ACL 2022
- **Tags:** BitFit, Bias Tuning, PEFT, Simple Fine-tuning, BERT

## Key Findings
1. BitFit fine-tunes only the bias parameters of a transformer model (k_b + b_b, k_a + b_a in attention layers) while freezing all other weights.
2. Only ~2% of total model parameters are needed for fine-tuning across a wide variety of NLP tasks, matching full fine-tuning performance.
3. Works well for BERT-style and GPT-style model base architectures.
4. Bias-tuning requires no additional model modules — extremely simple to implement in practice.
5. BitFit matches or approaches full fine-tuning on tasks like GLUE, with up to 1000x fewer trainable parameters for BERT-large.

## Relevance to Thesis (Specifically Mentioned Thesis Gap: §4.3 Bias Tuning)
- Extremely relevant: bias tuning is the cheapest "adapter" — just sharing 2% of a model's bias vectors.
- Ideal for peer-to-peer marketplace: transmission cost is minimal (few MB per adapter peer-to-peer exchange).
- Demonstrates that not all modules need updating — only bias parameters crucial for domain adaptation vs. full fine-tuning.

## Key Metrics / Results
- BitFit trains 0.08M–0.1M parameters out of 110M (BERT-base) → 0.1%.
- 1000x fewer trained params compared to full model fine-tune for BERT-large.
- GLUE scores comparable to full fine-tuning.

## Limitations / Gaps
- Capacity limited: bias-only adaptation cannot capture complex cross-task differences.
- Only evaluated on encoder and base LMs — not large-scale generative LMs.
- Small capacity suggests unsuitability for cross-domain transfer on large-scale NLP tasks.

## Relevance to Thesis Sections
- §4.3 Bias Tuning
- §4.5.2 BitFit