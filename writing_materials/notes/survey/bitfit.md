## Meta
- **Citation:** Ben-Zaken, E., Sabri, H., Mehta, A., & Belinkov, Y. (2022). BitFit: Simple Parameter-efficient Fine-tuning for Transformer and Beyond. *ACL*.
- **Venue:** ACL
- **Tags:** BitFit, Bias Tuning, PEFT, Simple Fine-tuning
- **Thesis sections:** §4.3 Bias Tuning, §4.5.2 BitFit

## Key Findings
1. Fine-tunes only bias parameters (k_b + b_b, k_a + b_a) of the model while freezing all weights.
2. Only 2% of total model parameters needed for fine-tuning across varied NLP tasks, matching full fine-tune.
3. Works well for BERT and GPT-like models.
4. Simplicity: no added module like adapter or low-rank factor, B too — 1000x fewer params than full fine-tune for BERT.

## Relevance to Thesis
- Bias tuning is an even cheaper adapter sharing: sharing 2% bias vectors costs as much as commit weight.
- Transforms bias value adaptation to share — the simplest PEFT in marketplace.

## Limitations / Gaps
- Smallest of the PEFT but capacity limited — may not suit all tasks or cross-domain transfer.
- Only evaluated on BERT/Large LMs.

The capacity of bias-only adaptation is limited; cannot capture complex task differences in large cross-task space.