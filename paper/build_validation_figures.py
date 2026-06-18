#!/usr/bin/env python3
"""Build HardwareX validation figures and metrics from the archived run logs.

Reproducible: reads the per-run CSV traces in
``docs/data_log/processed/csv/`` (produced by ``build_run_traces.py``) and the
run summary, then writes figures to ``paper/figures/`` and a machine-readable
``paper/validation-metrics.json`` plus a human-readable
``paper/validation-metrics.md``.

The cohorts, runs, and analysis approach follow the Edison Analysis
data-incorporation review (``paper/edison-feedback/data-incorporation-suggestions.md``):
all comparisons are restricted to internally consistent subsets and the
power->temperature calibration is reported only for one fixed configuration.

Usage::

    python3 paper/build_validation_figures.py
"""
from __future__ import annotations

import csv
import json
import math
import os
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parent.parent
CSV_DIR = ROOT / "docs" / "data_log" / "processed" / "csv"
SUMMARY = ROOT / "docs" / "data_log" / "processed" / "run_summary.csv"
FIG_DIR = Path(__file__).resolve().parent / "figures"
FIG_DIR.mkdir(parents=True, exist_ok=True)

# Cohorts identified by the Edison review (run -> CSV basename without suffix).
CALIBRATION = [
    "IFrun039_Ni4N5_026_1200C_6h",
    "IFrun040_Ni4N5_027_1250C_6h",
    "IFrun038_Ni4N5_025_1300C_1h",
    "IFrun032_Ni4N5_022_1400C_10min",
]
REPRESENTATIVE = "IFrun079_Ni4N5_084_1300C_12h"
REPEATABILITY = [
    "IFrun052_Ni4N5_040_1200C_12h",
    "IFrun054_Ni4N5_042,044_1200C_12h",
    "IFrun055_Ni4N5_045,046_1200C_12h",
    "IFrun056_Ni4N5_047,048_1200C_12h",
    "IFrun057_Ni4N5_049,050_1200C_12h",
    "IFrun058_Ni4N5_051,052_1200C_12h",
    "IFrun059_Ni4N5_053,054_1200C_12h",
    "IFrun060_Ni4N5_056,057_1200C_12h",
]
LONG_SOAK = [
    "IFrun081_Ni200_015_1325C_20h",
    "IFrun080_Ni200_017_1325C_40h",
]
BAND = 15.0  # +/- deg C deadband used to define the soak window


def load_trace(stem: str):
    path = CSV_DIR / f"{stem}.csv"
    t, p, temp = [], [], []
    with path.open(newline="") as fh:
        for row in csv.DictReader(fh):
            try:
                t.append(float(row["elapsed_s"]))
                p.append(float(row["power_mA"]))
                temp.append(float(row["temperature_C"]))
            except (ValueError, KeyError):
                continue
    return t, p, temp


def setpoint_from_stem(stem: str) -> float | None:
    for tok in stem.split("_"):
        if tok.endswith("C") and tok[:-1].isdigit():
            return float(tok[:-1])
    return None


def soak_indices(t, temp, setpoint):
    """Indices where temperature is within BAND of setpoint after first reaching it."""
    if setpoint is None:
        return []
    reached = None
    for i, v in enumerate(temp):
        if v >= setpoint - BAND:
            reached = i
            break
    if reached is None:
        return []
    return [i for i in range(reached, len(temp)) if abs(temp[i] - setpoint) <= BAND]


def mean(xs):
    return sum(xs) / len(xs) if xs else float("nan")


def std(xs):
    if len(xs) < 2:
        return 0.0
    m = mean(xs)
    return math.sqrt(sum((x - m) ** 2 for x in xs) / (len(xs) - 1))


def linregress(xs, ys):
    n = len(xs)
    mx, my = mean(xs), mean(ys)
    sxx = sum((x - mx) ** 2 for x in xs)
    sxy = sum((x - mx) * (y - my) for x, y in zip(xs, ys))
    slope = sxy / sxx
    intercept = my - slope * mx
    ss_tot = sum((y - my) ** 2 for y in ys)
    ss_res = sum((y - (intercept + slope * x)) ** 2 for x, y in zip(xs, ys))
    r2 = 1 - ss_res / ss_tot if ss_tot else float("nan")
    return slope, intercept, r2


def soak_metrics(stem):
    t, p, temp = load_trace(stem)
    sp = setpoint_from_stem(stem)
    idx = soak_indices(t, temp, sp)
    if not idx:
        return None
    st = [temp[i] for i in idx]
    sp_pow = [p[i] for i in idx]
    times = [t[i] for i in idx]
    # linear drift in deg C/h over the soak window
    drift = float("nan")
    if len(times) > 2 and times[-1] != times[0]:
        slope, _, _ = linregress(times, st)
        drift = slope * 3600.0
    # rise time 10-90% of setpoint relative to start temperature
    start_t = temp[0]
    rise = float("nan")
    if sp is not None:
        lo = start_t + 0.1 * (sp - start_t)
        hi = start_t + 0.9 * (sp - start_t)
        t_lo = next((t[i] for i in range(len(temp)) if temp[i] >= lo), None)
        t_hi = next((t[i] for i in range(len(temp)) if temp[i] >= hi), None)
        if t_lo is not None and t_hi is not None:
            rise = t_hi - t_lo
    overshoot = max(temp) - sp if sp is not None else float("nan")
    return {
        "setpoint_C": sp,
        "soak_mean_C": round(mean(st), 2),
        "soak_sd_C": round(std(st), 2),
        "soak_mean_power_mA": round(mean(sp_pow), 4),
        "power_sd_mA": round(std(sp_pow), 4),
        "max_dev_C": round(max(abs(v - sp) for v in st), 1) if sp is not None else None,
        "drift_C_per_h": round(drift, 4),
        "rise_time_s": round(rise, 0) if not math.isnan(rise) else None,
        "overshoot_C": round(overshoot, 1) if sp is not None else None,
        "soak_minutes_in_band": round((times[-1] - times[0]) / 60.0, 1),
    }


def fig_calibration(metrics):
    xs = [metrics[s]["soak_mean_power_mA"] for s in CALIBRATION]
    ys = [metrics[s]["soak_mean_C"] for s in CALIBRATION]
    xerr = [metrics[s]["power_sd_mA"] for s in CALIBRATION]
    slope, intercept, r2 = linregress(xs, ys)
    fig, ax = plt.subplots(figsize=(5.0, 3.6))
    ax.errorbar(xs, ys, xerr=xerr, fmt="o", color="#1f77b4", capsize=3, zorder=3)
    xline = [min(xs) - 0.02, max(xs) + 0.02]
    ax.plot(xline, [intercept + slope * x for x in xline], "--", color="#444",
            label=f"T = {intercept:.0f} + {slope:.0f}\u00b7I  (R\u00b2 = {r2:.3f})")
    for s, x, y in zip(CALIBRATION, xs, ys):
        ax.annotate(s.split("_")[0], (x, y), textcoords="offset points",
                    xytext=(6, -10), fontsize=7, color="#333")
    ax.set_xlabel("Soak-mean analog power command (mA)")
    ax.set_ylabel("Soak-mean pyrometer temperature (\u00b0C)")
    ax.set_title("Power-command \u2192 temperature (fixed Ni4N5 configuration)")
    ax.legend(fontsize=8, loc="upper left")
    ax.grid(alpha=0.3)
    fig.tight_layout()
    fig.savefig(FIG_DIR / "fig_calibration.png", dpi=200)
    plt.close(fig)
    return {"slope": round(slope, 1), "intercept": round(intercept, 1),
            "r2": round(r2, 3), "n": len(xs)}


def fig_representative(stem, m):
    t, p, temp = load_trace(stem)
    th = [x / 3600.0 for x in t]
    fig, (a1, a2) = plt.subplots(2, 1, figsize=(5.4, 4.4), sharex=True,
                                 gridspec_kw={"height_ratios": [2, 1]})
    a1.plot(th, temp, color="#d62728", lw=0.8)
    if m["setpoint_C"]:
        a1.axhline(m["setpoint_C"], ls="--", color="#555", lw=0.8,
                   label=f"setpoint {m['setpoint_C']:.0f} \u00b0C")
    a1.set_ylabel("Temperature (\u00b0C)")
    a1.legend(fontsize=8, loc="lower right")
    a1.grid(alpha=0.3)
    a1.set_title(f"{stem.split('_')[0]}: closed-loop 12 h soak\n"
                 f"soak {m['soak_mean_C']:.1f} \u00b1 {m['soak_sd_C']:.1f} \u00b0C, "
                 f"drift {m['drift_C_per_h']:+.3f} \u00b0C/h", fontsize=9)
    a2.plot(th, p, color="#1f77b4", lw=0.8)
    a2.set_ylabel("Power cmd (mA)")
    a2.set_xlabel("Elapsed time (h)")
    a2.grid(alpha=0.3)
    fig.tight_layout()
    fig.savefig(FIG_DIR / "fig_representative.png", dpi=200)
    plt.close(fig)


def fig_repeatability(metrics, summary):
    labels = [s.split("_")[0] for s in REPEATABILITY]
    soak = [metrics[s]["soak_mean_C"] for s in REPEATABILITY]
    m, sd = mean(soak), std(soak)
    fig, ax = plt.subplots(figsize=(5.4, 3.4))
    ax.plot(range(len(soak)), soak, "o", color="#2ca02c", zorder=3)
    ax.axhline(m, color="#444", lw=1)
    ax.axhspan(m - sd, m + sd, color="#2ca02c", alpha=0.15,
               label=f"mean {m:.1f} \u00b1 {sd:.1f} \u00b0C (n={len(soak)})")
    ax.set_xticks(range(len(labels)))
    ax.set_xticklabels(labels, rotation=45, ha="right", fontsize=7)
    ax.set_ylabel("Soak-mean temperature (\u00b0C)")
    ax.set_title("Repeatability: Ni4N5 1200 \u00b0C / 12 h cohort")
    ax.legend(fontsize=8)
    ax.grid(alpha=0.3, axis="y")
    fig.tight_layout()
    fig.savefig(FIG_DIR / "fig_repeatability.png", dpi=200)
    plt.close(fig)
    peaks = [float(summary[s]["peak_temp_C"]) for s in REPEATABILITY]
    durs = [float(summary[s]["duration_min"]) for s in REPEATABILITY]
    return {
        "n": len(soak),
        "soak_mean_C": round(m, 2), "soak_sd_C": round(sd, 2),
        "soak_min_C": round(min(soak), 1), "soak_max_C": round(max(soak), 1),
        "cv_pct": round(100 * sd / m, 3),
        "peak_mean_C": round(mean(peaks), 2), "peak_sd_C": round(std(peaks), 2),
        "duration_mean_min": round(mean(durs), 1), "duration_sd_min": round(std(durs), 1),
    }


def fig_longsoak(metrics):
    fig, ax = plt.subplots(figsize=(5.6, 3.4))
    colors = {"IFrun081_Ni200_015_1325C_20h": "#9467bd",
              "IFrun080_Ni200_017_1325C_40h": "#8c564b"}
    for stem in LONG_SOAK:
        t, _p, temp = load_trace(stem)
        th = [x / 3600.0 for x in t]
        m = metrics[stem]
        ax.plot(th, temp, lw=0.7, color=colors[stem],
                label=f"{stem.split('_')[0]} ({stem.split('_')[-1]}): "
                      f"{m['soak_mean_C']:.1f}\u00b1{m['soak_sd_C']:.1f} \u00b0C")
    ax.axhline(1325, ls="--", color="#555", lw=0.7)
    ax.set_xlabel("Elapsed time (h)")
    ax.set_ylabel("Temperature (\u00b0C)")
    ax.set_title("Long-duration stability (Ni200, 1325 \u00b0C)")
    ax.legend(fontsize=8, loc="lower center")
    ax.grid(alpha=0.3)
    fig.tight_layout()
    fig.savefig(FIG_DIR / "fig_longsoak.png", dpi=200)
    plt.close(fig)


def main():
    summary = {}
    with SUMMARY.open(newline="") as fh:
        for row in csv.DictReader(fh):
            summary[row["run"]] = row

    runs = CALIBRATION + [REPRESENTATIVE] + REPEATABILITY + LONG_SOAK
    metrics = {}
    for stem in runs:
        m = soak_metrics(stem)
        if m is None:
            print(f"WARN: no soak window for {stem}")
            continue
        metrics[stem] = m

    cal = fig_calibration(metrics)
    fig_representative(REPRESENTATIVE, metrics[REPRESENTATIVE])
    rep = fig_repeatability(metrics, summary)
    fig_longsoak(metrics)

    out = {
        "band_C": BAND,
        "calibration": {"runs": CALIBRATION, "fit": cal,
                        "points": {s: metrics[s] for s in CALIBRATION}},
        "representative": {"run": REPRESENTATIVE, "metrics": metrics[REPRESENTATIVE]},
        "repeatability": {"runs": REPEATABILITY, "stats": rep},
        "long_soak": {s: metrics[s] for s in LONG_SOAK},
    }
    (Path(__file__).resolve().parent / "validation-metrics.json").write_text(
        json.dumps(out, indent=2))

    md = ["# Validation metrics (computed from archived run logs)", "",
          "Generated by `build_validation_figures.py` from "
          "`docs/data_log/processed/csv/`. Soak window = within "
          f"\u00b1{BAND:.0f} \u00b0C of the nominal setpoint after first reach.", "",
          "## Power-command \u2192 temperature calibration (fixed Ni4N5 configuration)",
          f"Linear fit over {cal['n']} steady-state points: "
          f"T = {cal['intercept']:.0f} + {cal['slope']:.0f}\u00b7I (mA), "
          f"R\u00b2 = {cal['r2']:.3f}.", "",
          "| Run | Soak mean T (\u00b0C) | Soak mean power (mA) | Power SD (mA) |",
          "|---|---:|---:|---:|"]
    for s in CALIBRATION:
        m = metrics[s]
        md.append(f"| `{s}` | {m['soak_mean_C']:.2f} | "
                  f"{m['soak_mean_power_mA']:.4f} | {m['power_sd_mA']:.4f} |")
    rm = metrics[REPRESENTATIVE]
    md += ["", "## Representative closed-loop soak (`IFrun079`, 1300 \u00b0C / 12 h)",
           f"- soak mean {rm['soak_mean_C']:.2f} \u00b1 {rm['soak_sd_C']:.2f} \u00b0C; "
           f"rise time {rm['rise_time_s']:.0f} s; overshoot {rm['overshoot_C']:.1f} \u00b0C; "
           f"max deviation {rm['max_dev_C']:.1f} \u00b0C; drift {rm['drift_C_per_h']:+.3f} \u00b0C/h.",
           "", "## Repeatability (Ni4N5 1200 \u00b0C / 12 h, n = 8)",
           f"- soak temperature {rep['soak_mean_C']:.1f} \u00b1 {rep['soak_sd_C']:.1f} \u00b0C "
           f"(range {rep['soak_min_C']:.1f}\u2013{rep['soak_max_C']:.1f} \u00b0C; "
           f"CV {rep['cv_pct']:.3f}%); peak {rep['peak_mean_C']:.1f} \u00b1 "
           f"{rep['peak_sd_C']:.1f} \u00b0C; duration {rep['duration_mean_min']:.0f} \u00b1 "
           f"{rep['duration_sd_min']:.0f} min.", "",
           "## Long-duration stability (Ni200, 1325 \u00b0C)"]
    for s in LONG_SOAK:
        m = metrics[s]
        md.append(f"- `{s}`: soak {m['soak_mean_C']:.1f} \u00b1 {m['soak_sd_C']:.1f} \u00b0C, "
                  f"drift {m['drift_C_per_h']:+.4f} \u00b0C/h, "
                  f"{m['soak_minutes_in_band']:.0f} min in-band.")
    (Path(__file__).resolve().parent / "validation-metrics.md").write_text("\n".join(md) + "\n")

    print("Wrote figures to", FIG_DIR)
    print("calibration fit:", cal)
    print("repeatability:", rep)


if __name__ == "__main__":
    main()
