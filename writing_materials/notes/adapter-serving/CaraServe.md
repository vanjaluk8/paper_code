## Meta
- **Citation:** CaraServe: CPU-Assisted and Rank-Aware LoRA Serving for Generic Adapters (2024)
- **Venue:** arXiv 2024 (ASPLOS 2025)
- **Tags:** `adapter-serving` `lora` `cpu-offloading` `rank-aware`
- **Thesis sections:** §5.x

## Key Findings
1. CaraServe improves on S-LoRA by using CPU cores to compute LoRA adapter computations instead of offloading weights to GPU memory.
2. Proposes rank-aware offloading: adapters with different LoRA ranks are offloaded to CPU differently — high-rank adapters get more GPU time, low-rank adapters can be computed on CPU.
3. Achieves higher throughput than S-LoRA by overlapping GPU base model computation with CPU adapter computation.
4. The CPU target is not just used as slow memory — CPUs are used for useful computation on LoRA weights.
5. Key insight: LoRA adapter computations are embarrassingly parallel matrices small enough to be efficiently computed on a CPU while GPU handles the larger base model.

## Relevance to Thesis
- Most relevant among the "adapter serving" family because of its rank-aware approach: adapters of different ranks have different compute and memory profiles.
- The idea of heterogeneously treating adapters (high rank = GPU, low rank = CPU) generalizes to P2P: heavy adapters could be served by strong peers, light adapters by weaker peers.
- CaraServe's model of asynchronous, non-blocking adapter computation is an enabler for a P2P adapter marketplace.

## Limitations / Gaps
- Assumes adapters are stored on the CPU node — not retrieved over the network.
- Still CPU-GPU architecture within a single node — no P2P adapter transfer.
- Does not model network transfer latencies.
- Not addressing the discovery; all adapters are known a priori.