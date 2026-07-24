#!/usr/bin/env python3
"""Rebuild the power-command figures with the command axis in volts.

The LabVIEW VI logs the generator power command in a column headed
``Power Control (mA)``, but that header is a mislabel: per the operators
(R. Weber, C. Nyborg, relayed by R. Guymon, PR #12, 2026-07-24), the
command was generated on the DAQ's 0--5 V analog-output scale, not as a
loop current. The logged values are therefore volts: 0.43--0.74 V during
the calibration soaks and about 1.6 V during the representative
IFrun079 soak -- one consistent scale that also resolves why IFrun079's
values could never be a 0--1 fraction. Only the unit labels change; the
data and the fit's R^2 are untouched. A secondary top axis gives the
equivalent percent of full scale (V / 5 V x 100).

This supersedes build_power_figures_percent.py, which briefly relabeled
the calibration axis as percent under the earlier fraction reading.

Reads the per-run CSV traces in ``docs/data_log/processed/csv/``
(produced by ``build_run_traces.py`` on the data-import branch; the CSV
column name ``power_mA`` is kept to match the raw log header) and
rewrites ``paper/figures/fig_calibration.png`` (SI Fig. S4) and
``paper/figures/fig_representative.png`` (SI Fig. S5). Soak-window
logic and cohort are identical to ``build_validation_figures.py``.

Usage::

    python3 paper/build_power_figures_volts.py
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
REPRESENTATIVE = "IFrun079_Ni4N5_084_1300C_12h"
BAND = 15.0  # +/- deg C deadband used to define the soak window
FULL_SCALE_V = 5.0  # DAQ analog-output full scale


def load_trace(stem: str):
    t, p, temp = [], [], []
    with (CSV_DIR / f"{stem}.csv").open(newline="") as fh:
        for row in csv.DictReader(fh):
            try:
                t.append(float(row["elapsed_s"]))
                p.append(float(row["power_mA"]))  # logged value is volts
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


def add_percent_axis(ax):
    sec = ax.secondary_xaxis(
        "top",
        functions=(lambda v: v / FULL_SCALE_V * 100.0,
                   lambda p: p / 100.0 * FULL_SCALE_V),
    )
    sec.set_xlabel("Power command (% of full scale)", fontsize=8)
    sec.tick_params(labelsize=8)
    return sec


def fig_calibration():
    xs, ys, xerr = [], [], []
    for stem in CALIBRATION:
        t, p, temp = load_trace(stem)
        idx = soak_indices(temp, setpoint_from_stem(stem))
        xs.append(mean([p[i] for i in idx]))
        ys.append(mean([temp[i] for i in idx]))
        xerr.append(std([p[i] for i in idx]))
    slope, intercept, r2 = linregress(xs, ys)
    fig, ax = plt.subplots(figsize=(5.0, 3.8))
    ax.errorbar(xs, ys, xerr=xerr, fmt="o", color="#1f77b4", capsize=3, zorder=3)
    xline = [min(xs) - 0.02, max(xs) + 0.02]
    ax.plot(xline, [intercept + slope * x for x in xline], "--", color="#444",
            label=f"T = {intercept:.0f} + {slope:.0f}·V  (R² = {r2:.3f})")
    for s, x, y in zip(CALIBRATION, xs, ys):
        nominal = s.split("_")[3]  # e.g. "1200C"
        ax.annotate(nominal.replace("C", " °C"), (x, y),
                    textcoords="offset points",
                    xytext=(6, -10), fontsize=7, color="#333")
    ax.set_xlabel("Soak-mean power command (V, 0–5 V DAQ scale)")
    ax.set_ylabel("Soak-mean pyrometer temperature (°C)")
    ax.set_title("Power-command → temperature (fixed Ni4N5 configuration)",
                 fontsize=10, pad=28)
    add_percent_axis(ax)
    ax.legend(fontsize=8, loc="upper left")
    ax.grid(alpha=0.3)
    fig.tight_layout()
    fig.savefig(FIG_DIR / "fig_calibration.png", dpi=200)
    plt.close(fig)
    print(f"calibration fit: T = {intercept:.1f} + {slope:.1f}*V, R2 = {r2:.4f}")
    print("soak means (V):", [round(x, 3) for x in xs])


def fig_representative():
    t, p, temp = load_trace(REPRESENTATIVE)
    setpoint = setpoint_from_stem(REPRESENTATIVE)
    idx = soak_indices(temp, setpoint)
    st = [temp[i] for i in idx]
    times = [t[i] for i in idx]
    # least-squares drift over the soak window, deg C per hour
    slope, _, _ = linregress([x / 3600.0 for x in times], st)
    th = [x / 3600.0 for x in t]
    fig, (a1, a2) = plt.subplots(2, 1, figsize=(5.4, 4.4), sharex=True,
                                 gridspec_kw={"height_ratios": [2, 1]})
    a1.plot(th, temp, color="#d62728", lw=0.8)
    a1.axhline(setpoint, ls="--", color="#555", lw=0.8,
               label=f"setpoint {setpoint:.0f} °C")
    a1.set_ylabel("Temperature (°C)")
    a1.legend(fontsize=8, loc="lower right")
    a1.grid(alpha=0.3)
    a1.set_title(f"Representative closed-loop 12 h soak\n"
                 f"soak {mean(st):.1f} ± {std(st):.1f} °C, "
                 f"drift {slope:+.3f} °C/h", fontsize=9)
    a2.plot(th, p, color="#1f77b4", lw=0.8)
    a2.set_ylabel("Power cmd (V)")
    a2.set_xlabel("Elapsed time (h)")
    a2.grid(alpha=0.3)
    fig.tight_layout()
    fig.savefig(FIG_DIR / "fig_representative.png", dpi=200)
    plt.close(fig)
    sp_soak = [p[i] for i in idx]
    print(f"representative soak: {mean(st):.1f} +/- {std(st):.1f} C, "
          f"drift {slope:+.3f} C/h, power {mean(sp_soak):.2f} V "
          f"({mean(sp_soak) / FULL_SCALE_V * 100:.0f}% of full scale)")


if __name__ == "__main__":
    fig_calibration()
    fig_representative()
