#!/usr/bin/env python3
"""Generate four missing schematic figures for the MDPI manuscript.

Outputs PDFs into writing/mdpi_paper/figures/:
  1. fig_peft_taxonomy.pdf         — Taxonomy of PEFT families (S4)
  2. fig_adapterfusion.pdf          — AdapterFusion fusion layer (S5)
  3. fig_switch_transformer.pdf     — Switch Transformer Top-1 routing (S7)
  4. fig_petals.pdf                 — Petals collaborative inference (S8)

Style: matplotlib schematic diagrams (FancyBboxPatch, clean gray backgrounds,
       colour-coded components, 8–9 pt sans-serif labels) matching the
       existing manuscript figures.
"""

import matplotlib
matplotlib.use("PDF")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import numpy as np
from pathlib import Path

HERE = Path(__file__).resolve().parent

plt.rcParams.update({
    "font.family": "DejaVu Sans",
    "font.size": 9,
    "axes.titlesize": 9,
    "figure.dpi": 200,
})

# Colour palette (matched to existing figures)
CLR_BACK  = "#f5f5f5"
CLR_EDGE  = "#cccccc"
CLR_BLUE  = "#4C72B0"
CLR_ORANGE= "#DD8452"
CLR_GREEN = "#55A868"
CLR_RED   = "#C44E52"
CLR_PURPLE= "#8172B2"
CLR_BROWN = "#937860"
CLR_CYAN  = "#64B5CD"
CLR_WHITE = "#ffffff"
CLR_LTBLUE= "#D6E4F0"
CLR_LTORG = "#D5E8D4"
CLR_LTPURP= "#E8D5F0"


def _rounded_box(ax, x, y, w, h, facecolor=CLR_WHITE, edgecolor=CLR_EDGE,
                 linewidth=1.0, **kw):
    """Add a FancyBboxPatch at (x,y) with width w and height h."""
    box = FancyBboxPatch((x, y), w, h,
                         boxstyle="round,pad=0.08",
                         facecolor=facecolor, edgecolor=edgecolor,
                         linewidth=linewidth, **kw)
    ax.add_patch(box)
    return box


def _arrow(ax, x1, y1, x2, y2, color="#666666", lw=1.5, style='->',
           connectionstyle="arc3,rad=0", mutation_scale=15, **kw):
    """Add an arrow between two points."""
    arr = FancyArrowPatch((x1, y1), (x2, y2),
                          arrowstyle=style, color=color, lw=lw,
                          connectionstyle=connectionstyle,
                          mutation_scale=mutation_scale, **kw)
    ax.add_patch(arr)
    return arr


def _label(ax, x, y, text, ha='center', va='center', fontsize=8, **kw):
    """Add a text label."""
    ax.text(x, y, text, ha=ha, va=va, fontsize=fontsize, **kw)


# ═══════════════════════════════════════════════════════════════════
# FIGURE 1: PEFT Taxonomy — additive / reparameterisation / selective
# ═══════════════════════════════════════════════════════════════════
def draw_peft_taxonomy():
    fig, ax = plt.subplots(1, 1, figsize=(8, 4.5))
    ax.set_xlim(0, 8)
    ax.set_ylim(0, 4.5)
    ax.axis("off")

    # Title
    _label(ax, 4.0, 4.15, "Taxonomy of Parameter-Efficient Fine-Tuning",
           fontsize=11, fontweight="bold")

    # ── Top row: three family columns ──
    families = [
        ("Additive\nmethods", CLR_BLUE, 1.2, [
            "Bottleneck adapters",
            "(Houlsby 2019,\n  Pfeiffer 2021)",
            "Prefix tuning",
            "(Li & Liang 2021,\n  Lester 2021)",
        ]),
        ("Reparameterisation\nmethods", CLR_GREEN, 3.8, [
            "LoRA\n(Hu 2022)",
            "QLoRA\n(Dettmers 2023)",
            "DoRA\n(Liu 2024)",
        ]),
        ("Selective\nmethods", CLR_ORANGE, 6.4, [
            "BitFit\n(Ben Zaken 2022)",
            "Diff Pruning\n(Guo 2021)",
        ]),
    ]

    # Column backgrounds
    for title, clr, cx, items in families:
        bg = FancyBboxPatch((cx-0.95, 2.2), 1.9, 1.5,
                            boxstyle="round,pad=0.1",
                            facecolor=clr, edgecolor=clr, alpha=0.15, lw=0)
        ax.add_patch(bg)
        _label(ax, cx, 2.9, "\n".join(title.split("\n")),
               fontsize=9, fontweight="bold", color=clr)

    # ── Arrow from top title down to families ──
    for cx in [1.2, 3.8, 6.4]:
        _arrow(ax, cx, 3.9, cx, 3.75, style='->', lw=1.2,
               connectionstyle="arc3,rad=0", mutation_scale=10)

    # ── Middle section: trainable parameters per method ──
    # Add a horizontal band
    y_mid = 1.65
    _rounded_box(ax, 0.4, y_mid-0.35, 7.2, 0.55,
                 facecolor=CLR_LTBLUE, edgecolor=CLR_BLUE, linewidth=0.8)
    _label(ax, 4.0, y_mid+0.05,
           "Trainable parameters: add / decompose weights / select subset",
           fontsize=8, color=CLR_BLUE, fontstyle="italic")

    # ── Bottom: concrete method boxes ──
    methods = [
        ("Bottleneck\nAdapter", CLR_BLUE, 0.7),
        ("Prefix\nTuning", CLR_BLUE, 1.8),
        ("LoRA", CLR_GREEN, 3.2),
        ("QLoRA", CLR_GREEN, 4.0),
        ("DoRA", CLR_GREEN, 4.8),
        ("BitFit", CLR_ORANGE, 5.8),
        ("Diff.\nPruning", CLR_ORANGE, 6.8),
    ]

    for name, clr, cx in methods:
        _rounded_box(ax, cx-0.35, 0.2, 0.70, 0.80,
                     facecolor=clr, edgecolor=clr, linewidth=0.8, alpha=0.85)
        _label(ax, cx, 0.75, name, fontsize=7, color="white", fontweight="bold")
        # Lines from method down to taxonomy arrow
        _arrow(ax, cx, 1.05, cx, 1.20, style='->', lw=0.8, color=clr,
               mutation_scale=8)

    # Connecting line from middle section down to methods row
    for (name, clr, cx) in methods:
        plt.plot([cx, cx], [1.30, 1.65], color=clr, lw=0.8,
                 linestyle='--', alpha=0.6)

    # Legend box
    _rounded_box(ax, 0.3, 0.02, 7.4, 0.20,
                 facecolor=CLR_BACK, edgecolor=CLR_EDGE, linewidth=0.5)
    _label(ax, 4.0, 0.12,
           "Figure adapted from the unified framework of Han et al. (2024)",
           fontsize=6.5, color="#999999", fontstyle="italic")

    plt.tight_layout()
    out = HERE / "fig_peft_taxonomy.pdf"
    fig.savefig(out, bbox_inches="tight", pad_inches=0.05)
    plt.close(fig)
    print(f"  ✓ {out.name}  ({out.stat().st_size//1024} KB)")


# ═══════════════════════════════════════════════════════════════════
# FIGURE 2: AdapterFusion fusion layer
# ═══════════════════════════════════════════════════════════════════
def draw_adapterfusion():
    fig, ax = plt.subplots(1, 1, figsize=(7, 4.8))
    ax.set_xlim(0, 7)
    ax.set_ylim(0, 4.8)
    ax.axis("off")

    # Title
    _label(ax, 3.5, 4.55, "AdapterFusion — Non-Destructive Task Composition",
           fontsize=11, fontweight="bold")
    _label(ax, 3.5, 4.25, "Pfeiffer et al. (2021)",
           fontsize=8, color="#888888", fontstyle="italic")

    # ── Shared input arrow ──
    _label(ax, 3.5, 4.0, "Layer input hₗ", fontsize=8,
           bbox=dict(boxstyle="round,pad=0.2", facecolor=CLR_LTBLUE, edgecolor=CLR_BLUE))
    # Branch lines down to 4 adapter boxes
    for i in range(4):
        x_a = 1.0 + i * 1.5
        plt.plot([3.5, x_a], [3.9, 3.55], color="#999999", lw=0.8)
        _arrow(ax, x_a, 3.55, x_a, 3.3, style='->', lw=1.0, color=CLR_BLUE,
               mutation_scale=10)

    # ── Adapter boxes ──
    for i in range(4):
        x_a = 1.0 + i * 1.5
        _rounded_box(ax, x_a-0.40, 2.6, 0.80, 0.65,
                     facecolor=CLR_BLUE, edgecolor=CLR_BLUE, linewidth=1.0)
        _label(ax, x_a, 3.10, f"Adapter\nA¢₁⁻₄", fontsize=7, color="white")
        _label(ax, x_a, 2.75, f"Task {i+1}", fontsize=6, color="white", alpha=0.8)
        # Frozen label under each
        _label(ax, x_a, 2.50, "(frozen)", fontsize=6, color=CLR_BLUE, alpha=0.6)

    # ── Adapter outputs feed into fusion ──
    for i in range(4):
        x_a = 1.0 + i * 1.5
        plt.plot([x_a, x_a], [2.55, 2.15], color=CLR_BLUE, lw=0.8,
                 linestyle='--', alpha=0.4)
    # Horizontal bar representing concatenated adapter outputs
    _rounded_box(ax, 0.6, 2.05, 5.8, 0.20,
                 facecolor=CLR_LTBLUE, edgecolor=CLR_BLUE, linewidth=0.5, alpha=0.5)
    _label(ax, 3.5, 2.15, "Adapter outputs: [h₁, h₂, …, hₖ]",
           fontsize=7.5, color=CLR_BLUE)

    # ── Arrow into Fusion Layer ──
    _arrow(ax, 3.5, 2.0, 3.5, 1.7, style='->', lw=1.5, color=CLR_RED,
           mutation_scale=12)

    # ── Fusion Layer ──
    _rounded_box(ax, 1.8, 0.8, 3.4, 0.85,
                 facecolor=CLR_RED, edgecolor=CLR_RED, linewidth=1.5, alpha=0.9)
    _label(ax, 3.5, 1.35, "Fusion Layer (learnable)", fontsize=9,
           fontweight="bold", color="white")
    _label(ax, 3.5, 1.08,
           "Attention(Wᴩ, Wᴰ, Wᴵ)\n• Wᴩ: query projection  • Wᴰ: key projection  • Wᴵ: value projection",
           fontsize=6.5, color="white", alpha=0.9)

    # ── Output arrow ──
    _arrow(ax, 3.5, 0.75, 3.5, 0.40, style='->', lw=1.5, color=CLR_GREEN,
           mutation_scale=12)
    _label(ax, 3.5, 0.25, "Composed output h'", fontsize=8.5, fontweight="bold",
           bbox=dict(boxstyle="round,pad=0.2", facecolor=CLR_GREEN, edgecolor=CLR_GREEN,
                     alpha=0.2))

    # Note at bottom
    _rounded_box(ax, 0.3, 0.02, 6.4, 0.20,
                 facecolor=CLR_BACK, edgecolor=CLR_EDGE, linewidth=0.5)
    _label(ax, 3.5, 0.12,
           "AdapterFusion: task-specific adapters remain frozen; only fusion module weights are updated.",
           fontsize=6.5, color="#888888", fontstyle="italic")

    plt.tight_layout()
    out = HERE / "fig_adapterfusion.pdf"
    fig.savefig(out, bbox_inches="tight", pad_inches=0.05)
    plt.close(fig)
    print(f"  ✓ {out.name}  ({out.stat().st_size//1024} KB)")


# ═══════════════════════════════════════════════════════════════════
# FIGURE 3: Switch Transformer Top-1 routing (MoE)
# ═══════════════════════════════════════════════════════════════════
def draw_switch_transformer():
    fig, ax = plt.subplots(1, 1, figsize=(7.5, 4.8))
    ax.set_xlim(0, 7.5)
    ax.set_ylim(0, 4.8)
    ax.axis("off")

    # Title
    _label(ax, 3.75, 4.55, "Switch Transformer — Sparse Top-1 Expert Routing",
           fontsize=11, fontweight="bold")
    _label(ax, 3.75, 4.25, "Fedus, Zoph & Shazeer (2022)",
           fontsize=8, color="#888888", fontstyle="italic")

    # ── Input token ──
    _label(ax, 3.75, 3.85, "Token embedding xᵢ",
           fontsize=8.5, bbox=dict(boxstyle="round,pad=0.25",
                                   facecolor=CLR_LTBLUE, edgecolor=CLR_BLUE))
    _arrow(ax, 3.75, 3.70, 3.75, 3.45, style='->', lw=1.5, color="#666666",
           mutation_scale=12)

    # ── Router box ──
    _rounded_box(ax, 2.45, 2.6, 2.6, 0.80,
                 facecolor=CLR_PURPLE, edgecolor=CLR_PURPLE, linewidth=1.5)
    _label(ax, 3.75, 3.15, "Router (learned gate)", fontsize=9,
           fontweight="bold", color="white")
    _label(ax, 3.75, 2.85, "Assigns token to 1 expert", fontsize=7.5,
           color="white", alpha=0.85)

    # ── Routing arrows to experts ──
    # Three routing paths with the "Top-1" highlighted path drawn thicker
    expert_xs = [1.0, 3.75, 6.2]
    expert_labels = ["Expert A\n(FFN)", "Expert B\n(FFN)  ← Top-1 win!", "Expert N\n(FFN)"]
    expert_colors = [CLR_BROWN, CLR_GREEN, CLR_BROWN]

    for i, (ex, xpos, clr) in enumerate(zip(expert_labels, expert_xs, expert_colors)):
        # Arrow from router to expert (expert B gets thicker arrow)
        lw = 1.2 if i == 1 else 0.6
        col = clr if i == 1 else "#aaaaaa"
        _arrow(ax, 3.75, 2.55, xpos, 2.1, style='->', lw=lw, color=col,
               connectionstyle="arc3,rad=-0.35" if xpos < 3.75 else
                               "arc3,rad=0.35" if xpos > 3.75 else "arc3,rad=0",
               mutation_scale=10)

        # Expert box
        _rounded_box(ax, xpos-0.55, 1.2, 1.10, 0.85,
                     facecolor=clr if i == 1 else "#e0e0e0",
                     edgecolor=clr if i == 1 else "#cccccc",
                     linewidth=1.5 if i == 1 else 0.5)
        _label(ax, xpos, 1.75, ex, fontsize=7.5,
               color="white" if i == 1 else "#888888",
               fontweight="bold" if i == 1 else "normal")

    # ── "1 token → 1 expert" label ──
    _rounded_box(ax, 2.2, 0.4, 3.1, 0.40,
                 facecolor=CLR_LTORG, edgecolor=CLR_GREEN, linewidth=0.8)
    _label(ax, 3.75, 0.60, "Result: one token activates only one expert",
           fontsize=8, color=CLR_GREEN, fontweight="bold")

    # ── Balance loss note ──
    _rounded_box(ax, 4.8, 0.02, 2.5, 0.28,
                 facecolor="#fee8c8", edgecolor=CLR_ORANGE, linewidth=0.5)
    _label(ax, 6.05, 0.16, "Auxiliary load-balancing loss prevents collapse",
           fontsize=6.5, color=CLR_ORANGE)

    # Footnote
    _rounded_box(ax, 0.3, 0.02, 4.3, 0.28,
                 facecolor=CLR_BACK, edgecolor=CLR_EDGE, linewidth=0.5)
    _label(ax, 2.45, 0.16,
           "Achieves 7× pre-training speedup vs. dense T5 at equivalent quality",
           fontsize=6.5, color="#888888", fontstyle="italic")

    plt.tight_layout()
    out = HERE / "fig_switch_transformer.pdf"
    fig.savefig(out, bbox_inches="tight", pad_inches=0.05)
    plt.close(fig)
    print(f"  ✓ {out.name}  ({out.stat().st_size//1024} KB)")


# ═══════════════════════════════════════════════════════════════════
# FIGURE 4: Petals collaborative inference
# ═══════════════════════════════════════════════════════════════════
def draw_petals():
    fig, ax = plt.subplots(1, 1, figsize=(8.5, 5.0))
    ax.set_xlim(0, 8.5)
    ax.set_ylim(0, 5.0)
    ax.axis("off")

    # Title
    _label(ax, 4.25, 4.75, "Petals — Collaborative LLM Inference",
           fontsize=11, fontweight="bold")
    _label(ax, 4.25, 4.45, "Borzunov et al. (2023)",
           fontsize=8, color="#888888", fontstyle="italic")

    # ── Client node ──
    _rounded_box(ax, 0.2, 3.3, 1.6, 0.80,
                 facecolor=CLR_CYAN, edgecolor=CLR_CYAN, linewidth=1.2)
    _label(ax, 1.0, 3.85, "Client", fontsize=9, fontweight="bold", color="white")
    _label(ax, 1.0, 3.55, "Embeds query\nrequests inference", fontsize=6.5,
           color="white", alpha=0.85)

    # Arrow from client to first node
    _arrow(ax, 1.85, 3.70, 2.6, 3.70, style='->', lw=1.5, color="#666666",
           mutation_scale=12)

    # ── Volunteer nodes (transformer layer segments) ──
    node_data = [
        (3.0, "Node A\nLayers 1–8", CLR_BLUE, "#3d5a8e",
         "Hosts first 8\ntransformer layers"),
        (4.5, "Node B\nLayers 9–16", CLR_GREEN, "#3d8b41",
         "Hosts next 8\ntransformer layers"),
        (6.0, "Node C\nLayers 17–24", CLR_ORANGE, "#b86c2e",
         "Hosts last 8\ntransformer layers"),
    ]

    for xpos, title, color, dark, note in node_data:
        _rounded_box(ax, xpos-0.45, 2.60, 1.50, 1.10,
                     facecolor=color, edgecolor=color, linewidth=1.2, alpha=0.85)
        _label(ax, xpos+0.3, 3.45, title, fontsize=8, fontweight="bold",
               color="white")
        _label(ax, xpos+0.3, 2.95, note, fontsize=6, color="white", alpha=0.85)

        # Arrow between nodes
        if xpos < 6.0:
            _arrow(ax, xpos+1.1, 3.15, xpos+1.6, 3.15, style='->', lw=1.0,
                   color="#888888", mutation_scale=10)

    # ── Activation arrows between nodes (top path) ──
    nodes_x = [3.0, 4.5, 6.0]
    for i in range(len(nodes_x)-1):
        x1 = nodes_x[i] + 1.1
        x2 = nodes_x[i+1] - 0.45
        y = 3.80
        _arrow(ax, x1, y, x2, y, style='->', lw=1.2, color="#444444",
               mutation_scale=11)
        _label(ax, (x1+x2)/2, y+0.15, "activations", fontsize=5.5,
               color="#444444", alpha=0.7)

    # ── Backward arrows (for fine-tuning) ──
    for i in range(len(nodes_x)-1, 0, -1):
        x1 = nodes_x[i]
        x2 = nodes_x[i-1] + 0.45
        y = 2.45
        _arrow(ax, x1, y, x2, y, style='->', lw=0.8, color="#888888",
               linestyle='dashed', mutation_scale=8)
    _label(ax, 3.8, 2.30, "gradients (fine-tuning)", fontsize=5.5,
           color="#888888", alpha=0.6)

    # ── Bottom: result ──
    _rounded_box(ax, 1.5, 0.50, 5.7, 0.55,
                 facecolor=CLR_LTORG, edgecolor=CLR_GREEN, linewidth=0.8)
    _label(ax, 4.35, 0.85,
           "Result: BLOOM-176B inference on commodity hardware",
           fontsize=9, fontweight="bold", color=CLR_GREEN)
    _label(ax, 4.35, 0.65,
           "Collaborative volunteer nodes share backbone layers; activations pass node-to-node",
           fontsize=6.5, color="#666666")

    # ── Key limitation callout ──
    lim_x = 0.15
    _rounded_box(ax, lim_x, 0.08, 3.3, 0.35,
                 facecolor=CLR_LTPURP, edgecolor=CLR_PURPLE, linewidth=0.8, alpha=0.3)
    _label(ax, lim_x+0.05, 0.25,
           "⚠ No per-task adapter modules — all nodes serve identical backbone",
           fontsize=6.5, color=CLR_PURPLE, ha="left", va="center")

    # ── Top-right: key legend ──
    _rounded_box(ax, 6.2, 0.08, 2.0, 3.30,
                 facecolor=CLR_BACK, edgecolor=CLR_EDGE, linewidth=0.5)
    _label(ax, 7.2, 3.15, "Legend", fontsize=8, fontweight="bold", color="#444444")
    items = [
        ("Inference path", CLR_BLUE),
        ("Fine-tuning path", CLR_ORANGE),
        ("Commodity node", CLR_BLUE),
    ]
    for i, (lab, clr) in enumerate(items):
        y = 2.80 - i * 0.35
        plt.plot([6.5, 6.8], [y, y], color=clr, lw=2)
        _label(ax, 6.9, y, lab, fontsize=7, ha="left", va="center")

    plt.tight_layout()
    out = HERE / "fig_petals.pdf"
    fig.savefig(out, bbox_inches="tight", pad_inches=0.05)
    plt.close(fig)
    print(f"  ✓ {out.name}  ({out.stat().st_size//1024} KB)")


# ═══════════════════════════════════════════════════════════════════
if __name__ == "__main__":
    print("Generating 4 missing manuscript figures...\n")
    draw_peft_taxonomy()
    draw_adapterfusion()
    draw_switch_transformer()
    draw_petals()
    print("\nDone — all figures saved to figures/")