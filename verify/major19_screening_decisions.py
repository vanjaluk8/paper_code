#!/usr/bin/env python3
"""
Major #19 -- abstract-level topical-relevance screening of the 93
consolidated top-up candidates.

IMPORTANT SCOPE NOTE: this is a topical-relevance filter, read at the same
depth as the manuscript's own title/abstract screening stages (Layer 2 /
abstract review) -- it is NOT a substitute for the full PRISMA eligibility
assessment (Table A2 criteria, full-text read, quality appraisal) that a
genuine inclusion decision requires. The KEEP/DROP calls and one-line
rationale below are a recommendation for the author to confirm, not a final
inclusion decision -- consistent with the fact that even the original
review's own abstract-stage KEEP/SKIP dispositions were advisory until the
author's own full-text read.

DROP rationale used throughout: the paper's core contribution/application is
outside the review's three pillars in practice -- e.g. a medical-imaging,
industrial-IoT, telecom, or pure-vision-transformer application that borrows
LoRA/adapter/MoE terminology architecturally but does not engage adapter
exchange, PEFT-for-LLMs, or federated/P2P LLM serving in a way that speaks
to this review's synthesis questions.

Usage: python3 verify/major19_screening_decisions.py
"""
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# key: normalised prefix of title (first 40 chars, lowercased, for matching)
# value: (KEEP/DROP, one-line rationale)
DECISIONS = {
    "adafuse: accelerating dynamic adapter": ("KEEP", "Multi-adapter LLM inference latency (Pillar 3)"),
    "adaptive rank allocation for federate": ("KEEP", "Federated PEFT for LMs (Pillar 2)"),
    "clare: continual learning for vision-": ("DROP", "Robotics/VLA manipulation, not LLM adapter-exchange"),
    "domain-adaptive multimodal large lang": ("DROP", "Photovoltaic fault diagnosis application"),
    "dymerge-lora: on-gpu post-merge fusio": ("KEEP", "Multi-tenant composite LoRA serving (Pillar 3)"),
    "enhancing aggregation efficiency and ": ("KEEP", "Federated LoRA framework"),
    "fedalt: federated fine-tuning through": ("KEEP", "Federated LoRA for LLMs (already known via arXiv)"),
    "fedfa: efficient federated large lang": ("KEEP", "Federated LLM feature adapters"),
    "fedhydra: toward parameter-efficient ": ("DROP", "Federated unlearning in metaverse, tangential to adapter exchange"),
    "melora: probability measures-based lo": ("KEEP", "Core LoRA/PEFT method for LLMs (Pillar 1)"),
    "moe-ffd: mixture of experts for gener": ("DROP", "Face forgery detection (deepfakes), vision-only"),
    "multi-task unified domain incrementa": ("DROP", "Computer-vision domain-incremental learning"),
    "multi-task–driven adapter-based fou": ("DROP", "VR locomotion prediction application"),
    "pm-adapter: moe based dynamic denois": ("DROP", "Thermal infrared object detection, vision-only"),
    "privlora: enhancing privacy in lora-b": ("KEEP", "Federated LoRA for LLMs (Pillar 2)"),
    "spatiotemporal context-aware prompti": ("DROP", "Video class-incremental learning, vision-only"),
    "pfedlora: model-heterogeneous persona": ("KEEP", "Federated LoRA personalization (Pillar 2)"),
    "a multi-task prompt collaborative op": ("KEEP", "Multi-task PEFT (LoRA+Prompt) for NLP (Pillar 1/2)"),
    "a framework for efficient scientific": ("DROP", "Diagram captioning application, vision-language niche"),
    "ace: adapter consolidation across ex": ("KEEP", "PEFT+MoE for LLMs (Pillar 1/5)"),
    "awma-moe: attention-guided watermark": ("DROP", "Image watermarking for diffusion models, not LLM/NLP"),
    "alternating aggregation low-rank ada": ("KEEP", "Federated LoRA for large models"),
    "an enhanced low-rank fine-tuning fra": ("KEEP", "Federated LLM PEFT"),
    "automated federated pipeline for par": ("KEEP", "Federated PEFT pipeline for LLMs"),
    "beyond full-model rollback: aurosft ": ("KEEP", "Multi-task adapter-state fine-tuning for LLMs (Pillar 1/2)"),
    "bitlora: quantization-compatible ada": ("KEEP", "Federated on-device LLM LoRA"),
    "breaking the structural identity: pe": ("KEEP", "Federated LoRA under rank heterogeneity"),
    "cd-lora: consistency-driven low-rank": ("KEEP", "Multi-task LoRA fine-tuning for LLMs"),
    "clear: continuous latent adapter rou": ("KEEP", "Adapter routing for LLM safety alignment (Pillar 1/5)"),
    "colora: a collaborative scheduling f": ("KEEP", "Multi-tenant LoRA LLM inference serving (Pillar 3)"),
    "d2mora: diversity-regulated asymmetr": ("KEEP", "MoE-LoRA multi-task adaptation (Pillar 1/5)"),
    "dp-dylora: fine-tuning transformer-b": ("KEEP", "DP federated LoRA for transformers"),
    "dp-hm2f: data-driven lora with dual-": ("KEEP", "Federated LoRA for multimodal LLMs"),
    "decaf: decentralized consensus-and-f": ("KEEP", "Decentralised LoRA theory -- directly bears on P2P gap claims"),
    "decentralized lora augmented transfo": ("DROP", "Ophthalmic (eye) medical-imaging diagnosis application"),
    "dual-adaptive sam3: hierarchical rou": ("DROP", "Medical image segmentation application"),
    "epng: adaptive expert prune-and-grow": ("KEEP", "PEFT MoE for LLMs (Pillar 1/5)"),
    "echocardiography report translation ": ("DROP", "Clinical/medical translation application"),
    "efficient multi-adapter llm serving ": ("KEEP", "Multi-adapter LLM serving, KV-cache reuse (Pillar 3)"),
    "efficient multi-tenant lora serving ": ("KEEP", "Multi-tenant LoRA serving kernel optimisation (Pillar 3)"),
    "explainable multilingual nmt with ad": ("KEEP", "Adapters+MoE composition for NLP (machine translation)"),
    "exploring backdoor attacks in federa": ("KEEP", "Security analysis of federated PEFT (Pillar 2)"),
    "flaguard: efficient verifiable feder": ("KEEP", "Verifiable federated LoRA for LLMs"),
    "force: federated orthogonality-aware": ("KEEP", "Communication-efficient federated LoRA"),
    "feddlpd: an efficient personalized f": ("DROP", "IIoT intrusion detection application"),
    "fedgsa: geometry-consistent subspace": ("KEEP", "DP federated LoRA aggregation"),
    "fedlodrop: federated lora with dropo": ("KEEP", "Federated LoRA generalisation for LLMs"),
    "fedmosaic: federated retrieval-augme": ("KEEP", "Federated RAG via adapters for LLMs (Pillar 2)"),
    "fedp2eft: federated learning to pers": ("KEEP", "Federated PEFT personalisation, multilingual LLMs"),
    "fedquad: adaptive layer-wise lora de": ("KEEP", "Federated LoRA deployment+quantisation"),
    "fedweave: rethinking the unit of spe": ("KEEP", "Federated MoE-LoRA specialisation"),
    "federated adapter learning under ene": ("DROP", "IoV consumer-electronics generative personalisation application"),
    "federated lora adaptation of biomedc": ("DROP", "Biomedical imaging (chest X-ray) application"),
    "federated lora fine-tuning for llms ": ("KEEP", "Federated LoRA for LLMs, collaborative alignment"),
    "federated lora fine-tuning of llms w": ("KEEP", "Federated LoRA communication efficiency"),
    "fully decentralized inference for sp": ("DROP", "Spatial statistics (geostatistics) low-rank models -- different technical meaning of 'low-rank', not LoRA/LLM"),
    "graph cross-domain continual fine-tu": ("DROP", "Graph Foundation Models, not LLM/NLP modality"),
    "haflq: heterogeneous adaptive federa": ("KEEP", "Federated LoRA LLM with quantisation"),
    "improving dialect robustness in larg": ("KEEP", "LoRA+MoE for LLM dialect robustness (Pillar 1/5, NLP)"),
    "improving learning of new diseases t": ("DROP", "Healthcare/medical federated adapter application"),
    "llm-mm: end-to-end robust multimodal": ("DROP", "6G V2X telecom beam prediction, not language modelling despite 'LLM' in title"),
    "logic: multi-lora guided importance ": ("DROP", "Vision Transformer pruning, not LLMs"),
    "localized lora-moe: block-wise low-r": ("KEEP", "PEFT MoE architecture for LLMs/perception (Pillar 1/5)"),
    "mace: modular adaptive code engine w": ("KEEP", "LLM code generation with adapter expert routing (Pillar 1/5)"),
    "mhp-serve: mobile heterogeneous para": ("KEEP", "Mobile LoRA inference serving (Pillar 3)"),
    "mi-peft: mixture-of-experts integrat": ("DROP", "Protein language models / bioinformatics application"),
    "mllora: leveraging meta-learning and": ("DROP", "Medical LLM application (clinical decision support)"),
    "mmtuning: an advanced multi-adapter ": ("KEEP", "Multi-adapter PEFT for multimodal LLMs (Pillar 1/2)"),
    "mt-moa: a unified parameter-efficien": ("DROP", "Image Coding for Machines, compression application"),
    "moe$^2$-lora: when moe models meet m": ("KEEP", "Core PEFT MoE-LoRA for LLMs (Pillar 1/5)"),
    "moe-based feature adapter for prompt": ("DROP", "Coronary artery X-ray segmentation, medical imaging"),
    "moegen: mixture-of-experts for insta": ("KEEP", "MoE for instance-adaptive LoRA generation (Pillar 1/5)"),
    "multi-adapter llms: dynamic mixture ": ("KEEP", "Core multi-adapter LLM serving/personalisation (Pillar 1/2/3)"),
    "multi-adapter based federated learni": ("DROP", "Industrial predictive maintenance (RUL estimation) application"),
    "on the construction and implication": ("KEEP", "LoRA theory: Bayesian inference / loss landscape (Pillar 1)"),
    "peml: parameter-efficient multi-task": ("KEEP", "Multi-task PEFT with continuous prompts for LLMs (Pillar 1/2)"),
    "pfadapter: hierarchical lora decompo": ("KEEP", "Federated multimodal LLM adapters (Pillar 2)"),
    "parameter-efficient large model tran": ("KEEP", "Adapter-based cloud-edge LLM serving (Pillar 3)"),
    "per-fedlora: personalized federated ": ("KEEP", "Federated LoRA for multi-task LLMs"),
    "prelort: prefix-nested lora for fede": ("KEEP", "Federated LoRA under rank heterogeneity"),
    "priority-aware learning-unlearning c": ("KEEP", "Decentralised federated LoRA (P2P-adjacent, Pillar 2/4)"),
    "prototype-guided and lightweight ada": ("KEEP", "Federated adapters, interpretability (Pillar 2)"),
    "rw-lora: communication-efficient dec": ("KEEP", "Decentralised LoRA via random walks -- directly P2P-relevant"),
    "rethinking factor sharing in federat": ("KEEP", "Federated LoRA factor-sharing analysis"),
    "routing is not enough: diagnosing in": ("KEEP", "MoE+LoRA routing diagnostics for LLMs (Pillar 1/5)"),
    "specprefetch: parameter-efficient ex": ("KEEP", "MoE expert prefetching for foundation-model serving (Pillar 3/5)"),
    "spend experts where you are unsure: ": ("KEEP", "Confidence-adaptive MoE-LoRA routing (Pillar 1/5)"),
    "statistical inference for rank alloc": ("KEEP", "LoRA rank-allocation theory (Pillar 1)"),
    "tcpa-medmtl: a task-conditioned prot": ("DROP", "Medical image classification application"),
    "tailorllm: collaborative end-cloud i": ("KEEP", "LoRA-based end-cloud LLM serving (Pillar 3)"),
    "task-aware cloud-end offloading for ": ("KEEP", "Adapter-scheduled VLM serving (Pillar 3)"),
    "towards universal ultrasound analysi": ("DROP", "Medical ultrasound imaging application"),
    "transfr: transferable federated reco": ("KEEP", "Federated adapter tuning on pretrained LMs (Pillar 2)"),
}


def norm_key(title: str) -> str:
    return title.strip().lower()


def main():
    with open(ROOT / "verify" / "major19_topup_with_abstracts.csv", encoding="utf-8-sig") as f:
        rows = list(csv.DictReader(f))

    unmatched = []
    out_rows = []
    for r in rows:
        low = norm_key(r["title"])
        match = next((k for k in DECISIONS if low.startswith(k)), None)
        if match is None:
            unmatched.append(r["title"])
            decision, reason = "UNMATCHED", ""
        else:
            decision, reason = DECISIONS[match]
        out_rows.append({**r, "screening_decision": decision, "screening_rationale": reason})

    if unmatched:
        print(f"WARNING: {len(unmatched)} titles did not match a decision key:")
        for t in unmatched:
            print(f"    {t}")

    from collections import Counter
    counts = Counter(r["screening_decision"] for r in out_rows)
    print(f"Total: {len(out_rows)}")
    print(f"Decisions: {dict(counts)}")

    out_path = ROOT / "verify" / "major19_topup_screened.csv"
    with open(out_path, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["title", "year", "sources", "venue_or_id",
                                           "screening_decision", "screening_rationale", "abstract"])
        w.writeheader()
        for r in out_rows:
            w.writerow({k: r.get(k, "") for k in w.fieldnames})
    print(f"\nWrote {out_path}")

    kept_path = ROOT / "verify" / "major19_topup_kept_after_screening.csv"
    kept = [r for r in out_rows if r["screening_decision"] == "KEEP"]
    with open(kept_path, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["title", "year", "sources", "venue_or_id", "screening_rationale"])
        w.writeheader()
        for r in kept:
            w.writerow({k: r.get(k, "") for k in w.fieldnames})
    print(f"Wrote {len(kept)} KEEP rows to {kept_path}")


if __name__ == "__main__":
    main()
