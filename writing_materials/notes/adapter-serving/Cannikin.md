## Meta
- **Citation:** Cannikin: No Lagger of SLO in Concurrent Multiple LoRA LLM Serving (TPDS 2025)
- **Venue:** IEEE TPDS 2025
- **Tags:** `adapter-serving` `lora` `scheduling` `slo`
- **Thesis sections:** §5.x

## Key Findings
1. Proposes Cannikin, a serving system for concurrent multi-LoRA inference that addresses the "straggler problem" — slowest adapter-batch holds up the entire SLO.
2. Introduces prefill-decoding disaggregation for LoRA adapters — separates the prefill and decode phases into distinct GPU resources.
3. Employs a fine-grained, rank-level scheduler that batches adapters by LoRA rank heterogeneity.
4. Achieves up to 1.8x throughput improvement over S-LoRA under latency SLO constraints.
5. Proposes a "mirror-augment" mirroring policy that replicates adapters across GPUs to maximize batchable request combinations.

## Relevance to Thesis
- Relevant for the single-cluster adapter serving problem — shows how rank heterogeneity among adapters (different LoRA ranks) impacts scheduling efficiency.
- The "adapter straggler" phenomenon is analogous to a potential issue in P2P adapter serving: fetching a heavyweight adapter from a slow peer could become a bottleneck.
- Cannikin's solution to adapter heterogeneity (rank-aware scheduling) could be adapted for P2P context selection.
- Suggests that adapter metadata (rank, sparsity, etc.) is important for efficient scheduling — relevant to the discovery protocol.

## Limitations / Gaps
- Fully centralized single-cluster deployment — all GPUs are in the same NVLink-connected server.
- Assumes homogeneous GPU hardware (8x A100).
- No adapter fetching latency model — all adapters already in GPU memory.
- Does not address adapter versioning or composition across heterogeneous deployments.
- Only evaluates with LLaMA-based models and simulated adapter workloads.