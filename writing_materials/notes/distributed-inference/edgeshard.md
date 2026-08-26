## Meta
- **Citation:** Xu, M., et al. (2024). EdgeShard: Efficient LLM Inference via Collaborative Edge Computing. *IEEE IoT Journal*.
- **Venue:** IEEE IoT Journal
- **Tags:** LLM Inference, Edge Computing, Collaborative Inference, Model Sharding
- **Thesis sections:** §7.2 Edge Computing, §3.2 Distributed Inference, §5.3 Collaboration

## Key Findings
1. EdgeShard: collaborative LLM inference on edge devices through model sharding: each device hosts a portion of the LLM.
2. Sharding dynamic on demand: devices can selectively contribute their shard for joint multi-layer inference.
3. Optimization: least-recently used shard unloading from slower devices to conserve memory.
4. Evaluated on up to 8 Raspberry Pi / Jetson boards running a 13B-parameter LLM.
5. Achieves up to 70% reduction in memory.

## Relevance to Thesis
- Layer-level sharding across edge devices directly relevant if the architecture consists of shared-layer sharding across devices hosting different blocks.
- Dynamic shard allocation for demand-based execution can be adapted for adapter loading.
- Edge-level cooperative approach is P2P by nature.

## Limitations / Gaps
- Pre-defined sharding points fixed for a given model; no flexible selection across adapters for different tasks.
- Works only with homogeneous device types (only ARM-based edge devices).
- Requires controlled lab environment for tests; no real wireless network.