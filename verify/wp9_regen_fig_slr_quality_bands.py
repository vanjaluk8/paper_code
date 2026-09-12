import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

labels = ["High (9-10)", "Upper-mid (6-8)", "Lower-mid (3-5)", "Low (0-2)"]
values = [13, 59, 46, 2]
colors = ["#2e7d32", "#8bc34a", "#f9a825", "#c62828"]

fig, ax = plt.subplots(figsize=(9.5, 6))
bars = ax.bar(labels, values, color=colors, width=0.6)
for bar, v in zip(bars, values):
    ax.text(bar.get_x() + bar.get_width()/2, v + 1.2, str(v),
            ha="center", va="bottom", fontsize=15, fontweight="bold")

ax.set_ylabel("Papers", fontsize=13)
ax.set_ylim(0, 75)
ax.set_title("Reporting-completeness score distribution (N = 120, score 0–10)",
             fontsize=15, fontweight="bold")
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.tick_params(axis="both", labelsize=12)
plt.tight_layout()
plt.savefig("/tmp/fig_slr_quality_bands_new.pdf")
print("done")
