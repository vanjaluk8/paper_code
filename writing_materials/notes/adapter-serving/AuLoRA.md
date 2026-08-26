## Meta
- **Citation:** AuLoRA: Fine-Grained Loading and Computation Orchestration for Efficient LoRA LLM Serving (ICCD 2025)
- **Venue:** IEEE ICCD 2025
- **Tags:** `adapter-serving` `lora` `scheduling` `memory-management`
- **Thesis sections:** §5.x

## Key Findings
1. Proposes AuLoRA, a fine-grained loading and computation orchestration system for multi-LoRA serving.
2. Optimizes GPU memory usage by dynamically offloading LoRA weights between GPU/CPU memory during prefill vs. decoding phases.
3. Breaks down adapter computation into sub-operations (rank k sub-vectors) for fine-grained orchestration.
4. Achieves up to 2.56x throughput improvement compared to state-of-the-art systems.
5. Implements a mixed-precision strategy: low-precision for non-critical paths and high-precision for attention layers.
6. Uses a real-time profiler to adapt batch composition for memory and computation balancing.

## Relevance to Thesis
- Relevant for its approach to adapter serving under GPU memory constraints — shows that dynamic loading/offloading of LoRA weights is feasible without major throughput loss.
- Provides insights for a distributed setting: the idea of fine-grained (sub-adapter-level) orchestration could apply to P2P adapter sharing where adapters are partially transferred.
- The mixed-precision strategy could be relevant for minimizing bandwidth requirements in P2P adapter transfer.

## Limitations / Gaps
- Assumes all adapters are stored centrally and accessible by a single serving engine — no distributed/shared-nothing scenario.
- Offloading to CPU memory assumes co-located CPU-GPU (same node) — unrealistic in P2P where transfer cost is much higher.
- Lacks evaluation of cross-host transfer latency — all experiments are single-node multi-GPU.
- No consideration of adapter discovery or versioning across a P2P network.