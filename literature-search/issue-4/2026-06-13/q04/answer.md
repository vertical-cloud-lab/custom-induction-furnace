Question: Summarize literature on induction-heating process parameters (frequency, power ramp rate, coil coupling, dwell profile) and their effects on temperature uniformity and resulting microstructure/grain growth during annealing. Provide references with bibtex.

# Induction-Heating Process Parameters and Their Effects on Temperature Uniformity and Microstructure/Grain Growth During Annealing: A Literature Review

## 1. Introduction

Induction heating is widely employed for annealing, hardening, and other thermal treatments of metals due to its high energy density, rapid heating capability, and precise controllability. However, the inherent electromagnetic skin effect and the strong coupling between process parameters and material response make temperature uniformity and microstructural control challenging. This review synthesizes the literature on how four key process parameters—frequency, power ramp rate, coil coupling (air gap), and dwell profile—affect temperature distribution and the resulting microstructure and grain growth during induction annealing.

The following table summarizes the key relationships between process parameters and their thermal/metallurgical effects:

| Process Parameter | Effect on Temperature Uniformity | Effect on Microstructure/Grain Growth | Key References |
|---|---|---|---|
| Frequency (skin depth) | Higher frequency decreases skin depth and concentrates power near the surface, increasing surface-core gradients and reducing through-thickness uniformity; lower frequency improves penetration and volumetric heating, though too low a frequency can reduce efficiency. Frequency must be balanced with part size, conductivity, and desired uniformity. (rapoport2006optimalcontrolof pages 44-47, hammi2016studyoffrequency pages 3-5, hatem2024simulationandimplementation pages 4-6, rapoport2006optimalcontrolof pages 40-44) | By changing penetration depth and local heating rate, frequency shifts transformation paths and local grain-size evolution. Surface-localized high-frequency heating can intensify nonuniform austenitization and thus microstructural gradients unless followed by adequate soak/equalization. (cryderman2020effectsofrapid pages 1-2, yang2010simulationofsteel pages 1-2, yang2010simulationofsteel pages 5-6) | (rapoport2006optimalcontrolof pages 44-47, hammi2016studyoffrequency pages 3-5, hatem2024simulationandimplementation pages 4-6, rapoport2006optimalcontrolof pages 40-44, yang2010simulationofsteel pages 1-2, yang2010simulationofsteel pages 5-6) |
| Power ramp rate / heating rate | Faster ramps increase instantaneous surface power density and usually enlarge thermal gradients; pulsed or staged power can cap surface temperature and reduce surface-core differential. As heating proceeds, rising resistivity can increase penetration somewhat, but excessive ramp rates still risk stress and cracking. (rapoport2006optimalcontrolof pages 44-47, rapoport2006optimalcontrolof pages 40-44, rapoport2006optimalcontrolof pages 50-53) | In many steels, increasing heating rate from conventional to rapid/ultrafast values refines recrystallized or prior-austenite grain size by favoring nucleation over growth and limiting time for grain coarsening. However, at very high rates some alloys show incomplete homogenization, retained carbides/cementite, or even bimodal/coarser austenite due to massive transformation mechanisms. (muljono2001influenceofheating pages 1-2, ferry2001recrystallizationkineticsof pages 1-2, cryderman2020effectsofrapid pages 1-2, javaheri2019insightintothe pages 27-35, javaheri2019insightintothe pages 23-27, wang2011rapidheatingeffects pages 1-3, yonemura2019finemicrostructureformation pages 4-6) | (rapoport2006optimalcontrolof pages 44-47, rapoport2006optimalcontrolof pages 40-44, rapoport2006optimalcontrolof pages 50-53, muljono2001influenceofheating pages 1-2, ferry2001recrystallizationkineticsof pages 1-2, cryderman2020effectsofrapid pages 1-2, javaheri2019insightintothe pages 27-35, javaheri2019insightintothe pages 23-27, wang2011rapidheatingeffects pages 1-3, yonemura2019finemicrostructureformation pages 4-6) |
| Coil-workpiece coupling (air gap) | Smaller air gaps strengthen electromagnetic coupling, raise current density, and increase heating efficiency and heating rate; larger gaps weaken coupling and can worsen nonuniformity by reducing delivered power and altering field distribution. Very tight coupling may also create stronger local hot spots under the coil. (dalaee2020experimentalandnumerical pages 18-23, dalaee2020experimentalandnumerical pages 14-18, usman2017inductiveweldof pages 16-21, rapoport2006optimalcontrolof pages 47-50, rapoport2006optimalcontrolof pages 44-47) | Coupling affects local thermal history rather than microstructure directly; stronger local coupling can accelerate local recrystallization/austenitization and thus spatial microstructural variation if the field is not uniform. Nonuniform gap during processing can therefore translate into nonuniform grain size and transformed depth. (dalaee2020experimentalandnumerical pages 18-23, rapoport2006optimalcontrolof pages 22-25, yang2010simulationofsteel pages 5-6, yang2010simulationofsteel pages 6-7) | (dalaee2020experimentalandnumerical pages 18-23, dalaee2020experimentalandnumerical pages 14-18, usman2017inductiveweldof pages 16-21, rapoport2006optimalcontrolof pages 47-50, rapoport2006optimalcontrolof pages 22-25, rapoport2006optimalcontrolof pages 44-47, yang2010simulationofsteel pages 5-6, yang2010simulationofsteel pages 6-7) |
| Dwell profile (soak time) | Soaking after heating reduces surface-core temperature differences by allowing inward conduction while surface heating stops or slows; dwell is essential for low-conductivity alloys and for processes demanding uniform bulk temperature. Pulse heating plus short soak intervals can shorten cycle time while controlling peak gradients. (rapoport2006optimalcontrolof pages 44-47, rapoport2006optimalcontrolof pages 40-44, rapoport2006optimalcontrolof pages 50-53) | Short dwell suppresses grain growth and can preserve refined microstructures, but may leave incomplete carbide dissolution, incomplete recrystallization, or chemical inhomogeneity. Longer dwell improves homogenization and completion of recrystallization/austenitization, but increases risk of grain coarsening once transformation is complete. (cryderman2020effectsofrapid pages 1-2, ferry2001recrystallizationkineticsof pages 1-2, wang2011rapidheatingeffects pages 1-3, banis2019theeffectof pages 1-3, yang2010simulationofsteel pages 5-6) | (rapoport2006optimalcontrolof pages 44-47, rapoport2006optimalcontrolof pages 40-44, rapoport2006optimalcontrolof pages 50-53, cryderman2020effectsofrapid pages 1-2, ferry2001recrystallizationkineticsof pages 1-2, wang2011rapidheatingeffects pages 1-3, banis2019theeffectof pages 1-3, yang2010simulationofsteel pages 5-6) |
| Coil geometry / architecture | Coil shape and architecture strongly determine field distribution and in-plane temperature uniformity. Conventional pancake coils can create center cold zones and edge overheating, while optimized serial-parallel or segmented coils flatten the temperature field; one study reduced normalized surface-temperature deviation from 27.06% to 2.03%. (xu2026designandoptimization pages 1-2, xu2026designandoptimization pages 9-11, xu2026designandoptimization pages 5-9, xu2026designandoptimization pages 2-5, rapoport2006optimalcontrolof pages 40-44, rapoport2006optimalcontrolof pages 47-50) | More uniform coil architectures produce more uniform local thermal cycles, which should reduce spatial variation in recrystallization, austenite fraction, and grain size. Segmented or multistage coils also enable tailored heating/soaking sequences that limit overheating and grain growth while maintaining throughput. (rapoport2006optimalcontrolof pages 44-47, rapoport2006optimalcontrolof pages 40-44, yang2010simulationofsteel pages 1-2, yang2010simulationofsteel pages 6-7) | (xu2026designandoptimization pages 1-2, xu2026designandoptimization pages 9-11, rapoport2006optimalcontrolof pages 44-47, xu2026designandoptimization pages 5-9, xu2026designandoptimization pages 2-5, rapoport2006optimalcontrolof pages 40-44, rapoport2006optimalcontrolof pages 47-50, yang2010simulationofsteel pages 1-2, yang2010simulationofsteel pages 6-7) |


*Table: This table summarizes how key induction-heating process parameters influence temperature uniformity and the resulting annealing microstructure or grain growth. It is useful as a compact map from controllable process settings to expected thermal and metallurgical outcomes.*

## 2. Frequency and Skin Depth

The alternating current frequency is the primary parameter governing skin depth (δ), which determines how deeply eddy currents—and therefore volumetric heat generation—penetrate the workpiece. Skin depth is inversely related to the square root of frequency and magnetic permeability; higher frequency produces shallower penetration and concentrates power density at the workpiece surface (rapoport2006optimalcontrolof pages 44-47, hammi2016studyoffrequency pages 3-5). Hatem (2024) demonstrated through simulation that increasing frequency from 500 Hz to 60 kHz reduced skin depth from 3.67 mm to 0.335 mm in aluminum, with correspondingly higher surface temperatures and steeper through-thickness gradients (hatem2024simulationandimplementation pages 4-6). Rapoport and Pleshivtseva (2006) emphasize that the surface-to-core temperature differential is proportional to power density, which is itself strongly frequency-dependent; excessive frequency concentrates heating in a thin surface layer, producing poor core heating and reduced temperature uniformity, while too low a frequency risks eddy-current cancellation and poor coil efficiency (rapoport2006optimalcontrolof pages 44-47, rapoport2006optimalcontrolof pages 40-44). The optimal frequency is therefore a compromise that depends on workpiece dimensions, material properties (including the Curie temperature transition, which abruptly increases skin depth), and required uniformity (hammi2016studyoffrequency pages 3-5, rapoport2006optimalcontrolof pages 22-25).

From a microstructural standpoint, frequency controls the local thermal history experienced at different depths. Because austenitization, recrystallization, and grain growth are all temperature- and time-dependent, a frequency that produces steep thermal gradients will generate spatial variation in the transformed microstructure. Yang et al. (2010) showed, using a cellular automaton model, that the local time–temperature curve at each spatial location governs austenite nucleation and grain growth during rapid induction heating, with grain size profiles directly following the temperature profile through the hardened layer (yang2010simulationofsteel pages 1-2, yang2010simulationofsteel pages 5-6, yang2010simulationofsteel pages 6-7).

## 3. Power Ramp Rate and Heating Rate

The rate at which power is applied—and consequently the heating rate experienced by the workpiece—has profound effects on both temperature uniformity and microstructural evolution. Rapoport and Pleshivtseva (2006) describe how faster power ramps increase instantaneous surface power density and enlarge the surface-to-core temperature differential. However, as temperature rises, electrical resistivity increases and current penetration deepens, partially counteracting the gradient (rapoport2006optimalcontrolof pages 44-47, rapoport2006optimalcontrolof pages 40-44). Power pulsing—alternating short bursts of high power with off periods—is an effective strategy to maintain target surface temperatures and can reduce process time by up to ~40% while controlling maximum thermal gradients (rapoport2006optimalcontrolof pages 44-47).

The microstructural consequences of heating rate have been extensively studied. Muljono et al. (2001) and Ferry et al. (2001), using transverse-flux induction heating (TFIH) at 50–1000 °C/s, found that increasing heating rate raises the recrystallization start temperature, broadens the recrystallization temperature range, and reduces the final recrystallized grain size in low and ultra-low carbon steels (muljono2001influenceofheating pages 1-2, ferry2001recrystallizationkineticsof pages 1-2, muljono2001influenceofheating pages 5-7). The mechanism is that rapid heating favors nucleation over growth, producing finer grains. Ferry et al. (2001) developed a JMAK-based annealing model that predicts recrystallization kinetics for arbitrary combinations of heating rate, peak temperature, holding time, and cooling rate (ferry2001recrystallizationkineticsof pages 1-2).

In medium-carbon steels, Cryderman et al. (2020) showed that rapid induction heating (5–500 °C/s) raises Ac1 and Ac3 temperatures, limits cementite dissolution time, and can produce very fine austenite grains (<10 µm) under short austenitizing cycles (cryderman2020effectsofrapid pages 1-2). Javaheri et al. (2019) found an optimal intermediate heating rate (~50 °C/s) for a 0.40% C microalloyed steel, where the finest prior-austenite grain size and highest hardness (~650 HV) were achieved; at higher rates (100–500 °C/s), a massive transformation mechanism produced coarser, bimodal austenite grains (javaheri2019insightintothe pages 27-35, javaheri2019insightintothe pages 23-27).

Ultrafast heating (>1000 °C/s) introduces additional phenomena. Yonemura et al. (2019) observed that heating at 1.2 × 10⁴ °C/s suppressed crystallite growth in the austenite phase, retained high dislocation densities, and promoted fine microstructure formation via massive-like transformations (yonemura2019finemicrostructureformation pages 4-6, yonemura2019finemicrostructureformation pages 6-7). Castro Cerda et al. (2016) demonstrated that at 1500 °C/s, the fraction of recrystallized ferrite grains below 1 µm increased noticeably, indicating enhanced nucleation, while texture evolution shifted toward high stored-energy components such as rotated Goss {110}⟨110⟩ (cerda2016theeffectof pages 12-13, cerda2016theeffectof pages 1-3). Da Costa Reis et al. (2003) reported that grain refinement in interstitial-free steels saturates above ~1000 °C/s for ferrite-regime annealing, but ultrafast heating into the austenite field can produce markedly coarser transformation grains (reis2003grainrefinementand pages 1-2). Bodyako et al. (1962) confirmed that induction heating generally yields finer recrystallized structures than furnace heating because brief high-temperature exposure and rapid nucleation favor many recrystallization nuclei over grain growth (bodyako1962recrystallizationdiagramsfor pages 3-3).

For non-oriented electrical steels, Wang et al. (2011) showed that rapid annealing at 15–300 °C/s of 3% Si steel refined recrystallized grains, suppressed the {111} γ-fiber, and strengthened beneficial ⟨001⟩//RD and ⟨001⟩//ND texture components, with an intermediate rate of 100 °C/s giving optimized magnetic properties (core loss reduced 13%, B₅₀ increased 3%) (wang2011rapidheatingeffects pages 1-3).

## 4. Coil-Workpiece Coupling (Air Gap)

The electromagnetic coupling between the induction coil and the workpiece is critically dependent on the air gap between them. Coupling efficiency is inversely proportional to the square of the coil-to-workpiece distance, meaning that even modest increases in the air gap can substantially reduce the induced emf and eddy-current heating (usman2017inductiveweldof pages 16-21). Dalaee et al. (2020) demonstrated that reducing the coupling gap from 4 mm to 2 mm increased surface temperature by approximately 60% within the first 2 seconds (dalaee2020experimentalandnumerical pages 14-18). Magnetic flux density is non-uniform beneath the coil, being denser near coil turns and weaker at the center, which produces localized heating and potential temperature non-uniformity across the workpiece (usman2017inductiveweldof pages 16-21).

Rapoport and Pleshivtseva (2006) describe a fundamental design trade-off: refractory liners reduce heat losses (improving thermal efficiency) but increase the coil-to-workpiece gap, which weakens electromagnetic coupling and reduces electrical efficiency (rapoport2006optimalcontrolof pages 47-50, rapoport2006optimalcontrolof pages 44-47). Shape mismatches (e.g., round liners with square billets) further reduce coupling. Use of magnetic flux concentrators can compensate for larger gaps but may intensify local thermal gradients (dalaee2020experimentalandnumerical pages 18-23). Because coupling distance modulates the local thermal history, spatial variations in gap—whether from geometric tolerances, part movement, or build-up during processing—translate directly into non-uniform grain size and transformed-layer depth (dalaee2020experimentalandnumerical pages 18-23, rapoport2006optimalcontrolof pages 22-25).

## 5. Dwell Profile (Soak Time)

After the heating stage, a soak or dwell period allows heat to conduct from the surface into the core, reducing the surface-to-core temperature differential and promoting uniformity. This stage is especially critical for low-thermal-conductivity alloys (stainless steels, titanium, carbon steels) where thermal equalization is inherently slow (rapoport2006optimalcontrolof pages 44-47, rapoport2006optimalcontrolof pages 40-44). Rapoport and Pleshivtseva (2006) note that upon power cutoff the surface cools rapidly via radiation and convection while the core continues to warm by conduction, progressively narrowing the temperature differential (rapoport2006optimalcontrolof pages 40-44). Transfer time between the coil and downstream operations must also be accounted for, as uncontrolled delay can distort the temperature distribution (rapoport2006optimalcontrolof pages 50-53).

From a microstructural perspective, dwell time determines whether carbide dissolution, recrystallization, and chemical homogenization are completed. Short dwell times suppress grain growth and can preserve refined microstructures, but may leave incomplete cementite dissolution, partial recrystallization, or chemical inhomogeneity (cryderman2020effectsofrapid pages 1-2, banis2019theeffectof pages 1-3). Banis et al. (2019) showed that ultrashort heating of a dual-phase steel impeded cementite dissolution, leaving undissolved carbides in the final microstructure and driving an interface-controlled (massive) α→γ transformation instead of diffusion-controlled austenitization (banis2019theeffectof pages 1-3). Conversely, longer dwell times allow full completion of recrystallization and austenite homogenization, but risk grain coarsening once transformation is complete (ferry2001recrystallizationkineticsof pages 1-2, yang2010simulationofsteel pages 5-6).

## 6. Coil Geometry and Architecture

Coil design is a primary engineering lever for controlling temperature uniformity. Conventional pancake coils create characteristic annular heating patterns with cold zones at the center and overheated edges (xu2026designandoptimization pages 2-5). Xu et al. (2026) introduced a serial-parallel coil architecture that connects three identical longitudinal coils in parallel to equalize current and homogenize the electromagnetic field; their optimized design reduced the normalized standard deviation (NSD) of surface temperature from 27.06% to 2.03% while heating X46Cr13 steel to >1000 °C in 10 seconds (xu2026designandoptimization pages 1-2, xu2026designandoptimization pages 9-11). Multi-coil segmented architectures—where coils of different lengths and windings are individually powered—enable burst/pulse heating and independent power/frequency control for tailored heating/soaking sequences (rapoport2006optimalcontrolof pages 44-47, rapoport2006optimalcontrolof pages 40-44). Tight coil winding (space factor 0.7–0.9) and minimized gaps between coil units reduce energy losses and improve uniformity, while practical considerations such as refractory thickness, skid rail placement, and coil cooling proximity all influence the achievable temperature field (rapoport2006optimalcontrolof pages 47-50).

## 7. Simulation and Modeling Approaches

Numerical simulation plays a central role in understanding and optimizing induction heating processes. Yang et al. (2010) developed a cellular automaton (CA) model coupled with Monte Carlo methods to predict austenite nucleation and grain growth under non-uniform induction heating, accounting for heating-rate-dependent Ac1 shifts, enhanced nucleation at pearlite–ferrite interfaces, and carbon diffusion (yang2010simulationofsteel pages 1-2, yang2010simulationofsteel pages 2-3). Ferry et al. (2001) used a generalized JMAK transformation kinetics model for predicting recrystallization during arbitrary rapid thermal cycles (ferry2001recrystallizationkineticsof pages 1-2). Javaheri et al. (2019) employed DICTRA diffusion simulations and JMatPro to predict phase fractions and cementite dissolution during rapid heating (javaheri2019insightintothe pages 19-23, javaheri2019insightintothe pages 14-19). These models collectively demonstrate that local temperature history—controlled by frequency, power, coupling, and dwell—is the fundamental driver of spatial microstructural variation during induction annealing.

## 8. Conclusions

The literature consistently demonstrates that induction-heating process parameters are strongly interlinked and jointly determine temperature uniformity and microstructural outcomes during annealing. Higher frequency concentrates heating at the surface, increasing gradients; faster power ramps intensify surface–core differentials but promote grain refinement through enhanced nucleation; tighter coil coupling improves heating efficiency but can create local hot spots; and dwell/soak profiles are essential for temperature equalization and completion of metallurgical transformations. Coil geometry optimization—particularly serial-parallel and segmented architectures—offers substantial improvements in spatial uniformity. Optimal process design requires balancing these parameters for the specific alloy, geometry, and target microstructure, increasingly supported by coupled electromagnetic–thermal–metallurgical simulation frameworks.

## References (BibTeX)

```bibtex
@article{rapoport2006optimalcontrolof,
    author = "Rapoport, Edgar and Pleshivtseva, Yulia",
    title = "Optimal Control of Induction Heating Processes",
    year = "2006",
    journal = "ArXiv",
    month = "Jul",
    doi = "10.1201/9781420019490",
    url = "https://doi.org/10.1201/9781420019490",
    publisher = "CRC Press"
}

@article{rudnev2017handbookofinduction,
    author = "Rudnev, Valery and Loveless, Don and Cook, Raymond L. and Black, Micah",
    title = "Handbook of Induction Heating",
    year = "2017",
    journal = "ArXiv",
    month = "Dec",
    doi = "10.1201/9781420028904",
    url = "https://doi.org/10.1201/9781420028904",
    publisher = "CRC Press"
}

@article{hatem2024simulationandimplementation,
    author = "Hatem, Sude",
    title = "Simulation and Implementation of an Induction Heating System for Heating Brittle Thin Metal Sheets by Various Excitation Current Frequencies",
    year = "2024",
    journal = "Uluslararası Muhendislik Arastirma ve Gelistirme Dergisi",
    month = "Jun",
    doi = "10.29137/umagd.1439051",
    url = "https://doi.org/10.29137/umagd.1439051",
    publisher = "Uluslararasi Muhendislik Arastirma ve Gelistirme Dergisi",
    issn = "1308-5514"
}

@article{hammi2016studyoffrequency,
    author = "Hammi, Habib and Ouafi, Abderazzak El and Barka, Noureddine",
    title = "Study of Frequency Effects on Hardness Profile of Spline Shaft Heat-Treated by Induction",
    year = "2016",
    journal = "Journal of Materials Science and Chemical Engineering",
    volume = "4",
    pages = "1-9",
    month = "Mar",
    doi = "10.4236/msce.2016.43001",
    url = "https://doi.org/10.4236/msce.2016.43001",
    publisher = "Scientific Research Publishing, Inc.",
    issue = "03",
    issn = "2327-6045"
}

@article{dalaee2020experimentalandnumerical,
    author = "Dalaee, Mohammad Taghi and Gloor, Lars and Leinenbach, Christian and Wegener, Konrad",
    title = "Experimental and numerical study of the influence of induction heating process on build rates Induction Heating-assisted laser Direct Metal Deposition (IH-DMD)",
    year = "2020",
    journal = "Surface and Coatings Technology",
    month = "Feb",
    doi = "10.1016/j.surfcoat.2019.125275",
    url = "https://doi.org/10.1016/j.surfcoat.2019.125275",
    volume = "384",
    pages = "125275",
    publisher = "Elsevier BV",
    issn = "0257-8972"
}

@article{xu2026designandoptimization,
    author = "Xu, Yakun and Leonhardt, André and Birnbaum, Peter and Gruner, Jonas and Kunke, Andreas and Clausmeyer, Till",
    title = "Design and optimization of induction coil for improved temperature uniformity in fast heating of sheet metal",
    year = "2026",
    journal = "Discover Mechanical Engineering",
    volume = "5",
    month = "Apr",
    doi = "10.1007/s44245-026-00228-5",
    url = "https://doi.org/10.1007/s44245-026-00228-5",
    publisher = "Springer Science and Business Media LLC",
    issue = "1",
    issn = "2731-6564"
}

@article{usman2017inductiveweldof,
    author = "Usman, M",
    title = "Inductive weld of joints for optical fiber pipe",
    year = "2017",
    journal = "Unknown journal"
}

@article{muljono2001influenceofheating,
    author = "Muljono, D. and Ferry, M. and Dunne, D.",
    title = "Influence of heating rate on anisothermal recrystallization in low and ultra-low carbon steels",
    year = "2001",
    journal = "Materials Science and Engineering A-structural Materials Properties Microstructure and Processing",
    volume = "303",
    pages = "90-99",
    month = "May",
    doi = "10.1016/s0921-5093(00)01882-7",
    url = "https://doi.org/10.1016/s0921-5093(00)01882-7",
    publisher = "Elsevier BV",
    issue = "1-2",
    issn = "0921-5093"
}

@article{ferry2001recrystallizationkineticsof,
    author = "Ferry, M. and Muljono, D. and Dunne, D. P.",
    title = "Recrystallization Kinetics of Low and Ultra Low Carbon Steels during High-rate Annealing",
    year = "2001",
    journal = "Isij International",
    volume = "41",
    pages = "1053-1060",
    month = "Sep",
    doi = "10.2355/isijinternational.41.1053",
    url = "https://doi.org/10.2355/isijinternational.41.1053",
    publisher = "Iron and Steel Institute of Japan",
    issue = "9",
    issn = "0915-1559"
}

@article{cerda2016theeffectof,
    author = "Cerda, Felipe Castro and Kestens, Leo and Monsalve, Alberto and Petrov, Roumen",
    title = "The Effect of Ultrafast Heating in Cold-Rolled Low Carbon Steel: Recrystallization and Texture Evolution",
    year = "2016",
    journal = "ArXiv",
    volume = "6",
    pages = "288",
    month = "Nov",
    doi = "10.3390/met6110288",
    url = "https://doi.org/10.3390/met6110288",
    publisher = "MDPI AG",
    issue = "11",
    issn = "2075-4701"
}

@article{banis2019theeffectof,
    author = "Banis, Alexandros and Duran, Eliseo Hernandez and Bliznuk, Vitaliy and Sabirov, Ilchat and Petrov, Roumen H. and Papaefthymiou, Spyros",
    title = "The Effect of Ultra-Fast Heating on the Microstructure, Grain Size and Texture Evolution of a Commercial Low-C, Medium-Mn DP Steel",
    year = "2019",
    journal = "Metals",
    volume = "9",
    pages = "877",
    month = "Aug",
    doi = "10.3390/met9080877",
    url = "https://doi.org/10.3390/met9080877",
    publisher = "MDPI AG",
    issue = "8",
    issn = "2075-4701"
}

@article{yonemura2019finemicrostructureformation,
    author = "Yonemura, Mitsuharu and Nishibata, Hitomi and Nishiura, Tomohiro and Ooura, Natsumi and Yoshimoto, Yuki and Fujiwara, Kazuki and Kawano, Kaori and Terai, Tomoyuki and Inubushi, Yuichi and Inoue, Ichiro and Tono, Kensuke and Yabashi, Makina",
    title = "Fine microstructure formation in steel under ultrafast heating",
    year = "2019",
    journal = "Scientific Reports",
    volume = "9",
    month = "Aug",
    doi = "10.1038/s41598-019-47668-6",
    url = "https://doi.org/10.1038/s41598-019-47668-6",
    publisher = "Springer Science and Business Media LLC",
    issue = "1",
    issn = "2045-2322"
}

@misc{cryderman2020effectsofrapid,
    author = "Cryderman, Robert and Garrett, Dalton and Schlittenhart, Zachary and Seo, Eun Jung",
    title = "Effects of Rapid Induction Heating on Transformations in 0.6\% C Steels",
    year = "2020",
    journal = "Journal of Materials Engineering and Performance",
    volume = "29",
    pages = "3502-3515",
    month = "Feb",
    doi = "10.1007/s11665-020-04632-0",
    url = "https://doi.org/10.1007/s11665-020-04632-0",
    publisher = "Springer Science and Business Media LLC",
    issue = "6",
    issn = "1059-9495"
}

@article{javaheri2019insightintothe,
    author = "Javaheri, Vahid and Kolli, Satish and Grande, Bjørnar and Porter, David",
    title = "Insight into the Induction Hardening Behavior of a New 0.40\% C Microalloyed Steel: Effects of Initial Microstructure and Thermal Cycles",
    year = "2019",
    journal = "Text",
    month = "Jan",
    doi = "10.48550/arxiv.1812.10663",
    url = "https://doi.org/10.48550/arxiv.1812.10663",
    publisher = "arXiv"
}

@article{yang2010simulationofsteel,
    author = "Yang, B. J. and Hattiangadi, A. and Li, W. Z. and Zhou, G. F. and Mcgreevy, T.",
    title = "Simulation of steel microstructure evolution during induction heating",
    year = "2010",
    journal = "Materials Science and Engineering A-structural Materials Properties Microstructure and Processing",
    volume = "527",
    pages = "2978-2984",
    month = "May",
    doi = "10.1016/j.msea.2010.01.038",
    url = "https://doi.org/10.1016/j.msea.2010.01.038",
    publisher = "Elsevier BV",
    issue = "12",
    issn = "0921-5093"
}

@article{wang2011rapidheatingeffects,
    author = "Wang, Jian and Li, Jun and Wang, Xinfeng and Mi, Xiaochuan and Zhang, Shengen",
    title = "Rapid heating effects on grain-size, texture and magnetic properties of 3\% Si non-oriented electrical steel",
    year = "2011",
    journal = "Bulletin of Materials Science",
    volume = "34",
    pages = "1477-1482",
    month = "Dec",
    doi = "10.1007/s12034-011-0346-3",
    url = "https://doi.org/10.1007/s12034-011-0346-3",
    publisher = "Springer Science and Business Media LLC",
    issue = "7",
    issn = "0250-4707"
}

@article{bodyako1962recrystallizationdiagramsfor,
    author = "Bodyako, M. N. and Loiko, Yu. M. and Pavlyukevich, B. L. and Parkhimovich, V. I.",
    title = "Recrystallization diagrams for induction heating",
    year = "1962",
    journal = "Metal Science and Heat Treatment of Metals",
    volume = "2",
    pages = "57-59",
    doi = "10.1007/bf00655595",
    url = "https://doi.org/10.1007/bf00655595",
    month = "Jan",
    publisher = "Springer Science and Business Media LLC",
    issue = "1",
    issn = "2470-1963"
}

@article{reis2003grainrefinementand,
    author = "da Costa Reis, Ana Carmen and Bracke, Lieven and Petrov, Roumen and Kaluba, Wlodzimierz Jacek and Kestens, Leo",
    title = "Grain Refinement and Texture Change in Interstitial Free Steels after Severe Rolling and Ultra-short Annealing",
    year = "2003",
    journal = "ISIJ International",
    volume = "43",
    pages = "1260-1267",
    month = "Jan",
    doi = "10.2355/isijinternational.43.1260",
    url = "https://doi.org/10.2355/isijinternational.43.1260",
    publisher = "Iron and Steel Institute of Japan",
    issue = "8",
    issn = "0915-1559"
}

@article{gaggiotti2022ultrafastheatingheat,
    author = "Gaggiotti, Matteo and Albini, Luciano and Nunzio, Paolo Di and Schino, Andrea Di and Stornelli, Giulia and Tiracorrendo, Giulia",
    title = "Ultrafast Heating Heat Treatment Effect on the Microstructure and Properties of Steels",
    year = "2022",
    journal = "Metals",
    volume = "12",
    pages = "1313",
    month = "Aug",
    doi = "10.3390/met12081313",
    url = "https://doi.org/10.3390/met12081313",
    publisher = "MDPI AG",
    issue = "8",
    issn = "2075-4701"
}
```


*Code_block: This artifact provides the BibTeX entries for the main references used in the induction-heating annealing literature summary, making it easy to import the cited sources into a bibliography manager.*


References

1. (rapoport2006optimalcontrolof pages 44-47): Edgar Rapoport and Yulia Pleshivtseva. Optimal control of induction heating processes. ArXiv, Jul 2006. URL: https://doi.org/10.1201/9781420019490, doi:10.1201/9781420019490. This article has 292 citations.

2. (hammi2016studyoffrequency pages 3-5): Habib Hammi, Abderazzak El Ouafi, and Noureddine Barka. Study of frequency effects on hardness profile of spline shaft heat-treated by induction. Journal of Materials Science and Chemical Engineering, 4:1-9, Mar 2016. URL: https://doi.org/10.4236/msce.2016.43001, doi:10.4236/msce.2016.43001. This article has 10 citations.

3. (hatem2024simulationandimplementation pages 4-6): Sude Hatem. Simulation and implementation of an induction heating system for heating brittle thin metal sheets by various excitation current frequencies. Uluslararası Muhendislik Arastirma ve Gelistirme Dergisi, Jun 2024. URL: https://doi.org/10.29137/umagd.1439051, doi:10.29137/umagd.1439051. This article has 6 citations.

4. (rapoport2006optimalcontrolof pages 40-44): Edgar Rapoport and Yulia Pleshivtseva. Optimal control of induction heating processes. ArXiv, Jul 2006. URL: https://doi.org/10.1201/9781420019490, doi:10.1201/9781420019490. This article has 292 citations.

5. (cryderman2020effectsofrapid pages 1-2): Robert Cryderman, Dalton Garrett, Zachary Schlittenhart, and Eun Jung Seo. Effects of rapid induction heating on transformations in 0.6% c steels. Feb 2020. URL: https://doi.org/10.1007/s11665-020-04632-0, doi:10.1007/s11665-020-04632-0. This article has 15 citations and is from a peer-reviewed journal.

6. (yang2010simulationofsteel pages 1-2): B. J. Yang, A. Hattiangadi, W. Z. Li, G. F. Zhou, and T. Mcgreevy. Simulation of steel microstructure evolution during induction heating. Materials Science and Engineering A-structural Materials Properties Microstructure and Processing, 527:2978-2984, May 2010. URL: https://doi.org/10.1016/j.msea.2010.01.038, doi:10.1016/j.msea.2010.01.038. This article has 89 citations.

7. (yang2010simulationofsteel pages 5-6): B. J. Yang, A. Hattiangadi, W. Z. Li, G. F. Zhou, and T. Mcgreevy. Simulation of steel microstructure evolution during induction heating. Materials Science and Engineering A-structural Materials Properties Microstructure and Processing, 527:2978-2984, May 2010. URL: https://doi.org/10.1016/j.msea.2010.01.038, doi:10.1016/j.msea.2010.01.038. This article has 89 citations.

8. (rapoport2006optimalcontrolof pages 50-53): Edgar Rapoport and Yulia Pleshivtseva. Optimal control of induction heating processes. ArXiv, Jul 2006. URL: https://doi.org/10.1201/9781420019490, doi:10.1201/9781420019490. This article has 292 citations.

9. (muljono2001influenceofheating pages 1-2): D. Muljono, M. Ferry, and D. Dunne. Influence of heating rate on anisothermal recrystallization in low and ultra-low carbon steels. Materials Science and Engineering A-structural Materials Properties Microstructure and Processing, 303:90-99, May 2001. URL: https://doi.org/10.1016/s0921-5093(00)01882-7, doi:10.1016/s0921-5093(00)01882-7. This article has 106 citations.

10. (ferry2001recrystallizationkineticsof pages 1-2): M. Ferry, D. Muljono, and D. P. Dunne. Recrystallization kinetics of low and ultra low carbon steels during high-rate annealing. Isij International, 41:1053-1060, Sep 2001. URL: https://doi.org/10.2355/isijinternational.41.1053, doi:10.2355/isijinternational.41.1053. This article has 74 citations and is from a peer-reviewed journal.

11. (javaheri2019insightintothe pages 27-35): Vahid Javaheri, Satish Kolli, Bjørnar Grande, and David Porter. Insight into the induction hardening behavior of a new 0.40% c microalloyed steel: effects of initial microstructure and thermal cycles. Text, Jan 2019. URL: https://doi.org/10.48550/arxiv.1812.10663, doi:10.48550/arxiv.1812.10663. This article has 47 citations and is from a peer-reviewed journal.

12. (javaheri2019insightintothe pages 23-27): Vahid Javaheri, Satish Kolli, Bjørnar Grande, and David Porter. Insight into the induction hardening behavior of a new 0.40% c microalloyed steel: effects of initial microstructure and thermal cycles. Text, Jan 2019. URL: https://doi.org/10.48550/arxiv.1812.10663, doi:10.48550/arxiv.1812.10663. This article has 47 citations and is from a peer-reviewed journal.

13. (wang2011rapidheatingeffects pages 1-3): Jian Wang, Jun Li, Xinfeng Wang, Xiaochuan Mi, and Shengen Zhang. Rapid heating effects on grain-size, texture and magnetic properties of 3% si non-oriented electrical steel. Bulletin of Materials Science, 34:1477-1482, Dec 2011. URL: https://doi.org/10.1007/s12034-011-0346-3, doi:10.1007/s12034-011-0346-3. This article has 15 citations and is from a peer-reviewed journal.

14. (yonemura2019finemicrostructureformation pages 4-6): Mitsuharu Yonemura, Hitomi Nishibata, Tomohiro Nishiura, Natsumi Ooura, Yuki Yoshimoto, Kazuki Fujiwara, Kaori Kawano, Tomoyuki Terai, Yuichi Inubushi, Ichiro Inoue, Kensuke Tono, and Makina Yabashi. Fine microstructure formation in steel under ultrafast heating. Scientific Reports, Aug 2019. URL: https://doi.org/10.1038/s41598-019-47668-6, doi:10.1038/s41598-019-47668-6. This article has 27 citations and is from a peer-reviewed journal.

15. (dalaee2020experimentalandnumerical pages 18-23): Mohammad Taghi Dalaee, Lars Gloor, Christian Leinenbach, and Konrad Wegener. Experimental and numerical study of the influence of induction heating process on build rates induction heating-assisted laser direct metal deposition (ih-dmd). Surface and Coatings Technology, 384:125275, Feb 2020. URL: https://doi.org/10.1016/j.surfcoat.2019.125275, doi:10.1016/j.surfcoat.2019.125275. This article has 56 citations and is from a domain leading peer-reviewed journal.

16. (dalaee2020experimentalandnumerical pages 14-18): Mohammad Taghi Dalaee, Lars Gloor, Christian Leinenbach, and Konrad Wegener. Experimental and numerical study of the influence of induction heating process on build rates induction heating-assisted laser direct metal deposition (ih-dmd). Surface and Coatings Technology, 384:125275, Feb 2020. URL: https://doi.org/10.1016/j.surfcoat.2019.125275, doi:10.1016/j.surfcoat.2019.125275. This article has 56 citations and is from a domain leading peer-reviewed journal.

17. (usman2017inductiveweldof pages 16-21): M Usman. Inductive weld of joints for optical fiber pipe. Unknown journal, 2017.

18. (rapoport2006optimalcontrolof pages 47-50): Edgar Rapoport and Yulia Pleshivtseva. Optimal control of induction heating processes. ArXiv, Jul 2006. URL: https://doi.org/10.1201/9781420019490, doi:10.1201/9781420019490. This article has 292 citations.

19. (rapoport2006optimalcontrolof pages 22-25): Edgar Rapoport and Yulia Pleshivtseva. Optimal control of induction heating processes. ArXiv, Jul 2006. URL: https://doi.org/10.1201/9781420019490, doi:10.1201/9781420019490. This article has 292 citations.

20. (yang2010simulationofsteel pages 6-7): B. J. Yang, A. Hattiangadi, W. Z. Li, G. F. Zhou, and T. Mcgreevy. Simulation of steel microstructure evolution during induction heating. Materials Science and Engineering A-structural Materials Properties Microstructure and Processing, 527:2978-2984, May 2010. URL: https://doi.org/10.1016/j.msea.2010.01.038, doi:10.1016/j.msea.2010.01.038. This article has 89 citations.

21. (banis2019theeffectof pages 1-3): Alexandros Banis, Eliseo Hernandez Duran, Vitaliy Bliznuk, Ilchat Sabirov, Roumen H. Petrov, and Spyros Papaefthymiou. The effect of ultra-fast heating on the microstructure, grain size and texture evolution of a commercial low-c, medium-mn dp steel. Metals, 9:877, Aug 2019. URL: https://doi.org/10.3390/met9080877, doi:10.3390/met9080877. This article has 31 citations.

22. (xu2026designandoptimization pages 1-2): Yakun Xu, André Leonhardt, Peter Birnbaum, Jonas Gruner, Andreas Kunke, and Till Clausmeyer. Design and optimization of induction coil for improved temperature uniformity in fast heating of sheet metal. Discover Mechanical Engineering, Apr 2026. URL: https://doi.org/10.1007/s44245-026-00228-5, doi:10.1007/s44245-026-00228-5. This article has 1 citations and is from a peer-reviewed journal.

23. (xu2026designandoptimization pages 9-11): Yakun Xu, André Leonhardt, Peter Birnbaum, Jonas Gruner, Andreas Kunke, and Till Clausmeyer. Design and optimization of induction coil for improved temperature uniformity in fast heating of sheet metal. Discover Mechanical Engineering, Apr 2026. URL: https://doi.org/10.1007/s44245-026-00228-5, doi:10.1007/s44245-026-00228-5. This article has 1 citations and is from a peer-reviewed journal.

24. (xu2026designandoptimization pages 5-9): Yakun Xu, André Leonhardt, Peter Birnbaum, Jonas Gruner, Andreas Kunke, and Till Clausmeyer. Design and optimization of induction coil for improved temperature uniformity in fast heating of sheet metal. Discover Mechanical Engineering, Apr 2026. URL: https://doi.org/10.1007/s44245-026-00228-5, doi:10.1007/s44245-026-00228-5. This article has 1 citations and is from a peer-reviewed journal.

25. (xu2026designandoptimization pages 2-5): Yakun Xu, André Leonhardt, Peter Birnbaum, Jonas Gruner, Andreas Kunke, and Till Clausmeyer. Design and optimization of induction coil for improved temperature uniformity in fast heating of sheet metal. Discover Mechanical Engineering, Apr 2026. URL: https://doi.org/10.1007/s44245-026-00228-5, doi:10.1007/s44245-026-00228-5. This article has 1 citations and is from a peer-reviewed journal.

26. (muljono2001influenceofheating pages 5-7): D. Muljono, M. Ferry, and D. Dunne. Influence of heating rate on anisothermal recrystallization in low and ultra-low carbon steels. Materials Science and Engineering A-structural Materials Properties Microstructure and Processing, 303:90-99, May 2001. URL: https://doi.org/10.1016/s0921-5093(00)01882-7, doi:10.1016/s0921-5093(00)01882-7. This article has 106 citations.

27. (yonemura2019finemicrostructureformation pages 6-7): Mitsuharu Yonemura, Hitomi Nishibata, Tomohiro Nishiura, Natsumi Ooura, Yuki Yoshimoto, Kazuki Fujiwara, Kaori Kawano, Tomoyuki Terai, Yuichi Inubushi, Ichiro Inoue, Kensuke Tono, and Makina Yabashi. Fine microstructure formation in steel under ultrafast heating. Scientific Reports, Aug 2019. URL: https://doi.org/10.1038/s41598-019-47668-6, doi:10.1038/s41598-019-47668-6. This article has 27 citations and is from a peer-reviewed journal.

28. (cerda2016theeffectof pages 12-13): Felipe Castro Cerda, Leo Kestens, Alberto Monsalve, and Roumen Petrov. The effect of ultrafast heating in cold-rolled low carbon steel: recrystallization and texture evolution. ArXiv, 6:288, Nov 2016. URL: https://doi.org/10.3390/met6110288, doi:10.3390/met6110288. This article has 34 citations.

29. (cerda2016theeffectof pages 1-3): Felipe Castro Cerda, Leo Kestens, Alberto Monsalve, and Roumen Petrov. The effect of ultrafast heating in cold-rolled low carbon steel: recrystallization and texture evolution. ArXiv, 6:288, Nov 2016. URL: https://doi.org/10.3390/met6110288, doi:10.3390/met6110288. This article has 34 citations.

30. (reis2003grainrefinementand pages 1-2): Ana Carmen da Costa Reis, Lieven Bracke, Roumen Petrov, Wlodzimierz Jacek Kaluba, and Leo Kestens. Grain refinement and texture change in interstitial free steels after severe rolling and ultra-short annealing. ISIJ International, 43:1260-1267, Jan 2003. URL: https://doi.org/10.2355/isijinternational.43.1260, doi:10.2355/isijinternational.43.1260. This article has 41 citations and is from a peer-reviewed journal.

31. (bodyako1962recrystallizationdiagramsfor pages 3-3): M. N. Bodyako, Yu. M. Loiko, B. L. Pavlyukevich, and V. I. Parkhimovich. Recrystallization diagrams for induction heating. Metal Science and Heat Treatment of Metals, 2:57-59, Jan 1962. URL: https://doi.org/10.1007/bf00655595, doi:10.1007/bf00655595. This article has 3 citations.

32. (yang2010simulationofsteel pages 2-3): B. J. Yang, A. Hattiangadi, W. Z. Li, G. F. Zhou, and T. Mcgreevy. Simulation of steel microstructure evolution during induction heating. Materials Science and Engineering A-structural Materials Properties Microstructure and Processing, 527:2978-2984, May 2010. URL: https://doi.org/10.1016/j.msea.2010.01.038, doi:10.1016/j.msea.2010.01.038. This article has 89 citations.

33. (javaheri2019insightintothe pages 19-23): Vahid Javaheri, Satish Kolli, Bjørnar Grande, and David Porter. Insight into the induction hardening behavior of a new 0.40% c microalloyed steel: effects of initial microstructure and thermal cycles. Text, Jan 2019. URL: https://doi.org/10.48550/arxiv.1812.10663, doi:10.48550/arxiv.1812.10663. This article has 47 citations and is from a peer-reviewed journal.

34. (javaheri2019insightintothe pages 14-19): Vahid Javaheri, Satish Kolli, Bjørnar Grande, and David Porter. Insight into the induction hardening behavior of a new 0.40% c microalloyed steel: effects of initial microstructure and thermal cycles. Text, Jan 2019. URL: https://doi.org/10.48550/arxiv.1812.10663, doi:10.48550/arxiv.1812.10663. This article has 47 citations and is from a peer-reviewed journal.