#!/usr/bin/env python3
"""Rebuild the calibration figure with the command axis in percent.

The LabVIEW VI logs the generator power command in a column headed
``Power Control (mA)``, but the logged values in the calibration runs
(0.43--0.74 during soaks, 0.001 at idle) cannot be a physical 4--20 mA
loop current. Per the operators (C. Nyborg, R. Weber, confirmed by
R. Guymon, PR #12, 2026-07-24), the software command was a power
*percentage*; the logged value is the fractional command (0--1), so it
is plotted here scaled by 100 as percent of full scale. Only the unit
label and scale change; the data and the fit's R^2 are untouched.

Deliberately NOT converted: ``fig_representative.png`` (SI Fig. S5).
Its run (IFrun079) logs soak values around 1.5 in the same column --
already impossible as a 0--1 fraction -- so that run's logging scale is
still unresolved and its figure is left as archived.

Reads the per-run CSV traces in ``docs/data_log/processed/csv/``
(produced by ``build_run_traces.py`` on the data-import branch; the
column name ``power_mA`` is kept there to match the raw log header) and
rewrites ``paper/figures/fig_calibration.png`` (SI Fig. S4). The
soak-window logic and cohort are identical to
``build_validation_figures.py``.

Usage::

    python3 paper/build_power_figures_percent.py
"""
from __future__ import annotations

import csv
import math
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parent.parent
CSV_DIR = ROOT / "docs" / "data_log" / "processed" / "csv"
FIG_DIR = Path(__file__).resolve().parent / "figures"

CALIBRATION = [
    "IFrun039_Ni4N5_026_1200C_6h",
    "IFrun040_Ni4N5_027_1250C_6h",
    "IFrun038_Ni4N5_025_1300C_1h",
    "IFrun032_Ni4N5_022_1400C_10min",
]
BAND = 15.0  # +/- deg C deadband used to define the soak window


def load_trace(stem: str):
    t, p, temp = [], [], []
    with (CSV_DIR / f"{stem}.csv").open(newline="") as fh:
        for row in csv.DictReader(fh):
            try:
                t.append(float(row["elapsed_s"]))
                p.append(100.0 * float(row["power_mA"]))  # fraction -> percent
                temp.append(float(row["temperature_C"]))
            except (ValueError, KeyError):
                continue
    return t, p, temp


def setpoint_from_stem(stem: str) -> float | None:
    for tok in stem.split("_"):
        if tok.endswith("C") and tok[:-1].isdigit():
            return float(tok[:-1])
    return None


def soak_indices(temp, setpoint):
    reached = next((i for i, v in enumerate(temp) if v >= setpoint - BAND), None)
    if reached is None:
        return []
    return [i for i in range(reached, len(temp)) if abs(temp[i] - setpoint) <= BAND]


def mean(xs):
    return sum(xs) / len(xs)


def std(xs):
    m = mean(xs)
    return math.sqrt(sum((x - m) ** 2 for x in xs) / (len(xs) - 1))


def linregress(xs, ys):
    mx, my = mean(xs), mean(ys)
    sxx = sum((x - mx) ** 2 for x in xs)
    sxy = sum((x - mx) * (y - my) for x, y in zip(xs, ys))
    slope = sxy / sxx
    intercept = my - slope * mx
    ss_tot = sum((y - my) ** 2 for y in ys)
    ss_res = sum((y - (intercept + slope * x)) ** 2 for x, y in zip(xs, ys))
    return slope, intercept, 1 - ss_res / ss_tot


def fig_calibration():
    xs, ys, xerr = [], [], []
    for stem in CALIBRATION:
        t, p, temp = load_trace(stem)
        idx = soak_indices(temp, setpoint_from_stem(stem))
        xs.append(mean([p[i] for i in idx]))
        ys.append(mean([temp[i] for i in idx]))
        xerr.append(std([p[i] for i in idx]))
    slope, intercept, r2 = linregress(xs, ys)
    fig, ax = plt.subplots(figsize=(5.0, 3.6))
    ax.errorbar(xs, ys, xerr=xerr, fmt="o", color="#1f77b4", capsize=3, zorder=3)
    xline = [min(xs) - 2.0, max(xs) + 2.0]
    ax.plot(xline, [intercept + slope * x for x in xline], "--", color="#444",
            label=f"T = {intercept:.0f} + {slope:.2f}·P  (R² = {r2:.3f})")
    for s, x, y in zip(CALIBRATION, xs, ys):
        nominal = s.split("_")[3]  # e.g. "1200C"
        ax.annotate(nominal.replace("C", " °C"), (x, y),
                    textcoords="offset points",
                    xytext=(6, -10), fontsize=7, color="#333")
    ax.set_xlabel("Soak-mean power command (% of full scale)")
    ax.set_ylabel("Soak-mean pyrometer temperature (°C)")
    ax.set_title("Power-command → temperature\n(fixed Ni4N5 configuration)", fontsize=10)
    ax.legend(fontsize=8, loc="upper left")
    ax.grid(alpha=0.3)
    fig.tight_layout()
    fig.savefig(FIG_DIR / "fig_calibration.png", dpi=200)
    plt.close(fig)
    print(f"calibration fit: T = {intercept:.1f} + {slope:.3f}*P (%), R2 = {r2:.4f}")


if __name__ == "__main__":
    fig_calibration()
