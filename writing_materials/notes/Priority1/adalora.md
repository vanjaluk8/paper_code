## Meta
- **Citation:** Zhang, Q., Chen, M., Bukharin, A., He, P., Cheng, Y., Chen, W., & Zhao, T. (2023). AdaLoRA: Adaptive Budget Allocation for Parameter-Efficient Fine-Tuning. *ICLR*.
- **Venue:** ICLR 2023
- **Tags:** AdaLoRA, Adaptive LoRA, Rank Allocation, PEFT, SVD

## Key Findings (from PDF — paper known but NOT in our PDF collection)
1. PDF NOT FOUND: this paper was not in the PDF collection.
2. AdaLoRA employs singular value decomposition (SVD) to allocate rank budget adaptively across weight matrices.
3. Not all weight matrices need large rank — low-rank is sufficient for PEFT, some matrices benefit from higher ranks.
4. Regularization: SVD decomposition with singular value penalty to prune less important dimensions.

## Relevance to Thesis
- AdaLoRA contributes to §3.4 Advanced PEFT as method for adaptive rank allocation.
- Could enable more efficient PEFT weight transfer in decentralized systems: each task gets adaptive rank per weight matrix.

## Key Metrics / Results
- As reported in literature: AdaLoRA matches or surpasses LoRA with fixed rank across GLUE/SuperGLUE.
- Particularly useful for cross-task adapter composition: different tasks may need different rank budgets.

## Limitations / Gaps
- Additional overhead of SVD decomposition per weight.
- Better rank allocation doesn't reduce memory footprint compared to fixed-rank LoRA during training.
- Not designed for multi-task head composition.

## How to Write for Thesis
- Use in §3.4 Advanced PEFT as an example of rank optimization in LoRA.
- Explain the mechanism: regularized SVD-based dynamic rank allocation.
- Compare with standard LoRA to demonstrate improvement.

## Relevance to Thesis Sections
- §3.4 Advanced PEFT