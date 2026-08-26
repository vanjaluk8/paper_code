## Meta
- **Citation:** Rock: Serving Multimodal Models in Cloud with Heterogeneous-Aware Resource Orchestration for Thousands of LoRA Adapters (CLUSTER 2025)
- **Venue:** IEEE CLUSTER 2025
- **Tags:** `adapter-serving` `lora` `scheduling` `multi-modal`
- **Thesis sections:** §5.x

## Key Findings
1. Proposes Rock, a system for serving large-scale LoRA adapters for multimodal models (LLaVA) with heterogeneous-aware orchestration.
2. Introduces MTS (Multi-Tenant Scheduling) algorithm to batch co-located heterogeneous requests for improved GPU utilization.
3. Rock achieves up to 2.54x throughput improvement over S-LoRA under latency SLO constraints.
4. Uses a 3-layer orchestration: request-level, adapter-level, and GPU-level scheduling.
5. Designs custom CUDA kernels that merge adapter computations with residual streams — optimizing for heterogeneous adapter ranks.

## Relevance to Thesis
- Directly relevant to the unified adapter serving landscape. Shows that _centralized_ cloud-side orchestration can handle thousands of adapters for multimodal models.
- Demonstrates GPU-level heterogeneous co-location for capacity, but storage and retrieval of adapters is all central (cloud) — no P2P or decentralized aspect.
- The CUDA kernel optimization (efficient handling of different LoRA ranks) is a generally applicable insight for adapter runtime optimization.

## Limitations / Gaps
- Fully centralized orchestration: all adapters and the base model are in the same cloud GPU cluster. No P2P or decentralized adapter sharing.
- Lacks any discovery or sharing mechanism for adapters across different deployment environments.
- Evaluated with only LLaVA models on a single cluster; generalization to other architectures is unverified.
- Does not address adapter storage or transfer — assumes all adapters are pre-loaded into the same GPU cluster memory.