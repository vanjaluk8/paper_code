## Meta
- **Citation:** FlashServe: Cost-Efficient Serverless Inference Scheduling for Large Language Models via Tiered Memory Management and Predictive Autoscaling (2025)
- **Venue:** ACM SIGMETRICS 2025
- **Tags:** `adapter-serving` `serverless` `autoscaling` `tiered-memory`
- **Thesis sections:** §5.x

## Key Findings
1. FlashServe addresses the problem of serverless LLM inference with adaptive autoscaling of serverless resources.
2. Introduces a tiered memory management system to decide what is stored in GPU, CPU, and local SSD for cost-efficient serving.
3. Uses an autoscaling orchestration that predicts and pre-allocates GPU slots to minimize cold start.
4. Reduces serving latency by 2x compared to standard serverless (AWS Lambda-style) scaling.
5. Proposes a "predictive autoscaler" that uses past request patterns to forecast GPU needs.

## Relevance to Thesis
- FlashServe's tiered memory (GPU-CPU-SSD) could be extended to P2P:
  - GPU = active adapters
  - CPU = adapters being served locally
  - SSD = adapters cached from other peers (local device persistent storage)
  - Remote = adapters stored on remote peers (over network)
- The autoscaling prediction could be adapted for marketplace "demand prediction" — which adapters will be requested next from which peers.
- Serving multiple adapters across serverless resources relates to P2P service chain provisioning: how peers serve adapters to each other based on task loads.

## Limitations / Gaps
- Assumes all adapters pre-loaded on the same serverless infrastructure — central provider manages resources.
- Predictive autoscaling limited to a single region's resources.
- No decentralized equivalent exists for P2P — does the marketplace need its own autoscaling?
- Not addressing P2P distribution of adapters (between autonomous micropools).
- No discovery layer needed — the orchestrator knows every adapter.