## Meta
- **Citation:** SLoRA: Scalable Serving of Thousands of LoRA Adapters (2024)
- **Venue:** arXiv 2024
- **Tags:** `adapter-serving` `lora` `scheduling` `memory-management`
- **Thesis sections:** §5.x

## Key Findings
1. SLoRA proposes an improved version of S-LoRA with more efficient kernel fusion for LoRA adapters.
2. Unifies the compute and memory allocation for different LoRA adapters through a single virtualized memory space.
3. Achieves higher throughput than S-LoRA by merging similar-adapter batches into a single kernel.
4. Introduces a "single-batch merge" for homogeneous ranks and sizes of adapters.
5. Evaluated up to 8000 adapters — showing that a single model can serve up to 8000 adapters simultaneously.

## Relevance to Thesis
- SLoRA's core idea of merging adapters with the same rank and applying them to the base model in a single fused kernel operation is interesting for a P2P marketplace: adapters with the same metrics (rank, intermediate dimension) could be combined for batch deployment on the same peer.
- The "virtual memory pool" idea across adapter types could generalize to a P2P multi-node cache if peers can share memory caches.
- SLoRA's clustering of adapter types suggests that P2P marketplace could serve similar adapters.

## Limitations / Gaps
- Singular, centralized serving system — no P2P interaction.
- Performance evaluation shows results only on highly homogeneous adapter sizes (same rank/type) — real-world more diverse.
- Does not propose protocols for finding adapters in P2P — assumes central API for accessing adapters.
- No method for trust or quality evaluation of adapters.
- Not addressing version drift or adapter update propagation over the network.