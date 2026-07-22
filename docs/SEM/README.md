# SEM / EBSD characterization data

Scanning-electron-microscopy and EBSD data for the induction-furnace annealing
study, downloaded from the lab's Box share
(`https://byu.box.com/s/myzj1xxrty9phulplxjqhrgzeqg0y32u`). Folders are named by
date and specimen (e.g. `200423_Ni4N5_069`), and the `Ni4N5_###` / `Ni200_###`
specimen IDs map to the annealing runs in `docs/data_log/` (see the
specimen ↔ thermal-history linkage table in `paper/paper.tex`).

## What is committed here

The **full** SEM archive is ~8.7 GB across 2,870 files (including very large
`.oim` / `.osc` / `.ang` EBSD scans, DREAM.3D reconstruction volumes, and the
DREAM.3D/MTEX analysis-software trees). Committing all of it to plain git is not
practical, so this directory contains a **representative subset** (≈340 MB) that
preserves the original Box folder structure: a handful of the highest-detail
micrographs/maps per specimen folder plus small notes/metadata files, excluding
the bundled analysis-software trees (`DREAM.3D/`, `MTEX/`) and any file ≥100 MB.

- [`CATALOG.csv`](CATALOG.csv) — the **complete** inventory of every file in the
  Box SEM share (path, size, extension, and whether it is committed here). Use it
  to locate any file in the full archive; uncommitted files can be fetched with
  `python download_box_docs.py --shared-link <SEM link> --max-bytes 0`.

The full raster/EBSD archive remains on Box and is the source of record; large
binaries would need Git LFS to be version-controlled in full.
