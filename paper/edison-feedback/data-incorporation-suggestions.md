<!-- Edison ANALYSIS task 3f37bef1-8d91-4a59-ae17-3a7771cf49c9 (data-incorporation suggestions) -->

# HardwareX validation guidance: fold the existing run archive into the paper now

## Bottom line

You already have enough to replace the current validation-section placeholders with **real empirical evidence**. The cleanest, most credible HardwareX story is:

1. **closed-loop thermal control works across 1200–1400 °C**,  
2. **the same programmed 1200 °C / 12 h Ni4N5 profile is repeatable across 8 archived runs**,  
3. **the system remains stable for 20–40 h soaks**, and  
4. **the furnace produces real microstructural change in traceable specimens**, once the SEM/optical image sets are linked to run IDs.

The strongest currently attached thermal cohorts are:
- **Calibration subset:** `IFrun039_Ni4N5_026_1200C_6h`, `IFrun040_Ni4N5_027_1250C_6h`, `IFrun038_Ni4N5_025_1300C_1h`, `IFrun032_Ni4N5_022_1400C_10min`
- **Repeatability subset:** `IFrun052`, `054`, `055`, `056`, `057`, `058`, `059`, `060` (all `Ni4N5`, all `1200C_12h`, all `has_flow=yes`)
- **Long-soak subset:** `IFrun081_Ni200_015_1325C_20h`, `IFrun080_Ni200_017_1325C_40h`
- **Good representative single-run traces already exported:** `IFrun079_Ni4N5_084_1300C_12h`, `IFrun072_Ni4N5_079,080_1400C_12h`, `IFrun081_Ni200_015_1325C_20h`, `IFrun080_Ni200_017_1325C_40h`

I would **not** present a universal power-command→temperature calibration for the whole archive. The data show setup dependence. Present it as an **operational calibration for a fixed specimen/crucible/coil/optical geometry subset**.

---

## 1. Validation figures: exactly what to use and what to compute

## Figure 2. Power-command → steady-state temperature calibration

### What to use
Use the **Ni4N5 no-flow, same-era subset** already exported as per-run CSVs:
- `IFrun039_Ni4N5_026_1200C_6h`
- `IFrun040_Ni4N5_027_1250C_6h`
- `IFrun038_Ni4N5_025_1300C_1h`
- `IFrun032_Ni4N5_022_1400C_10min`

These four runs give a clean monotonic steady-state relation within one operational regime.

### Why this subset
Because the archive is not one clean DOE. When I computed soak-mean power from the exported per-run CSVs, the broader archive showed obvious setup dependence. Example:
- `IFrun039` at ~1200 °C had mean soak power **0.440 mA**
- `IFrun049` at ~1200 °C had mean soak power **0.658 mA**

Same nominal temperature, very different command. That is a red flag for changed geometry/load/era. Good. Useful. Honest. It means the figure must be scoped, not oversold.

### What to plot
For each selected run, compute from the steady-state soak segment:
- **mean analog power command (mA)**
- **SD of analog power command during soak**
- **mean pyrometer temperature during soak**
- optionally the run label beside each point

From the current derived values:

| Run | Mean soak T (°C) | Mean soak power (mA) | Power SD (mA) |
|---|---:|---:|---:|
| `IFrun039_Ni4N5_026_1200C_6h` | 1200.39 | 0.4399 | 0.0055 |
| `IFrun040_Ni4N5_027_1250C_6h` | 1250.03 | 0.4888 | 0.0057 |
| `IFrun038_Ni4N5_025_1300C_1h` | 1299.94 | 0.5786 | 0.0251 |
| `IFrun032_Ni4N5_022_1400C_10min` | 1399.63 | 0.7441 | 0.0322 |

A simple linear fit on these four points gives:
- **T ≈ 931.0 + 633.3 × power(mA)**
- **R² = 0.991**
- **n = 4 steady-state operating points**

### How to report scatter honestly
Do **not** write “the system calibration is linear” without qualifiers.
Write instead:

> For one fixed Ni4N5/quartz/graphite/optical configuration, four archived steady-state anneals spanning 1200–1400 °C showed a monotonic power-command/temperature relation. A linear guide-to-the-eye fit over this subset gave R² = 0.991; however, the full retrospective archive showed configuration-dependent offsets, so this calibration is presented as operational rather than universal.

### What not to use in the calibration panel
Do not pool these into one line:
- `IFrun049_Ni4N5_034_1200C_12h`
- `IFrun072_Ni4N5_079,080_1400C_12h`
- `IFrun079_Ni4N5_084_1300C_12h`
- `IFrun080/081` Ni200 runs

Those are useful elsewhere, but not for a single “calibration” figure unless you separate them by configuration/material.

---

## Figure 3. Representative ramp/soak with quantitative control metrics

### Best run to use
Use **`IFrun079_Ni4N5_084_1300C_12h`** as the main representative closed-loop trace.

Why this run:
- long enough to show control quality over a meaningful soak,
- cleaner than the 10 min run,
- not so long that the panel becomes unreadable,
- already exported as both `.png` and `.csv`.

### Metrics to compute
Using the per-run CSV (`elapsed_s`, `power_mA`, `temperature_C`) and the nominal setpoint from filename (`1300C`), compute:
- **10–90% rise time**
- **overshoot** = max(T before stable soak) − setpoint
- **settling time** = time until temperature remains within a chosen deadband for at least a fixed dwell
- **soak mean temperature**
- **soak SD**
- **maximum absolute deviation during soak**
- **linear drift during soak** in °C/h

From the current derived values for `IFrun079`:
- nominal setpoint: **1300 °C**
- **10–90% rise time:** **1135 s**
- **overshoot:** **12.0 °C**
- **settling time to ±10 °C band:** **1262 s**
- **soak mean temperature:** **1302.08 °C**
- **soak SD:** **3.00 °C**
- **maximum absolute deviation during soak:** **10.0 °C**
- **soak duration in-band:** **720.7 min**
- **linear drift during soak:** **−0.021 °C/h**

### How to display it
Top panel:
- temperature vs time
- show setpoint as dashed line
- annotate rise, overshoot, and soak window

Bottom panel:
- power command vs time

Inset or caption table:
- the metrics above

### Alternate choice
If you want a shorter plot for readability, use **`IFrun038_Ni4N5_025_1300C_1h`** in the main panel and move `IFrun079` to the long-soak/repeatability discussion. For `IFrun038` the derived metrics were:
- rise time **1134 s**
- overshoot **11.0 °C**
- settling time **1187 s**
- soak mean **1299.94 °C**
- soak SD **3.48 °C**

That said, for HardwareX I’d still use `IFrun079` because it proves control over a 12 h soak.

---

## Figure 4. Repeatability across runs

### The genuine same-profile cohort
Use the **8-run Ni4N5 1200 °C / 12 h cohort**:
- `IFrun052_Ni4N5_040_1200C_12h`
- `IFrun054_Ni4N5_042,044_1200C_12h`
- `IFrun055_Ni4N5_045,046_1200C_12h`
- `IFrun056_Ni4N5_047,048_1200C_12h`
- `IFrun057_Ni4N5_049,050_1200C_12h`
- `IFrun058_Ni4N5_051,052_1200C_12h`
- `IFrun059_Ni4N5_053,054_1200C_12h`
- `IFrun060_Ni4N5_056,057_1200C_12h`

These are the strongest retrospective repeatability evidence in the attached archive because they are all:
- same material: **Ni4N5**
- same nominal condition: **1200 °C / 12 h**
- same era/profile family
- same `has_flow=yes` flag in `run_summary.csv`

### What to report
From `run_summary.csv` for this cohort:
- **n = 8 runs**
- mean soak temperature: **1201.12 °C**
- soak-temperature SD across runs: **1.30 °C**
- range: **1199.8–1204.1 °C**
- coefficient of variation: **0.108%**
- mean peak temperature: **1212.59 °C**
- SD of peak temperature: **6.74 °C**
- mean duration: **766.2 min**
- SD of duration: **15.3 min**

### What to show
Best option:
- overlay the 8 temperature traces if you can export the raw curves from the archived `.xlsx` files
- if you cannot do that quickly, show a summary panel with per-run points for:
  - soak mean T
  - peak T
  - duration

And write clearly that this figure uses **summary metrics across a same-profile archival cohort**.

### Important caution
Do not mix in:
- `IFrun016`, `IFrun019`, or `IFrun049`

Even though they are also around 1200 °C, they are from a different setup era (`has_flow=no`) and should not be pooled into the repeatability claim.

### Exact sentence for the paper
> Repeatability was assessed on the most internally consistent retrospective cohort available: eight Ni4N5 anneals at a nominal 1200 °C / 12 h condition (`IFrun052–060`, excluding missing run numbers), all logged under the same gas-flow configuration. Across these runs, the reported soak temperature was 1201.1 ± 1.3 °C (mean ± SD; range 1199.8–1204.1 °C; n = 8), supporting run-to-run thermal reproducibility within this configuration.

---

## Figure 4 or separate panel: long-soak stability

I would make long-soak stability either:
- a **second panel of Figure 4**, or
- a **standalone subpanel of Figure 3**

because it is one of your strongest hardware claims.

### Use these runs
- `IFrun081_Ni200_015_1325C_20h`
- `IFrun080_Ni200_017_1325C_40h`

### Quantitative results already derivable from the exported CSVs
`IFrun081_Ni200_015_1325C_20h`
- setpoint: **1325 °C**
- rise time: **1130 s**
- overshoot: **9.0 °C**
- settling time: **1182 s**
- soak mean: **1326.49 °C**
- soak SD: **1.48 °C**
- max deviation during soak: **10.0 °C**
- in-band soak duration: **1198.0 min**
- drift: **−0.0043 °C/h**

`IFrun080_Ni200_017_1325C_40h`
- setpoint: **1325 °C**
- rise time: **2500 s**
- overshoot: **25.0 °C**
- settling time: **12090 s**
- soak mean: **1326.34 °C**
- soak SD: **5.50 °C**
- max deviation during soak: **10.0 °C**
- in-band soak duration: **2400.3 min**
- drift: **−0.028 °C/h**

### How to frame it
The 20 h run is the cleaner demonstration of steady control. The 40 h run is the brute-force proof that the system can hold temperature for a very long time.

Suggested text:

> Long-duration stability was demonstrated retrospectively using archived Ni200 anneals at 1325 °C for 20 h and 40 h. The 20 h run showed a soak mean of 1326.5 °C with an in-soak SD of 1.5 °C and near-zero drift (−0.004 °C/h), while the 40 h run maintained a soak mean of 1326.3 °C over 2400 min in-band, with an in-soak SD of 5.5 °C.

That is a solid HardwareX result.

---

## Figure 5. Microstructural validation

This is the only figure that still needs the image archive pulled and registered. But the structure of the figure should be locked now.

### What to use
Prioritize the specimens that map to your strongest thermal cohorts.

#### Highest-priority repeatability/microstructure group
From the 1200 °C / 12 h Ni4N5 cohort:
- `IFrun052` → `Ni4N5_040`
- `IFrun054` → `Ni4N5_042`, `Ni4N5_044`
- `IFrun055` → `Ni4N5_045`, `Ni4N5_046`
- `IFrun056` → `Ni4N5_047`, `Ni4N5_048`
- `IFrun057` → `Ni4N5_049`, `Ni4N5_050`
- `IFrun058` → `Ni4N5_051`, `Ni4N5_052`
- `IFrun059` → `Ni4N5_053`, `Ni4N5_054`
- `IFrun060` → `Ni4N5_056`, `Ni4N5_057`

That gives **15 specimens across 8 runs**.

#### Highest-priority process-window group
Use one specimen each from the already exported thermal traces:
- `IFrun039` → `Ni4N5_026` at 1200 °C / 6 h
- `IFrun040` → `Ni4N5_027` at 1250 °C / 6 h
- `IFrun038` → `Ni4N5_025` at 1300 °C / 1 h
- `IFrun079` → `Ni4N5_084` at 1300 °C / 12 h
- `IFrun032` → `Ni4N5_022` at 1400 °C / 10 min
- `IFrun072` → `Ni4N5_079`, `Ni4N5_080` at 1400 °C / 12 h
- `IFrun081` → `Ni200_015` at 1325 °C / 20 h
- `IFrun080` → `Ni200_017` at 1325 °C / 40 h

### Minimum figure content
Panel A:
- as-received Ni4N5 micrograph
- annealed Ni4N5 examples from low/intermediate/high severity conditions

Panel B:
- as-received Ni200 micrograph
- annealed Ni200 examples from 20 h and 40 h

Panel C:
- grain-size summary plot vs soak T/time, using only specimens with secure linkage

### How to quantify grain size
Use one method only across the whole figure:
- equivalent circle diameter from segmented grains, or
- lineal intercept if boundaries are clearer than polygons

Report:
- number of fields per specimen
- number of grains/intercepts per specimen
- median and IQR if skewed
- mean ± SD only if approximately symmetric
- whether twins were merged or separated
- minimum included grain area/intercept length

### Statistical unit
Very important:
- **run/specimen is the experimental unit**
- not the individual grain

If you have many grains from one specimen, that improves the estimate of that specimen’s grain size, but it does **not** increase n for between-condition inference.

### Recommended microstructure claim
Do not claim formal grain-growth kinetics unless the image archive is exceptionally clean. For HardwareX, you don’t need that. The right claim is:

> linked archived micrographs show that the furnace produces systematic microstructural coarsening across increasing soak severity, and that the repeated 1200 °C / 12 h Ni4N5 condition yields comparable final grain structures across runs.

---

## 2. Specimen ↔ thermal-history linkage table

## How to populate it
The current empty table should become a **provenance table**, not a giant characterization dump.

### Recommended columns
Use these columns:

| Column | Source |
|---|---|
| Specimen ID | filename / image folder label |
| Material | specimen prefix (`Ni4N5`, `Ni200`, `YSZ`, etc.) |
| Run ID | parsed from filename and confirmed against `run_summary.csv` |
| Raw log file | path or basename of `.xlsx/.txt/.lvm` |
| Nominal soak T (°C) | parsed from filename where present |
| Logged soak T (°C) | `run_summary.csv` `soak_temp_C` |
| Soak duration (min or h) | `run_summary.csv` `duration_min` and/or parsed nominal label |
| Atmosphere / flow flag | `run_summary.csv` `has_flow`; plus text note from SOP if known |
| Crucible / susceptor geometry | fixed text for the chosen figure cohort; if variable, note variant |
| Cooling description | from SOP or run notes if known; otherwise “cooling not retrospectively parameterized” |
| Characterization files | SEM/optical/EBSD filenames |
| Included in figure? | Fig. 5A / 5B / supplementary only |

### Important distinction
Keep both:
- **nominal soak condition from filename**
- **logged soak temperature from trace summary**

That avoids reviewer complaints when the pyrometer mean is 1302 °C for a “1300C” file.

### Canonical run IDs to feature in the main table
Feature a compact set first:
- `IFrun039_Ni4N5_026_1200C_6h`
- `IFrun040_Ni4N5_027_1250C_6h`
- `IFrun038_Ni4N5_025_1300C_1h`
- `IFrun079_Ni4N5_084_1300C_12h`
- `IFrun032_Ni4N5_022_1400C_10min`
- `IFrun072_Ni4N5_079,080_1400C_12h`
- `IFrun081_Ni200_015_1325C_20h`
- `IFrun080_Ni200_017_1325C_40h`
- the 8-run repeatability block `IFrun052–060`

### Example row structure

| Specimen | Material | Run ID | Nominal soak | Logged soak T | Soak time | Atmosphere | Characterization |
|---|---|---|---|---:|---|---|---|
| `Ni4N5_026` | Ni4N5 | `IFrun039_Ni4N5_026_1200C_6h` | 1200 °C | 1200.2 °C | 6 h | no-flow archived configuration | `Ni4N5_026_SEM_*.tif`; `Ni4N5_026_optical_*.jpg` |

### What to do with atmosphere
From the attached data, you have `has_flow` yes/no. That is enough for the table now. Do not invent gas composition per run unless it is explicitly documented in the SOP or filename.

Suggested wording for the table note:

> “Atmosphere” indicates whether active gas flow was present in the machine-parsed log summary (`has_flow`), not a complete reconstructed gas chemistry for every retrospective run.

---

## 3. Honest treatment of limitations: exact caveat sentences to add

These sentences should go into the validation section and discussion.

## Retrospective data / non-DOE
> The validation dataset is retrospective rather than prospectively designed. Accordingly, the archived runs are not treated as a balanced factorial experiment, and comparisons are restricted to internally consistent subsets with matching nominal profile, material, and operating configuration.

## Configuration dependence of calibration
> Because induction coupling, radiative view factors, and pyrometer line-of-sight depend on specimen/crucible geometry and optical alignment, the power-command/temperature calibration is reported only for fixed archived configurations and should not be interpreted as a universal transfer function for all loads.

## Pyrometer / emissivity limitation
> The reported temperatures are closed-loop ratio-pyrometer readings obtained in a fixed optical geometry. For retrospective validation, these values are used as the operational control temperature; absolute specimen temperature may still depend on emissivity, surface condition, and line-of-sight details not fully reconstructable for every archived run.

## Repeatability scope
> Run-to-run repeatability is evaluated only within the most internally consistent cohort available in the archive (`IFrun052–060`, Ni4N5, 1200 °C / 12 h, flow-enabled configuration). Runs from other periods or geometries are not pooled into that estimate.

## Single-operator / long-term archive
> The system was operated over multiple years primarily within one laboratory workflow. This improves procedural consistency but limits assessment of inter-operator variability.

## Microstructure linkage
> Microstructural comparisons are reported only for specimens whose image files can be linked unambiguously to a logged thermal history. Unlinked or ambiguously labeled images are excluded rather than inferred.

## Missing baselines
> Where as-received baseline images are unavailable for a specific specimen batch, microstructural results are framed as final-state comparisons across archived anneals rather than as fully parameterized grain-growth kinetics.

## Sparse replicates
> Most archived temperature/time conditions are singletons; therefore, statistical inference is limited to descriptive summaries except for the small number of repeated conditions available in the archive.

## Experimental unit / pseudoreplication
> For grain-size analysis, the specimen or run is treated as the experimental unit. Multiple grains measured within a field are used to estimate specimen-level grain size but are not treated as independent replicate experiments.

---

## 4. Which empirical results strengthen which hardware claims

## Claim: generator-agnostic closed-loop control can hold a programmed soak
Where to support it:
- Validation section, Figure 3
- cite `IFrun079` and `IFrun081`

Use these numbers:
- `IFrun079`: **1302.1 ± 3.0 °C** during a **12 h** soak, drift **−0.021 °C/h**
- `IFrun081`: **1326.5 ± 1.5 °C** during a **20 h** soak, drift **−0.004 °C/h**

## Claim: the platform is repeatable in a fixed configuration
Where to support it:
- Validation section, Figure 4
- mention in abstract if space permits

Use this cohort:
- `IFrun052–060` Ni4N5 1200 °C / 12 h, `n = 8`
- soak T **1201.1 ± 1.3 °C**, range **1199.8–1204.1 °C**

## Claim: wide operating window
Where to support it:
- Results text introducing validation section
- possibly specs/operation section

Use archive summary:
- temperatures represented in attached parsed runs: roughly **1200–1400 °C** among the good exported figure traces
- full inventory spans **900–1400 °C**
- soak durations from **10 min to 40 h**

## Claim: long-duration high-vacuum induction annealing is practical
Where to support it:
- Figure 4 long-soak panel or validation text

Use:
- `IFrun080` 40 h
- `IFrun081` 20 h

## Claim: material versatility / susceptor-coupled heating
Where to support it:
- hardware description and validation text

Use cautiously:
- full inventory includes **Ni200, Ni4N5, crucible, Pd evaporation, YSZ-related work**
- this supports **breadth of use**, not equal-depth validation across all materials

Suggested sentence:

> Beyond the Ni-based annealing runs used for quantitative validation, the archived record also includes crucible-only tests and YSZ/Pd-related processing runs, indicating that the same furnace architecture has been applied to both directly coupled metallic loads and susceptor-mediated oxide workflows.

Do not make a quantitative YSZ control claim unless you have the linked thermal/microstructural files in hand.

---

## 5. Concrete ordered to-do list

## Can be done now from attached data

### 1. Replace the validation-plan prose with real results prose
- convert Figure 2–5 paragraphs from future tense to present/past tense
- insert the run IDs named above
- insert the quantitative metrics already computed from the exported CSVs

### 2. Build Figure 2 from the existing per-run CSVs
- use `IFrun039`, `040`, `038`, `032`
- extract soak-mean power and soak-mean temperature
- plot points with horizontal error bars from power SD if desired
- fit a line as a guide only for this subset
- caption must say “fixed archived Ni4N5 configuration”

### 3. Build Figure 3 from `IFrun079_Ni4N5_084_1300C_12h`
- temperature vs time with setpoint overlay
- power vs time below
- annotate rise, overshoot, settling, soak region
- add inset table with the computed metrics

### 4. Build Figure 4A repeatability summary from `run_summary.csv`
- use only `IFrun052,054,055,056,057,058,059,060`
- plot soak temperature by run with mean ± SD line
- optionally add peak temperature and duration as small side panels
- if possible, regenerate and overlay full traces from the raw logs for these runs

### 5. Build Figure 4B long-soak panel
- use `IFrun081` and `IFrun080`
- show full temperature and power traces or a compressed view with a zoomed soak inset
- report soak mean, SD, drift, and in-band duration

### 6. Populate the specimen ↔ thermal-history linkage table for the thermal cohorts
- start with the canonical runs listed above
- fill nominal and logged soak conditions from filename + `run_summary.csv`
- include a placeholder “characterization file(s)” column waiting for image filenames

### 7. Fix the current TODO that points to `RyanWeber.pdf`
- remove the implication that the Ryan Weber PDF is the source of Ni micrographs
- it is not your main Ni/Ni4N5 validation asset
- point instead to the actual SEM/optical image directories keyed by `Ni4N5_###` and `Ni200_###`

## Needs the SEM/optical image sets pulled and registered

### 8. Pull the image directories and build a specimen manifest
For every `Ni4N5_###` and `Ni200_###` image set:
- specimen ID
- file names
- microscopy mode
- magnification / scale bar
- whether as-received or annealed
- whether EBSD exists

### 9. Join the image manifest to the run manifest
- map each specimen ID to one run ID
- exclude any ambiguous mappings
- produce a clean `specimen_run_linkage.csv`

### 10. Choose the microstructure figure specimens
Minimum set:
- one as-received Ni4N5
- one each from 1200/6 h, 1250/6 h, 1300/1 h, 1300/12 h, 1400/10 min or 1400/12 h
- one as-received Ni200
- Ni200 20 h and 40 h
- 3–4 specimens from the 1200 °C / 12 h repeatability cohort

### 11. Measure grain size with one locked workflow
- define segmentation/intercept rules before measuring
- record fields/specimen and grains/specimen
- summarize at specimen level first
- only then compare across runs

### 12. Finish Figure 5 and the linkage table together
- every image in Figure 5 must appear in the linkage table
- every grain-size point must map to a specific run ID and file set

---

## Section-by-section manuscript edits

## Abstract
Add one sentence with real validation numbers, for example:

> Retrospective analysis of archived anneal logs showed repeatable 1200 °C / 12 h Ni4N5 processing within a fixed configuration (1201.1 ± 1.3 °C across 8 runs) and stable long-duration control up to 40 h at 1325 °C.

## Validation and characterization
Replace the current forward-looking figure plan with:
- actual figure captions
- actual run IDs
- actual metrics above
- explicit limitations paragraph at the end

## Hardware/operation section
When describing the pyrometer-feedback control loop, cross-reference Figure 3 and the long-soak panel.

## Safety / operating envelope
If you mention operating range, support it with the archive summary:
- full inventory spans **900–1400 °C** and soaks from **minutes to 40 h**

## Discussion / limitations
Add the caveat block almost verbatim from Section 3 above.

---

## Recommended final figure set

### Figure 1
System overview photo/schematic composite.

### Figure 2
Operational power-command → steady-state temperature calibration for fixed Ni4N5 configuration:
`IFrun039`, `040`, `038`, `032`.

### Figure 3
Representative closed-loop temperature and power trace with metrics:
`IFrun079_Ni4N5_084_1300C_12h`.

### Figure 4
Two-panel validation summary:
- **4A:** repeatability across `IFrun052–060` (Ni4N5 1200 °C / 12 h, n = 8)
- **4B:** long-soak stability from `IFrun081` (20 h) and `IFrun080` (40 h)

### Figure 5
Microstructural validation with linked Ni4N5/Ni200 specimens plus grain-size summary.

That set is strong, honest, and very HardwareX.

- Discretionary analytical decisions made during the analysis:
  - Used the **Ni4N5 no-flow subset** (`IFrun039`, `040`, `038`, `032`) for the power-command/temperature calibration because it is the cleanest internally consistent archived configuration; excluded broader mixed-era runs from the same fit.
  - Treated the **IFrun052–060 Ni4N5 1200 °C / 12 h flow-enabled cohort** as the main repeatability set because it is the strongest same-profile repeated condition in the attached archive.
  - Used **`IFrun079_Ni4N5_084_1300C_12h`** as the representative control-trace figure because it balances readability with a long enough soak to demonstrate real closed-loop stability.
  - Used **`IFrun081` and `IFrun080`** as the long-soak stability examples because they provide 20 h and 40 h demonstrations in the same nominal Ni200 1325 °C condition.
  - Computed control metrics using a **±10 °C soak deadband** around nominal setpoint to define the steady-state segment, because the manuscript asks for practical control-performance metrics and the archive is retrospective rather than a formal control-design experiment.
  - Reported **simple descriptive statistics** for archival repeatability and microstructure planning rather than formal hypothesis tests because most conditions are unreplicated and the data are retrospective, non-DOE, and vulnerable to pseudoreplication.
  - Recommended presenting the power-command/temperature relation as an **operational calibration** rather than a universal transfer function because the archive contains configuration-dependent offsets at the same nominal temperature.
  - Recommended treating the **specimen/run** rather than individual grains as the experimental unit for microstructure analysis to avoid pseudoreplication.
  - Recommended separating **nominal filename-derived soak condition** from **logged soak temperature from `run_summary.csv`** in the linkage table because both are scientifically useful and they are not always identical.