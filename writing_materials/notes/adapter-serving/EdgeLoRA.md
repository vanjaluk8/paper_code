## Meta
- **Citation:** EdgeLoRA: An Efficient Multi-Tenant LLM Serving System on Edge Devices (2025)
- **Venue:** ACM Web Conference 2025
- **Tags:** `adapter-serving` `lora` `edge` `edge-devices`
- **Thesis sections:** §5.x, §6.x

## Key Findings
1. EdgeLoRA proposes a multi-tenant LLM serving system specifically for resource-constrained edge devices.
2. Uses adaptive compression (pruning, quantization) to fit multiple LoRA adapters on edge devices like Jetson and Raspberry Pi.
3. Achieves up to 70% memory savings compared to naive loading of all adapters.
4. Supports multiple tenants on a single edge device through time-sharing the same adapter compute resources.
5. Uses dynamic LoRA loading to switch between different tenants' adapters onboard a single edge device's GPU memory.

## Relevance to Thesis
- Directly relevant: serves the edge deployment scenario where P2P between edge devices could build networks of edge served APIs.
- EdgeLoRA's dynamic loading of adapters onto memory-constrained devices suggests that edge devices can serve adapters to others as well as use them.
- The "marketplace" aspect: edge devices could discover, fetch, and compose adapters from other edge devices.
- EdgeLoRA overlaps with cross-device adapter discovery (but its design lacks the P2P layer).

## Limitations / Gaps
- All adapters are hosted on a single cloud server — edge devices file a request to central storage, not P2P.
- No P2P node-to-node fetching.
- Adaptive compression on the edge is central-to-edge, not peer-to-edge.
- No adapter discovery — adapters are pre-defined and stored on the central server.
- Not adaptive to bandwidth fluctuations which matter in P2P.
- Trust, identity, and version tracking are left unresolved.