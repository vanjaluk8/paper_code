## Meta
- **Citation:** Compress-then-Serve: Serving Thousands of LoRA Adapters with Compression
- **Venue:** arXiv 2024
- **Tags:** `adapter-serving` `lora` `compression` `memory-efficiency`
- **Thesis sections:** §5.x

## Key Findings
1. Proposes compressing LoRA adapter weights using quantization and pruning to fit more adapters into GPU memory.
2. Achieves 4x-8x compression of LoRA adapters with minimal accuracy drop (less than 1%).
3. Integrates compression-aware scheduling that matches compressed and uncompressed adapters efficiently.
4. Evaluated on RoBERTa and LLaMA models showing throughput improvements of 2-3x depending on adapter sparsity.
5. Demonstrates that compression-aware scheduling reduces memory fragmentation when adapters have varying sizes.

## Relevance to Thesis
- Highly relevant for P2P adapter transfer: compression reduces the amount of data that needs to be transferred between peers.
- The 4x-8x compression ratio means a peer could download a compressed adapter in 1/4 to 1/8 of the time of a full adapter, significantly reducing P2P transfer latency.
- Compression techniques (pruning + quantization) could be applied at P2P storage layer: store compressed, serve decompressed.
- Integration of this into a P2P marketplace could be a key contribution.

## Limitations / Gaps
- Compression/decompression overhead is not modeled in networking scenarios — only in GPU memory scenarios.
- Assumes all compressed adapters are stored centrally — no P2P distribution challenges.
- The decompression latency (when adapters are needed) could become significant in a P2P setting where network latency already exists.
- Uncertainty about task-specific accuracy drop after compression on diverse adapter types (beyond the few evaluated) remains unclear.