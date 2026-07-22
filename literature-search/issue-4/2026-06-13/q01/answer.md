# Best Practices for Controlling Grain Growth during Vacuum Induction Furnace Annealing of Steels and Alloys

## 1. Introduction

Vacuum induction furnace annealing is widely used for stress relief, homogenization, and solution treatment of steels and nickel-based alloys. The vacuum environment (typically 8 × 10⁻³ Pa or better) eliminates oxidation and decarburization while providing precise temperature control (meng2023designofvacuum pages 4-7, meng2023designofvacuum pages 2-4). However, the high temperatures required for homogenization and stress relief inevitably promote grain growth, which must be carefully managed to preserve mechanical performance. This document summarizes best practices for controlling grain growth while achieving the intended metallurgical objectives, drawing on peer-reviewed literature across carbon steels, stainless steels, and nickel-based superalloys.

## 2. Fundamental Mechanisms of Grain Growth during Annealing

Grain growth during annealing is driven by the reduction of grain boundary energy. Grain boundary mobility follows an Arrhenius relationship, increasing strongly with temperature (liu2021studyofgrain pages 2-5, liu2021studyofgrain pages 1-2). For Ni-based superalloys, grain growth kinetics have been described by a near-parabolic law with an exponent slightly above 2, indicating boundary-migration-controlled kinetics with minor precipitate pinning contributions (liu2021studyofgrain pages 1-2). Experimental data confirm that grain size increases continuously with both holding time and temperature; for example, in one Ni-based superalloy, grain size grew from ~106 µm at 1353 K/600 s to ~299 µm at 1473 K/540 s (liu2021studyofgrain pages 2-5).

Two primary mechanisms retard grain growth during annealing:

**Zener pinning** by second-phase precipitates restricts grain boundary migration. The limiting grain size scales approximately as D_lim ∝ d/f, where d is the mean particle diameter and f is the volume fraction of pinning particles (ringer1990oninteractionsand pages 167-174, kisko2015effectofnb pages 6-7). Smaller, more numerous precipitates provide stronger pinning, and particles with elongated or coherent morphologies are even more effective (mohrbacher2026applicationofmicroalloying pages 2-4, ringer1989ontheinteraction pages 5-7). Ti-rich carbonitrides (e.g., TiN) are particularly effective due to their low solubility and resistance to Ostwald coarsening (ringer1990oninteractionsand pages 77-83, ringer1990oninteractionsand pages 90-95).

**Solute drag** occurs when dissolved microalloying atoms (Nb, Mo) segregate to grain boundaries and impede their motion. In microalloyed steels, solute drag has a relatively more significant contribution to austenite conditioning than precipitation pinning alone (mohrbacher2026applicationofmicroalloying pages 1-2, mohrbacher2026applicationofmicroalloying pages 2-4). Solute Nb in combination with Mo provides enhanced resistance to grain growth at temperatures up to ~1050°C during vacuum carburizing operations (seo2020effectofmo pages 1-2).

## 3. Practical Soak Temperature–Time Guidance

The following table provides practical soak temperature and time guidance ranges organized by alloy class and treatment objective, drawn from experimental and handbook data.

| Alloy Class | Treatment Objective | Soak Temperature Range (°C) | Typical Soak Time | Grain Growth Risk Level | Key Notes |
|---|---|---:|---|---|---|
| Low/medium carbon steels | Stress relief / process anneal | 540–650 | 0.5–1 h/in section thickness; often ~1 h minimum after equalization | Low | Prefer the lowest temperature that achieves stress relief; staying below Ac1 minimizes recrystallization and grain coarsening. Digges notes process annealing near ~650°C and lower stress-relief around ~540°C when no further cold work is intended; vacuum heating improves surface cleanliness but soak should still be limited to the minimum needed for uniform temperature (digges1966heattreatmentand pages 13-15, meng2023designofvacuum pages 4-7, meng2023designofvacuum pages 2-4) |
| Low/medium carbon steels | Full anneal | 800–900 | 0.5–1 h/in after the part reaches temperature | Medium–High | Heat about 15–30°C above the critical range, then soak only long enough for thermal equalization; longer hold increases ferrite/austenite grain size. Use the lower end for small sections and the upper end for large sections (digges1966heattreatmentand pages 13-15, digges1966heattreatmentand pages 36-37) |
| Alloy steels (e.g., 4140) | Stress relief | 540–675 | 0.5–1 h/in section thickness | Low–Medium | Keep below Ac1 to avoid unnecessary phase transformation. Vacuum processing is advantageous where scale-free surfaces or low decarburization are required; grain growth risk remains modest unless hold is excessive (digges1966heattreatmentand pages 13-15, meng2023designofvacuum pages 4-7) |
| Alloy steels (e.g., 4140) | Full anneal | 815–845 | 0.5–1 h/in after equalization | Medium | Digges tabulates ~816–843°C for 4140-class annealing. Use shortest effective soak because grain growth depends strongly on time and temperature (digges1966heattreatmentand pages 36-37, digges1966heattreatmentand pages 13-15) |
| Alloy steels (e.g., 4340) | Full anneal | 870–900 | 0.5–1 h/in after equalization | Medium–High | Digges tabulates ~871–899°C for 4340-class annealing. Large sections may need the high end of the range, but higher soak severity increases grain-coarsening tendency (digges1966heattreatmentand pages 36-37, digges1966heattreatmentand pages 13-15) |
| Austenitic stainless steels (e.g., 316L) | Stress relief / recovery anneal | 600–800 | ~0.5–2 h depending on section size and residual stress level | Low–Medium | Favor recovery-only schedules when dimensional stability is the goal. In heavily cold-worked stainless steels, higher heating rates suppress selective grain growth and produce finer recrystallized structures; slow heating raises grain-growth risk (hirota2008recrystallizationandgrain pages 6-7, hirota2008recrystallizationandgrain pages 1-2, meng2023designofvacuum pages 4-7) |
| Austenitic stainless steels (e.g., 316L) | Recrystallization / solution anneal | 800–950 for strong recrystallization; ~1050 typical solutionizing window by practice | ~0.5–1 h for sheet/light section; thicker sections need longer equalization | Medium–High | SUS316L showed annealing between 1073–1223 K (800–950°C) with finer grains at higher heating rates; once recrystallization is complete, further time at temperature promotes grain growth. Use rapid heat-up and minimum hold (hirota2008recrystallizationandgrain pages 6-7, hirota2008recrystallizationandgrain pages 1-2) |
| PH stainless steels (e.g., 17-4 PH) | Stress relief | 550–650 | ~1–4 h, depending on residual stress and section | Low | Stress relief can reduce residual stress with limited coarsening. Keep below solutionizing/homogenization temperatures if grain size must be preserved (cheruvathur2016additivemanufacturingof pages 7-11, meng2023designofvacuum pages 4-7) |
| PH stainless steels (e.g., 17-4 PH) | Homogenization / solutionizing | ~1050–1150 | Solutionizing ~1 h; homogenization ~1150°C for >90 min in cited cast-alloy guidance | Medium–High | For 17-4 PH analogs, homogenization at 1150°C for >90 min followed by solutionizing at 1050°C reduces segregation, but carbide coarsening still occurs and full microchemical homogenization may remain incomplete below the carbide solvus (~1250°C) (cheruvathur2016additivemanufacturingof pages 7-11) |
| Ni-based superalloys (Alloy 718) | Sub-solvus solution / stress relief | 954–982 | ~1 h typical; repeated 0.5 h steps also reported | Medium | Alloy 718 schedules of 954°C/1 h and 982°C/1 h are documented; 954°C/15 h produced much larger δ-phase content, so long holds should be avoided unless intentionally precipitating. Good choice when stress relief or controlled sub-solvus solution is needed without aggressive grain coarsening (andersson2011weldabilityofprecipitation pages 41-44) |
| Ni-based superalloys (Waspaloy) | Sub-solvus / solution treatment | 996–1080 | ~4 h | Medium–High | Waspaloy solution treatment in this range produced larger grains at the higher temperatures. Stay at the lowest temperature consistent with dissolution/homogenization targets (andersson2011weldabilityofprecipitation pages 41-44) |
| Ni-based superalloys (PM alloys) | Sub-solvus solution | 950–1050 | ~5–60 min; often ≤45–60 min | Low–Medium below ~1010°C; Medium near 1050°C | PM superalloy data show slow grain growth near ~1010°C, with only small size increase from 5 to 45 min. This is the preferred regime when stress relief/homogenization is needed with minimal coarsening (tian2009experimentalandsimulation pages 1-2) |
| Ni-based superalloys (PM alloys) | Near-/super-solvus solution | 1100–1150 | Typically 15–60 min; keep <60 min when dual microstructure or limited coarsening is required | High | Grain growth accelerates sharply above ~1110°C. A furnace set ~20–40°C above the γ′ solvus and hold times beyond ~60 min caused rapid coarsening, especially in hotter regions; temperature uniformity is critical (tian2009experimentalandsimulation pages 6-7) |
| Ni-based superalloys (cast 718Plus / similar) | Homogenization | 1125–1200 | ~5 h per step; combined 1125°C/5 h + 1200°C/5 h also reported | High | Effective for reducing segregation, but grain growth and eutectic/Laves-related risks rise rapidly as temperature increases. Use only where chemistry requires it, and verify against incipient-melting limits and segregation state (andersson2011weldabilityofprecipitation pages 41-44) |
| Ni-based superalloys (cast VDM780-like) | Homogenization / preheat | ~1160 | Alloy-specific; evidence supports the temperature but not a general soak time | High | VIM-produced VDM780 used ~10^-3 mbar melting and selected 1160°C from STA as a homogenization/preheat temperature. Good example that homogenization temperature should be tied to thermal analysis and segregation morphology, not a generic rule (chavilian2025acceleratedhomogenizationof pages 2-4) |
| Ni-based superalloys (general grain-growth kinetics reference) | Isothermal anneal after solutionizing | 1080–1200 | 180–2400 s in experiments | Medium–Very High | Experimental Ni-superalloy grain growth rises strongly with both temperature and time: e.g., after solution treatment, grain size increased substantially between 1353–1473 K and 180–2400 s. This supports a best practice of shortest possible hold and avoiding unnecessary exposure above solvus (liu2021studyofgrain pages 2-5, liu2021studyofgrain pages 1-2) |


*Table: This table summarizes practical soak temperature and time ranges for vacuum furnace annealing of steels and nickel-based alloys, organized by alloy class and treatment objective. It also flags relative grain-growth risk and notes the main control levers needed to achieve stress relief or homogenization without excessive coarsening.*

Key principles underlying this guidance include:

- **Process (stress-relief) annealing** of steels is performed below the lower critical temperature (Ac₁), typically around 540–650°C, with soak time scaled to section thickness at approximately 0.5–1 h per inch of cross-section (digges1966heattreatmentand pages 13-15). At these temperatures, grain growth risk is minimal because the driving force for boundary migration is low.

- **Full annealing** of steels requires heating 15–50°F (~10–30°C) above the upper critical temperature to achieve complete austenitization, with minimum soak time for thermal equalization; extended dwell promotes undesirable ferrite grain coarsening (digges1966heattreatmentand pages 13-15, digges1966heattreatmentand pages 36-37).

- **Sub-solvus solution treatment** of Ni-based superalloys (typically 950–1050°C) retains undissolved γ′ or δ-phase precipitates that pin grain boundaries, preserving fine grain structures. Alloy 718 schedules of 954°C/1 h and 982°C/1 h are commonly documented (andersson2011weldabilityofprecipitation pages 41-44). PM superalloys show slow grain growth near ~1010°C with only ~4 µm increase over 45 min of additional holding (tian2009experimentalandsimulation pages 1-2).

- **Near-/super-solvus treatment** of Ni-based superalloys (1100–1200°C) causes rapid grain coarsening once pinning precipitates dissolve. In PM superalloys, furnace temperatures set 20–40°C above the γ′ solvus (~1150°C) with hold times beyond 60 min produce substantial coarsening, particularly in hotter regions of the part (tian2009experimentalandsimulation pages 6-7).

- **Homogenization of cast superalloys** may require multi-step treatments (e.g., 1125°C/5 h + 1200°C/5 h for Allvac 718Plus) to eliminate microsegregation and Laves phases, but carries high grain growth risk that must be accepted as a necessary trade-off (andersson2011weldabilityofprecipitation pages 41-44).

## 4. Best Practices for Grain Growth Control

The following table summarizes evidence-based strategies for limiting grain coarsening during vacuum furnace annealing while achieving the intended treatment objective.

| Strategy | Mechanism/Rationale | Practical Guidance | Applicable Alloy Systems |
|---|---|---|---|
| Minimize soak temperature | Grain growth rate rises strongly with temperature because grain-boundary mobility increases; full anneals and near-/above-solvus treatments promote much more coarsening than recovery/stress-relief cycles (digges1966heattreatmentand pages 13-15, liu2021studyofgrain pages 2-5, liu2021studyofgrain pages 1-2) | Use the lowest temperature that still achieves the objective: for steel stress relief stay subcritical when possible; for stainless and Ni alloys prefer recovery or sub-solvus schedules unless segregation or phase-dissolution requirements force higher temperatures (digges1966heattreatmentand pages 13-15, andersson2011weldabilityofprecipitation pages 41-44, tian2009experimentalandsimulation pages 1-2) | Carbon and alloy steels, stainless steels, PH stainless steels, Ni-based superalloys |
| Minimize soak time | Time at temperature adds directly to grain coarsening; even when temperature is fixed, longer holds increase grain size and can coarsen pinning precipitates (digges1966heattreatmentand pages 13-15, liu2021studyofgrain pages 2-5, tian2009experimentalandsimulation pages 1-2) | For steels, use only the time needed for thermal equalization, commonly about 0.5–1 h/in section thickness; for Ni alloys keep high-temperature holds as short as practical, often tens of minutes rather than hours near the solvus unless homogenization specifically requires longer exposure (digges1966heattreatmentand pages 13-15, andersson2011weldabilityofprecipitation pages 41-44, tian2009experimentalandsimulation pages 6-7) | Steels, stainless steels, Ni-based superalloys |
| Control heating rate | Faster heating increases nucleation density during recrystallization and reduces the time spent in the temperature window where selective grain growth can occur; slow heating permits preferential growth of some grains (hirota2008recrystallizationandgrain pages 6-7, hirota2008recrystallizationandgrain pages 1-2, strady2026grainstructurebehavior pages 1-2) | Ramp as quickly as part geometry and distortion limits allow through the recrystallization range; avoid unnecessarily slow ramps for cold-worked stainless steels and PM superalloys, especially near solvus temperatures where abnormal grains can form during prolonged heat-up (hirota2008recrystallizationandgrain pages 6-7, hirota2008recrystallizationandgrain pages 1-2, strady2026grainstructurebehavior pages 1-2) | Cold-worked stainless steels, PM Ni superalloys, heavily deformed alloys |
| Microalloying with Nb, Ti, V, Mo | Fine carbides/nitrides/carbonitrides pin grain boundaries by Zener pinning and solute drag; Nb, Ti, V, and Mo improve resistance to abnormal grain growth, especially in austenite (seo2020effectofmo pages 1-2, mohrbacher2026applicationofmicroalloying pages 1-2, kisko2015effectofnb pages 6-7, sha2009graingrowthbehavior pages 3-6) | Where chemistry can be selected, use Nb/Ti/V microalloying for steels and Nb+Mo combinations for high-temperature vacuum-carburizing or annealing steels; maintain precipitates fine and numerous rather than relying on coarse particles (seo2020effectofmo pages 1-2, kisko2015effectofnb pages 6-7, sha2009graingrowthbehavior pages 3-6, mohrbacher2026applicationofmicroalloying pages 2-4) | Microalloyed steels, vacuum-carburizing steels, austenitic stainless steels |
| Hollomon-Jaffe parameter optimization | Temperature and time act together; the Hollomon-Jaffe parameter provides a compact way to compare schedules and avoid drifting from recovery/stress relief into recrystallization and grain growth (mohrbacher2026applicationofmicroalloying pages 4-6) | For microalloyed steels, keep the parameter in the recovery-dominant window when stress relief is the goal; avoid HP values associated with full recrystallization and grain growth unless refinement via recrystallization is desired (mohrbacher2026applicationofmicroalloying pages 4-6) | Steels, especially microalloyed and cold-worked strip/product forms |
| Sub-solvus vs super-solvus selection | Below the solvus, undissolved precipitates remain to pin boundaries; above the solvus, pinning is lost and grain growth accelerates sharply (tian2009experimentalandsimulation pages 6-7, andersson2011weldabilityofprecipitation pages 41-44) | Stay sub-solvus whenever stress relief or moderate homogenization is sufficient; move to near-/super-solvus only when segregation removal or phase dissolution requires it, and then strictly limit hold time and thermal gradients (tian2009experimentalandsimulation pages 6-7, andersson2011weldabilityofprecipitation pages 41-44) | Ni-based superalloys, PH alloys, some stainless and tool steels with stable precipitates |
| Precipitate size and volume fraction control | Limiting grain size scales roughly with particle size divided by particle volume fraction; smaller, more numerous particles give stronger pinning, and elongated/coherent particles can be even more effective (kisko2015effectofnb pages 6-7, ringer1990oninteractionsand pages 167-174, ringer1990oninteractionsand pages 90-95, mohrbacher2026applicationofmicroalloying pages 2-4) | Design process routes to preserve fine precipitates: avoid overlong holds that coarsen them, exploit lower-temperature precipitation where feasible, and recognize that coarse solidification precipitates are usually less effective than fine solid-state precipitates (ringer1990oninteractionsand pages 77-83, ringer1990oninteractionsand pages 167-174, mohrbacher2026applicationofmicroalloying pages 2-4) | Microalloyed steels, precipitation-strengthened stainless steels, Ni superalloys |
| Vacuum level and temperature uniformity | Vacuum limits oxidation/decarburization and contamination, but grain control still depends on uniform temperature; local hot spots and radial gradients produce localized rapid grain growth (chavilian2025acceleratedhomogenizationof pages 2-4, meng2023designofvacuum pages 4-7, meng2023designofvacuum pages 2-4) | Heat only after the target vacuum is achieved; maintain stable vacuum, good thermocouple coverage, and tight uniformity. Typical reported practice includes high vacuum for annealing and minimizing losses/leaks through penetrations. Avoid load arrangements that create rim-to-core temperature differences near critical temperatures (chavilian2025acceleratedhomogenizationof pages 2-4, meng2023designofvacuum pages 4-7, meng2023designofvacuum pages 2-4, tian2009experimentalandsimulation pages 6-7) | All vacuum-annealed steels and alloys; especially large sections and PM/cast superalloys |
| Cooling rate control | Cooling affects re-precipitation, retained phase fractions, and post-soak coarsening; too slow a cool can allow unwanted precipitation or continued microstructural coarsening, while controlled cooling can preserve the intended sub-solvus/supersolvus result (andersson2011weldabilityofprecipitation pages 41-44, strady2026grainstructurebehavior pages 1-2) | After high-temperature holds, cool at the rate required by the alloy system: enforce sufficiently fast cooling from solution temperatures in Ni alloys and PH stainless steels to prevent unwanted precipitation during descent, but tailor the cool to avoid distortion or cracking in steels (andersson2011weldabilityofprecipitation pages 41-44, strady2026grainstructurebehavior pages 1-2, cheruvathur2016additivemanufacturingof pages 7-11) | PH stainless steels, Ni-based superalloys, alloy steels |
| Tie cycle design to section size and segregation severity | Thick sections need more time to equalize, but excess dwell beyond equalization only increases coarsening; heavily segregated cast structures may justify harsher homogenization than wrought or PM materials (digges1966heattreatmentand pages 13-15, cheruvathur2016additivemanufacturingof pages 7-11, chavilian2025acceleratedhomogenizationof pages 2-4) | Use mild stress-relief schedules for wrought parts and reserve long high-temperature homogenization cycles for castings or severely segregated material. Validate temperature selection with thermal analysis/solvus data rather than using one generic recipe across alloys (cheruvathur2016additivemanufacturingof pages 7-11, chavilian2025acceleratedhomogenizationof pages 2-4) | Wrought steels, cast stainless steels, cast and wrought Ni-based superalloys |


*Table: This table summarizes evidence-based strategies for limiting grain coarsening during vacuum furnace annealing while still achieving stress relief or homogenization. It is useful as a process-planning checklist across steels, stainless steels, and Ni-based alloys.*

### 4.1 Temperature and Time Minimization

The most straightforward approach is to use the lowest soak temperature and shortest soak time consistent with the treatment objective (digges1966heattreatmentand pages 13-15, tian2009experimentalandsimulation pages 1-2). The Hollomon–Jaffe parameter (HP = T·[log(t) + 20]·10⁻³) provides a useful framework for combining temperature and time into a single parameter; for microalloyed steels, keeping HP in the recovery-dominant window (HP ≈ 16–19.3) avoids recrystallization and grain growth, while HP values above ~20.5 enter the grain-growth regime (mohrbacher2026applicationofmicroalloying pages 4-6).

### 4.2 Heating Rate Control

Higher heating rates through the recrystallization range produce more dispersed nucleation sites and finer recrystallized microstructures. In cold-rolled SUS316L, heating rates above ~1 K/s produced homogeneously nucleated, randomly oriented grains with a lognormal size distribution, whereas slow heating rates (0.031 K/s) allowed selective grain growth of preferred orientations and coarser final structures (hirota2008recrystallizationandgrain pages 6-7, hirota2008recrystallizationandgrain pages 1-2). For PM Ni-based superalloys, slower heating rates (e.g., 2°C/min) to the solution temperature increase the propensity for abnormal grain growth (>200 µm grains) due to prolonged exposure near the γ′ solvus where ripening and partial dissolution of precipitates reduce pinning pressure (strady2026grainstructurebehavior pages 1-2).

### 4.3 Microalloying and Precipitate Engineering

Microalloying with Nb, Ti, V, and/or Mo produces fine carbide, nitride, or carbonitride precipitates that pin austenite grain boundaries via the Zener mechanism (kisko2015effectofnb pages 6-7, sha2009graingrowthbehavior pages 3-6). In vacuum carburizing steels, Nb combined with Mo provides grain-growth resistance up to ~1050°C, whereas Nb alone offers adequate control at conventional carburizing temperatures of 920–940°C (seo2020effectofmo pages 1-2). In austenitic stainless steels, ≥0.28 wt% Nb provides sufficient pinning force via fine NbC/NbN precipitates (<50 nm) to prevent grain coarsening at 1373 K (kisko2015effectofnb pages 6-7).

The effectiveness of Zener pinning depends critically on preserving fine precipitate sizes: prolonged annealing coarsens particles following Lifshitz–Wagner kinetics, diminishing the pinning pressure (ringer1990oninteractionsand pages 77-83, mohrbacher2026applicationofmicroalloying pages 2-4). Coarsening accelerates above the Curie temperature due to enhanced diffusivity in paramagnetic ferrite, and particles formed during solidification are typically too coarse to be effective pinning agents (mohrbacher2026applicationofmicroalloying pages 2-4, ringer1990oninteractionsand pages 77-83).

### 4.4 Sub-Solvus vs. Super-Solvus Selection

Whenever possible, conducting annealing below the precipitate solvus temperature retains the second-phase particles needed for grain boundary pinning. For Ni-based superalloys, remaining below the γ′ solvus (typically 1100–1160°C depending on alloy) preserves fine γ′ precipitates and nanometric oxides/carbides that stabilize the grain structure (strady2026grainstructurebehavior pages 1-2). Above the solvus, precipitate dissolution removes the pinning force and grain growth accelerates sharply; grain coarsening in PM superalloys increased from grade 9–10 (bore, <1110°C) to grade 5.5–6 (rim, 1130–1150°C) within 60 min at these temperatures (tian2009experimentalandsimulation pages 6-7).

### 4.5 Vacuum Level and Temperature Uniformity

Vacuum furnace operation requires establishing and maintaining the target vacuum level before initiating heating to prevent contamination and ensure consistent heat transfer (meng2023designofvacuum pages 2-4). Temperature uniformity across the load is critical: reported vacuum annealing furnaces target ±5°C uniformity and ±3°C control accuracy, with multiple thermocouple zones monitoring the workpiece (meng2023designofvacuum pages 4-7). Local hot spots, particularly at outer surfaces of large parts, can cause localized rapid grain growth even when the bulk remains at acceptable temperatures (tian2009experimentalandsimulation pages 6-7). Radiation-dominated heat transfer in vacuum furnaces means careful load arrangement and possibly stepped heating are needed to minimize thermal gradients through thick sections.

### 4.6 Cooling Rate Management

Post-soak cooling must be managed to control precipitation and avoid continued coarsening during descent. For Ni-based superalloys, enforced argon cooling at rates >0.3°C/min to 500°C has been documented, with the cooling rate controlling the size, morphology, and distribution of reprecipitated phases (andersson2011weldabilityofprecipitation pages 41-44, strady2026grainstructurebehavior pages 1-2). For PH stainless steels such as 17-4 PH, controlled cooling from solutionizing affects retained austenite fraction and carbide populations, with both cryogenic and multiple tempering cycles used to optimize the final microstructure (cheruvathur2016additivemanufacturingof pages 7-11).

## 5. BibTeX References

The following BibTeX entries provide the primary references supporting the guidance in this document:

```bibtex
@article{digges1966heattreatmentand,
  author = {Digges, Thomas G. and Rosenberg, Samuel J.},
  title = {Heat Treatment and Properties of Iron and Steel},
  journal = {National Bureau of Standards Monograph},
  year = {1966},
  month = {Oct},
  doi = {10.6028/NBS.MONO.18},
  url = {https://doi.org/10.6028/NBS.MONO.18}
}

@article{mohrbacher2026applicationofmicroalloying,
  author = {Mohrbacher, Hardy},
  title = {Application of Microalloying for Controlling Recrystallization and Grain Growth During Downstream Steel Processing},
  journal = {Metallurgical and Materials Transactions A},
  volume = {57},
  number = {6},
  pages = {2548--2571},
  year = {2026},
  month = {Mar},
  doi = {10.1007/s11661-026-08172-5},
  url = {https://doi.org/10.1007/s11661-026-08172-5}
}

@article{hirota2008recrystallizationandgrain,
  author = {Hirota, Noriaki and Yin, Fuxing and Inoue, Tadanobu and Azuma, Tsukasa},
  title = {Recrystallization and Grain Growth Behavior in Severe Cold-Rolling Deformed SUS316L Steel under Anisothermal Annealing Condition},
  journal = {ISIJ International},
  volume = {48},
  number = {4},
  pages = {475--482},
  year = {2008},
  month = {Apr},
  doi = {10.2355/isijinternational.48.475},
  url = {https://doi.org/10.2355/isijinternational.48.475}
}

@article{seo2020effectofmo,
  author = {Seo, Eun Jung and Speer, John G. and Matlock, David K. and Cryderman, Robert L.},
  title = {Effect of Mo in Combination with Nb on Austenite Grain Size Control in Vacuum Carburizing Steels},
  journal = {Journal of Materials Engineering and Performance},
  volume = {29},
  number = {6},
  pages = {3575--3584},
  year = {2020},
  month = {Apr},
  doi = {10.1007/s11665-020-04751-8},
  url = {https://doi.org/10.1007/s11665-020-04751-8}
}

@article{tian2009experimentalandsimulation,
  author = {Tian, Gaofeng and Jia, Chengchang and Liu, Jiantao and Hu, Benfu},
  title = {Experimental and Simulation on the Grain Growth of P/M Nickel-Base Superalloy during the Heat Treatment Process},
  journal = {Materials \& Design},
  volume = {30},
  number = {3},
  pages = {433--439},
  year = {2009},
  month = {Mar},
  doi = {10.1016/j.matdes.2008.06.007},
  url = {https://doi.org/10.1016/j.matdes.2008.06.007}
}

@article{liu2021studyofgrain,
  author = {Liu, Yan-Xing and Ke, Zhi-Jiang and Li, Run-Hua and Song, Ju-Qing and Ruan, Jing-Jing},
  title = {Study of Grain Growth in a Ni-Based Superalloy by Experiments and Cellular Automaton Model},
  journal = {Materials},
  volume = {14},
  number = {22},
  pages = {6922},
  year = {2021},
  month = {Nov},
  doi = {10.3390/ma14226922},
  url = {https://doi.org/10.3390/ma14226922}
}

@article{kisko2015effectofnb,
  author = {Kisko, Anna and Talonen, Juho and Porter, David Arthur and Karjalainen, Leo Pentti},
  title = {Effect of Nb Microalloying on Reversion and Grain Growth in a High-Mn 204Cu Austenitic Stainless Steel},
  journal = {ISIJ International},
  volume = {55},
  number = {10},
  pages = {2217--2224},
  year = {2015},
  month = {Oct},
  doi = {10.2355/isijinternational.ISIJINT-2015-156},
  url = {https://doi.org/10.2355/isijinternational.ISIJINT-2015-156}
}

@article{sha2009graingrowthbehavior,
  author = {Sha, Qingyun and Sun, Zuqing},
  title = {Grain Growth Behavior of Coarse-Grained Austenite in a Nb-V-Ti Microalloyed Steel},
  journal = {Materials Science and Engineering A},
  volume = {523},
  number = {1--2},
  pages = {77--84},
  year = {2009},
  month = {Oct},
  doi = {10.1016/j.msea.2009.05.037},
  url = {https://doi.org/10.1016/j.msea.2009.05.037}
}

@article{ringer1989ontheinteraction,
  author = {Ringer, S. P. and Li, W. B. and Easterling, K. E.},
  title = {On the Interaction and Pinning of Grain Boundaries by Cubic Shaped Precipitate Particles},
  journal = {Acta Metallurgica},
  volume = {37},
  number = {3},
  pages = {831--841},
  year = {1989},
  month = {Mar},
  doi = {10.1016/0001-6160(89)90010-2},
  url = {https://doi.org/10.1016/0001-6160(89)90010-2}
}

@article{cheruvathur2016additivemanufacturingof,
  author = {Cheruvathur, Sudha and Lass, Eric A. and Campbell, Carelyn E.},
  title = {Additive Manufacturing of 17-4 PH Stainless Steel: Post-Processing Heat Treatment to Achieve Uniform Reproducible Microstructure},
  journal = {JOM},
  volume = {68},
  number = {3},
  pages = {930--942},
  year = {2016},
  month = {Dec},
  doi = {10.1007/s11837-015-1754-4},
  url = {https://doi.org/10.1007/s11837-015-1754-4}
}

@article{meng2023designofvacuum,
  author = {Meng, Jintao and Gao, Haitao and Ruan, Mixue and Guo, Hai and Zhou, Xiaojie and Zhang, Di},
  title = {Design of Vacuum Annealing Furnace Temperature Control System Based on GA-Fuzzy-PID Algorithm},
  journal = {PLOS ONE},
  volume = {18},
  number = {11},
  pages = {e0293823},
  year = {2023},
  month = {Nov},
  doi = {10.1371/journal.pone.0293823},
  url = {https://doi.org/10.1371/journal.pone.0293823}
}

@article{andersson2011weldabilityofprecipitation,
  author = {Andersson, J.},
  title = {Weldability of Precipitation Hardening Superalloys: Influence of Microstructure},
  year = {2011},
  note = {Source retrieved from available corpus metadata; journal not specified in retrieved record}
}

@article{strady2026grainstructurebehavior,
  author = {Strady, C. and Nicolay, A. and Bignon, M. and Agnoli, A. and de Jaeger, J. and Bozzolo, N. and Bernacki, M.},
  title = {Grain Structure Behavior of Powder Metallurgy Nickel Base $\gamma$--$\gamma'$ Superalloys Under $\gamma'$-Supersolvus Solution Heat-Treatment},
  journal = {Metallurgical and Materials Transactions A},
  volume = {57},
  number = {5},
  pages = {1872--1883},
  year = {2026},
  month = {Jan},
  doi = {10.1007/s11661-025-08107-6},
  url = {https://doi.org/10.1007/s11661-025-08107-6}
}

@article{graux2019precipitationandgrain,
  author = {Graux, Alexis and Cazottes, Sophie and De Castro, David and San Mart{\'i}n, David and Capdevila, Carlos and Cabrera, Jose Maria and Molas, S{\'i}lvia and Schreiber, Sebastian and Mirkovi{\'c}, Djordje and Danoix, Fr{\'e}d{\'e}ric and Bugnet, Matthieu and Fabr{\`e}gue, Damien and Perez, Michel},
  title = {Precipitation and Grain Growth Modelling in Ti-Nb Microalloyed Steels},
  journal = {Materialia},
  volume = {5},
  pages = {100233},
  year = {2019},
  month = {Mar},
  doi = {10.1016/j.mtla.2019.100233},
  url = {https://doi.org/10.1016/j.mtla.2019.100233}
}

@book{dossett2013asmhandbook4a,
  editor = {Dossett, Jon L. and Totten, George E.},
  title = {ASM Handbook, Volume 4A: Steel Heat Treating Fundamentals and Processes},
  publisher = {ASM International},
  address = {Materials Park, OH},
  year = {2013},
  isbn = {978-1-62708-011-8}
}

@article{wu2022meanfieldmodeling,
  author = {Wu, Kaisheng and Jeppsson, Johan and Mason, Paul},
  title = {Mean Field Modeling of Grain Growth and Zener Pinning},
  journal = {Journal of Phase Equilibria and Diffusion},
  volume = {43},
  number = {6},
  pages = {866--875},
  year = {2022},
  month = {Nov},
  doi = {10.1007/s11669-022-01005-z},
  url = {https://doi.org/10.1007/s11669-022-01005-z}
}
```


*Code_block: This BibTeX block compiles the main high-quality sources supporting guidance on vacuum annealing, stress relief, homogenization, and grain-growth control in steels and nickel-based alloys. It is useful as a ready-to-use reference list for citation managers and technical reports.*

## 6. Summary

Controlling grain growth during vacuum induction furnace annealing requires balancing the competing demands of stress relief or homogenization (which require elevated temperature and time) against the thermodynamic and kinetic drivers of grain coarsening. The principal best practices are: (1) use the minimum effective temperature and soak time, scaling soak duration to section thickness; (2) exploit faster heating rates to promote finer recrystallized microstructures; (3) leverage microalloying and precipitate engineering (Nb, Ti, Mo, V) for Zener pinning; (4) select sub-solvus treatment temperatures when feasible; (5) maintain vacuum integrity and tight temperature uniformity; and (6) control post-soak cooling to manage re-precipitation. Alloy-specific solvus data, thermal analysis, and segregation characterization should guide cycle design rather than relying on generic temperature–time recipes.
