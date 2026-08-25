"""
Generates targeted conceptual figures for P2P concepts and PEFT adapter structures.
Output: writing/figures/fig_p2p_*.png
"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch
import numpy as np
from pathlib import Path

OUT = Path("latex_folder/figures")  # relative to cwd (writing/)
OUT.mkdir(parents=True, exist_ok=True)

plt.rcParams.update({
    "font.family": "DejaVu Sans",
    "font.size": 9,
    "axes.titlesize": 8,
    "figure.dpi": 180,
})


# ──────────────────────────────────────────────────────────────
# 1) Adapter structural types: LoRA vs Bottleneck vs Prefix vs Adapter
# ──────────────────────────────────────────────────────────────
def draw_adapter_structures():
    fig, axes = plt.subplots(1, 4, figsize=(11, 3.2))

    titles = ["(a) Bottleneck\nAdapter", "(b) LoRA\n(Low-Rank Adapt.)",
              "(c) Prefix\nTuning", "(d) Adapter as\nAtomic Unit"]

    labels_data = [
        [("Down-proj.", 1, 1.0),  ("NonLin", 2, 1.0), ("Up-proj.", 3, 1.0)],
        [("A (down)", 1, 1.0), ("B (up)", 2, 1.0)],
        [("P_k keys", 1, 0.8)],
        [("Weights\n+ meta", 1, 1.2)],
    ]

    colors = [["#4C72B0", "#DD8452", "#55A868"],
              ["#4C72B0", "#DD8452"],
              ["#DD8452"],
              ["#C44E52"]]

    for idx, ax in enumerate(axes):
        items = labels_data[idx]
        cols = colors[idx]
        y_offset = 0
        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1)
        ax.set_aspect('equal')

        # Background
        rect = FancyBboxPatch((0.02, 0.02), 0.96, 0.96,
                              boxstyle="round,pad=0.08", fill=True,
                              facecolor="#f5f5f5", edgecolor="#cccccc", lw=1)
        ax.add_patch(rect)
        ax.text(0.5, 0.94, titles[idx], ha="center", va="top",
                fontsize=8, fontweight="bold")

        for j, (label, level, height) in enumerate(items):
            h_norm = height * 0.22
            y_bot = 1 - 0.08 - (1 - 0.08 - 0.08) * (y_offset + h_norm)
            y_top = y_bot + 0.065
            bx = FancyBboxPatch((0.25, y_bot - 0.02), 0.5, y_top - y_bot + 0.02,
                                boxstyle="round,pad=0.04", fill=True,
                                facecolor=cols[j] if j == 0 else "#e0e0e0",
                                edgecolor="#999999", lw=0.5)
            ax.add_patch(bx)
            ax.text(0.5, y_bot - 0.01 + 0.5*(y_top - y_bot), label,
                    ha="center", va="center", fontsize=7,
                    color="white" if j == 0 else "#333333")
            y_offset += h_norm
            if j < len(items) - 1:
                mid_prev = y_bot
                mid_next = y_bot - 0.005
                ax.annotate("", xy=(0.5, mid_next), xytext=(0.5, mid_prev),
                            arrowprops=dict(arrowstyle="->", color="#888888", lw=0.7))

        ax.set_xticks([])
        ax.set_yticks([])
        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)
        ax.spines["left"].set_visible(False)
        ax.spines["bottom"].set_visible(False)

    axes[0].text(0.5, -0.2,
        "Down-proj + NonLin + Up-proj\ninserted into transformer block",
        ha="center", va="top", fontsize=6, color="#666666")
    axes[1].text(0.5, -0.2,
        "Low-rank matrices A, B\nadded to Q/K/V weight",
        ha="center", va="top", fontsize=6, color="#666666")
    axes[2].text(0.5, -0.2,
        "Learnable vectors prepended\nto each layer's KV",
        ha="center", va="top", fontsize=6, color="#666666")
    axes[3].text(0.5, -0.2,
        "Self-contained weight,\nmetadata + capability",
        ha="center", va="top", fontsize=6, color="#666666")

    fig.suptitle("PEFT Adapter Types: Structure and Abstraction", fontsize=10, y=1.02)
    fig.tight_layout(pad=2.5)
    fig.savefig(OUT / "fig_p2p_adapter_types.png", bbox_inches="tight")
    plt.close(fig)
    print("  ✔ fig_p2p_adapter_types.png")


# ──────────────────────────────────────────────────────────────
# 2) DHT Lookup Sequence (Kademlia)
# ──────────────────────────────────────────────────────────────
def draw_dht_lookup():
    fig, axes = plt.subplots(1, 4, figsize=(10, 2.8))

    node_x = [0.15, 0.36, 0.50, 0.65, 0.85]
    node_y = [0.50, 0.45, 0.55, 0.35, 0.65]

    titles = ["Step 1\nInitial Query", "Step 2\nProbe Closest",
              "Step 3\nIterate", "Step 4\nFound!"]

    for idx, ax in enumerate(axes):
        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1)
        ax.set_facecolor("#fafafa")
        ax.set_title(titles[idx], fontsize=8)

        # DHT ring
        circle = plt.Circle((0.5, 0.5), 0.42, fill=False, edgecolor="#e0e0e0", lw=10)
        ax.add_patch(circle)
        labels = ["Query node", "Closest\nnode", "Near\nnode", "Target\nadapter"]
        steps_to_highlight = min(idx + 2, len(node_x))
        for i, (nx, ny) in enumerate(zip(node_x[:steps_to_highlight], node_y[:steps_to_highlight])):
            col = "#4C72B0" if i < steps_to_highlight else "#cccccc"
            sz = 120 if i == 0 else 80 + 10 * (steps_to_highlight - i)
            ax.scatter(nx, ny, s=sz, color=col if i < steps_to_highlight else "#e0e0e0",
                        edgecolors="#555555" if i < steps_to_highlight else "#dddddd",
                        linewidth=0.5, zorder=5)
            ax.text(nx, ny - 0.08, labels[i] if i < len(labels) else "",
                    ha="center", va="top", fontsize=6, color="#666666")

        visited = min(idx + 2, len(node_x))
        for j in range(visited - 1):
            ax.annotate("", xy=(node_x[j+1], node_y[j+1]),
                        xytext=(node_x[j], node_y[j]),
                        arrowprops=dict(arrowstyle="->", color="#C44E52", lw=0.8))

        ax.set_xticks([])
        ax.set_yticks([])
        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)
        ax.spines["left"].set_visible(False)
        ax.spines["bottom"].set_visible(False)

    fig.text(0.5, -0.05,
        "DHT lookup: query node iteratively probes closer peers until finding the target adapter.",
        ha="center", va="top", fontsize=7, color="#666666")
    fig.tight_layout(pad=2)
    fig.savefig(OUT / "fig_p2p_dht_lookup.png", bbox_inches="tight")
    plt.close(fig)
    print("  ✔ fig_p2p_dht_lookup.png")


# ──────────────────────────────────────────────────────────────
# 3) Gossip propagation rounds
# ──────────────────────────────────────────────────────────────
def draw_gossip():
    fig, axes = plt.subplots(1, 3, figsize=(9, 2.8))

    np.random.seed(42)
    positions = np.asarray([
        [0.3, 0.8], [0.7, 0.85], [0.5, 0.5], [0.2, 0.45],
        [0.6, 0.3], [0.3, 0.15], [0.7, 0.6], [0.85, 0.35]
    ])
    edges = [
        (0, 1), (0, 3), (1, 2), (2, 3),
        (2, 6), (3, 4), (4, 6), (5, 3), (5, 7), (6, 7)
    ]
    colors_infected = ["#C44E52", "#C44E52", "#DD8452", "#55A868", "#4C72B0",
                       "#4C72B0", "#C44E52", "#55A868"]

    titles = ["Round 1", "Round 2", "Round 3"]

    for idx_round, ax in enumerate(axes):
        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1)
        ax.set_facecolor("#fafafa")

        for (u, v) in edges:
            ax.plot([positions[u][0], positions[v][0]],
                     [positions[u][1], positions[v][1]],
                     color="#cccccc", lw=0.5)

        if idx_round == 0:
            infected_mask = [True, False, False, False, False, False, False, False]
        elif idx_round == 1:
            infected_mask = [True, True, False, True, True, False, False, False]
        else:
            infected_mask = [True, True, True, True, True, True, True, True]

        for i, pos in enumerate(positions):
            if infected_mask[i]:
                ax.scatter(pos[0], pos[1], s=120,
                          color=colors_infected[i], edgecolors="#555555",
                          linewidth=0.5, zorder=5)
            else:
                ax.scatter(pos[0], pos[1], s=80,
                          color="#cccccc", edgecolors="#999999",
                          linewidth=0.5, zorder=5)
            ax.text(pos[0], pos[1]-0.07, f"{i+1}", ha="center", va="top",
                    fontsize=6, color="#666666")

        ax.set_title(titles[idx_round], fontsize=8)
        ax.set_xticks([])
        ax.set_yticks([])
        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)
        ax.spines["left"].set_visible(False)
        ax.spines["bottom"].set_visible(False)

    fig.text(0.5, -0.05,
        "Gossip propagation: infected peers spread adapter metadata to randomly chosen neighbours each round",
        ha="center", va="top", fontsize=7, color="#666666")
    fig.tight_layout(pad=2)
    fig.savefig(OUT / "fig_p2p_gossip.png", bbox_inches="tight")
    plt.close(fig)
    print("  ✔ fig_p2p_gossip.png")


# ──────────────────────────────────────────────────────────────
# 4) Adapter as exchange unit (bridge between PEFT and P2P)
# ──────────────────────────────────────────────────────────────
def draw_adapter_bridge():
    fig, ax = plt.subplots(1, 1, figsize=(8, 3.5))

    # PEFT methods icon (left)
    ax.text(0.05, 0.7, "PEFT\nMethods", fontsize=7, ha="center", va="center",
            fontweight="bold",
            bbox=dict(boxstyle="round,pad=0.3", facecolor="#4C72B0",
                      edgecolor="#2a5a8a", lw=1))
    ax.text(0.05, 0.5, "Bottleneck\nAdapter", fontsize=6, ha="center", va="center",
            bbox=dict(boxstyle="round,pad=0.2", facecolor="#4C72B0",
                      edgecolor="#2a5a8a", lw=0.5, alpha=0.6))
    ax.text(0.05, 0.3, "LoRA\n$\\Delta W = BA$", fontsize=6, ha="center", va="center",
            bbox=dict(boxstyle="round,pad=0.2", facecolor="#4C72B0",
                      edgecolor="#2a5a8a", lw=0.5, alpha=0.6))

    # Adapter as central unit
    rect = FancyBboxPatch((0.35, 0.15), 0.3, 0.7,
                           boxstyle="round,pad=0.2", fill=True,
                           facecolor="#DD8452", edgecolor="#a35b1f", lw=1)
    ax.add_patch(rect)
    ax.text(0.5, 0.5, "Adapter as\nAtomic Unit:\nweights + metadata\n+ capability",
            ha="center", va="center", fontsize=7, fontweight="bold",
            color="white")

    # P2P components (right)
    ax.text(0.85, 0.7, "P2P\nNetwork", fontsize=7, ha="center", va="center",
            fontweight="bold",
            bbox=dict(boxstyle="round,pad=0.3", facecolor="#55A868",
                      edgecolor="#2a5a8a", lw=1))
    ax.text(0.85, 0.5, "DHT lookup\nGossip prop.\nNo central coord.",
            fontsize=6, ha="center", va="center",
            bbox=dict(boxstyle="round,pad=0.3", facecolor="#55A868",
                      edgecolor="#3d7a4e", lw=0.5))
    ax.text(0.85, 0.3, "Decentralized\nMarketplace",
            fontsize=6, ha="center", va="center",
            bbox=dict(boxstyle="round,pad=0.2", facecolor="#55A868",
                      edgecolor="#3d7a4e", lw=0.5))

    # Arrows
    ax.annotate("", xy=(0.32, 0.55), xytext=(0.65, 0.55),
                arrowprops=dict(arrowstyle="->", color="#C44E52", lw=0.8))
    ax.annotate("", xy=(0.35, 0.45), xytext=(0.08, 0.5),
                arrowprops=dict(arrowstyle="->", color="#C44E52", lw=0.8))

    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_axis_off()
    fig.suptitle("Bridge Between PEFT and P2P: The Adapter as Exchange Unit",
                 fontsize=10, y=1.02)
    fig.tight_layout(pad=1.5)
    fig.savefig(OUT / "fig_p2p_bridge.png", bbox_inches="tight")
    plt.close(fig)
    print("  ✔ fig_p2p_bridge.png")


if __name__ == "__main__":
    print("Generating P2P concept figures...")
    draw_adapter_structures()
    draw_dht_lookup()
    draw_gossip()
    draw_adapter_bridge()
    print(f"All figures saved to {OUT.resolve()}")