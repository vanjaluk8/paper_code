## Meta
- **Citation:** Serving Heterogeneous LoRA Adapters in Distributed LLM Inference with Different Quantized Configurations
- **Venue:** arXiv 2025
- **Tags:** `adapter-serving` `lora` `distributed` `quantization`
- **Thesis sections:** §5.x

## Key Findings
1. Addresses the problem of serving LoRA adapters distributed across multiple GPUs with different quantization configurations.
2. Proposes a method to partition adapters across heterogeneous GPUs based on adapter size and GPU memory capacity.
3. Handles weight quantization to FP8/FP4/INT8 while maintaining accuracy — different GPUs may use different quantization levels.
4. Introduces a placement algorithm that minimizes inter-GPU communication when adapters span multiple GPUs.
5. Supports "adapter migration" across GPUs based on real-time request distribution.

## Relevance to Thesis
- Relevant to P2P deployment diversity: in a P2P marketplace, peers will have heterogeneous hardware (different GPU memory, different quantized base models).
- Adapter migration is the key concept for item granularity in the P2P marketplace: "search across nodes for the right adapter" and "move (locate) it if necessary".
- The cross-GPU adapter placement algorithm generalizes to a P2P placement algorithm across independent peer nodes.
- The decentralized aspect of serving adapters is relevant to how Peers could serve as "heterogeneous compute capacity" for the marketplace.

## Limitations / Gaps
- All GPUs are assumed to be controlled by a single orchestrator (e.g., within same organization).
- Inter-node communication costs for adapter fetching over a network (outside datacenter) are not modeled.
- Adapter discovery is not addressed — all adapters are pre-known by the orchestrator.
- No trust or authentication model for adapter sharing.
- Does not address real-time adapter serving across nodes with high network latency.