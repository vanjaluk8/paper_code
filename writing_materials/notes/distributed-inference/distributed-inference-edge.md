## Meta
- **Citation:** Teerapittayanon, S., McDanel, B., & Kung, H. T. (2017). Distributed Inference with Deep Learning Models across Heterogeneous Edge Devices. *INFOCOM*.
- **Venue:** IEEE INFOCOM
- **Tags:** Distributed Inference, Edge Computing, Model Splitting, Heterogeneous Devices
- **Thesis sections:** §3.2 Distributed Inference, §7.2 Edge Inference Splitting

## Key Findings
1. Model partitioned, early layers on resource-limited device, deeper layers on cloud/edge server.
2. Asymmetric architecture: compute-intensive layers on server with stronger hardware, early layers on low-latency device to reduce transmit bandwidth.
3. Partition point determined based on network speed and computational capacity of each device.
4. Energy consumption for early edge devices roughly is split: communication and computation trade-off.
5. Various splitting points for different devices and models.

## Relevance to Thesis
- Real-distributed inference concept splitting a model across devices — directly translates to P2P adapter inference: the frozen backbone runs on one node, specific adapters on other peers.
- Edge heterogeneity: partition selection dependent on peer hardware.
- Key reference for splitting inference.

## Limitations / Gaps
- Only one single model split — no MoE or adapter selection for multiple tasks.
- Static split once selected; no dynamic adaptation to network changes.
- No support for multiple adapter selections across users.