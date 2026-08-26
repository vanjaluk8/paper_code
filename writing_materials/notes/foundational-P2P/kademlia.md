## Meta
- **Citation:** Maymounkov, P., & Mazieres, D. (2002). Kademlia: A Peer-to-Peer Information System Based on the XOR Metric. *IPTPS*.
- **Venue:** IPTPS
- **Tags:** DHT, P2P, Kademlia, XOR Distance, Decentralized Hash Table
- **Thesis sections:** §5.1 Kademlia, §6.2 DHT for Adapter Discovery

## Key Findings
1. Kademlia DHT: nodes organize into Kademlia tree, with key-value maps across P2P network.
2. XOR metric: measure distance between two nodes (160-bit node IDs), facilitating near-optimal lookup messages O(log N).
3. Robust lookup in probabilistic O(log N) messages even when half the nodes fail.
4. Self-stabilizing: nodes join and leave without manual management.

## Relevance to Thesis
- The most popular DHT for decentralized service discovery — template for adapter hub: adapter key (task description) → value (peer hosting specific adapter).
- XOR lookup can discover adapter peers in O(log N) hops.
- Churn resilience for adapter queries when many nodes temporary leave.
- Demonstrated lookup speed and correctness for semi-static network.

## Limitations / Gaps
- Requires node IDs and IP addresses — no content retrieval by similarity.
- Efficient only when key is known exactly — not a search system.
- Not designed for large payload (adapter weights) distribution across P2P nodes.