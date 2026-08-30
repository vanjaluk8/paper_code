Dear Editor,

I am pleased to submit my manuscript titled **"Decentralised Adapter-Based
LLM Inference: A Systematic Literature Review—Mapping the Research Gap at
the Intersection of PEFT, P2P Systems, and Multi-Task Serving"** for
consideration as a Systematic Review in *AI* (MDPI).

**Significance and scope fit.** Large language model inference is
increasingly deployed on resource-constrained and distributed hardware,
while parameter-efficient fine-tuning (PEFT) methods — LoRA and adapters in
particular — have made it practical to store and exchange small,
task-specific modules on top of a single frozen backbone. Almost all
existing systems that serve such adapters (multi-tenant inference servers,
federated PEFT frameworks) assume a centralised orchestrator. This review
asks a specific, testable question: does the literature already contain the
building blocks needed for a peer-to-peer (P2P) network of autonomous nodes
to discover, retrieve, compose, and serve adapters over a shared frozen
backbone, entirely without central coordination? *AI*'s scope explicitly
covers both foundational machine learning methods and applied/systems
research on AI deployment, which this review bridges directly.

**Novelty.** To my knowledge, no prior systematic review synthesises these
three normally separate literatures — PEFT/adapter architectures, adapter
composition and mixture-of-experts routing, and P2P/federated systems —
around a single feasibility question for decentralised, adapter-based
multi-task inference. Following PRISMA 2020 and Wohlin et al. snowballing,
the review screened 1,150 snowball candidates, merged the 162 that passed
screening with a 352-paper pre-validated corpus, and appraised 123 included
records (120 distinct papers) across five thematic clusters using a
six-dimension quality rubric. The synthesis shows that while every
individual building block (transmissible adapters, training-free
composition, MoE-style routing, federated aggregation) exists in isolation,
no reviewed system combines a frozen shared backbone, adapter-level
exchange, P2P topology, decentralised discovery, multi-task fusion, and the
absence of a central coordinator. The review organises the resulting open
problems into four gap quadrants (conceptual, algorithmic, systems,
empirical), giving the field a concrete research agenda rather than a
general survey of adjacent literatures.

**Reporting standards.** The review follows PRISMA 2020 reporting
guidelines; the completed 27-item checklist and the per-study
quality-appraisal data are included as Supplementary Materials S1 and S2
respectively.

This manuscript is not under consideration elsewhere, and I have no
conflicts of interest to declare. I confirm that I have read and agree to
the journal's Instructions for Authors.

**Suggested reviewers:**
1. [Name] — [Affiliation] — [email] — [area: PEFT/LoRA]
2. [Name] — [Affiliation] — [email] — [area: P2P/federated systems]
3. [Name] — [Affiliation] — [email] — [area: MoE / adapter routing]
4. [Name] — [Affiliation] — [email] — [area: systematic review methodology]

Thank you for considering this manuscript. I look forward to your response.

Sincerely,
Vanja Luk
Faculty of Informatics and Digital Technologies, University of Rijeka
vluk@uniri.hr
