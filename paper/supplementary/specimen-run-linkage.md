# Table S1 — Specimen ↔ thermal-history linkage (supplementary)

Specimen ↔ run linkage and archived characterization data for the runs used in
the manuscript's validation sections. This table carries the run-ID-level
detail deliberately kept out of the main text; every row hyperlinks to the raw
run log in the data archive (GitHub development repository; an archival
snapshot is deposited at Zenodo, [10.5281/zenodo.20878017](https://doi.org/10.5281/zenodo.20878017)).

Column notes: "Nominal soak" is the target parsed from the run filename;
"Logged soak T" is the machine-parsed soak-mean from the trace
([`run_summary.csv`](../../docs/data_log/processed/run_summary.csv));
"Atmosphere" indicates whether active gas flow was present in the parsed log
summary, not a fully reconstructed gas chemistry; "Characterization" gives
archived SEM/optical file counts and flags archived EBSD/OIM data. Machine-
parsed per-run CSV traces and PNG plots for every linked run are in
[`docs/data_log/processed/`](../../docs/data_log/processed/). The complete
35-specimen cross-reference, including characterized specimens whose run logs
are not in the parsed set, is
[`paper/characterization-crossref.csv`](../characterization-crossref.csv) /
[`.md`](../characterization-crossref.md).

| Specimen | Material | Run (raw log) | Nominal soak | Logged soak T | Soak time | Atmos. | Characterization | Role / manuscript figure |
|---|---|---|---|---|---|---|---|---|
| Ni4N5_026 | Ni4N5 | [IFrun039](../../docs/data_log/IFrun021-040/IFrun039_Ni4N5_026_1200C_6h.xlsx) | 1200 °C | 1200.4 °C | 6 h | no-flow | — | Calibration (Fig. S5) |
| Ni4N5_027 | Ni4N5 | [IFrun040](../../docs/data_log/IFrun021-040/IFrun040_Ni4N5_027_1250C_6h.xlsx) | 1250 °C | 1250.0 °C | 6 h | no-flow | — | Calibration |
| Ni4N5_025 | Ni4N5 | [IFrun038](../../docs/data_log/IFrun021-040/IFrun038_Ni4N5_025_1300C_1h.xlsx) | 1300 °C | 1299.9 °C | 1 h | no-flow | — | Calibration |
| Ni4N5_022 | Ni4N5 | [IFrun032](../../docs/data_log/IFrun021-040/IFrun032_Ni4N5_022_1400C_10min.xlsx) | 1400 °C | 1399.6 °C | 10 min | no-flow | — | Calibration |
| Ni4N5_084 | Ni4N5 | [IFrun079](../../docs/data_log/IFrun061-080/IFrun079_Ni4N5_084_1300C_12h.xlsx) | 1300 °C | 1302.1 °C | 12 h | flow | — | Representative soak (Fig. S6) |
| Ni4N5_040 | Ni4N5 | [IFrun052](../../docs/data_log/IFrun041-060/IFrun052_Ni4N5_040_1200C_12h.xlsx) | 1200 °C | 1199.8 °C | 12 h | flow | — | Repeatability run 1 (Fig. S7) |
| Ni4N5_042,044 | Ni4N5 | [IFrun054](../../docs/data_log/IFrun041-060/IFrun054_Ni4N5_042,044_1200C_12h.xlsx) | 1200 °C | 1201.5 °C | 12 h | flow | — | Repeatability run 2 |
| Ni4N5_045,046 | Ni4N5 | [IFrun055](../../docs/data_log/IFrun041-060/IFrun055_Ni4N5_045,046_1200C_12h.xlsx) | 1200 °C | 1204.2 °C | 12 h | flow | — | Repeatability run 3 |
| Ni4N5_047,048 | Ni4N5 | [IFrun056](../../docs/data_log/IFrun041-060/IFrun056_Ni4N5_047,048_1200C_12h.xlsx) | 1200 °C | 1200.6 °C | 12 h | flow | — | Repeatability run 4 |
| Ni4N5_049,050 | Ni4N5 | [IFrun057](../../docs/data_log/IFrun041-060/IFrun057_Ni4N5_049,050_1200C_12h.xlsx) | 1200 °C | 1201.2 °C | 12 h | flow | — | Repeatability run 5 |
| Ni4N5_051,052 | Ni4N5 | [IFrun058](../../docs/data_log/IFrun041-060/IFrun058_Ni4N5_051,052_1200C_12h.xlsx) | 1200 °C | 1201.0 °C | 12 h | flow | — | Repeatability run 6 |
| Ni4N5_053,054 | Ni4N5 | [IFrun059](../../docs/data_log/IFrun041-060/IFrun059_Ni4N5_053,054_1200C_12h.xlsx) | 1200 °C | 1200.3 °C | 12 h | flow | 4 SEM, 3 opt. (Ni4N5_053) | Repeatability run 7; GB grooving (main text Fig. 5) |
| Ni4N5_056,057 | Ni4N5 | [IFrun060](../../docs/data_log/IFrun041-060/IFrun060_Ni4N5_056,057_1200C_12h.xlsx) | 1200 °C | 1200.9 °C | 12 h | flow | — | Repeatability run 8 |
| Ni200_015 | Ni200 | [IFrun081](../../docs/data_log/IFrun081-100/IFrun081_Ni200_015_1325C_20h.xlsx) | 1325 °C | 1326.5 °C | 20 h | flow | 3 opt. | Long soak, 20 h (Fig. S8) |
| Ni200_017 | Ni200 | [IFrun080](../../docs/data_log/IFrun061-080/IFrun080_Ni200_017_1325C_40h.xlsx) | 1325 °C | 1326.3 °C | 40 h | flow | 2 opt. | Long soak, 40 h |
| Ni4N5_079,080 | Ni4N5 | [IFrun072](../../docs/data_log/IFrun061-080/IFrun072_Ni4N5_079,080_1400C_12h.xlsx) | 1400 °C | — | 12 h | flow | — | Process-window specimen |
| Ni4N5_034 | Ni4N5 | [IFrun049](../../docs/data_log/IFrun041-060/IFrun049_Ni4N5_034_1200C_12h.xlsx) | 1200 °C | 1200.0 °C | 12 h | no-flow | 4 SEM, EBSD | EBSD IPF map (Fig. S9) |
| Ni4N5_081 | Ni4N5 | [IFrun082](../../docs/data_log/IFrun081-100/IFrun082_Ni4N5_081_1300C_20h.xlsx) | 1300 °C | 1301.4 °C | 20 h | flow | 10 SEM, 10 opt., EBSD | Microstructure (main text Fig. 6) |
| Ni4N5_010 | Ni4N5 | [IFrun016](../../docs/data_log/IFrun001-020/IFrun016_Ni4N5_010.xlsx) | 1200 °C | 1199.9 °C | — | no-flow | 4 opt. | Characterization only |
| Ni4N5_012 | Ni4N5 | [IFrun019](../../docs/data_log/IFrun001-020/IFrun019_Ni4N5_012.xlsx) | 1200 °C | 1199.6 °C | — | no-flow | 1 opt. | Characterization only |
| Ni200_001 | Ni200 | [IFrun004](../../docs/data_log/IFrun001-020/Ni200_001_IFrun004.lvm)/[IFrun005](../../docs/data_log/IFrun001-020/Ni200_001_IFrun005.lvm) | — | — | — | no-flow | 3 opt. | Characterization only |
| Ni4N5_001b | Ni4N5 | IFrun006 (log not in parsed set) | — | — | — | no-flow | 2 opt. | Characterization only |

Additional raw-pattern context for the Kikuchi figures (main text Fig. 4 and Fig. S10):
the live-pattern screenshot of Ni4N5_028 is
[`docs/SEM/raw-kikuchi-patterns/200203_Ni4N5_028_s1/Scan3.JPG`](../../docs/SEM/raw-kikuchi-patterns/200203_Ni4N5_028_s1/Scan3.JPG),
and the >100,000 archived per-scan-point raw patterns of the early-campaign
Ni_003-series specimens are inventoried in
[`docs/SEM/raw-kikuchi-patterns/README.md`](../../docs/SEM/raw-kikuchi-patterns/README.md).
