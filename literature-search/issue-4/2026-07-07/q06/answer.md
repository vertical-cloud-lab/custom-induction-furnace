Question: Review the literature on grain growth in yttria-stabilized zirconia (YSZ): kinetics (growth exponents, activation energies), temperature-time regimes for producing large-grained (tens of microns) equiaxed microstructures at 1700-2500 C, and the effects of atmosphere (vacuum, argon, reducing conditions) and contamination (carbon, refractory metals) on grain growth, darkening/reduction, and specimen integrity. Cite high-quality sources with bibtex.

# Grain Growth in Yttria-Stabilized Zirconia: A Literature Review

## 1. Grain Growth Kinetics: The Power-Law Framework

Grain growth in yttria-stabilized zirconia (YSZ) is conventionally described by the phenomenological power-law equation:

**D^n − D₀^n = K·t**

where D is the instantaneous grain size, D₀ is the initial grain size, n is the grain growth exponent, K is a temperature-dependent rate constant following Arrhenius behavior K = K₀·exp(−Q/RT), and Q is the activation energy (aktas2014crystallizationandgrain pages 3-5, sharif1998controlofgrain pages 4-8). The grain growth exponent n encodes the rate-limiting mechanism: n = 2 corresponds to grain-boundary-mobility-controlled (parabolic) growth in single-phase systems; n = 3 indicates solute or impurity drag at grain boundaries; and n = 4 suggests pore-drag-controlled growth (aktas2014crystallizationandgrain pages 3-5, sharif1998controlofgrain pages 4-8).

### 1.1 Growth Exponents

For cubic 8 mol% YSZ (8Y-CSZ), Sharif et al. (1998) reported n ≈ 3 for pure material sintered between 1400–1600°C, consistent with impurity-drag-controlled growth. The addition of intergranular silicate phases altered the exponent: barium silicate and borosilicate additions yielded n = 4 (pore/glass drag), while lithium silicate gave n = 2 (parabolic, approaching intrinsic boundary-controlled growth) (sharif1998controlofgrain pages 4-8). Dong and Chen (2018) demonstrated that above 1300°C, 8YSZ obeys parabolic grain growth (n = 2) described by G² − G₀² = 2Mγt, where M is the grain boundary mobility and γ ≈ 0.3 J/m² is the grain boundary energy. However, below 1300°C, the exponent increases dramatically to n ≈ 4.9 at 1200°C and n ≈ 6.7 at 1175°C, reflecting a sharp mobility transition associated with the immobilization of four-grain junctions (dong2018mobilitytransitionat pages 5-12, dong2018mobilitytransitionat pages 1-5). Aktas et al. (2014) found n = 3 for both undoped and La₂O₃-doped 8YSZ in the 1400–1600°C range (aktas2014crystallizationandgrain pages 3-5). In SPS processing, Flaureau et al. (2021) reported m = 2 for 3Y-TZP and m = 3 for 8Y-FSZ powders (flaureau2021studyofthe pages 11-12, flaureau2021studyofthe pages 8-9).

### 1.2 Activation Energies

Activation energies for grain growth in YSZ span a wide range depending on composition, grain size regime, and temperature window:

- **Cubic 8Y-CSZ (conventional):** 289–398 kJ/mol. Lee and Chen reported Q = 289 kJ/mol for 8Y-CSZ with n = 2, while Sharif et al. found Q = 398 ± 217 kJ/mol for pure 8Y-CSZ with n = 3 (sharif1998controlofgrain pages 4-8). The value of 580 kJ/mol reported by Nieh et al. for Y-TZP is significantly higher, as expected for the tetragonal phase (sharif1998controlofgrain pages 4-8).

- **Y-TZP (tetragonal):** Chaim (2008) identified two distinct regimes: below ~1400°C, Q = 280 ± 10 kJ/mol, attributed to limited Y³⁺ lattice diffusion; above ~1400°C, Q = 546 ± 22 kJ/mol, attributed to enhanced grain boundary diffusion following Y³⁺ redistribution (chaim2008activationenergyand pages 3-4, chaim2008activationenergyand pages 1-3, chaim2008activationenergyand pages 4-5). The high-temperature activation energy matches grain boundary diffusion of Y³⁺ in the tetragonal phase (~506 kJ/mol) (chaim2008activationenergyand pages 4-5).

- **8YSZ grain boundary mobility:** Dong and Chen (2018) reported an activation energy of 4.2 eV (~405 kJ/mol) for grain boundary mobility above 1300°C, but a dramatically higher apparent activation energy of 10.8 eV (~1040 kJ/mol) below 1300°C, reflecting the junction-controlled mobility transition (dong2018mobilitytransitionat pages 5-12).

- **ZrO₂-Y₂O₃ (alkoxide-derived):** Van de Graaf et al. (1985) estimated Q = 450 kJ/mol for grain growth, which they interpreted as intermediate between grain boundary diffusion and lattice diffusion activation energies, and likely controlled by Y³⁺ lattice diffusion being the slowest process (graaf1985microstructureandsintering pages 8-10, graaf1985microstructureandsintering pages 10-12).

- **Nanocrystalline regime:** Shukla et al. (2003) reported a dramatically reduced Q = 13.0 ± 0.9 kJ/mol for nanocrystalline 3YSZ (sol-gel synthesized) in the 400–1200°C calcination range, attributed to the large concentration of oxygen-ion vacancies in the nanocrystalline material (shukla2003reducedactivationenergy pages 1-2).

- **Cation diffusion:** Swaroop et al. (2005) measured grain boundary diffusion activation energies of ~400 kJ/mol for Hf⁴⁺ and Yb³⁺ in 3YTZ, with grain boundary diffusivities approximately five orders of magnitude higher than lattice diffusivities (swaroop2005latticeandgrain pages 7-8).

The following table provides a comprehensive compilation of reported kinetic parameters:

| Reference | Material/Composition | Grain Growth Exponent (n) | Activation Energy (kJ/mol) | Temperature Range (°C) | Proposed Mechanism |
|---|---|---:|---:|---|---|
| Sharif et al., 1998 | 8Y-CSZ (pure) | 3 | 398 | 1400–1600 | Normal grain growth in cubic YSZ; impurity/solute drag still present, but closer to intrinsic behavior than glass-containing samples (sharif1998controlofgrain pages 4-8) |
| Sharif et al., 1998 | 8Y-CSZ + 1 wt% BaS | 4 | 443 | 1400–1600 | Grain growth retarded by residual porosity and intergranular barium silicate; pore/glass drag dominated (sharif1998controlofgrain pages 4-8) |
| Sharif et al., 1998 | 8Y-CSZ + 1 wt% BS | 4 | 418 | 1400–1600 | Borosilicate grain-boundary phase pins boundaries; high-viscosity intergranular phase limits matter transfer (sharif1998controlofgrain pages 4-8) |
| Sharif et al., 1998 | 8Y-CSZ + 1 wt% LiS | 2 | 390 | 1400–1600 | Faster grain growth via highly soluble, lower-viscosity Li-silicate intergranular phase; closer to parabolic growth (sharif1998controlofgrain pages 4-8) |
| Aktas et al., 2014 | 8YSZ (undoped) | 3 | 358 | 1400–1600 | Impurity-drag-controlled growth in 8YSZ (aktas2014crystallizationandgrain pages 3-5) |
| Aktas et al., 2014 | 8YSZ + La2O3 (1–15 wt%) | 3 | 334–413 | 1400–1600 | Impurity drag; higher Q at high La due to secondary La2Zr2O7 phase and stronger boundary pinning (aktas2014crystallizationandgrain pages 3-5) |
| Chaim, 2008 | Nanocrystalline Y-TZP, low-T regime | 2–3 | 280 ± 10 | <1400 | Slow grain growth; attributed to limited Y3+ lattice diffusion / constrained low-temperature growth regime (chaim2008activationenergyand pages 3-4, chaim2008activationenergyand pages 1-3, chaim2008activationenergyand pages 4-5) |
| Chaim, 2008 | Nanocrystalline Y-TZP, high-T regime | 2–3 | 546 ± 22 | >1400 | Faster grain growth; associated with grain-boundary diffusion after Y redistribution/equilibrium phase development (chaim2008activationenergyand pages 3-4, chaim2008activationenergyand pages 1-3, chaim2008activationenergyand pages 4-5) |
| Dong & Chen, 2018 | 8YSZ, high-T regime | 2 (parabolic) | ~405 (4.2 eV) | 1300–1450 | 2-grain-boundary-controlled parabolic growth; normal grain growth with mobile boundaries (dong2018mobilitytransitionat pages 5-12, dong2018mobilitytransitionat pages 1-5) |
| Dong & Chen, 2018 | 8YSZ, low-T regime | 4.9 at 1200; 6.7 at 1175 | ~1040 (10.8 eV) | 1175–1200 | Strongly quenched mobility; inhomogeneous immobile 4-grain-junction control / mobility transition below 1300°C (dong2018mobilitytransitionat pages 5-12, dong2018mobilitytransitionat pages 1-5) |
| Shukla et al., 2003 | Nanocrystalline 3YSZ | — | 13.0 ± 0.9 | 400–1200 | Nanocrystalline growth with exceptionally low apparent barrier, attributed to high vacancy/disorder concentration (shukla2003reducedactivationenergy pages 1-2) |
| Nieh et al. (as cited by Sharif et al., 1998) | Y-TZP | 3 | 580 | Not specified in excerpt | Conventional Y-TZP grain growth; higher barrier than cubic 8Y-CSZ (sharif1998controlofgrain pages 4-8) |
| van de Graaf et al., 1985 | ZrO2–Y2O3 ceramics | 2–3 (reported/interpretive) | 450 | Mainly 1100–1600 | Grain growth activation energy intermediate between grain-boundary and lattice diffusion; interpreted as cation-diffusion-controlled with Y3+ likely rate-limiting (graaf1985microstructureandsintering pages 8-10, graaf1985microstructureandsintering pages 10-12) |
| Flaureau et al., 2021 | 3Y-TZP via SPS | 2 | not directly reported for grain growth in excerpt | SPS regime, submicron powders | Grain-boundary-motion-controlled growth under SPS conditions (flaureau2021studyofthe pages 11-12, flaureau2021studyofthe pages 8-9) |
| Flaureau et al., 2021 | 8Y-FSZ via SPS | 3 (literature comparison) | not directly reported for grain growth in excerpt | SPS regime, submicron powders | Impure fully stabilized zirconia literature behavior; SPS modifies apparent mechanism relative to conventional expectations (flaureau2021studyofthe pages 11-12) |
| Lee & Chen (as tabulated by Sharif et al., 1998) | 8Y-CSZ | 2 | 289 | Not specified in excerpt | Parabolic grain growth in cubic YSZ (sharif1998controlofgrain pages 4-8) |
| Lee & Chen (as tabulated by Sharif et al., 1998) | 2Y-TZP | 2 | 440 | Not specified in excerpt | Parabolic grain growth in tetragonal zirconia polycrystal (sharif1998controlofgrain pages 4-8) |


*Table: This table compiles reported grain-growth exponents, activation energies, temperature windows, and inferred mechanisms for major YSZ compositions from the literature. It is useful for comparing cubic vs tetragonal YSZ, conventional vs nanocrystalline behavior, and the effects of intergranular phases or SPS processing.*

## 2. Temperature-Time Regimes for Large-Grained Equiaxed Microstructures

### 2.1 Grain Size as a Function of Temperature and Time

The literature establishes a clear scaling of grain size with sintering temperature and hold time. For 8YSZ sintered by conventional methods, Dong and Chen (2018) reported grain sizes of 1.7 ± 0.05 µm at 1300°C/12 h, 3.2 ± 0.2 µm at 1400°C/4 h, 4.6 ± 0.3 µm at 1450°C/2.5 h, and 5.8 ± 0.2 µm at 1500°C/2 h (dong2018mobilitytransitionat pages 5-12). Sharif et al. (1998) showed that starting from HIP-densified microstructures (~3.5 µm), pure 8Y-CSZ reached ~12 µm after 100 h at 1400°C with equiaxed, faceted grain morphology (sharif1998controlofgrain pages 3-4, sharif1998controlofgrain pages 4-8).

Badwal (1995) provided grain size data extending to 1700°C: YSZ7 (7 mol% Y₂O₃-stabilized) reached 11.8 µm at 1500°C, 16.0 µm at 1600°C, and 19.6 µm at 1700°C (badwal1995grainboundaryresistivity pages 4-6). For 3Y-TZP (TZ3Y), grain sizes remained smaller at 1700°C (~4.2 µm), reflecting the stronger grain growth resistance of the tetragonal phase (badwal1995grainboundaryresistivity pages 4-6). At 1700°C, significant precipitation of the tetragonal ZrO₂ phase occurs during sintering and subsequent slow cooling in cubic compositions (badwal1995grainboundaryresistivity pages 4-6).

### 2.2 Reaching Tens of Microns

To achieve grain sizes in the tens of microns range for equiaxed microstructures, the literature indicates several pathways:

1. **Extended annealing at 1400–1600°C:** Pure 8Y-CSZ reaches ~12–16 µm after 100 h at 1400–1600°C in air (sharif1998controlofgrain pages 4-8). Even faster growth occurs with lithium silicate intergranular phases (~16 µm at 1400°C/100 h) (sharif1998controlofgrain pages 4-8).

2. **Sintering at 1600–1700°C:** Cubic YSZ compositions (7–8 mol% Y₂O₃) reach ~16–20 µm at 1600–1700°C within standard sintering hold times (badwal1995grainboundaryresistivity pages 4-6).

3. **Very high temperatures (1800–2500°C):** While direct data for YSZ in this range are sparse in the accessible literature, plasma arc sintering of CeO₂-stabilized ZrO₂ at 2000°C has been reported to produce coarse grains of approximately 100 µm (kulyk2022theeffectof pages 2-3). Extrapolation of the Arrhenius-type grain growth kinetics from lower temperatures, using activation energies of 400–450 kJ/mol, predicts that processing at 1800–2000°C for moderate hold times (hours) should readily produce equiaxed grains in the 50–100+ µm range for cubic YSZ.

4. **Abnormal grain growth:** Van de Graaf et al. (1985) noted that abnormal grain growth occurs at 1100–1200°C and again at 1500–1600°C in fine-grained YSZ from alkoxide-derived powders, producing pockets of strongly coarsened grains amid finer-grained regions (graaf1985microstructureandsintering pages 8-10, graaf1985microstructureandsintering pages 10-12). Above 1600°C, pores detach from grain boundaries, leading to uninhibited coarsening (graaf1985microstructureandsintering pages 10-12).

| Reference | Material | Sintering Temperature (°C) | Time | Atmosphere | Grain Size (µm) | Notes |
|---|---|---:|---|---|---:|---|
| Dong & Chen 2018 | 8YSZ | 1300 | 12 h | not specified in excerpt | 1.7 | Normal sintering; parabolic growth regime above 1300°C (dong2018mobilitytransitionat pages 5-12, dong2018mobilitytransitionat pages 1-5) |
| Dong & Chen 2018 | 8YSZ | 1400 | 4 h | not specified in excerpt | 3.2 | Normal sintering; parabolic growth (dong2018mobilitytransitionat pages 5-12) |
| Dong & Chen 2018 | 8YSZ | 1450 | 2.5 h | not specified in excerpt | 4.6 | Normal sintering; parabolic growth (dong2018mobilitytransitionat pages 5-12) |
| Dong & Chen 2018 | 8YSZ | 1500 | 2 h | not specified in excerpt | 5.8 | Normal sintering; common 1400–1500°C processing yields ~5 µm grains (dong2018mobilitytransitionat pages 5-12, dong2018mobilitytransitionat pages 1-5) |
| Badwal 1995 | TZ3Y | 1700 | not specified in excerpt | not specified in excerpt | 4.2 | Table 2 grain size for TZ3Y at 1700°C (badwal1995grainboundaryresistivity pages 4-6) |
| Badwal 1995 | YSZ7 | 1500 | not specified in excerpt | not specified in excerpt | 11.8 | Table 2 grain size for YSZ7 at 1500°C (badwal1995grainboundaryresistivity pages 4-6) |
| Badwal 1995 | YSZ7 | 1600 | not specified in excerpt | not specified in excerpt | 16.0 | Table 2 grain size for YSZ7 at 1600°C (badwal1995grainboundaryresistivity pages 4-6) |
| Badwal 1995 | YSZ7 | 1700 | not specified in excerpt | not specified in excerpt | 19.6 | Large grains at 1700°C; associated with phase precipitation during sintering/cooling (badwal1995grainboundaryresistivity pages 4-6) |
| Sharif et al. 1998 | 8Y-CSZ (pure) | 1400 | 100 h | air | ~12 | Equiaxed faceted grains after annealing; started from HIP-densified ~3.5 µm microstructure (sharif1998controlofgrain pages 3-4, sharif1998controlofgrain pages 4-8) |
| Sharif et al. 1998 | 8Y-CSZ + 1 wt% LiS | 1400 | 100 h | air | ~16 | Largest grains among compositions at 1400°C/100 h; Li-silicate promoted fastest growth (sharif1998controlofgrain pages 3-4, sharif1998controlofgrain pages 4-8) |
| Sharif et al. 1998 | 8Y-CSZ (pure) | 1600 | up to 100 h | air | not numerically stated in excerpt | Grain-size-vs-time plot shows substantial coarsening; pure 8Y-CSZ grew faster than BS/BaS-containing materials (sharif1998controlofgrain pages 4-8) |
| Kulyk et al. 2022 | CeO2-stabilized ZrO2 | 2000 | plasma arc sintering; time not specified in excerpt | plasma arc / reducing-local high-T process | ~100 | Coarse-grain reference point showing very high temperature can generate ~100 µm grains (not YSZ, but relevant upper-bound comparison) (kulyk2022theeffectof pages 2-3) |
| Dash et al. 2019 | SPS/HIP zirconia composites containing YSZ-related phases | 1100 | SPS/HIP schedule; anneal 700°C/100 h | SPS in vacuum/graphite; HIP in Ar; re-anneal in air | not primary outcome | Vacuum/graphite SPS produced black, strongly reduced ceramics via oxygen-vacancy color centers; HIP in Ar also generated oxygen vacancies/nanopores; air annealing at 700°C for 100 h reversed darkening from vacancies (dash2019transparenttetragonalcubiczirconia pages 5-7, dash2019transparenttetragonalcubiczirconia pages 7-9) |
| Biesuz et al. 2018 | 8YSZ | 700 | during flash incubation/sintering | air or Ar under electric field; lower pO2 promotes reduction | localized abnormal grain growth near cathode | Cathodic reduction formed F/F+ color centers and darkening; lower pO2 increased reduction and conductivity; blackened cathodic regions showed abnormal grain growth (biesuz2018investigationofelectrochemical pages 9-12, biesuz2018investigationofelectrochemical pages 6-9, biesuz2018investigationofelectrochemical pages 12-13, biesuz2018investigationofelectrochemical pages 1-3, biesuz2018investigationofelectrochemical pages 3-6) |
| Sondhi 2014 | 3YSZ / YSZ exposed to carbon | 1800 | reaction time not fully specified in excerpt | He with graphite/carbon contamination | conversion zone ~25–50 µm penetration scale | Carbon contamination caused carbothermal reduction of YSZ to ZrC; carbon diffusion coefficient in YSZ at 1800°C was 3×10^-14 m^2/s; yttria segregated as Y2O3-rich pockets, compromising specimen integrity/composition (sondhi2014investigationsinthe pages 70-76, sondhi2014investigationsinthe pages 109-119, sondhi2014investigationsinthe pages 100-109, sondhi2014investigationsinthe pages 62-70, sondhi2014investigationsinthe pages 76-81, sondhi2014investigationsinthe pages 53-62) |


*Table: This table summarizes reported grain sizes achieved in YSZ and related zirconias across key temperature-time regimes, and adds atmosphere/contamination cases that affect reduction, darkening, and integrity. It is useful for identifying when equiaxed grains in the 1–20 µm range are expected and when vacuum, argon, low pO2, or carbon create processing risks.*

## 3. Effects of Atmosphere on Grain Growth, Darkening, and Specimen Integrity

### 3.1 Vacuum and Reducing Atmospheres: Oxygen Vacancy Formation and Darkening

Processing YSZ under low oxygen partial pressure—whether in vacuum, argon, or reducing atmospheres—creates oxygen vacancies that fundamentally alter the material's optical and electrical properties. Dash et al. (2019) demonstrated that spark plasma sintering (SPS) in vacuum with graphite tooling produces strongly reduced, black YSZ ceramics. The darkening arises from color centers: F-centers (oxygen vacancies with two trapped electrons, V_O) and F⁺-centers (vacancies with one trapped electron, V_O·), which create energy levels 1.5–2.3 eV below the conduction band and absorb visible light in the 1.8–3.1 eV range (dash2019transparenttetragonalcubiczirconia pages 5-7, biesuz2018investigationofelectrochemical pages 6-9). During hot isostatic pressing (HIP) in argon, oxygen vacancies also form, though less severely. Prolonged HIP can cause oxygen vacancies to coalesce into immobile nanopores that cannot be removed by subsequent air annealing, creating permanent scattering centers and degraded transparency (dash2019transparenttetragonalcubiczirconia pages 5-7).

Biesuz et al. (2018) provided a detailed mechanistic picture during flash sintering of 8YSZ, showing that cathodic partial reduction under DC fields creates blackened regions where the electrochemical reaction O_O^x ↔ V_O·· + 2e' + ½O₂(g) shifts toward vacancy creation. Lower oxygen partial pressure (e.g., argon atmosphere) inhibits the non-reducing cathodic reaction and promotes electrolytic reduction, darkening, and the switch from ionic to electronic (n-type) conductivity (biesuz2018investigationofelectrochemical pages 9-12, biesuz2018investigationofelectrochemical pages 6-9, biesuz2018investigationofelectrochemical pages 12-13, biesuz2018investigationofelectrochemical pages 1-3). Notably, the blackened cathodic regions also exhibited abnormal grain growth, attributed to reduced activation energy for defect migration in partially-reduced zones (biesuz2018investigationofelectrochemical pages 1-3).

### 3.2 Reversibility of Darkening

The darkening caused by oxygen vacancies is largely reversible through air annealing. Dash et al. (2019) showed that air annealing at 700°C for 100 h effectively annihilates oxygen vacancies and restores optical transmission, achieving 40% total forward transmission at 640 nm for SPS-HIP treated zirconia ceramics (dash2019transparenttetragonalcubiczirconia pages 7-9). During flash sintering with low-frequency AC fields (0.1–10 Hz), the blackening was observed to be reversible, following the imposed polarity switching (biesuz2018investigationofelectrochemical pages 1-3, biesuz2018investigationofelectrochemical pages 3-6).

### 3.3 Carbon Contamination: Carbothermal Reduction

Carbon contamination represents a severe threat to YSZ integrity at high temperatures. Sondhi (2014) systematically investigated the carbothermal reduction of 3 mol% YSZ in contact with graphite at 1800°C under helium. The key findings are:

- Carbon is the primary mobile species driving carbothermal reduction, rather than CO gas as previously assumed. Carbon atoms penetrate YSZ via grain boundaries, interstitial sites, and lattice defect sites, despite slow bulk diffusion (D_C = 3 × 10⁻¹⁴ m²/s at 1800°C) (sondhi2014investigationsinthe pages 70-76, sondhi2014investigationsinthe pages 62-70).

- Even low carbon activity (as low as 0.31) is sufficient to completely convert ZrO₂ to ZrC thermodynamically (sondhi2014investigationsinthe pages 76-81). In practice, conversion is localized at contact surfaces, with ZrC formation penetrating approximately 25–50 µm at 1800°C (sondhi2014investigationsinthe pages 62-70).

- With pure graphite sources, up to 74% ZrC conversion was observed on contact faces; sintered samples showed less conversion because sintering eliminates internal surface area available as reaction sites (sondhi2014investigationsinthe pages 53-62).

- Carbothermal reduction causes yttria segregation: Y₂O₃ has very low solubility in ZrC (~1.5–2 wt%), so yttrium diffuses along grain boundaries and accumulates as distinct Y₂O₃-rich pockets, fundamentally compromising the stabilized zirconia microstructure (sondhi2014investigationsinthe pages 109-119, sondhi2014investigationsinthe pages 100-109).

### 3.4 Refractory Metal Contamination

While specific studies on refractory metal (W, Mo, Ta) contamination of YSZ during high-temperature processing were not extensively found in the retrieved literature, the carbothermal reduction studies indicate that any processing environment involving carbonaceous species or reducing conditions at temperatures approaching 1800°C and above poses a risk of phase decomposition. Graphite furnace elements and tooling are particularly problematic, as the graphite environment generates CO/CO₂ atmospheres during densification (dash2019transparenttetragonalcubiczirconia pages 5-7). The use of refractory metal crucibles or heating elements (which are typically used in vacuum or inert atmosphere at 1700–2500°C) introduces both reducing conditions and the possibility of metallic contamination via vapor transport, though quantitative data specific to YSZ are limited in the retrieved sources.

## 4. Summary and Practical Implications

The grain growth kinetics of YSZ are governed by cation diffusion, primarily Y³⁺, with activation energies ranging from ~280 to 580 kJ/mol depending on the phase (cubic vs. tetragonal), temperature regime, and grain size scale. Cubic YSZ (8Y-CSZ) exhibits more rapid grain growth than tetragonal Y-TZP, with parabolic kinetics (n = 2) predominating above 1300°C and activation energies of ~290–450 kJ/mol (dong2018mobilitytransitionat pages 5-12, sharif1998controlofgrain pages 4-8, graaf1985microstructureandsintering pages 10-12). To produce equiaxed microstructures with grain sizes in the tens of microns, sintering at 1600–1700°C for extended times or brief processing above 1800°C is required (badwal1995grainboundaryresistivity pages 4-6, kulyk2022theeffectof pages 2-3).

Processing at 1700–2500°C introduces significant atmospheric challenges. Vacuum and inert gas environments create oxygen vacancies that darken YSZ and alter its electrical properties, though this effect is largely reversible by air annealing (dash2019transparenttetragonalcubiczirconia pages 5-7, dash2019transparenttetragonalcubiczirconia pages 7-9). Carbon contamination from graphite furnace components causes irreversible carbothermal reduction to ZrC with concomitant yttria segregation (sondhi2014investigationsinthe pages 70-76, sondhi2014investigationsinthe pages 109-119). These findings underscore the importance of atmosphere control: air sintering preserves stoichiometry but limits attainable temperatures to furnace capability, while vacuum or inert gas processing at very high temperatures requires careful engineering to avoid reduction and contamination.

## References (BibTeX)

```bibtex
@article{sharif1998controlofgrain,
    author = "Sharif, A.A. and Imamura, P.H. and Mitchell, T.E. and Mecartney, M.L.",
    title = "Control of grain growth using intergranular silicate phases in cubic yttria stabilized zirconia",
    year = "1998",
    journal = "Acta Materialia",
    volume = "46",
    pages = "3863-3872",
    doi = "10.1016/s1359-6454(98)00080-9"
}

@article{aktas2014crystallizationandgrain,
    author = "Aktas, Bulent and Tekeli, Suleyman and Salman, Serdar",
    title = "Crystallization and grain growth behavior of La2O3-doped yttria-stabilized zirconia",
    year = "2014",
    journal = "Advanced Materials Letters",
    volume = "5",
    pages = "260-264",
    doi = "10.5185/amlett.2014.amwc1011"
}

@article{chaim2008activationenergyand,
    author = "Chaim, Rachman",
    title = "Activation energy and grain growth in nanocrystalline Y-TZP ceramics",
    year = "2008",
    journal = "Materials Science and Engineering A",
    volume = "486",
    pages = "439-446",
    doi = "10.1016/j.msea.2007.09.022"
}

@article{dong2018mobilitytransitionat,
    author = "Dong, Yanhao and Chen, I-Wei",
    title = "Mobility transition at grain boundaries in two-step sintered 8 mol% yttria-stabilized zirconia",
    year = "2018",
    journal = "Journal of the American Ceramic Society",
    volume = "101",
    pages = "1857-1869",
    doi = "10.1111/jace.15362"
}

@article{shukla2003reducedactivationenergy,
    author = "Shukla, Satyajit and Seal, Sudipta and Vij, Rashmi and Bandyopadhyay, Sri",
    title = "Reduced Activation Energy for Grain Growth in Nanocrystalline Yttria-Stabilized Zirconia",
    year = "2003",
    journal = "Nano Letters",
    volume = "3",
    pages = "397-401",
    doi = "10.1021/nl0259380"
}

@article{flaureau2021studyofthe,
    author = "Flaureau, Andreas and Weibel, Alicia and Chevallier, Geoffroy and Estournes, Claude",
    title = "Study of the densification and grain growth mechanisms occurring during spark plasma sintering of different submicronic yttria-stabilized zirconia powders",
    year = "2021",
    journal = "Journal of the European Ceramic Society",
    volume = "41",
    pages = "3581-3594",
    doi = "10.1016/j.jeurceramsoc.2021.01.032"
}

@article{graaf1985microstructureandsintering,
    author = "Van De Graaf, M.A.C.G. and Ter Maat, J.H.H. and Burggraaf, A.J.",
    title = "Microstructure and sintering kinetics of highly reactive ZrO2-Y2O3 ceramics",
    year = "1985",
    journal = "Journal of Materials Science",
    volume = "20",
    pages = "1407-1418",
    doi = "10.1007/bf01026338"
}

@article{badwal1995grainboundaryresistivity,
    author = "Badwal, S.P.S.",
    title = "Grain boundary resistivity in zirconia-based materials: effect of sintering temperatures and impurities",
    year = "1995",
    journal = "Solid State Ionics",
    volume = "76",
    pages = "67-80",
    doi = "10.1016/0167-2738(94)00236-l"
}

@article{kulyk2022theeffectof,
    author = "Kulyk, Volodymyr and Duriagina, Zoia and Kostryzhev, Andrii and Vasyliv, Bogdan and Vavrukh, Valentyna and Marenych, Olexandra",
    title = "The Effect of Yttria Content on Microstructure, Strength, and Fracture Behavior of Yttria-Stabilized Zirconia",
    year = "2022",
    journal = "Materials",
    volume = "15",
    pages = "5212",
    doi = "10.3390/ma15155212"
}

@article{dash2019transparenttetragonalcubiczirconia,
    author = "Dash, Apurv and Kim, Byung-Nam and Klimke, Jens and Vleugels, Jef",
    title = "Transparent tetragonal-cubic zirconia composite ceramics densified by spark plasma sintering and hot isostatic pressing",
    year = "2019",
    journal = "Journal of the European Ceramic Society",
    volume = "39",
    pages = "1428-1435",
    doi = "10.1016/j.jeurceramsoc.2018.12.004"
}

@article{biesuz2018investigationofelectrochemical,
    author = "Biesuz, Mattia and Pinter, Lorenzo and Saunders, Theo and Reece, Mike and Binner, Jon and Sglavo, Vincenzo M. and Grasso, Salvatore",
    title = "Investigation of Electrochemical, Optical and Thermal Effects during Flash Sintering of 8YSZ",
    year = "2018",
    journal = "Materials",
    volume = "11",
    pages = "1214",
    doi = "10.3390/ma11071214"
}

@article{sondhi2014investigationsinthe,
    author = "Sondhi, Anchal",
    title = "Investigations in the Mechanism of Carbothermal Reduction of Yttria Stabilized Zirconia for Ultra-high Temperature Ceramics Application",
    year = "2014",
    doi = "10.12794/metadc500159"
}

@article{swaroop2005latticeandgrain,
    author = "Swaroop, Sathya and Kilo, Martin and Argirusis, Christos and Borchardt, Gunter and Chokshi, Atul H.",
    title = "Lattice and grain boundary diffusion of cations in 3YTZ analyzed using SIMS",
    year = "2005",
    journal = "Acta Materialia",
    volume = "53",
    pages = "4975-4985",
    doi = "10.1016/j.actamat.2005.05.031"
}

@article{matsui2003cubic,
    author = "Matsui, Koji and Horikoshi, Hideharu and Ohmichi, Nobukatsu and Ohgai, Michiharu and Yoshida, Hidehiro and Ikuhara, Yuichi",
    title = "Cubic-Formation and Grain-Growth Mechanisms in Tetragonal Zirconia Polycrystal",
    year = "2003",
    journal = "Journal of the American Ceramic Society",
    volume = "86",
    pages = "1401-1408",
    doi = "10.1111/j.1151-2916.2003.tb03483.x"
}
```

References

1. (aktas2014crystallizationandgrain pages 3-5): Bulent Aktas, Suleyman Tekeli, and Serdar Salman. Crystallization and grain growth behavior of la 2 o 3 -doped yttria-stabilized zirconia. Advanced Materials Letters, 5:260-264, May 2014. URL: https://doi.org/10.5185/amlett.2014.amwc1011, doi:10.5185/amlett.2014.amwc1011. This article has 13 citations.

2. (sharif1998controlofgrain pages 4-8): A.A. Sharif, P.H. Imamura, T.E. Mitchell, and M.L. Mecartney. Control of grain growth using intergranular silicate phases in cubic yttria stabilized zirconia. Acta Materialia, 46:3863-3872, Jul 1998. URL: https://doi.org/10.1016/s1359-6454(98)00080-9, doi:10.1016/s1359-6454(98)00080-9. This article has 36 citations and is from a highest quality peer-reviewed journal.

3. (dong2018mobilitytransitionat pages 5-12): Yanhao Dong and I‐Wei Chen. Mobility transition at grain boundaries in two‐step sintered 8 mol% yttria‐stabilized zirconia. Journal of the American Ceramic Society, 101:1857-1869, Dec 2018. URL: https://doi.org/10.1111/jace.15362, doi:10.1111/jace.15362. This article has 54 citations and is from a domain leading peer-reviewed journal.

4. (dong2018mobilitytransitionat pages 1-5): Yanhao Dong and I‐Wei Chen. Mobility transition at grain boundaries in two‐step sintered 8 mol% yttria‐stabilized zirconia. Journal of the American Ceramic Society, 101:1857-1869, Dec 2018. URL: https://doi.org/10.1111/jace.15362, doi:10.1111/jace.15362. This article has 54 citations and is from a domain leading peer-reviewed journal.

5. (flaureau2021studyofthe pages 11-12): Andréas Flaureau, Alicia Weibel, Geoffroy Chevallier, and Claude Estournès. Study of the densification and grain growth mechanisms occurring during spark plasma sintering of different submicronic yttria-stabilized zirconia powders. Journal of the European Ceramic Society, 41:3581-3594, Jun 2021. URL: https://doi.org/10.1016/j.jeurceramsoc.2021.01.032, doi:10.1016/j.jeurceramsoc.2021.01.032. This article has 48 citations and is from a domain leading peer-reviewed journal.

6. (flaureau2021studyofthe pages 8-9): Andréas Flaureau, Alicia Weibel, Geoffroy Chevallier, and Claude Estournès. Study of the densification and grain growth mechanisms occurring during spark plasma sintering of different submicronic yttria-stabilized zirconia powders. Journal of the European Ceramic Society, 41:3581-3594, Jun 2021. URL: https://doi.org/10.1016/j.jeurceramsoc.2021.01.032, doi:10.1016/j.jeurceramsoc.2021.01.032. This article has 48 citations and is from a domain leading peer-reviewed journal.

7. (chaim2008activationenergyand pages 3-4): Rachman Chaim. Activation energy and grain growth in nanocrystalline y-tzp ceramics. Materials Science and Engineering A-structural Materials Properties Microstructure and Processing, 486:439-446, Jul 2008. URL: https://doi.org/10.1016/j.msea.2007.09.022, doi:10.1016/j.msea.2007.09.022. This article has 80 citations.

8. (chaim2008activationenergyand pages 1-3): Rachman Chaim. Activation energy and grain growth in nanocrystalline y-tzp ceramics. Materials Science and Engineering A-structural Materials Properties Microstructure and Processing, 486:439-446, Jul 2008. URL: https://doi.org/10.1016/j.msea.2007.09.022, doi:10.1016/j.msea.2007.09.022. This article has 80 citations.

9. (chaim2008activationenergyand pages 4-5): Rachman Chaim. Activation energy and grain growth in nanocrystalline y-tzp ceramics. Materials Science and Engineering A-structural Materials Properties Microstructure and Processing, 486:439-446, Jul 2008. URL: https://doi.org/10.1016/j.msea.2007.09.022, doi:10.1016/j.msea.2007.09.022. This article has 80 citations.

10. (graaf1985microstructureandsintering pages 8-10): M. A. C. G. Van De Graaf, J. H. H. Ter Maat, and A. J. Burggraaf. Microstructure and sintering kinetics of highly reactive zro2-y2o3 ceramics. Journal of Materials Science, 20:1407-1418, Apr 1985. URL: https://doi.org/10.1007/bf01026338, doi:10.1007/bf01026338. This article has 151 citations and is from a peer-reviewed journal.

11. (graaf1985microstructureandsintering pages 10-12): M. A. C. G. Van De Graaf, J. H. H. Ter Maat, and A. J. Burggraaf. Microstructure and sintering kinetics of highly reactive zro2-y2o3 ceramics. Journal of Materials Science, 20:1407-1418, Apr 1985. URL: https://doi.org/10.1007/bf01026338, doi:10.1007/bf01026338. This article has 151 citations and is from a peer-reviewed journal.

12. (shukla2003reducedactivationenergy pages 1-2): Satyajit Shukla, Sudipta Seal, Rashmi Vij, and Sri Bandyopadhyay. Reduced activation energy for grain growth in nanocrystalline yttria-stabilized zirconia. Nano Letters, 3:397-401, Feb 2003. URL: https://doi.org/10.1021/nl0259380, doi:10.1021/nl0259380. This article has 205 citations and is from a highest quality peer-reviewed journal.

13. (swaroop2005latticeandgrain pages 7-8): Sathya Swaroop, Martin Kilo, Christos Argirusis, Günter Borchardt, and Atul H. Chokshi. Lattice and grain boundary diffusion of cations in 3ytz analyzed using sims. Acta Materialia, 53:4975-4985, Nov 2005. URL: https://doi.org/10.1016/j.actamat.2005.05.031, doi:10.1016/j.actamat.2005.05.031. This article has 133 citations and is from a highest quality peer-reviewed journal.

14. (sharif1998controlofgrain pages 3-4): A.A. Sharif, P.H. Imamura, T.E. Mitchell, and M.L. Mecartney. Control of grain growth using intergranular silicate phases in cubic yttria stabilized zirconia. Acta Materialia, 46:3863-3872, Jul 1998. URL: https://doi.org/10.1016/s1359-6454(98)00080-9, doi:10.1016/s1359-6454(98)00080-9. This article has 36 citations and is from a highest quality peer-reviewed journal.

15. (badwal1995grainboundaryresistivity pages 4-6): SPS Badwal. Grain boundary resistivity in zirconia-based materials: effect of sintering temperatures and impurities. Solid State Ionics, 76:67-80, Feb 1995. URL: https://doi.org/10.1016/0167-2738(94)00236-l, doi:10.1016/0167-2738(94)00236-l. This article has 271 citations and is from a peer-reviewed journal.

16. (kulyk2022theeffectof pages 2-3): Volodymyr Kulyk, Zoia Duriagina, Andrii Kostryzhev, Bogdan Vasyliv, Valentyna Vavrukh, and Olexandra Marenych. The effect of yttria content on microstructure, strength, and fracture behavior of yttria-stabilized zirconia. Materials, 15:5212, Jul 2022. URL: https://doi.org/10.3390/ma15155212, doi:10.3390/ma15155212. This article has 100 citations.

17. (dash2019transparenttetragonalcubiczirconia pages 5-7): Apurv Dash, Byung-Nam Kim, Jens Klimke, and Jef Vleugels. Transparent tetragonal-cubic zirconia composite ceramics densified by spark plasma sintering and hot isostatic pressing. Journal of the European Ceramic Society, 39:1428-1435, Apr 2019. URL: https://doi.org/10.1016/j.jeurceramsoc.2018.12.004, doi:10.1016/j.jeurceramsoc.2018.12.004. This article has 66 citations and is from a domain leading peer-reviewed journal.

18. (dash2019transparenttetragonalcubiczirconia pages 7-9): Apurv Dash, Byung-Nam Kim, Jens Klimke, and Jef Vleugels. Transparent tetragonal-cubic zirconia composite ceramics densified by spark plasma sintering and hot isostatic pressing. Journal of the European Ceramic Society, 39:1428-1435, Apr 2019. URL: https://doi.org/10.1016/j.jeurceramsoc.2018.12.004, doi:10.1016/j.jeurceramsoc.2018.12.004. This article has 66 citations and is from a domain leading peer-reviewed journal.

19. (biesuz2018investigationofelectrochemical pages 9-12): Mattia Biesuz, Lorenzo Pinter, Theo Saunders, Mike Reece, Jon Binner, Vincenzo M. Sglavo, and Salvatore Grasso. Investigation of electrochemical, optical and thermal effects during flash sintering of 8ysz. Materials, 11:1214, Jul 2018. URL: https://doi.org/10.3390/ma11071214, doi:10.3390/ma11071214. This article has 210 citations.

20. (biesuz2018investigationofelectrochemical pages 6-9): Mattia Biesuz, Lorenzo Pinter, Theo Saunders, Mike Reece, Jon Binner, Vincenzo M. Sglavo, and Salvatore Grasso. Investigation of electrochemical, optical and thermal effects during flash sintering of 8ysz. Materials, 11:1214, Jul 2018. URL: https://doi.org/10.3390/ma11071214, doi:10.3390/ma11071214. This article has 210 citations.

21. (biesuz2018investigationofelectrochemical pages 12-13): Mattia Biesuz, Lorenzo Pinter, Theo Saunders, Mike Reece, Jon Binner, Vincenzo M. Sglavo, and Salvatore Grasso. Investigation of electrochemical, optical and thermal effects during flash sintering of 8ysz. Materials, 11:1214, Jul 2018. URL: https://doi.org/10.3390/ma11071214, doi:10.3390/ma11071214. This article has 210 citations.

22. (biesuz2018investigationofelectrochemical pages 1-3): Mattia Biesuz, Lorenzo Pinter, Theo Saunders, Mike Reece, Jon Binner, Vincenzo M. Sglavo, and Salvatore Grasso. Investigation of electrochemical, optical and thermal effects during flash sintering of 8ysz. Materials, 11:1214, Jul 2018. URL: https://doi.org/10.3390/ma11071214, doi:10.3390/ma11071214. This article has 210 citations.

23. (biesuz2018investigationofelectrochemical pages 3-6): Mattia Biesuz, Lorenzo Pinter, Theo Saunders, Mike Reece, Jon Binner, Vincenzo M. Sglavo, and Salvatore Grasso. Investigation of electrochemical, optical and thermal effects during flash sintering of 8ysz. Materials, 11:1214, Jul 2018. URL: https://doi.org/10.3390/ma11071214, doi:10.3390/ma11071214. This article has 210 citations.

24. (sondhi2014investigationsinthe pages 70-76): Anchal Sondhi. Investigations in the mechanism of carbothermal reduction of yttria stabilized zirconia for ultra-high temperature ceramics application and its influence on yttria contained in it. Unknown journal, May 2014. URL: https://doi.org/10.12794/metadc500159, doi:10.12794/metadc500159. This article has 3 citations.

25. (sondhi2014investigationsinthe pages 109-119): Anchal Sondhi. Investigations in the mechanism of carbothermal reduction of yttria stabilized zirconia for ultra-high temperature ceramics application and its influence on yttria contained in it. Unknown journal, May 2014. URL: https://doi.org/10.12794/metadc500159, doi:10.12794/metadc500159. This article has 3 citations.

26. (sondhi2014investigationsinthe pages 100-109): Anchal Sondhi. Investigations in the mechanism of carbothermal reduction of yttria stabilized zirconia for ultra-high temperature ceramics application and its influence on yttria contained in it. Unknown journal, May 2014. URL: https://doi.org/10.12794/metadc500159, doi:10.12794/metadc500159. This article has 3 citations.

27. (sondhi2014investigationsinthe pages 62-70): Anchal Sondhi. Investigations in the mechanism of carbothermal reduction of yttria stabilized zirconia for ultra-high temperature ceramics application and its influence on yttria contained in it. Unknown journal, May 2014. URL: https://doi.org/10.12794/metadc500159, doi:10.12794/metadc500159. This article has 3 citations.

28. (sondhi2014investigationsinthe pages 76-81): Anchal Sondhi. Investigations in the mechanism of carbothermal reduction of yttria stabilized zirconia for ultra-high temperature ceramics application and its influence on yttria contained in it. Unknown journal, May 2014. URL: https://doi.org/10.12794/metadc500159, doi:10.12794/metadc500159. This article has 3 citations.

29. (sondhi2014investigationsinthe pages 53-62): Anchal Sondhi. Investigations in the mechanism of carbothermal reduction of yttria stabilized zirconia for ultra-high temperature ceramics application and its influence on yttria contained in it. Unknown journal, May 2014. URL: https://doi.org/10.12794/metadc500159, doi:10.12794/metadc500159. This article has 3 citations.
