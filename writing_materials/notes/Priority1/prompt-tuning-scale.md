## Meta
- **Citation:** Lester, B., Al-Rfou, R., & Constant, N. (2021). The Power of Scale for Parameter-Efficient Prompt Tuning. *EMNLP*.
- **Venue:** EMNLP 2021
- **Tags:** Prompt Tuning, PEFT, Scaling, LLMs, Soft Prompt, Virtual Token

## Key Findings
1. Prompt tuning trains a single "soft prompt" (learnable embedding prepended to the input) — no base model fine-tuning needed.
2. Matches GPT-3 full fine-tuning quality at large model scale (>10B parameters).
3. "Prompt ensembling": multiple prompts can be used concurrently to produce predictions; ensemble voting improves robustness over a single prompt.
4. Prompt length flexibility: 5 to 150 tokens of embedding, typically 5–150 trainable tokens.
5. Soft prompt initialized at "T5 engineer" initialization (embedding of the empty prompt string) yields best performance.

## Relevance to Thesis (Specifically Mentioned Thesis Gap: §4.4.2 Prompt Tuning)
- Prompt tuning is among the lightest PEFT methods — only 5–100 trainable tokens per task/virtual token.
- Immediate relevance to marketplace: each task gets its soft prompt (adapter), a few tens of embeddings ~5-20kB per task.
- Scale-dependent behaviour: as models grow, prompt tuning catches up — this aligns with thesis Chapter 5 narrative: large frozen model + small pluggable prompts.

## Key Metrics / Results
- Soft prompt: 5,120 trainable parameters for T5-Large (5120 tokens) up to 102,400 for T5-11B (many tasks).
- Up to 0.1–0.5% of full fine-tune parameters.
- Ensemble of 20 prompts outperforms single full fine-tune on SuperGLUE.

## Limitations / Gaps
- Only evaluated on T5 encoder-decoder architecture.
- Prompt performance depends heavily on scale — below 1B parameters, quality lags behind full tuning.
- Requires model warm-start from fine-tuning for stable training.
- Prompt embedding matrix dimension equals model-embedding size (1024 for T5-large) — not as transmit-efficient as LoRA.

## Relevance to Thesis Sections
- §4.4 Prompt Tuning
- §5.1 PEFT for Generation