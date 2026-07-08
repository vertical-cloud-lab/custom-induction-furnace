#!/usr/bin/env python3
"""Build the YSZ grain-growth results figure.

Requested by R. Guymon (PR #3, 2026-07-08): a graph conveying grain-growth
results (Ni or YSZ). Uses the quantified YSZ outcomes recorded in the lab's
archived grain-growth survey:

* ``Grain Growth Summary.pdf`` (repo root) --- per-anneal records for the
  tantalum-susceptor induction-furnace configuration:
    - 2500 degC / 45 min:  20 um -> 90 um   (first clean, successful anneal)
    - ~2500 degC / 8 h:   ~10 um -> ~400 um (grain size uncertain: Ta vapor
                                             deposited on the specimen)
    - 2000 degC / 24 h:    10 um -> 20 um
  (The remaining survey entries record failed/contaminated runs with no
  extractable grain size and are therefore not plotted.)
* ``RyanWeber.pdf`` (repo root, lab poster) --- the lab's comparison anneal in
  a commercial 1600 degC box furnace: 10 um -> 80 um in over 228 h.

Rendered as a before->after "dumbbell" per anneal on log time / log grain-size
axes: open marker = grain size before the anneal, filled marker = after.

Output: ``paper/figures/fig_grain_growth.png``.

Usage::

    python3 paper/build_grain_growth_figure.py
"""
from __future__ import annotations

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

FIG_DIR = Path(__file__).resolve().parent / "figures"
FIG_DIR.mkdir(parents=True, exist_ok=True)

BLUE = "#1f77b4"   # induction furnace (matches the manuscript's other figures)
GRAY = "#7f7f7f"   # commercial box-furnace comparison

# (condition label, soak time [h], d_initial [um], d_final [um],
#  final size certain?, color)
ANNEALS = [
    ("2500°C / 45 min", 0.75, 20, 90, True, BLUE),
    ("~2500°C / 8 h", 8.0, 10, 400, False, BLUE),
    ("2000°C / 24 h", 24.0, 10, 20, True, BLUE),
    ("1600°C / 228 h", 228.0, 10, 80, True, GRAY),
]


def build_figure() -> Path:
    fig, ax = plt.subplots(figsize=(3.5, 3.15))

    for name, t_h, d0, d1, certain, color in ANNEALS:
        ax.annotate(
            "", xy=(t_h, d1), xytext=(t_h, d0),
            arrowprops=dict(
                arrowstyle="-|>", color=color, lw=1.4, shrinkA=4, shrinkB=4,
                linestyle="-" if certain else (0, (3, 2)),
            ),
        )
        ax.plot([t_h], [d0], "o", ms=6, mfc="white", mec=color, mew=1.4)
        ax.plot([t_h], [d1], "o" if certain else "o", ms=6,
                mfc=color if certain else "white", mec=color, mew=1.4)
        ax.annotate(name, xy=(t_h, max(d0, d1)), xytext=(0, 7),
                    textcoords="offset points", ha="center", fontsize=7.5,
                    color=color)

    ax.annotate("final size uncertain\n(Ta deposition)", xy=(8.0, 55),
                xytext=(8, 0), textcoords="offset points", ha="left",
                va="center", fontsize=6.5, color=BLUE, style="italic")

    ax.set_xscale("log")
    ax.set_yscale("log")
    ax.set_xlim(0.3, 900)
    ax.set_ylim(6, 900)
    ax.set_xlabel("Soak time (h)")
    ax.set_ylabel("YSZ grain size (µm)")
    ax.grid(True, which="major", lw=0.4, alpha=0.35)

    handles = [
        plt.Line2D([], [], color=BLUE, lw=1.4, marker="o", ms=5, mfc=BLUE,
                   label="This furnace (Ta susceptor)"),
        plt.Line2D([], [], color=GRAY, lw=1.4, marker="o", ms=5, mfc=GRAY,
                   label="Commercial 1600°C box furnace"),
    ]
    # open marker = "before the anneal" is stated in the manuscript caption;
    # the legend sits above the axes so it never covers a data label
    ax.legend(handles=handles, fontsize=7, loc="lower left",
              bbox_to_anchor=(0.0, 1.01), ncol=1, frameon=False,
              borderpad=0, handletextpad=0.6, labelspacing=0.3)

    fig.tight_layout()
    out = FIG_DIR / "fig_grain_growth.png"
    fig.savefig(out, dpi=300)
    plt.close(fig)
    return out


def main() -> int:
    print(f"wrote {build_figure()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
