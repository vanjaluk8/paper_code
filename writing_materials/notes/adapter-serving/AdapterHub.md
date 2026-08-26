## Meta
- **Citation:** AdapterHub: A Framework for Adapting Transformers (Pfeiffer et al., 2020)
- **Venue:** arXiv 2020
- **Tags:** `adapter-sharing` `adapter-hub` `centralized`
- **Thesis sections:** §5.x

## Key Findings
1. Introduces AdapterHub, a centralized repository for sharing pre-trained adapter modules for transformer models.
2. Provides a unified framework (adapter-transformers) for adding adapters to Hugging Face Transformers models.
3. Proposes adapter composition and stacking as primitive operations enabling multi-task inference.
4. Demonstrates that adapters can be downloaded and injected into a base model at inference time without retraining the base model.
5. The hub serves as a central store: users upload adapters and others download them — discovery is centralized via the Hugging Face Hub as the backend.

## Relevance to Thesis
- Foundationally relevant: AdapterHub is arguably the most direct predecessor of a P2P adapter marketplace. It establishes the concept of _discoverable, shareable adapters_ that can be plugged into a frozen base model at runtime.
- The work represents the _centralized_ paradigm: a single server hosts all adapters; clients download adapters from this central server.
- The idea of adapter composition (adapterFusion, stacking) is directly carried forward into a P2P context in the proposed thesis — where peers both consume and contribute adapters.
- Shows there is a community demand for adapter sharing — thousands of adapter downloads, hundreds of adapter uploads — validating the use case.

## Limitations / Gaps
- **Centralization is the main limitation:** all adapters are hosted on the Hugging Face Hub. There is no P2P component at all.
- No bandwidth/latency model for adapter transfer (since transfers are always from a centralized server).
- Lacks sorting/ranking/trust mechanisms for discovered adapters — which a decentralized version would need.
- Adapter versions are not tracked explicitly — discoverability is name-based on the Hugging Face Hub.
- No support for fragmentation-aware placement of adapters across GPUs — that came later in works like Punica/S-LoRA.
- Does not consider a decentralized discovery layer (DHT, Kademlia, etc.) which a P2P marketplace would require.