## Meta
- **Citation:** Dettmers, T., et al. (2023). QLoRA: Efficient Finetuning of Quantized LLMs. *NeurIPS*.
- **Venue:** NeurIPS
- **Tags:** QLoRA, Quantization, LoRA, PEFT, Memory Efficiency
- **Thesis sections:** §4.2 LoRA, §4.6.3 Quantized PEFT, §3.2 Memory Efficiency

## Key Findings
1. QLoRA combines 4-bit NormalFloat quantization + LoRA fine-tuning without any degradation.
2. Memory: fine-tuning 65B model with QLoRA uses single 48GB GPU (vs. 8x GPUs without QLoRA)
3. Quantization of base model is brand new NormalFloat format; LoRA is an adaptor that stays full-precision (FP16) during training.
4. Key innovations: NF4 quantisation (4-bit normal float), double quantization, paged optimisers.
5. Base model is stored in 4-bit; LoRA adaptor weights stay in FP16. Using both NF4 base + LoRA equals total memory = 4-bit base + 0.3x per rank adaptors per task.
6. Results: QLoRA achieves same performance as full fine-tune on benchmark evaluations: Guanaco family matches Chat variants at 96% of ChatGPT.

## Relevance to Thesis
- Directly applicable: adapter-sharing across QLoRA peers — each peer maintains its trained 4-bit base model, downloads lightweight adapters from the marketplace.
- Combined memory footprint: 4-bit base + LoRA (16-bit) = total task increment is small (adapter only).
- Demonstrates that switching adapters on a quantized base model is possible without re-loading the base — just download 2 small A/B matrices.

## Limitations / Gaps
- LoRA layers stay FP16 — memory saving is all in base model quantization.
- Quantized base model (NF4) cannot be fine-tuned — you can tune the LoRA but not the base.
- Single-quant approach for base; any adapter added to the mixture must be LoRA quant rate.
- Only 7B/13B/65B aligned PLM explored — not the largest current models (e.g. 70B+).