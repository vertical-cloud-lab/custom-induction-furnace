# Raw (as-collected) Kikuchi patterns

Curated raw electron-backscatter (Kikuchi) patterns and OIM Data Collection
screenshots for the furnace-annealed nickel specimens. Unlike the main
`docs/SEM/` tree (which mirrors the lab's primary SEM Box share), the archives
sampled here live in **separate single-file Box shares** — zip files of
per-scan-point patterns exported by OIM DC during mapping. In total, **more
than 100,000 saved raw patterns** survive across four archives:

| Archive (Box share) | Specimen | Date | Saved patterns | Notes |
|---|---|---|---|---|
| `191026_Ni_003b1a.zip` (~909 MB) — <https://byu.box.com/s/x2aubchd6wurmfxjijk28capvu3e6kjn> | Ni_003b1a | 2019-10-26 | 64,659 (scans `overview`, `reg1a`, `rega1a1`, `reg1a1_lscn1`) | Also `.ang`/`.ohp`/`.osc` scans and `OIM_reg1a_screenshot.JPG` |
| `191031_Ni_003b1a.zip` (~741 MB) — <https://byu.box.com/s/pyqwe8tyrx48d0u8v91sp436jt2uspyg> | Ni_003b1a | 2019-10-31 | ≥37,812 recoverable (scan `reg2`) | **The zip is truncated on Box itself** (upload was cut off; no end-of-central-directory record). `unzip` rejects it; extract with `7z x`, which reads the intact local headers. Full-size scan files (`reg2.oim/.osc/.ang`) and two OIM screenshots are recoverable. |
| `191231-200212.zip` (~1.17 GB) — <https://byu.box.com/s/tbezxw0hkfoinzlbrbfjngvsizobwpn2> | Ni4N5_007, Ni4N5_028, Ni4N5_030 | 2019-12-31 – 2020-02-12 | none per-point | Contains the `..._patterns.ang/.osc` scans of Ni4N5_028 and `200203_Ni4N5_028_s1/Scan3.JPG` — a live OIM screenshot with a **high-quality raw Kikuchi pattern of Ni4N5_028** (committed here). |
| `boxscan_003a1b_0degRot.zip` (79.6 MB, inside the main SEM share at `200616_Ni4N5_007,081_Ni_003b2/Ni4N5_007/`) | Ni_003a1b | 2020-06-16 | 7,358 | Background-corrected, very clean patterns; three representative ones are committed next to the zip's location in `docs/SEM/200616_Ni4N5_007,081_Ni_003b2/Ni4N5_007/boxscan_003a1b_0degRot/`. |

Every saved pattern is a 115×115 px JPEG (the detector's 8×8-binned output),
named by scan-grid position (`<scan>_x<X>y<Y>.jpg`, stage microns). This
directory commits a small representative selection per archive — chosen for
clearly resolved bands/zone axes — plus the OIM screenshots that record the
acquisition settings (binning, exposure, gain, scan geometry, sample ID):

- `191026_Ni_003b1a/` — `OIM_reg1a_screenshot.JPG` (scan `reg1a`: 400×, hex
  grid, 4 µm step, 18,198 points, Nickel phase, sample ID `Ni_003b1a`) and five
  per-point patterns from `reg1a` / `rega1a1`.
- `191031_Ni_003b1a/` — `OIM_reg2(partial)_screenshot.JPG` (scan `reg2`: 240×,
  square grid, 12.5 µm step, 328,947 points planned; the screenshot shows 38 %
  complete) and one `reg2` pattern.
- `200203_Ni4N5_028_s1/` — `Scan3.JPG` (line scans across thermally grooved
  grain boundaries of **Ni4N5_028** at 70,068×, 8×8 binning / 174×130, 30 ms
  exposure; the live pattern panel shows crisp bands and zone axes) and
  `reg1_summary_exposureTimes.pptx` (exposure-time comparison for the same
  session).

Provenance: `Ni_003`-series specimens were annealed during the project's early
commissioning campaign (September–October 2019), which predates the logged-run
series (`IFrun001` logging began 2019-11-11), so they have no `IFrun` linkage.
`Ni4N5_028` is the specimen of run `IFrun043` (see
`docs/data_log/IFrun041-060/IFrun043_extra/`), whose raw log is not among the
parsed set.

No other saved-pattern sources exist: the main SEM share contains **no
`.up1`/`.up2` pattern archives**, and its only other zips are DREAM.3D test
data. The optical share contains none. The full pattern archives remain on Box
at the links above (single-file shares; `download_box_docs.py` handles them
directly, or download via browser).
