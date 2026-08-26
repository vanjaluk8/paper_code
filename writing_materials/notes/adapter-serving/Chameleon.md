## Meta
- **Citation:** Chameleon: Adaptive Caching and Scheduling for Many-Adapter LLM Inference Environments (2025)
- **Venue:** IEEE INFOCOM 2025
- **Tags:** `adapter-serving` `caching` `scheduling` `many-adapters`
- **Thesis sections:** §5.x

## Key Findings
1. Chameleon proposes an adaptive caching and scheduling system for many-adapter inference environments.
2. Introduces a "manifold-based adapter similarity metric" to cluster adapters by function/task, rather than just rank/memory.
3. Uses reinforcement learning to predict which adapters to cache based on request patterns.
4. Achieves up to 1.5x throughput improvement compared to standard LRU-based caching only.
5. Adapters are not just different tasks but similar tasks can be merged in batch — enhances efficiency.

## Relevance to Thesis
- Chameleon's adapter similarity metric for clustering adapters by task is promising for P2P — could be used for grouping similar adapters for caching on the same peer.
- The RL-based adapter prefetching is relevant to a P2P marketplace where which adapters to pre-fetch from which peer.
- Adapter caching policies (warm caches) are highly relevant for P2P: which adapters should a peer pre-fetch from the broader network?

## Limitations / Gaps
- All serving orchestration is centralized — P2P discovery not considered.
- Adapter similarity metric is for local caching — network load not modeled.
- Not addressing out-of-building or internet retrieval (fetch from a remote datacenter).
- Not addressing decentralized adapter discovery or marketplace dimension.
- Does not eliminate the need for a central orchestrator to synchronize caching decisions.