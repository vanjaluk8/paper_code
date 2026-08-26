## Meta
- **Citation:** Kortoci, P., et al. (2024). An Overview of Autonomous Connection Establishment Methods in Peer-to-Peer Deep Learning. *IEEE Access*.
- **Venue:** IEEE Access
- **Tags:** P2P Deep Learning, Connection Establishment, NAT Traversal, Network Protocols
- **Thesis sections:** §5.2 P2P Network Overlay, §6.3 Peer Discovery

## Key Findings
1. Comprehensive survey of P2P connection methods for distributed deep learning.
2. Surveys overlay network types: structured DHT-based vs unstructured flooding.
3. NAT traversal techniques: STUN, TURN, ICE relay within P2P-DL.
4. Communication protocols' effect on training convergence time.
5. Addresses bootstrapping problem: how new peers find initial contacts.
6. NAT hole punching power law benefits projects built on DHT.

## Relevance to Thesis
- Directly surveys methods for building P2P network for distributed deep learning — the foundational networking layer for the adapter marketplace.
- NAT traversal and hole punching are essential for actual P2P adapter exchange between peers behind NATs.
- Bootstrapping protocols — essential for new peers entering marketplace.
- Categorizes trade-offs between structured (DHT) and unstructured (gossip) P2P orchestrations.

## Limitations / Gaps
- Survey was published early 2024 — recent developments in P2P LLM serving (e.g., Petals, HMI) not included.
- No deep analysis of adapter transfer protocol implications.
- Focuses on existing testbeds rather than theory.