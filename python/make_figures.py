"""Matplotlib figures for the book (figures 3.1, 4.1, 5.1). Palette: docs/STYLE_GUIDE.md section 6.

Run from the project root:  python python/make_figures.py
Figure 5.1 is drawn from python/data/digits_accuracy.csv (run generate_chart.py first).
"""
import csv, re
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "assets" / "charts"
MIDNIGHT, TURQ, VIOLET, GOLD, PAPER = "#101B35", "#00C9C8", "#7956D8", "#E4B65C", "#F5F7FA"

plt.rcParams.update({
    "pdf.fonttype": 42, "ps.fonttype": 42,           # TrueType, not Type 3
    "font.family": "Assistant", "font.size": 10,
    "axes.edgecolor": MIDNIGHT, "axes.labelcolor": MIDNIGHT, "text.color": MIDNIGHT,
    "xtick.color": MIDNIGHT, "ytick.color": MIDNIGHT,
    "axes.facecolor": PAPER, "figure.facecolor": PAPER, "savefig.facecolor": PAPER,
    "axes.spines.top": False, "axes.spines.right": False, "axes.grid": True,
    "grid.color": "#D5DAE3", "grid.linewidth": 0.6,
})

_RTL = re.compile(r"[֐-׿]")


def he(text: str) -> str:
    """Visual-order a one-line label for Matplotlib (which has no bidi support).

    Splits into Hebrew and non-Hebrew runs, reverses run order and the characters of
    Hebrew runs only; Latin words and numbers keep their internal order. Mirrors brackets.
    """
    runs = re.findall(r"[֐-׿\s'\"״׳-]+|[^֐-׿]+", text)
    out = []
    for r in reversed(runs):
        if _RTL.search(r):
            out.append(r[::-1])
        else:
            out.append(r)
    s = "".join(out).translate(str.maketrans("()", ")("))
    return s.strip()


def _save(fig, name):
    OUT.mkdir(parents=True, exist_ok=True)
    fig.savefig(OUT / f"{name}.pdf", bbox_inches="tight")
    fig.savefig(OUT / f"{name}.png", dpi=200, bbox_inches="tight")
    plt.close(fig)


def fig3_1():
    z = np.linspace(-5, 5, 401)
    funcs = [("Sigmoid", 1 / (1 + np.exp(-z)), (-0.1, 1.1)),
             ("tanh", np.tanh(z), (-1.15, 1.15)),
             ("ReLU", np.maximum(0, z), (-0.4, 5.2))]
    fig, axes = plt.subplots(1, 3, figsize=(7.2, 2.4))
    for ax, (name, val, ylim) in zip(axes, funcs):
        ax.axvline(0, color=MIDNIGHT, lw=0.6, alpha=0.5)
        ax.plot(z, val, color=TURQ, lw=2.2)
        z0 = {"Sigmoid": 0.5, "tanh": 0.0, "ReLU": 0.0}[name]
        ax.plot([0], [z0], "o", ms=7, color=GOLD, mec=MIDNIGHT, mew=0.6, zorder=5)
        ax.set_title(name, fontsize=11, color=MIDNIGHT)
        ax.set_xlabel("z"); ax.set_ylim(*ylim); ax.set_xlim(-5, 5)
    axes[0].set_ylabel("f(z)")
    fig.tight_layout()
    _save(fig, "fig3_1_activations")


def softmax_t(p_at_t1, t):
    logits = np.log(p_at_t1)          # scores chosen so that softmax at t=1 reproduces p
    e = np.exp(logits / t)
    return e / e.sum()


def fig4_1():
    labels = ["כמה", "מספר", "סיבות", "לא"]
    named = np.array([0.46, 0.22, 0.12, 0.05])
    # "כל השאר" (0.15) is modelled as 15 further tokens of 0.01 each, so temperature acts on
    # every token separately (see R-ch04-10); their sum is shown as one bar.
    p1 = np.concatenate([named, np.full(15, 0.01)])
    rows = {}
    for t in (1.0, 0.5):
        q = softmax_t(p1, t)
        rows[t] = np.concatenate([q[:4], [q[4:].sum()]])
    x = np.arange(5)
    w = 0.38
    fig, ax = plt.subplots(figsize=(6.4, 3.0))
    # RTL reading order: first candidate on the right.
    xr = x[::-1]
    for i, (t, col) in enumerate(((1.0, TURQ), (0.5, VIOLET))):
        bars = ax.bar(xr + (w / 2 if i == 0 else -w / 2), rows[t], w, color=col,
                      label=f"t = {t:g}", edgecolor=MIDNIGHT, linewidth=0.4)
        bars[0].set_edgecolor(GOLD); bars[0].set_linewidth(2.4)   # chosen token "כמה"
        for b, v in zip(bars, rows[t]):
            ax.text(b.get_x() + b.get_width() / 2, v + 0.012, f"{v:.2f}", ha="center", fontsize=8)
    ax.set_xticks(xr, [he(l) for l in labels] + [he("כל השאר")])
    ax.set_ylabel(he("הסתברות"))
    ax.set_ylim(0, 0.88)
    from matplotlib.patches import Patch
    ax.legend(handles=[Patch(facecolor=TURQ, edgecolor=MIDNIGHT, lw=0.4, label="t = 1"),
                       Patch(facecolor=VIOLET, edgecolor=MIDNIGHT, lw=0.4, label="t = 0.5"),
                       Patch(facecolor="none", edgecolor=GOLD, lw=2.4, label=he("הטוקן שנבחר"))],
              frameon=False, loc="upper left")
    ax.text(0.5, 0.97, he("נתוני הדגמה, לא פלט של מודל"), transform=ax.transAxes,
            ha="center", va="top", fontsize=8.5, style="italic")
    fig.tight_layout()
    _save(fig, "fig4_1_temperature")
    return rows


def fig5_1(rows=None):
    if rows is None:
        with (ROOT / "python" / "data" / "digits_accuracy.csv").open(encoding="utf-8") as f:
            rows = [{k: float(v) for k, v in r.items()} for r in csv.DictReader(f)]
    ep = [int(r["epoch"]) for r in rows]
    tr = [r["train_accuracy"] for r in rows]
    te = [r["test_accuracy"] for r in rows]
    # Highlighted point chosen by a fixed rule (not by eye): the epoch with the widest
    # train-test gap, earliest on ties.
    gaps = [a - b for a, b in zip(tr, te)]
    k = int(np.argmax(gaps))
    fig, ax = plt.subplots(figsize=(6.4, 3.3))
    ax.plot(ep, tr, color=TURQ, lw=2.2, label=he("דיוק אימון"))
    ax.plot(ep, te, color=VIOLET, lw=2.2, label=he("דיוק בדיקה"))
    ax.plot([ep[k]], [te[k]], "o", ms=8, color=GOLD, mec=MIDNIGHT, mew=0.7, zorder=5)
    ax.plot([ep[k], ep[k]], [te[k], tr[k]], color=GOLD, lw=1.6, zorder=4)
    label = chr(10).join([he(f"תקופה {ep[k]}"), he(f"אימון {tr[k]:.3f}"), he(f"בדיקה {te[k]:.3f}")])
    ax.annotate(label,
                xy=(ep[k], te[k]), xytext=(ep[k] + 3 if ep[k] < 25 else ep[k] - 16, te[k] - 0.12),
                fontsize=8.5, arrowprops=dict(arrowstyle="-", color=MIDNIGHT, lw=0.6))
    ax.set_xlabel(he("תקופת אימון") + " (epoch)")
    ax.set_ylabel(he("דיוק"))
    lo = min(min(tr), min(te))
    ax.set_ylim(max(0.0, lo - 0.05), 1.01)
    ax.set_xlim(0.5, ep[-1] + 0.5)
    ax.legend(frameon=False, loc="lower right")
    fig.tight_layout()
    _save(fig, "fig5_1_accuracy")
    return k


if __name__ == "__main__":
    fig3_1()
    print("fig4_1 values:", {t: [round(float(v), 3) for v in r] for t, r in fig4_1().items()})
    fig5_1()
