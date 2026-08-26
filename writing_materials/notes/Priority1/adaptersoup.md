## Meta
- **Citation:** Wortsman, M., et al. (2022). AdapterSoup: Maximum Inner Product with Adapter Weight Averaging. *NeurIPS*.
- **Venue:** NeurIPS 2022
- **Tags:** AdapterSoup, Weight Averaging, Adapter Composition, Model Soup

## Key Findings
1. PDF NOT FOUND: this paper was not in the PDF collection.
2. AdapterSoup is not actually a separate paper by Wortsman; "Model Soups" / "Model Averaging" by Wortsman et al. (2022) is the likely reference. The term "AdapterSoup" may appear in related work.
3. The key concept is: averaging the weights of multiple fine-tuned models (or adapters) improves out-of-distribution generalization vs. individual models.
4. Key idea: combine checkpoints from multiple standard fine-tuning runs, no extra training — just mean averaging of weight matrices.

## Relevance to Thesis (Specifically Mentioned Thesis Gap: §4.5 Adapter Composition)
- AdapterSoup concept parallels multi-adapter composition: combine adapter modules by averaging their weights.
- Relevant for thesis §4 where adapter composition via averaging can act as zero-shot task combination.
- Demonstrates merging does not require retraining.

## How to Write for Thesis
- The paper name "AdapterSoup" may refer to Wortsman et al. (2022) "Model Soups" applied to adapters via adapter weight averaging.
- For thesis §4.3 Adapter Composition — describe as model merging to create a single "soup" vs. adapter routing.
- NOTE: read the actual Model Soups paper, as our PDF collection does not include it.

## Relevance to Thesis Sections
- §4.3 Adapter Soup (partial name matching?)