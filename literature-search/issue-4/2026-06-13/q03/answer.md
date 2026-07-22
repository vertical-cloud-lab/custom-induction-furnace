Question: Review literature on contamination/oxidation/decarburization control in vacuum or inert-atmosphere annealing furnaces relevant to induction systems. Include mechanisms, mitigation strategies, and cited references with bibtex.

# Contamination, Oxidation, and Decarburization Control in Vacuum and Inert-Atmosphere Annealing Furnaces: Relevance to Induction Systems

## 1. Introduction

Vacuum and inert-atmosphere annealing furnaces are widely used to heat-treat metals while minimizing surface degradation. However, even under nominally protective conditions, residual contamination, oxidation, and decarburization can occur through multiple pathways. These phenomena are of particular importance for induction heating systems, where rapid, localized heating introduces unique challenges related to atmosphere synchronization and surface quality control. This review synthesizes the available literature on contamination sources and mechanisms, oxidation and decarburization pathways, and practical mitigation strategies, with specific attention to their relevance for induction annealing.

## 2. Contamination Sources and Mechanisms in Vacuum and Inert-Atmosphere Furnaces

### 2.1 Residual Atmospheric Gases

Even in well-sealed vacuum or inert-gas systems, trace amounts of O₂, H₂O, and CO₂ persist as residual atmospheric gases. These species originate from incomplete purging, real and virtual leaks, permeation through elastomeric seals, and desorption from chamber walls (mattox1998preparationandcleaning pages 39-42). Water vapor is particularly problematic because it sets the effective oxygen potential even in nominally reducing H₂/N₂ atmospheres and can drive both oxidation and decarburization reactions (herring2010annealingofwire pages 1-2). The recommended practice for furnace purging is to flow inert gas (typically nitrogen) at a rate sufficient to achieve five volume changes per hour, continuing until oxygen content drops below 1% as measured by in-line oxygen analyzers (herring2010annealingofwire pages 1-2).

### 2.2 Outgassing from Chamber Walls and Fixtures

Outgassing and outdiffusion from bulk materials represent major contamination sources in vacuum furnaces. Metals typically release hydrogen upon heating, while polymers and elastomers emit water vapor, solvent vapors, and low-molecular-weight organics (mattox1998preparationandcleaning pages 14-17). Heating during processing exacerbates outgassing. Porous or rough surfaces increase the amount of retained water and particulates and impede pump-down (mattox1998preparationandcleaning pages 14-17). Recommended mitigations include bakeout procedures (>400°C with no cold spots), minimizing chamber-open time, venting with dry gas, and using load-locks so that materials are preprocessed before entering the main chamber (mattox1998preparationandcleaning pages 42-46, mattox1998preparationandcleaning pages 48-51).

### 2.3 Oil Backstreaming from Pumps

Oil-sealed vacuum pumps can introduce hydrocarbon contamination through backstreaming and wall creep. These oil vapors can decompose under thermal or plasma conditions to leave carbonaceous deposits and can fill cryopump adsorbent pores, reducing pumping capacity (mattox1998preparationandcleaning pages 39-42). Mitigations include using dry (oil-free) pumps, maintaining the roughing manifold in the viscous (turbulent) flow regime (P[torr] × D[inches] > 0.18) to reduce backstreaming, employing LN₂ cold traps and cold panels, and installing ballast orifice/valve or normally-closed pneumatic/solenoid valves that prevent oil suck-back during power failures (mattox1998preparationandcleaning pages 39-42, mattox1998preparationandcleaning pages 42-46).

### 2.4 Heating Element and Hardware Contamination

Furnace hardware itself can act as a contamination source. In vacuum heat treatment of powder metallurgical steels, aluminum detected on powder surfaces was attributed to transfer from Kanthal A-1 heating elements (brust2013transformationofsurface pages 84-87). Hot hardware contributes desorption and vaporization products that can alter surface chemistry and produce unwanted inclusions or particulates (mattox1998preparationandcleaning pages 53-54, mattox1998preparationandcleaning pages 11-14). Maintenance of clean hot-zone materials and identification of hardware-derived species during troubleshooting are essential controls.

### 2.5 Hydrocarbon Contamination

Common contaminants in vacuum systems include hydrocarbons, intermediate-vapour-pressure organics, low-vapour-pressure metals (e.g., Cd, Zn), halogens, and silicones. These can deteriorate the vacuum, propagate through the system, promote corrosion (halogens), or transform into insulating layers upon irradiation (silicones) (taborelli2020cleaningandsurface pages 8-10). Surface-analytical methods such as XPS, AES, and SIMS can identify and quantify these contaminants at the 1–3 nm depth scale with approximately 1 at% sensitivity (taborelli2020cleaningandsurface pages 8-10).

## 3. Oxidation Mechanisms during Annealing

### 3.1 Surface Oxide Scale Formation

Oxide scale formation occurs whenever the oxygen potential exceeds the thermodynamic threshold for oxidation of the base metal. Scale structure—composition, thickness, and morphology—depends on temperature, atmosphere, alloy chemistry, and time. In Fe–Si steels, the type of oxide formed (FeO, Fe₂SiO₄, or continuous SiO₂) depends strongly on the H₂O partial pressure ratio (P_H₂O/P_H₂). At high H₂O levels, FeO or FeO + Fe₂SiO₄ scales form and promote severe decarburization, whereas in dry O₂-containing atmospheres a continuous SiO₂ layer can form that greatly alleviates decarburization by lowering the oxygen potential at the oxide–steel interface (chen2020decarburizationof60si2mna pages 19-21, chen2020decarburizationof60si2mna pages 7-13). The relationship between oxide-layer structure and decarburization depth is complex and non-monotonic: scale composition and permeability, not merely thickness, determine the extent of carbon loss (chen2020decarburizationof60si2mna pages 13-16).

### 3.2 Selective Oxidation of Alloying Elements

Even when iron oxide is fully reduced in H₂/N₂ atmospheres, residual H₂O can selectively oxidize stronger oxide-forming elements such as Mn, Si, Al, V, and Ti. Olefjord et al. (1980) demonstrated using in-situ ESCA/SAM that annealing cold-rolled steel in 15% H₂/85% N₂ with dew points of −20 to −30°C completely reduces iron oxide but produces Mn, Si, Al, V, and Ti oxides distributed along grain boundaries and as islands approximately 50 nm thick on the surface (olefjord1980selectivesurfaceace pages 1-4). The distribution of these oxides depends on the annealing mode: closed-coil batch annealing produces relatively uniform Mn- and Cr-oxide distributions, while open-coil annealing concentrates oxides along grain boundaries (olefjord1980selectivesurfaceace pages 1-4).

Grabke et al. (1995) described how selective oxidation follows Wagner's model, where the balance between inward oxygen flux and outward solute flux determines whether oxidation is external (surface scale) or internal (subsurface precipitates). The H₂/H₂O ratio and oxygen partial pressure set the dissolved oxygen molar fraction and thus the oxidation regime (grabke1995segregationonthe pages 13-13). Elements with high oxygen affinity (Si, P, B) oxidize at the wustite/metal interface, forming silicates, phosphates, or borates that suppress vacancy annihilation and promote void formation by vacancy condensation (grabke1995segregationonthe pages 17-17).

During vacuum annealing of powder metallurgical hot-work tool steel, surface oxide reduction proceeds in at least two steps: iron oxides are largely reduced by ~600–700°C, while more stable Cr–Mn and V oxides require temperatures of ~900°C (brust2013transformationofsurface pages 84-87). MnCr₂O₄ spinels can form by diffusion-driven enrichment of strong oxide-forming elements to the surface (brust2013transformationofsurface pages 79-82). The annealing atmosphere (vacuum vs. hydrogen) also influences subsequent oxidation kinetics: Inaba et al. (1986) found that oxide growth rates on Fe–36Ni alloy were two to three times higher on hydrogen-annealed samples than vacuum-annealed samples, linked to dislocation density differences in the inner oxide layer (inaba1986effectsofthe pages 1-4).

## 4. Decarburization Mechanisms

### 4.1 Chemical Reactions and Kinetics

Surface decarburization occurs when carbon at or near the steel surface reacts with atmospheric species (O₂, CO₂, H₂O, H₂) to form gaseous products (CO, CO₂, CH₄), leading to carbon depletion (stojanovic2025decarburizationandits pages 2-5). The process involves several sequential steps: (1) diffusion of carbon from the bulk to the surface, (2) adsorption of gas species (particularly H₂O and H₂) on the surface, (3) oxidation of carbon at the surface, and (4) possible formation of iron oxide scale that isolates the metal surface (marra2004decarburizationkineticsduring pages 1-2). Initially, the surface chemical reaction controls the decarburization rate, but with time, water–iron reactions can form an oxide layer that slows further decarburization (marra2004decarburizationkineticsduring pages 1-2).

Decarburization onset temperatures vary with atmosphere: ~790°C in 100% H₂, >700°C in 2% O₂, and >570°C in ambient air (stojanovic2025decarburizationandits pages 2-5). Rates accelerate with higher temperature and longer exposure, with documented cases of carbon dropping from 1.67 to 0.22 wt% C after 12 days at 950–1050°C (stojanovic2025decarburizationandits pages 2-5). Decarburization typically penetrates only small depths, generally no more than approximately 2% of the workpiece thickness, and can be either partial or complete (100% ferrite at the surface) (herring2010annealingofwirea pages 4-4).

### 4.2 Role of Oxide Layer Structure

The oxide scale structure plays a critical role in modulating decarburization. In Fe–3%Si steel, Guo et al. (2018) showed that internal oxidation produces silica particles that transition from spherical to lamellar morphology with increasing P_H₂O/P_H₂ and temperature. These oxide particles and the thicker oxidized layer act as barriers to outward carbon diffusion, reducing decarburization depth. The diffusion coefficient of oxygen through SiO₂ (D_O–SiO₂ ≈ 3.29 × 10⁻¹⁷ cm²/s) is many orders of magnitude lower than in the steel matrix (D_O ≈ 1.56 × 10⁻⁷ cm²/s at 1103 K), so silica-rich layers substantially hinder transport (guo2018effectofsurface pages 6-7). An optimum condition for maximum decarburization was identified at 1103 K and P_H₂O/P_H₂ = 0.374; below this ratio mass transfer dominates and decarburization increases, while above it oxide-particle effects dominate and decarburization decreases (guo2018effectofsurface pages 7-8).

Chen et al. (2020) demonstrated that when FeO forms on 60Si2MnA steel, dissolved carbon reacts with FeO via [C] + FeO → Fe + CO, and the equilibrium carbon activity at the FeO–steel interface is set by CO/CO₂ equilibria. Carbon then diffuses through a ferrite layer, and the decarburization rate is governed by the relative carbon permeability P_α–FeC = D_α–FeC × ΔC, which peaks around 800°C, explaining the maximum decarburization depth observed at that temperature (chen2020decarburizationof60si2mna pages 21-24). In contrast, continuous SiO₂ formation lowers the oxygen potential at the oxide–steel interface and can suppress decarburization entirely (chen2020decarburizationof60si2mna pages 19-21).

### 4.3 Carbon Deposition (Sooting)

The reverse problem—unwanted carbon deposition—can occur in CO-rich atmospheres via the Boudouard reaction (2CO → CO₂ + C) in the 300–500°C range. Carbon pickup can cause surface cracking and must be avoided by controlling endothermic/exothermic gas carbon potential and shutting off hydrocarbon feeds during soak after reactions are complete (herring2010annealingofwirea pages 4-4, herring2010annealingofwire pages 4-4).

## 5. Mitigation Strategies

### 5.1 Atmosphere Selection and Control

The choice of protective atmosphere is the primary mitigation strategy. Common options include nitrogen or N₂–hydrocarbon blends, hydrogen or H₂/N₂ blends for bright annealing, dissociated ammonia (≈75% H₂/25% N₂), exothermic gas, purified rich exothermic gas (CO₂ < 0.1%), and endothermic gas (herring2010annealingofwire pages 1-2, herring2010annealingofwirea pages 1-2). Endothermic gas provides significantly better protection against decarburization than nitrogen alone, with maximum decarburization depths of 10 μm with endothermic gas versus 70 μm with nitrogen reported for comparable conditions (stojanovic2025decarburizationandits pages 9-11). Argon is also effective as an inert blanket, particularly during austenitization (stojanovic2025decarburizationandits pages 7-9).

### 5.2 Atmosphere Monitoring and Instrumentation

Active atmosphere monitoring is essential and requires multiple complementary instruments: dew point analyzers for water vapor, infrared multi-gas analyzers for CO/CO₂, and oxygen probes for ppm-level O₂ measurement (herring2010annealingofwirea pages 2-4, herring2010annealingofwire pages 2-4). Monitoring must be integrated with temperature control, and atmosphere stability should be confirmed before heating begins (herring2010annealingofwire pages 2-4).

### 5.3 Purging and Volume Changeover

Cold purging with nitrogen or lean non-combustible gas until oxygen falls below ~1% is critical before any heating step. A common flow-rate guideline is five volume changes per hour (herring2010annealingofwire pages 1-2). During initial heating, volatilized surface contaminants (oils, residues) must be flushed from the furnace atmosphere before the soak phase (herring2010annealingofwirea pages 2-4).

### 5.4 Vacuum System Design

For vacuum furnaces, design measures include heating exterior surfaces while the chamber is open to minimize water adsorption, venting with dry gas, using load-locks for preprocessing, maintaining the roughing manifold in the viscous flow regime, employing fail-safe valve and interlock designs, and performing regular bakeouts and residual gas analysis (mattox1998preparationandcleaning pages 39-42, mattox1998preparationandcleaning pages 42-46).

### 5.5 Physical Barriers and Packaging

When controlled-atmosphere infrastructure is limited, protective packaging can reduce reliance on inert gases. Options include stainless-steel foil wrapping, charcoal- or coal-surrounded containers, pack carburizing, and iron filings to create a physical barrier against the furnace environment (stojanovic2025decarburizationandits pages 7-9).

### 5.6 Process Parameter Optimization

Temperature–time profiles must be optimized to minimize residence in the most severe decarburization regime. Controlling the ramp from initial heating to soak temperature is necessary to prevent decarburization (herring2010annealingofwirea pages 2-4). Cooling to near-ambient under protective atmosphere before exposure to air is recommended for bright finish preservation (herring2010annealingofwirea pages 2-4).

## 6. Relevance to Induction Heating Systems

Induction heating systems introduce several distinctive considerations for contamination, oxidation, and decarburization control.

### 6.1 Rapid Heating and Reduced Exposure Time

The characteristically rapid and localized heating of induction systems inherently reduces the time available for oxidation and decarburization reactions, provided that the atmosphere is already stable. The Handbook of Induction Heating cites multiple studies demonstrating that inert atmospheres can significantly reduce scaling on induction-heated forging stock, and that "scale-free heating of slabs and billets" is an achievable engineering objective (rudnev2017handbookofinduction pages 46-47). Lee et al. (2014) showed that increased heating rate produces thinner oxide layers with different morphology (thin Al₂O₃ rather than thick ZnO on galvanized press-hardening steel) and smoother surfaces (R_q ≈ 0.86 μm at +10 K/s versus R_q ≈ 2.00 μm at +5 K/s) (lee2014surfaceoxideformation pages 1-2).

### 6.2 Atmosphere–Heating Synchronization

A critical challenge for induction systems is ensuring that the protective atmosphere is fully established before rapid heating begins. Because induction heating can reach target temperatures in seconds, any lag between atmosphere stabilization and heating onset risks surface degradation. Ramp control, pre-purging, and integration of temperature and atmosphere control systems are emphasized as essential (herring2010annealingofwire pages 2-4, rudnev2017handbookofinduction pages 29-32).

### 6.3 Equipment-Specific Design

The Handbook of Induction Heating documents industry efforts to modify induction heater designs for scale reduction, including atmosphere generation/management systems and induction-specific improvements such as enclosing the heated zone in controlled-atmosphere chambers (rudnev2017handbookofinduction pages 46-47, rudnev2017handbookofinduction pages 29-32). Quality assurance in induction systems relies on closed-loop/open-loop control modes, PLCs, energy monitoring, and signature monitoring to ensure consistent surface quality (rudnev2017handbookofinduction pages 29-32).

## 7. Summary Table of Mechanisms and Mitigations

The following table consolidates the principal contamination, oxidation, and decarburization mechanisms along with their effects and mitigation strategies:

| Category | Mechanism/Source | Effect on Workpiece | Mitigation Strategy | Key References |
|---|---|---|---|---|
| Residual gas contamination (O2, H2O, CO2) | Trace oxidizing species enter from leaks, incomplete purge, wet gas supply, or residual atmosphere; in H2/N2 or inert atmospheres, residual H2O sets oxygen potential and can still oxidize reactive alloying elements or drive decarburization | Surface oxidation/discoloration, selective oxidation, carbon loss, hardness loss, poorer fatigue resistance, non-bright finish | Cold purge to <1% O2 before heating; monitor O2, dew point, CO2/CO with probes and IR analyzers; dry gases and lower dew point; use purified gas blends or vacuum/partial-pressure bright annealing; cool under protection before air exposure | (herring2010annealingofwire pages 1-2, herring2010annealingofwirea pages 1-2, olefjord1980selectivesurfaceace pages 1-4, grabke1995segregationonthe pages 13-13) |
| Outgassing from chamber walls and fixtures | Adsorbed water, hydrocarbons, solvents, and dissolved gases desorb from chamber walls, fixtures, seals, polymers, and prior-process residues; heating accelerates outgassing | Reactive background gas load, oxidation/decarburization risk, thin-film or residue deposition, inconsistent surface chemistry, longer pumpdown | Bakeout; minimize chamber-open time; vent with dry gas; use load-lock/precleaning; clean and vacuum-bake polymers; maintain logs of pumpdown/leak-up and residual gas signatures | (mattox1998preparationandcleaning pages 39-42, mattox1998preparationandcleaning pages 14-17, mattox1998preparationandcleaning pages 48-51) |
| Oil backstreaming from pumps | Pump oils backstream or creep into the hot zone/foreline; oil vapors or residues can decompose thermally or under discharge/plasma exposure into carbonaceous films and particles | Hydrocarbon contamination, soot/carbon deposits, adhesion defects, vacuum degradation, variable surface cleanliness | Use dry pumps or traps; keep roughing manifold in viscous-flow regime; use ballast/orifice and fail-safe valves; interlock pumps/traps; monitor blanked-off pump condition | (mattox1998preparationandcleaning pages 39-42, mattox1998preparationandcleaning pages 42-46, taborelli2020cleaningandsurface pages 8-10) |
| Heating element contamination | Furnace hardware can be a source of volatile or transferable species; e.g., Al detected at steel powder surfaces may originate from Kanthal A-1 elements; hot hardware also contributes desorption/vaporization | Surface contamination, altered oxide chemistry, unwanted inclusions/particulates, degraded interparticle bonding in PM materials | Identify hardware-derived species during troubleshooting; maintain clean hot-zone materials; control temperature/vacuum quality; clean surfaces before critical anneals | (brust2013transformationofsurface pages 84-87, mattox1998preparationandcleaning pages 53-54, mattox1998preparationandcleaning pages 11-14) |
| Surface oxidation / oxide scale formation | Oxides form when oxygen potential is sufficient; scale structure depends on temperature, atmosphere, alloy chemistry, and time; in Fe-Si steels, FeO/Fe2SiO4 or SiO2-rich layers form depending on H2O/O2 potential | Discoloration, scale removal cost, altered carbon activity at interface, impaired downstream coating/joining, possible embrittlement or reduced bond quality | Lower oxygen potential with vacuum or dried/reducing atmospheres; purge thoroughly; select atmosphere chemistry to favor protective/non-scaling conditions; optimize time/temperature to limit thick scale | (chen2020decarburizationof60si2mna pages 21-24, chen2020decarburizationof60si2mna pages 13-16, grabke1995segregationonthe pages 13-13, grabke1995segregationonthe pages 17-17, chen2020decarburizationof60si2mna pages 19-21, chen2020decarburizationof60si2mna pages 7-13) |
| Selective oxidation of alloying elements (Mn, Cr, Si) | Even when iron oxide is reduced, residual H2O/O2 can selectively oxidize stronger oxide formers such as Mn, Si, Cr, Al, V, Ti; oxides may appear at grain boundaries, as islands, or as spinels/silica-rich lamellae | Surface chemistry becomes heterogeneous; reduced wettability/coating response; more stable oxides are harder to reduce; possible entrapped oxides in PM processing | Reduce dew point and oxygen potential; use vacuum or better-dried H2/N2 or inert gas; choose annealing mode/time to minimize selective external oxidation; reduce stable oxides at higher temperatures where thermodynamically feasible | (olefjord1980selectivesurfaceace pages 1-4, brust2013transformationofsurface pages 79-82, grabke1995segregationonthe pages 13-13, brust2013transformationofsurface pages 84-87, inaba1986effectsofthe pages 1-4, grabke1995segregationonthe pages 12-13) |
| Decarburization by H2O and CO2 | Surface carbon reacts with H2O/O2/CO2 to form CO/CO2/CH4; CO2 can increase decarburization directly and via water-forming equilibria; humid atmospheres strongly accelerate ferritic decarburized-layer formation | Carbon depletion near surface, lower hardness and fatigue resistance, ferritic surface layer, property scatter | Lower dew point and CO2 partial pressure; use argon or endothermic atmospheres rather than plain N2 when needed; dry gas supply; packaging/barriers such as stainless foil, charcoal, iron filings | (stojanovic2025decarburizationandits pages 7-9, marra2004decarburizationkineticsduring pages 1-2, stojanovic2025decarburizationandits pages 2-5, chen2020decarburizationof60si2mna pages 21-24) |
| Decarburization by diffusion-limited processes | After initial surface reaction, kinetics can become limited by carbon diffusion from bulk, oxygen diffusion through oxide, and interface carbon activity; oxide scale structure can either accelerate or suppress carbon loss depending on FeO vs SiO2-rich morphology | Nonlinear depth-vs-time behavior; maximum decarburization may occur in specific temperature windows; thicker or silica-rich internal oxidation zones can suppress further carbon loss | Control temperature/time to avoid the most severe decarb regime; design oxide structure/oxygen potential to avoid FeO-dominated scales; shorten exposure; use faster heat-up with stable atmosphere | (marra2004decarburizationkineticsduring pages 1-2, stojanovic2025decarburizationandits pages 7-9, stojanovic2025decarburizationandits pages 5-7, guo2018effectofsurface pages 7-8, guo2018effectofsurface pages 2-5, chen2020decarburizationof60si2mna pages 13-16) |
| Carbon deposition (sooting) from Boudouard reaction | In CO-rich atmospheres, especially around 300–500°C, 2CO -> CO2 + C can deposit soot; hydrocarbon additions can also form carbon if not shut off appropriately after reactions complete | Carbon pickup, dirty/blackened surfaces, possible surface cracking, variable carbon potential and finish | Avoid CO-rich conditions in the critical temperature window; tightly control endo/exo gas carbon potential; shut off hydrocarbon feeds during soak; rapidly cool retort gas where applicable | (herring2010annealingofwire pages 2-4, herring2010annealingofwirea pages 4-4, herring2010annealingofwire pages 4-4, herring2010annealingofwirea pages 2-4) |
| Rapid heating rate effects relevant to induction systems | Induction systems heat rapidly and locally, reducing time available for oxidation/decarburization if atmosphere is already stable; however, rapid heating under poor atmosphere can still form oxides, and ramp control remains critical | Potential reduction in scale/decarb due to shorter exposure, but risk of nonuniform oxide morphology or defects if purge/atmosphere stability lags heating; surface finish is sensitive to process synchronization | Synchronize fast heat-up with pre-purge and stable atmosphere; integrate temperature and atmosphere control; use inert/protective atmospheres for scale-free induction heating; avoid air-burnoff segments when possible | (herring2010annealingofwire pages 2-4, rudnev2017handbookofinduction pages 46-47, rudnev2017handbookofinduction pages 29-32, herring2010annealingofwirea pages 2-4, lee2014surfaceoxideformation pages 1-2) |


*Table: This table summarizes the main contamination, oxidation, and decarburization mechanisms reported for vacuum and inert-atmosphere annealing, along with practical mitigation measures. It also highlights where rapid-heating induction systems change the balance of risks and controls.*

## 8. BibTeX References

The following BibTeX entries correspond to the key references cited throughout this review:

```bibtex
@article{herring2010annealingofwire,
  author    = {Herring, D. H. and Sisson, R. D., Jr.},
  title     = {Annealing of wire products: atmospheres},
  year      = {2010},
  journal   = {Unknown journal}
}

@article{stojanovic2025decarburizationandits,
  author    = {Stojanovi{\'c}, \v{Z}eljko and Gligorijevi{\'c}, Bojan and Prvulovi{\'c}, Slavica and But, Adrian and Svoboda, Petr and Pite{\v{l}}, J{\'a}n and Vencl, Aleksandar},
  title     = {Decarburization and Its Effects on the Properties of Plasma-Nitrided AISI 4140 Steel: A Review},
  journal   = {Materials},
  year      = {2025},
  volume    = {18},
  number    = {10},
  pages     = {2207},
  month     = {May},
  doi       = {10.3390/ma18102207},
  url       = {https://doi.org/10.3390/ma18102207},
  publisher = {MDPI AG},
  issn      = {1996-1944}
}

@article{brust2013transformationofsurface,
  author    = {Brust, S.},
  title     = {Transformation of surface oxides during vacuum heat treatment of a powder metallurgical hot work tool steel},
  year      = {2013},
  journal   = {Unknown journal}
}

@article{mattox1998preparationandcleaning,
  author    = {Mattox, Donald M.},
  title     = {Preparation and Cleaning of Vacuum Surfaces},
  year      = {1998},
  journal   = {ArXiv},
  pages     = {553--606},
  month     = {Jan},
  doi       = {10.1016/B978-012352065-4/50070-5},
  url       = {https://doi.org/10.1016/B978-012352065-4/50070-5},
  publisher = {Elsevier}
}

@article{marra2004decarburizationkineticsduring,
  author    = {Marra, Kleiner Marques and de Azevedo Alvarenga, Evandro and Buono, Vicente Tadeu Lopes},
  title     = {Decarburization Kinetics during Annealing of a Semi-processed Electrical Steel},
  journal   = {ISIJ International},
  year      = {2004},
  volume    = {44},
  number    = {3},
  pages     = {618--622},
  month     = {Mar},
  doi       = {10.2355/isijinternational.44.618},
  url       = {https://doi.org/10.2355/isijinternational.44.618},
  publisher = {Iron and Steel Institute of Japan},
  issn      = {0915-1559}
}

@article{chen2020decarburizationof60si2mna,
  author    = {Chen, Yisheng R. and Xu, Xuanxuan and Liu, Yu},
  title     = {Decarburization of 60Si2MnA in Atmospheres Containing Different Levels of Oxygen, Water Vapour and Carbon Dioxide at 700--1000 {\textdegree}C},
  journal   = {Oxidation of Metals},
  year      = {2020},
  volume    = {93},
  number    = {1--2},
  pages     = {105--129},
  month     = {Dec},
  doi       = {10.1007/s11085-019-09949-3},
  url       = {https://doi.org/10.1007/s11085-019-09949-3},
  publisher = {Springer Science and Business Media LLC},
  issn      = {0030-770X}
}

@article{guo2018effectofsurface,
  author    = {Guo, Yue and Dai, Fangqin and Hu, Shoutian and Xu, Guang},
  title     = {Effect of Surface Oxidation on Decarburization of a Fe-3\%Si Steel during Annealing},
  journal   = {ISIJ International},
  year      = {2018},
  volume    = {58},
  number    = {9},
  pages     = {1727--1734},
  month     = {Sep},
  doi       = {10.2355/isijinternational.isijint-2018-233},
  url       = {https://doi.org/10.2355/isijinternational.isijint-2018-233},
  publisher = {Iron and Steel Institute of Japan},
  issn      = {0915-1559}
}

@article{olefjord1980selectivesurfaceace,
  author    = {Olefjord, I. and Leijon, W. and Jelvestam, U.},
  title     = {Selective surface oxidation during annealing of steel sheets in H2/N2},
  journal   = {Applications of Surface Science},
  year      = {1980},
  volume    = {6},
  number    = {3--4},
  pages     = {241--255},
  month     = {Nov},
  doi       = {10.1016/0378-5963(80)90015-X},
  url       = {https://doi.org/10.1016/0378-5963(80)90015-X},
  publisher = {Elsevier BV},
  issn      = {0378-5963}
}

@article{grabke1995segregationonthe,
  author    = {Grabke, H. J. and Leroy, V. and Viefhaus, H.},
  title     = {Segregation on the Surface of Steels in Heat Treatment and Oxidation},
  journal   = {ISIJ International},
  year      = {1995},
  volume    = {35},
  pages     = {95--113},
  month     = {Feb},
  doi       = {10.2355/isijinternational.35.95},
  url       = {https://doi.org/10.2355/isijinternational.35.95}
}

@article{rudnev2017handbookofinduction,
  author    = {Rudnev, Valery and Loveless, Don and Cook, Raymond L. and Black, Micah},
  title     = {Handbook of Induction Heating},
  journal   = {ArXiv},
  year      = {2017},
  month     = {Dec},
  doi       = {10.1201/9781420028904},
  url       = {https://doi.org/10.1201/9781420028904},
  publisher = {CRC Press}
}

@article{lee2014surfaceoxideformation,
  author    = {Lee, Chang Wook and Choi, Won Seok and Cho, Yeol Rae and De Cooman, Bruno Charles},
  title     = {Surface Oxide Formation during Rapid Heating of Zn-coated Press Hardening Steel},
  journal   = {ISIJ International},
  year      = {2014},
  volume    = {54},
  number    = {10},
  pages     = {2364--2368},
  month     = {Oct},
  doi       = {10.2355/isijinternational.54.2364},
  url       = {https://doi.org/10.2355/isijinternational.54.2364},
  publisher = {Iron and Steel Institute of Japan},
  issn      = {0915-1559}
}

@article{inaba1986effectsofthe,
  author    = {Inaba, Michihiko and Honma, Yoshinori and Hatanaka, Tatsuya and Otake, Yasuhisa},
  title     = {Effects of the annealing conditions on the oxidation behavior of Fe-36Ni alloys},
  journal   = {Applied Surface Science},
  year      = {1986},
  volume    = {27},
  number    = {2},
  pages     = {164--179},
  month     = {Nov},
  doi       = {10.1016/0169-4332(86)90105-4},
  url       = {https://doi.org/10.1016/0169-4332(86)90105-4},
  publisher = {Elsevier BV},
  issn      = {0169-4332}
}

@article{meng2023designofvacuum,
  author    = {Meng, Jintao and Gao, Haitao and Ruan, Mixue and Guo, Hai and Zhou, Xiaojie and Zhang, Di},
  title     = {Design of vacuum annealing furnace temperature control system based on GA-Fuzzy-PID algorithm},
  journal   = {PLOS ONE},
  year      = {2023},
  volume    = {18},
  number    = {11},
  pages     = {e0293823},
  month     = {Nov},
  doi       = {10.1371/journal.pone.0293823},
  url       = {https://doi.org/10.1371/journal.pone.0293823},
  publisher = {Public Library of Science (PLoS)},
  issn      = {1932-6203}
}

@article{taborelli2020cleaningandsurface,
  author    = {Taborelli, Mauro},
  title     = {Cleaning and Surface Properties},
  journal   = {Preprint},
  year      = {2020},
  month     = {Jan},
  doi       = {10.48550/arXiv.2006.01585},
  url       = {https://doi.org/10.48550/arXiv.2006.01585},
  publisher = {arXiv}
}
```


*Code_block: This artifact compiles BibTeX entries for the core sources used in the literature review on contamination, oxidation, and decarburization control in vacuum and inert-atmosphere annealing, including induction-relevant references.*

## 9. Conclusions

Contamination, oxidation, and decarburization in vacuum and inert-atmosphere annealing furnaces arise from a complex interplay of residual gas chemistry, outgassing, oil backstreaming, hardware-derived species, selective oxidation of alloying elements, and diffusion-controlled surface reactions. The oxide scale structure—particularly its composition (FeO vs. SiO₂-rich), morphology, and permeability—plays a critical and sometimes non-intuitive role in modulating decarburization kinetics (guo2018effectofsurface pages 7-8, chen2020decarburizationof60si2mna pages 19-21). Effective mitigation requires a multi-pronged approach encompassing atmosphere selection and monitoring, rigorous purging protocols, vacuum system design, physical barriers, and optimized process parameters. For induction heating systems, the rapid heating rate offers an inherent advantage in limiting exposure time to oxidizing conditions, but this advantage can only be realized when atmosphere stabilization is synchronized with the heating cycle and when enclosure/atmosphere management hardware is appropriately integrated into the system design (rudnev2017handbookofinduction pages 46-47, rudnev2017handbookofinduction pages 29-32).

References

1. (mattox1998preparationandcleaning pages 39-42): Donald M. Mattox. Preparation and cleaning of vacuum surfaces. ArXiv, pages 553-606, Jan 1998. URL: https://doi.org/10.1016/b978-012352065-4/50070-5, doi:10.1016/b978-012352065-4/50070-5. This article has 2 citations.

2. (herring2010annealingofwire pages 1-2): DH Herring and RD Sisson Jr. Annealing of wire products: atmospheres. Unknown journal, 2010.

3. (mattox1998preparationandcleaning pages 14-17): Donald M. Mattox. Preparation and cleaning of vacuum surfaces. ArXiv, pages 553-606, Jan 1998. URL: https://doi.org/10.1016/b978-012352065-4/50070-5, doi:10.1016/b978-012352065-4/50070-5. This article has 2 citations.

4. (mattox1998preparationandcleaning pages 42-46): Donald M. Mattox. Preparation and cleaning of vacuum surfaces. ArXiv, pages 553-606, Jan 1998. URL: https://doi.org/10.1016/b978-012352065-4/50070-5, doi:10.1016/b978-012352065-4/50070-5. This article has 2 citations.

5. (mattox1998preparationandcleaning pages 48-51): Donald M. Mattox. Preparation and cleaning of vacuum surfaces. ArXiv, pages 553-606, Jan 1998. URL: https://doi.org/10.1016/b978-012352065-4/50070-5, doi:10.1016/b978-012352065-4/50070-5. This article has 2 citations.

6. (brust2013transformationofsurface pages 84-87): S Brust. Transformation of surface oxides during vacuum heat treatment of a powder metallurgical hot work tool steel. Unknown journal, 2013.

7. (mattox1998preparationandcleaning pages 53-54): Donald M. Mattox. Preparation and cleaning of vacuum surfaces. ArXiv, pages 553-606, Jan 1998. URL: https://doi.org/10.1016/b978-012352065-4/50070-5, doi:10.1016/b978-012352065-4/50070-5. This article has 2 citations.

8. (mattox1998preparationandcleaning pages 11-14): Donald M. Mattox. Preparation and cleaning of vacuum surfaces. ArXiv, pages 553-606, Jan 1998. URL: https://doi.org/10.1016/b978-012352065-4/50070-5, doi:10.1016/b978-012352065-4/50070-5. This article has 2 citations.

9. (taborelli2020cleaningandsurface pages 8-10): Mauro Taborelli. Cleaning and surface properties. Preprint, Jan 2020. URL: https://doi.org/10.48550/arxiv.2006.01585, doi:10.48550/arxiv.2006.01585. This article has 45 citations.

10. (chen2020decarburizationof60si2mna pages 19-21): Yisheng R. Chen, Xuanxuan Xu, and Yu Liu. Decarburization of 60si2mna in atmospheres containing different levels of oxygen, water vapour and carbon dioxide at 700–1000 °c. Oxidation of Metals, 93:105-129, Dec 2020. URL: https://doi.org/10.1007/s11085-019-09949-3, doi:10.1007/s11085-019-09949-3. This article has 21 citations.

11. (chen2020decarburizationof60si2mna pages 7-13): Yisheng R. Chen, Xuanxuan Xu, and Yu Liu. Decarburization of 60si2mna in atmospheres containing different levels of oxygen, water vapour and carbon dioxide at 700–1000 °c. Oxidation of Metals, 93:105-129, Dec 2020. URL: https://doi.org/10.1007/s11085-019-09949-3, doi:10.1007/s11085-019-09949-3. This article has 21 citations.

12. (chen2020decarburizationof60si2mna pages 13-16): Yisheng R. Chen, Xuanxuan Xu, and Yu Liu. Decarburization of 60si2mna in atmospheres containing different levels of oxygen, water vapour and carbon dioxide at 700–1000 °c. Oxidation of Metals, 93:105-129, Dec 2020. URL: https://doi.org/10.1007/s11085-019-09949-3, doi:10.1007/s11085-019-09949-3. This article has 21 citations.

13. (olefjord1980selectivesurfaceace pages 1-4): I. Olefjord, W. Leijon, and U. Jelvestam. Selective surface ace oxidation during annealing of steel sheets in h2/n2. Applications of Surface Science, 6:241-255, Nov 1980. URL: https://doi.org/10.1016/0378-5963(80)90015-x, doi:10.1016/0378-5963(80)90015-x. This article has 100 citations.

14. (grabke1995segregationonthe pages 13-13): H. J. Grabke, V. Leroy, and H. Viefhaus. Segregation on the surface of steels in heat treatment and oxidation. Isij International, 35:95-113, Feb 1995. URL: https://doi.org/10.2355/isijinternational.35.95, doi:10.2355/isijinternational.35.95. This article has 169 citations and is from a peer-reviewed journal.

15. (grabke1995segregationonthe pages 17-17): H. J. Grabke, V. Leroy, and H. Viefhaus. Segregation on the surface of steels in heat treatment and oxidation. Isij International, 35:95-113, Feb 1995. URL: https://doi.org/10.2355/isijinternational.35.95, doi:10.2355/isijinternational.35.95. This article has 169 citations and is from a peer-reviewed journal.

16. (brust2013transformationofsurface pages 79-82): S Brust. Transformation of surface oxides during vacuum heat treatment of a powder metallurgical hot work tool steel. Unknown journal, 2013.

17. (inaba1986effectsofthe pages 1-4): Michihiko Inaba, Yoshinori Honma, Tatsuya Hatanaka, and Yasuhisa Otake. Effects of the annealing conditions on the oxidation behavior of fe-36ni alloys. Applied Surface Science, 27:164-179, Nov 1986. URL: https://doi.org/10.1016/0169-4332(86)90105-4, doi:10.1016/0169-4332(86)90105-4. This article has 21 citations and is from a domain leading peer-reviewed journal.

18. (stojanovic2025decarburizationandits pages 2-5): Željko Stojanović, Bojan Gligorijević, Slavica Prvulović, Adrian But, Petr Svoboda, Ján Piteľ, and Aleksandar Vencl. Decarburization and its effects on the properties of plasma-nitrided aisi 4140 steel: a review. Materials, 18:2207, May 2025. URL: https://doi.org/10.3390/ma18102207, doi:10.3390/ma18102207. This article has 8 citations.

19. (marra2004decarburizationkineticsduring pages 1-2): Kleiner Marques Marra, Evandro de Azevedo Alvarenga, and Vicente Tadeu Lopes Buono. Decarburization kinetics during annealing of a semi-processed electrical steel. Isij International, 44:618-622, Mar 2004. URL: https://doi.org/10.2355/isijinternational.44.618, doi:10.2355/isijinternational.44.618. This article has 32 citations and is from a peer-reviewed journal.

20. (herring2010annealingofwirea pages 4-4): DH Herring and RD Sisson Jr. Annealing of wire products: atmospheres. Unknown journal, 2010.

21. (guo2018effectofsurface pages 6-7): Yue Guo, Fangqin Dai, Shoutian Hu, and Guang Xu. Effect of surface oxidation on decarburization of a fe-3%si steel during annealing. ISIJ International, 58:1727-1734, Sep 2018. URL: https://doi.org/10.2355/isijinternational.isijint-2018-233, doi:10.2355/isijinternational.isijint-2018-233. This article has 14 citations and is from a peer-reviewed journal.

22. (guo2018effectofsurface pages 7-8): Yue Guo, Fangqin Dai, Shoutian Hu, and Guang Xu. Effect of surface oxidation on decarburization of a fe-3%si steel during annealing. ISIJ International, 58:1727-1734, Sep 2018. URL: https://doi.org/10.2355/isijinternational.isijint-2018-233, doi:10.2355/isijinternational.isijint-2018-233. This article has 14 citations and is from a peer-reviewed journal.

23. (chen2020decarburizationof60si2mna pages 21-24): Yisheng R. Chen, Xuanxuan Xu, and Yu Liu. Decarburization of 60si2mna in atmospheres containing different levels of oxygen, water vapour and carbon dioxide at 700–1000 °c. Oxidation of Metals, 93:105-129, Dec 2020. URL: https://doi.org/10.1007/s11085-019-09949-3, doi:10.1007/s11085-019-09949-3. This article has 21 citations.

24. (herring2010annealingofwire pages 4-4): DH Herring and RD Sisson Jr. Annealing of wire products: atmospheres. Unknown journal, 2010.

25. (herring2010annealingofwirea pages 1-2): DH Herring and RD Sisson Jr. Annealing of wire products: atmospheres. Unknown journal, 2010.

26. (stojanovic2025decarburizationandits pages 9-11): Željko Stojanović, Bojan Gligorijević, Slavica Prvulović, Adrian But, Petr Svoboda, Ján Piteľ, and Aleksandar Vencl. Decarburization and its effects on the properties of plasma-nitrided aisi 4140 steel: a review. Materials, 18:2207, May 2025. URL: https://doi.org/10.3390/ma18102207, doi:10.3390/ma18102207. This article has 8 citations.

27. (stojanovic2025decarburizationandits pages 7-9): Željko Stojanović, Bojan Gligorijević, Slavica Prvulović, Adrian But, Petr Svoboda, Ján Piteľ, and Aleksandar Vencl. Decarburization and its effects on the properties of plasma-nitrided aisi 4140 steel: a review. Materials, 18:2207, May 2025. URL: https://doi.org/10.3390/ma18102207, doi:10.3390/ma18102207. This article has 8 citations.

28. (herring2010annealingofwirea pages 2-4): DH Herring and RD Sisson Jr. Annealing of wire products: atmospheres. Unknown journal, 2010.

29. (herring2010annealingofwire pages 2-4): DH Herring and RD Sisson Jr. Annealing of wire products: atmospheres. Unknown journal, 2010.

30. (rudnev2017handbookofinduction pages 46-47): Valery Rudnev, Don Loveless, Raymond L. Cook, and Micah Black. Handbook of induction heating. ArXiv, Dec 2017. URL: https://doi.org/10.1201/9781420028904, doi:10.1201/9781420028904. This article has 1969 citations.

31. (lee2014surfaceoxideformation pages 1-2): Chang Wook Lee, Won Seok Choi, Yeol Rae Cho, and Bruno Charles De Cooman. Surface oxide formation during rapid heating of zn-coated press hardening steel. Isij International, 54:2364-2368, Oct 2014. URL: https://doi.org/10.2355/isijinternational.54.2364, doi:10.2355/isijinternational.54.2364. This article has 32 citations and is from a peer-reviewed journal.

32. (rudnev2017handbookofinduction pages 29-32): Valery Rudnev, Don Loveless, Raymond L. Cook, and Micah Black. Handbook of induction heating. ArXiv, Dec 2017. URL: https://doi.org/10.1201/9781420028904, doi:10.1201/9781420028904. This article has 1969 citations.

33. (grabke1995segregationonthe pages 12-13): H. J. Grabke, V. Leroy, and H. Viefhaus. Segregation on the surface of steels in heat treatment and oxidation. Isij International, 35:95-113, Feb 1995. URL: https://doi.org/10.2355/isijinternational.35.95, doi:10.2355/isijinternational.35.95. This article has 169 citations and is from a peer-reviewed journal.

34. (stojanovic2025decarburizationandits pages 5-7): Željko Stojanović, Bojan Gligorijević, Slavica Prvulović, Adrian But, Petr Svoboda, Ján Piteľ, and Aleksandar Vencl. Decarburization and its effects on the properties of plasma-nitrided aisi 4140 steel: a review. Materials, 18:2207, May 2025. URL: https://doi.org/10.3390/ma18102207, doi:10.3390/ma18102207. This article has 8 citations.

35. (guo2018effectofsurface pages 2-5): Yue Guo, Fangqin Dai, Shoutian Hu, and Guang Xu. Effect of surface oxidation on decarburization of a fe-3%si steel during annealing. ISIJ International, 58:1727-1734, Sep 2018. URL: https://doi.org/10.2355/isijinternational.isijint-2018-233, doi:10.2355/isijinternational.isijint-2018-233. This article has 14 citations and is from a peer-reviewed journal.