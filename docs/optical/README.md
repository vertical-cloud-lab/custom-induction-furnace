# Optical-microscopy characterization data

Optical-microscopy data for the induction-furnace annealing study, downloaded
from the lab's Box share
(`https://byu.box.com/s/slnz5cki15w462pxkdkljyodh582lrk6`). The two top-level
collections are `Zeta/` (Zeta optical-profilometer image sets) and `CB121/`
(stitched/standard optical micrographs); folders are named by date and specimen
so the `Ni4N5_###` / `Ni200_###` / `Fe_###` labels map back to the annealing
runs in `docs/data_log/` where applicable.

## What is committed here

The **full** optical archive is ~3.5 GB across 1,484 files. Committing all of it
to plain git is not practical, so this directory contains a **representative
subset** (≈230 MB) that preserves the original Box folder structure: a couple of
representative micrographs per specimen folder plus small notes/metadata files,
excluding bundled analysis-software trees (e.g. `fiji-win64/`) and any file
≥100 MB.

- [`CATALOG.csv`](CATALOG.csv) — the **complete** inventory of every file in the
  Box optical share (path, size, extension, and whether it is committed here).
  Uncommitted files can be fetched with
  `python download_box_docs.py --shared-link <optical link> --max-bytes 0`.

The full archive remains on Box and is the source of record.
