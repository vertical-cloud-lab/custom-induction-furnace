#!/usr/bin/env python3
"""
Parse the raw furnace run logs and emit static CSV + PNG copies of each run.

The lab's anneal runs are logged as binary spreadsheets (``.xlsx``) and LabVIEW
measurement files (``.lvm``) under ``docs/data_log/``. Each log records, at a
minimum, a time axis, the analog power-control command (mA), and the pyrometer
temperature (deg C); later runs also log a gas flow-rate (sccm). Those binaries
are not diff-able or viewable on GitHub, so this script reads each one and writes
a reproducible, version-controlled view of every run:

  * ``docs/data_log/processed/csv/<run>.csv``  -- normalized columns
    (``elapsed_s, power_mA, temperature_C[, flow_sccm]``)
  * ``docs/data_log/processed/png/<run>.png``  -- temperature + power vs. time

It also writes ``docs/data_log/processed/run_summary.csv`` with one row per run
(peak/soak temperature, soak time, sample, duration, point count) which feeds the
data inventory in ``paper/journal-assessment/DATA_INVENTORY.md``.

The script is idempotent and re-runnable. Requires ``python-calamine``,
``matplotlib``, and ``numpy``.

Usage:
    python build_run_traces.py [--data-dir docs/data_log]
"""

from __future__ import annotations

import argparse
import csv
import re
import statistics
import sys
from datetime import datetime, date, time as dtime
from pathlib import Path

try:
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    import numpy as np
    from python_calamine import CalamineWorkbook
except ImportError as exc:  # pragma: no cover - hard dependencies
    print(f"❌ missing dependency: {exc}. "
          "Install with: pip install python-calamine matplotlib numpy")
    sys.exit(1)

REPO_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_DATA_DIR = REPO_ROOT / "docs" / "data_log"

# Header keywords -> normalized column role.
TIME_KEYS = ("time", "x_value", "x array")
POWER_KEYS = ("power", "signal", "control", "command", "current", "ma")
TEMP_KEYS = ("temp", "deg c", "pyro", "celsius")
FLOW_KEYS = ("flow", "sccm")


def _to_seconds(values: list) -> list[float] | None:
    """Convert a column of timestamps/numbers into elapsed seconds.

    The logs sample at a fixed cadence, but the stored timestamps occasionally
    wrap or contain stray outliers. We therefore estimate a robust uniform
    sample interval from the positive consecutive differences and build a clean
    monotonic axis from it; if the column is already plain seconds, that is
    detected and used directly.
    """
    nums: list[float] = []
    kind = None
    for v in values:
        if isinstance(v, datetime):
            nums.append(v.timestamp())
            kind = "dt"
        elif isinstance(v, (int, float)):
            nums.append(float(v))
            kind = kind or "num"
        elif isinstance(v, dtime):
            nums.append(v.hour * 3600 + v.minute * 60 + v.second + v.microsecond / 1e6)
            kind = "dt"
        else:
            return None
    if not nums:
        return None
    if kind == "num" and all(b >= a for a, b in zip(nums, nums[1:])):
        # Already monotonic numeric seconds.
        return [n - nums[0] for n in nums]
    diffs = [b - a for a, b in zip(nums, nums[1:]) if 0 < (b - a) <= 3600]
    dt = statistics.median(diffs) if diffs else 1.0
    return [i * dt for i in range(len(nums))]


def _classify(header: list[str]) -> dict[str, int]:
    """Map column roles to indices from a header row."""
    roles: dict[str, int] = {}
    norm = [str(h).strip().lower() for h in header]
    for i, h in enumerate(norm):
        if not h or h.startswith("untitled"):
            continue
        if "time" not in roles and any(k in h for k in TIME_KEYS):
            roles["time"] = i
        elif "flow" not in roles and any(k in h for k in FLOW_KEYS):
            roles["flow"] = i
        elif "power" not in roles and any(k in h for k in POWER_KEYS):
            roles["power"] = i
        elif "temp" not in roles and any(k in h for k in TEMP_KEYS):
            roles["temp"] = i
    return roles, norm


def _looks_like_temp(col: list) -> bool:
    vals = [v for v in col if isinstance(v, (int, float))]
    if not vals:
        return False
    med = statistics.median(vals)
    return 200 <= med <= 2000


def read_xlsx(path: Path):
    wb = CalamineWorkbook.from_path(str(path))
    rows = wb.get_sheet_by_index(0).to_python()
    if not rows:
        return None
    header = rows[0]
    roles, norm = _classify([str(c) for c in header])
    data = rows[1:]
    ncol = max((len(r) for r in data[:50]), default=len(header))

    def col(idx):
        return [r[idx] if idx < len(r) else None for r in data]

    # Fall back: find a temperature-like column among the unlabeled ones.
    if "temp" not in roles:
        for i in range(ncol):
            if i in roles.values():
                continue
            if _looks_like_temp(col(i)):
                roles["temp"] = i
                break
    if "time" not in roles:
        roles["time"] = 0
    return roles, data, col


def read_lvm(path: Path):
    text = path.read_text(errors="replace").splitlines()
    start = None
    for i, line in enumerate(text):
        if line.startswith("X_Value"):
            start = i + 1
            break
    if start is None:
        return None
    times, sig = [], []
    for line in text[start:]:
        parts = line.split("\t")
        nums = [p for p in parts if p.strip() not in ("", None)]
        try:
            vals = [float(p) for p in nums]
        except ValueError:
            continue
        if len(vals) >= 2:
            times.append(vals[-2])
            sig.append(vals[-1])
    if not times:
        return None
    return times, sig


def _floats(col):
    return [float(v) if isinstance(v, (int, float)) else float("nan") for v in col]


def process_run(path: Path, out_csv: Path, out_png: Path) -> dict | None:
    try:
        if path.suffix.lower() == ".xlsx":
            parsed = read_xlsx(path)
            if not parsed:
                return None
            roles, data, col = parsed
            elapsed = _to_seconds(col(roles["time"]))
            if elapsed is None:
                elapsed = list(range(len(data)))
            power = _floats(col(roles["power"])) if "power" in roles else None
            temp = _floats(col(roles["temp"])) if "temp" in roles else None
            flow = _floats(col(roles["flow"])) if "flow" in roles else None
        else:  # .lvm
            res = read_lvm(path)
            if not res:
                return None
            elapsed, power = res
            elapsed = [e - elapsed[0] for e in elapsed]
            temp = flow = None
    except Exception as exc:  # noqa: BLE001
        print(f"  ✗ {path.name}: {exc}")
        return None

    n = len(elapsed)
    if n < 2:
        return None

    # Trim trailing all-empty rows (xlsx logs are often padded to Excel's
    # 1,048,576-row maximum with blank cells).
    def _finite(seq, i):
        v = seq[i] if seq is not None and i < len(seq) else None
        return isinstance(v, float) and np.isfinite(v)

    last = n - 1
    while last > 0 and not (_finite(power, last) or _finite(temp, last)
                            or _finite(flow, last)):
        last -= 1
    n = last + 1
    elapsed = elapsed[:n]
    if power is not None:
        power = power[:n]
    if temp is not None:
        temp = temp[:n]
    if flow is not None:
        flow = flow[:n]
    if n < 2:
        return None
    out_csv.parent.mkdir(parents=True, exist_ok=True)
    cols = [("elapsed_s", elapsed)]
    if power is not None:
        cols.append(("power_mA", power))
    if temp is not None:
        cols.append(("temperature_C", temp))
    if flow is not None:
        cols.append(("flow_sccm", flow))
    with out_csv.open("w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow([c[0] for c in cols])
        for i in range(n):
            w.writerow([f"{c[1][i]:.4g}" if isinstance(c[1][i], float) else c[1][i]
                        for c in cols])

    # Plot.
    out_png.parent.mkdir(parents=True, exist_ok=True)
    t_min = np.array(elapsed) / 60.0
    fig, ax1 = plt.subplots(figsize=(7, 4))
    peak_t = soak_t = None
    if temp is not None and any(np.isfinite(temp)):
        ax1.plot(t_min, temp, color="tab:red", lw=1.0, label="Temperature (°C)")
        ax1.set_ylabel("Temperature (°C)", color="tab:red")
        ax1.tick_params(axis="y", labelcolor="tab:red")
        finite = np.array([v for v in temp if np.isfinite(v)])
        if finite.size:
            peak_t = float(np.nanmax(finite))
            hot = finite[finite >= 0.9 * peak_t]
            soak_t = float(np.median(hot)) if hot.size else peak_t
    if power is not None and any(np.isfinite(power)):
        ax2 = ax1.twinx()
        ax2.plot(t_min, power, color="tab:blue", lw=0.8, alpha=0.7,
                 label="Power command (mA)")
        ax2.set_ylabel("Power command (mA)", color="tab:blue")
        ax2.tick_params(axis="y", labelcolor="tab:blue")
    ax1.set_xlabel("Elapsed time (min)")
    ax1.set_title(path.stem, fontsize=9)
    fig.tight_layout()
    fig.savefig(out_png, dpi=110)
    plt.close(fig)

    return {
        "run": path.stem,
        "source": str(path.relative_to(REPO_ROOT)),
        "points": n,
        "duration_min": round(elapsed[-1] / 60.0, 1),
        "peak_temp_C": round(peak_t, 1) if peak_t else "",
        "soak_temp_C": round(soak_t, 1) if soak_t else "",
        "has_flow": "yes" if flow is not None else "no",
    }


RUN_RE = re.compile(r"IFrun\d+", re.IGNORECASE)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--data-dir", default=str(DEFAULT_DATA_DIR))
    args = ap.parse_args()
    data_dir = Path(args.data_dir)
    out_dir = data_dir / "processed"

    files = sorted(
        p for p in data_dir.rglob("*")
        if p.suffix.lower() in (".xlsx", ".lvm")
        and "processed" not in p.parts
        and not p.name.startswith("~$")
    )
    print(f"Found {len(files)} run log(s) under {data_dir.relative_to(REPO_ROOT)}.")

    summary = []
    for p in files:
        stem = p.stem
        out_csv = out_dir / "csv" / f"{stem}.csv"
        out_png = out_dir / "png" / f"{stem}.png"
        row = process_run(p, out_csv, out_png)
        if row:
            summary.append(row)
            print(f"  ✓ {stem}: {row['points']} pts, "
                  f"peak {row['peak_temp_C']}°C, {row['duration_min']} min")

    if summary:
        sumcsv = out_dir / "run_summary.csv"
        with sumcsv.open("w", newline="") as fh:
            w = csv.DictWriter(fh, fieldnames=list(summary[0].keys()))
            w.writeheader()
            w.writerows(summary)
        print(f"\nWrote {sumcsv.relative_to(REPO_ROOT)} ({len(summary)} runs).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
