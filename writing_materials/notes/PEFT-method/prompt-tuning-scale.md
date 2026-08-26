## Meta
- **Citation:** Lester, B., Al-Rfou, R., & Constant, N. (2021). The Power of Scale for Parameter-Efficient Prompt Tuning. *EMNLP*.
- **Venue:** EMNLP
- **Tags:** Prompt Tuning, PEFT, Scaling, LLMs
- **Thesis sections:** §4.4 Prompt Tuning, §5.1 PEFT for Generation

## Key Findings
1. Prompt tuning: train a single "soft prompt" (learned embedding) placed at the encoder input, no fine-tuning of the model.
2. Matches GPT-3 quality at scale: as model size grows, prompt tuning catches up to full fine-tune.
3. Prompt tuning matches fine-tune quality for large models (>10B parameters) across a variety of tasks.
4. "Prompt ensembling": use multiple prompts for different examples and aggregate outputs — performs better than a single prompt.
5. Prompt length can be varied for fine-grained control over capacity: 5 tokens for small prompts, 100 tokens maximum.
6. Ablation: longer prompts help more for larger models.

## Relevance to Thesis
- Prompt tuning is the most lightweight PEFT method: only 5-100 trainable embeddings per task.
- Prompt ensemble concept directly maps to adapter marketplace: each task gets a separate prompt, multiple prompts can be mixed.
- Scale-dependent reasoning aligns with the idea of large frozen foundation combined with many pluggable adapters (prompts).

## Limitations / Gaps
- Prompt tuning only studied for encoder-decoder T5 architecture.
- Prompt-only improvement requires model-wide warm-start from fine-tuning for stable training.
- Prompt embedding matrix is not as efficient for transmission as LoRA or adapter: same dimension is model-embedding size (1024 continuous embeddings per token per layer).