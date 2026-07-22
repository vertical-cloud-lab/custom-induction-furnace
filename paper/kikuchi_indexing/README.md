# Open-source indexing of the raw Kikuchi patterns

Requested by S. Baird (PR #12, 2026-07-22): *"see if there are multiple
patterns like this, run some open-source indexing of these patterns."*

## Are there multiple patterns like the main-text figure?

Yes. Beyond the single pattern shown in the main text (specimen Ni4N5_028,
live OIM capture in `docs/SEM/raw-kikuchi-patterns/200203_Ni4N5_028_s1/
Scan3.JPG`), **more than 100,000 saved per-scan-point raw patterns**
survive across four Box archives, documented in
[`docs/SEM/raw-kikuchi-patterns/README.md`](../../docs/SEM/raw-kikuchi-patterns/README.md).
Nine representative per-scan-point patterns (115×115 px, the detector's
8×8-binned JPEG output) are committed in this repository:

- 5 from `191026_Ni_003b1a` (scans `reg1a`, `rega1a1`)
- 1 from `191031_Ni_003b1a` (scan `reg2`)
- 3 from `200616 Ni_003a1b` (`boxscan_003a1b_0degRot`, background-corrected)

All are from furnace-annealed nickel specimens that received **no
metallographic preparation** (no grinding, polishing, or etching).

## Open-source indexing result

[`index_raw_patterns.py`](index_raw_patterns.py) indexes all nine committed
patterns with [PyEBSDIndex](https://github.com/USNavalResearchLaboratory/PyEBSDIndex)
(the open-source Radon/Hough band-detection indexer used by kikuchipy),
fitting the unrecorded detector pattern center per acquisition session with
`pyebsdindex.pcopt` and then Hough-indexing against an FCC (nickel) phase.

**All 9 of 9 patterns index as FCC nickel.** Full numbers are in
[`results.csv`](results.csv); summary:

| Session | Patterns | Bands matched | Mean band fit | Confidence metric |
|---|---|---|---|---|
| 191026_Ni_003b1a (reg1a, rega1a1) | 5/5 indexed | 6–8 of 9 | 0.22–0.48° | 0.54–0.76 |
| 191031_Ni_003b1a (reg2) | 1/1 indexed | 8 of 9 | 0.62° | 0.77 |
| 200616 Ni_003a1b (boxscan) | 3/3 indexed | 3 of 9 | 0.35–0.40° | 0.18–0.30 |

Notes:

- The 0.2–0.6° mean band fits are ordinary good-quality Hough-indexing
  values, i.e., these coarse 8×8-binned patterns from **unprepared,
  as-annealed surfaces** index about as well as patterns from conventionally
  prepared specimens.
- The pattern center had to be *fitted* (it is not stored in the JPEG
  exports), so the absolute Euler angles in `results.csv` carry the usual
  PC-uncertainty caveat; the phase discrimination and band fits are robust
  to this.
- The `boxscan` patterns match fewer bands because their background
  correction flattens the outer-band contrast the default detection
  settings expect; the bands that are found still fit to <0.4°.
- The commercial-software confidence index (CI) for the *full* scans is a
  separate question (asked by R. Guymon in PR #12); the full `.ang`/`.osc`
  scan files that carry per-point CI live in the Box archives, not in this
  repository (see `docs/SEM/CATALOG.csv` and the raw-kikuchi-patterns
  README).
