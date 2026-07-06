#!/usr/bin/env python3
"""Build the tantalum-susceptor (YSZ configuration) heat-curve figure.

Reproducible: reads the committed lab workbook
``docs/YSZ/Tantalum-Heat-Curve.xlsx`` (contributed by R. Guymon, PR #3),
which records pyrometer temperature vs. generator power command for the
tantalum-susceptor stack used for high-temperature ceramic (YSZ) anneals:

* single Ta block, power % -> steady temperature (original and replacement
  power controller);
* two Ta blocks, a timed ramp/soak log (power %, temperature, elapsed time)
  reaching a 2000 degC hold;
* two Ta blocks, a second ramp pushed to 2344 degC at 33 % power, ended by
  the chamber pressure interlock ("Test Failed: Pressure Limit Reached").

Output: ``paper/figures/fig_ta_heatcurve.png``.

Usage::

    python3 paper/build_ysz_figures.py
"""
from __future__ import annotations

import datetime
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import openpyxl

ROOT = Path(__file__).resolve().parent.parent
WORKBOOK = ROOT / "docs" / "YSZ" / "Tantalum-Heat-Curve.xlsx"
FIG_DIR = Path(__file__).resolve().parent / "figures"
FIG_DIR.mkdir(parents=True, exist_ok=True)


def _minutes(t: datetime.time) -> float:
    return t.hour * 60 + t.minute + t.second / 60


def load_series(ws):
    """Parse the four data blocks out of Sheet1 (fixed lab-notebook layout)."""
    rows = list(ws.iter_rows(values_only=True))

    # Block 1 (A/B, rows 2..): single Ta block, original controller.
    single_old = [(r[0], r[1]) for r in rows[1:14]
                  if isinstance(r[0], (int, float)) and isinstance(r[1], (int, float))]
    # Block 2 (E/F, rows 2..): single Ta block, replacement controller.
    single_new = [(r[4], r[5]) for r in rows[1:15]
                  if isinstance(r[4], (int, float)) and isinstance(r[5], (int, float))]

    # Block 3 (A/B/C below the "Two TA Blocks" header): timed ramp/soak log.
    two_soak = []
    started = False
    for r in rows:
        if r[0] == "Two TA Blocks":
            started = True
            continue
        if started and isinstance(r[0], (int, float)) and isinstance(r[2], datetime.time):
            two_soak.append((r[0], r[1], _minutes(r[2])))

    # Block 4 (O/P/Q): second two-block ramp, ended by the pressure interlock.
    two_max = [(r[14], r[15], _minutes(r[16])) for r in rows
               if isinstance(r[14], (int, float)) and isinstance(r[15], (int, float))
               and isinstance(r[16], datetime.time)]

    return single_old, single_new, two_soak, two_max


def build_figure() -> Path:
    ws = openpyxl.load_workbook(WORKBOOK, data_only=True)["Sheet1"]
    single_old, single_new, two_soak, two_max = load_series(ws)

    fig, (a1, a2) = plt.subplots(1, 2, figsize=(7.6, 3.4))

    # (a) power command -> temperature for the Ta-susceptor stack.
    a1.plot([p for p, _ in single_new], [t for _, t in single_new], "o-",
            color="#1f77b4", ms=4, lw=1.0, label="1 Ta block")
    a1.plot([p for p, _ in single_old], [t for _, t in single_old], "s--",
            color="#1f77b4", ms=4, lw=0.8, alpha=0.45,
            label="1 Ta block (orig. controller)")
    a1.plot([p for p, _, _ in two_max], [t for _, t, _ in two_max], "^-",
            color="#d62728", ms=4, lw=1.0, label="2 Ta blocks")
    pmax, tmax, _ = max(two_max, key=lambda r: r[1])
    a1.annotate(f"{tmax:.0f}°C @ {pmax:.0f}%\n(pressure interlock)",
                xy=(pmax, tmax), xytext=(-8, -34), textcoords="offset points",
                fontsize=7, color="#d62728", ha="right")
    a1.set_xlabel("Power command (%)")
    a1.set_ylabel("Pyrometer temperature (°C)")
    a1.legend(fontsize=7, loc="lower right")
    a1.set_title("(a)", fontsize=10, fontweight="bold", loc="left")

    # (b) timed two-block ramp/soak reaching a 2000 degC hold.
    th = [m for _, _, m in two_soak]
    temp = [t for _, t, _ in two_soak]
    power = [p for p, _, _ in two_soak]
    a2.plot(th, temp, "o-", color="#d62728", ms=3.5, lw=1.0)
    a2.set_xlabel("Elapsed time (min)")
    a2.set_ylabel("Pyrometer temperature (°C)", color="#d62728")
    a2.tick_params(axis="y", labelcolor="#d62728")
    a2b = a2.twinx()
    a2b.step(th, power, where="post", color="#1f77b4", lw=0.9, alpha=0.8)
    a2b.set_ylabel("Power command (%)", color="#1f77b4")
    a2b.tick_params(axis="y", labelcolor="#1f77b4")
    a2.set_title("(b)", fontsize=10, fontweight="bold", loc="left")

    fig.tight_layout()
    out = FIG_DIR / "fig_ta_heatcurve.png"
    fig.savefig(out, dpi=300)
    plt.close(fig)
    return out


def main() -> int:
    print(f"wrote {build_figure()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
