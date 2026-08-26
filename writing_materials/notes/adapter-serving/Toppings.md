## Meta
- **Citation:** Toppings: CPU-Assisted, Rank-Aware Adapter Serving for LLM Inference (2025)
- **Venue:** arXiv 2025 (Ma et al.)
- **Tags:** `adapter-serving` `lora` `cpu-offloading` `rank-aware`
- **Thesis sections:** §5.x

## Key Findings
1. Toppings proposes a CPU-assisted serving system that jointly schedules all adapter computations across CPU and GPU resources.
2. Exploits the structure of LoRA: the LoRA adapter matrices are small and can be efficiently computed on the CPU to avoid memory overhead on the GPU.
3. Achieves an average throughput gain of 2.3x compared to baseline (GPU-only). Outperforms CaraServe in throughput by having better CPU/GPU compute overlap.
4. The key insight: LoRA adapter (A/B) matrices are small — they do not need full GPU memory. The base model (large) uses GPU compute, but the adapters can be computed on the CPU without affecting throughput.
5. Introduces a "heads-up display" for adaptive task assignment: GPU tasks vs CPU tasks.

## Relevance to Thesis
- Toppings extends the CaraServe idea: heterogenous compute paradigms for adapter serving: different devices (CPU vs GPU) serve different parts of the lifecycle.
- Important for a P2P marketplace: peers can play "specialty" roles — some peers use their CPUs for cheap adapter compute, others provide high-performance GPU compute for base models.
- The CPU-side compute offload suggests that weaker peers (laptops, Raspberry Pis) could contribute by computing lighter adapter operations while stronger peers handle base models.
- The "heads-up display" task assignment generalizes to a marketplace: role-based marketplace: "are you providing adapter compute, base model, or both?"

## Limitations / Gaps
- Assumes CPU and GPU are in the same box — not applicable across a network full of different nodes.
- CPU-batch loading creates an assumption of zero-latency interconnect: unrealistic in P2P.
- CPU compute is cheap but requires fast network interconnect for efficient direct memory transfer.
- No distributed/adapter sharing/marketplace concept — everything in single box.
- Not addressing P2P adapter retrieval or storage allocation cost.
- Limited number of adapters evaluated per second (<=100 concurrent).