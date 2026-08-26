## Meta
- **Citation:** Dettmers, T., Pagnoni, A., Holtzman, A., & Zettlemoyer, L. (2023). QLoRA: Efficient Finetuning of Quantized LLMs. *NeurIPS*.
- **Venue:** NeurIPS 2023
- **Tags:** QLoRA, Quantization, LoRA, PEFT, Memory Efficiency, NF4

## Key Findings
1. QLoRA combines 4-bit NormalFloat quantization with LoRA fine-tuning without degradation in model quality.
2. Memory reduction: fine-tuning a 65B model uses single 48GB GPU (vs. 780GB with full fine-tuning).
3. Key innovations: NF4 quantisation (4-bit NormalFloat), double quantization (quantize quantization constants), paged optimizers (for GPU memory spiking).
4. Base model stored in 4-bit NF4; LoRA adaptor weights stay in FP16 during training.
5. Guanaco family (QLoRA-finetuned models) matches ChatGPT performance at 96% on Vicuna benchmark.
6. Double quantization halves memory overhead of the quantization constants.

## Relevance to Thesis (Specifically Mentioned Thesis Gap: §4.6.3 Quantized PEFT)
- Highly relevant for decentralized adapter-based systems: each peer can maintain a 4-bit quantized base model and download lightweight LoRA adapters from the marketplace.
- Combined memory footprint tiny: 4-bit base + small LoRA adapters from marketplace → very small deployment overhead.
- Implicit contribution: switching adapters on a quantized base is cheap — just download small A/B matrices as adapters.

## Key Metrics / Results
- 4-bit NormalFloat (NF4) base model + FP16 LoRA: 34% reduction in total memory compared to FP16 base + LoRA.
- 65B model fine-tuned with 4-bit NF4 base + LoRA on single 48GB GPU (vs. 780GB with full fine-tune and >300GB with FP16 base + LoRA alone).
- Guanaco 65B achieves 99.3% of ChatGPT's performance on Vicuna benchmark.

## Limitations / Gaps
- LoRA layers remain FP16 → memory saving is entirely in base model quantization, not in adapter.
- Quantized NF4 base model cannot be fine-tuned directly; only the LoRA adapters can be updated.
- Limited to LoRA-style adapters; other PEFT methods not explored.
- Only studied at 7B/13B/33B/65B scales.