## Meta
- **Citation:** Li, Y., et al. (2023). Privacy and Efficiency of Communications in Federated Split Learning. *IEEE Transactions on Big Data*.
- **Venue:** IEEE Trans. on Big Data
- **Tags:** Split Learning, Federated Learning, Privacy, Communication Efficiency
- **Thesis sections:** §3.2 Distributed Training, §7.2 Split Computing

## Key Findings
1. Split Learning distributes the model across client and server: share only activations (smashed data) between client and server, not model parameters or data.
2. Customer privacy is preserved because the server only sees intermediate smashed data (activations) from the client split layer, not raw data.
3. Proposes strategies to minimize communication overhead during split learning.
4. Demonstrates communication efficiency: up to 80% reduction in client-to-server communication compared to full gradient transfer.
5. Evaluated on vision datasets (CIFAR-10, CIFAR-100); VGG, ResNet, and Transformer architectures.

## Relevance to Thesis
- Split learning works with distribution of model activations only — can be adapted to pass adapter features from one peer to another for P2P adapter sessions.
- Communication efficiency is critical: send adapter weights and intermediate activations rather than entire model weights — aligns with PEFT adapter transmission concept.
- Privacy analysis extends to the adapter exchange scenario: peers only see adapter outputs rather than full model or raw data.

## Limitations / Gaps
- Split models are split client-side base + server-side fine-tunner — not directly extensible to arbitrarily shared adapters.
- Communication overhead still high for iterative training rounds.
- Only binary client-server setting — not evaluated in multi-peer (P2P) collaboration.
- No support for heterogeneous model architectures.
- Split activations are tied to specific model splits and layers, limiting flexibility.