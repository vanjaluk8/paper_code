## Meta
- **Citation:** Rajbhandari, S., et al. (2022). DeepSpeed-MoE: Advancing Mixture-of-Experts Inference and Training to Power Next-Generation AI Scale. *ICML*.
- **Venue:** ICML
- **Tags:** MoE, Large-Scale Training, Distributed Training, Inference Optimization
- **Thesis sections:** §3.2 Distributed Training, §7.1 MoE

## Key Findings
1. DeepSpeed-MoE extends DeepSpeed with MoE support including: (a) mixed-precision training, (b) dynamic expert loading, (c) hierarchical all-to-all communication grouping.
2. Pyramid-shaped MoE: varying expert capacity across layers reduces computation with minimal accuracy loss — fewer experts in early and late layers, more in middle layers.
3. Proposes PR-MoE (Pyramid-Residual-MoE) combining pyramid structure with residual connections, achieving 4.5x speedup over dense baseline with less than 0.5% accuracy loss.
4. Introduces memory-efficient inference by loading experts only when needed (demand-based), reducing peak memory.
5. Zero-bubble pipeline parallelism for MoE training and ZeRO-optimized memory.

## Relevance to Thesis
- Dynamic expert loading on demand is a direct parallel to decentralized adapter discovery — peers could load adapters based on routing decisions rather than storing all variants.
- Pyramid placement of capacity informs where to place adapter-level MoE in a distributed architecture.
- The hierarchical all-to-all communication grouping relates to the P2P overlay where adapter search happens across peer neighborhoods.

## Limitations / Gaps
- Designed for homogeneous, tightly-coupled DGX clusters with high bandwidth interconnects.
- Does not address churn, peer discovery, or NAT traversal issues inherent to P2P.
- Expert capacity is fixed per layer — P2P adapter systems need adaptive capacity based on fluctuating peer availability.