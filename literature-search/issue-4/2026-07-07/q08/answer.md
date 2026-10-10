Question: Review literature on low-cost, open-source, or custom-built laboratory high-temperature furnaces and instrument retrofits/modernizations: computer/DAQ-based (e.g., LabVIEW) analog power control of induction or resistance furnaces, closed-loop PID temperature control using non-contact (pyrometer) feedback, vacuum or controlled-atmosphere chamber integration, and open-source-hardware approaches to scientific furnace construction, validation, and publication. Cite high-quality sources with bibtex.

# Literature Review: Low-Cost, Open-Source, and Custom-Built Laboratory High-Temperature Furnaces — Computer-Based Control, Pyrometric Feedback, Vacuum Integration, and Open-Source Hardware Approaches

## 1. Introduction

The design, construction, and modernization of high-temperature laboratory furnaces is a multidisciplinary endeavor intersecting materials science, instrumentation engineering, and the growing open-source hardware movement. Researchers seeking to build, retrofit, or publish custom furnace systems must draw on literature spanning custom furnace engineering, computer-based data acquisition and power control, non-contact temperature sensing (pyrometry), vacuum/controlled-atmosphere chamber design, and the principles of free and open-source hardware (FOSH) for scientific equipment. This review synthesizes the relevant literature across these domains.

The following table summarizes the key sources reviewed and their topical contributions.

| Reference (Author, Year) | Topic Area | Key Contribution | Journal |
|---|---|---|---|
| Niedziela et al., 2017 | Custom Furnace Design; Vacuum Integration; PID Control | Describes a custom-built high-temperature vacuum furnace for neutron scattering with integrated vacuum hardware, active cooling, interlocks, remote computer control, programmable/dynamic PID control, and power limiting; useful as a detailed model of laboratory furnace engineering and validation. (niedziela2017designandoperating pages 7-8, niedziela2017designandoperating pages 1-3, niedziela2017designandoperating pages 5-7) | *Review of Scientific Instruments* |
| Oberloier & Pearce, 2017 | FOSH Principles; Scientific Instrument Construction | Formalizes a five-step free/open-source hardware design procedure for scientific equipment, emphasizing open CAD, minimization of complexity/cost, validation, thorough documentation, and public sharing; highly relevant as a methodological template for publishing custom furnace builds. (oberloier2017generaldesignprocedure pages 1-3, oberloier2017generaldesignprocedure pages 11-13) | *Designs* |
| Wenzel, 2023 | Open Hardware; Access to Laboratory Equipment | Synthesizes how open hardware transforms access to laboratory instruments through local fabrication, adaptability, and knowledge transfer; frames DIY/custom instruments as “appropriate technology” rather than merely cheap substitutes. (wenzel2023openhardwarefrom pages 5-9, wenzel2023openhardwarefrom pages 9-13, wenzel2023openhardwarefrom pages 13-17, wenzel2023openhardwarefrom pages 20-25) | *PLOS Biology* |
| Pearce, 2020 | FOSH Economics; Validation/Adoption Case for Open Instruments | Reviews evidence that scientific FOSH commonly reduces costs dramatically while improving customization, maintainability, and resistance to vendor lock-in; supports the economic rationale for open or custom furnace control and retrofit projects. (pearce2020economicsavingsfor pages 12-13, pearce2020economicsavingsfor pages 13-14) | *HardwareX* |
| Baden et al., 2015 | Open Labware; 3D-Printed Scientific Equipment | Landmark review of open labware showing how 3D printing plus low-cost electronics enables rapid, local, customizable fabrication of scientific equipment; conceptually important for open furnace accessories, enclosures, mounts, and control interfaces. (baden2015openlabware3d pages 1-3, baden2015openlabware3d pages 3-4, baden2015openlabware3d pages 4-7) | *PLOS Biology* |
| McDermott et al., 2024 | Instrument Retrofit; Legacy Equipment Modernization | Presents LabThings Retro, an open-source framework for retrofitting older instruments with modern web-based control, networking, and closed-loop automation; directly relevant to furnace/control modernization where existing heaters or controllers are upgraded rather than replaced. (mcdermott2024usingoldlaboratorya pages 4-5, mcdermott2024usingoldlaboratory pages 1-2, mcdermott2024usingoldlaboratory pages 7-9, mcdermott2024usingoldlaboratorya pages 1-2, mcdermott2024usingoldlaboratory pages 9-10, mcdermott2024usingoldlaboratory pages 2-4, mcdermott2024usingoldlaboratorya pages 5-6, mcdermott2024usingoldlaboratorya pages 2-3) | *Royal Society Open Science* |
| Grujić, 2023 | Pyrometry; Thermal Spectral Imaging; Non-Contact Sensing | Reviews radiation thermometry and thermal spectral imaging for extreme-temperature process monitoring, emphasizing emissivity uncertainty, detector selection, blackbody calibration, and multispectral approaches; highly relevant to pyrometer-based furnace feedback design. (grujic2023areviewof pages 2-4, grujic2023areviewof pages 6-8, grujic2023areviewof pages 16-18, grujic2023areviewof pages 26-27, grujic2023areviewof pages 14-16, grujic2023areviewof pages 1-2) | *Sensors* |
| Usamentiaga et al., 2014 | Infrared Thermography; Temperature Measurement Review | Comprehensive review of infrared thermography for temperature measurement, covering Planck/Wien/Stefan-Boltzmann relations, emissivity, reflected radiation, atmospheric effects, calibration, and multi-wavelength pyrometry; foundational for designing reliable non-contact furnace feedback loops. (usamentiaga2014infraredthermographyfor pages 10-13, usamentiaga2014infraredthermographyfor pages 5-8, usamentiaga2014infraredthermographyfor pages 3-5, usamentiaga2014infraredthermographyfor pages 8-10) | *Sensors* |
| Giulietti et al., 2025 | Spectral Emissivity; High-Temperature Measurement | Systematic review of emissivity measurement methods for high-temperature applications, including direct/indirect radiometric approaches, uncertainty sources, and vacuum-assisted measurement strategies; important for validating pyrometer accuracy in furnace systems. (giulietti2025spectralemissivitymeasurement pages 11-12, giulietti2025spectralemissivitymeasurement pages 9-10, giulietti2025spectralemissivitymeasurement pages 10-11) | *Acta IMEKO* |
| Liu et al., 2022 | Surface Thermometry Methods; Combustion/High-Temperature Sensing | Compares contact and non-contact surface thermometry methods, with clear discussion of radiation thermometry, detector classes, spectral sensitivity, and suitability for harsh high-temperature environments; useful for choosing between thermocouples and pyrometers in furnace control. (liu2022reviewofdevelopment pages 12-13, liu2022reviewofdevelopment pages 11-12) | *Processes* |
| Doloi et al., 2025 | Open-Source Automation; Low-Cost Scientific Hardware | Reviews how low-cost 3D printing, Arduino/Raspberry Pi integration, and open-source design democratize laboratory automation and self-driving labs; useful for envisioning open, modular furnace DAQ/control ecosystems and publishable low-cost implementations. (doloi2025democratizingselfdrivinglabs pages 1-2, doloi2025democratizingselfdrivinglabs pages 3-4, doloi2025democratizingselfdrivinglabs pages 8-9) | *Digital Discovery* |


*Table: This table organizes the most relevant reviewed sources by topic area, highlighting how each contributes to custom furnace design, control, pyrometry, retrofit, or open-hardware methodology. It is useful as a quick map of the literature and as a guide for selecting sources to support design, validation, and publication of modernized laboratory furnace systems.*

## 2. Custom-Built High-Temperature Furnace Design and Validation

A thorough exemplar of custom-built laboratory furnace engineering is provided by Niedziela et al. (2017), who describe the design, construction, and characterization of the MICAS vacuum furnace at Oak Ridge National Laboratory's Spallation Neutron Source. This actively water-cooled radiant heating furnace achieves temperatures up to 1873 K and was developed specifically for time-of-flight inelastic neutron scattering experiments (niedziela2017designandoperating pages 1-3). The authors document the full development process—from design rationale, through operational characteristics, to performance comparisons with commercially available furnaces—providing a valuable template for researchers seeking to publish custom furnace builds in the peer-reviewed literature (niedziela2017designandoperating pages 1-3).

The MICAS furnace control system features a custom-designed control rack containing a DC power supply, temperature controller, over-temperature sensor, turbo pump controller, and vacuum gauges with integrated latching interlocks that monitor pressure, chilled water supply, and unit temperature (niedziela2017designandoperating pages 5-7). Temperature monitoring employs commercially available type-K thermocouples (below 1573 K) and type-C thermocouples at higher temperatures, with the system supporting temperature ramping capabilities across its full operating range (niedziela2017designandoperating pages 5-7).

## 3. Computer/DAQ-Based Power Control and PID Temperature Regulation

The MICAS furnace illustrates state-of-the-art computer-based control integration: its control application is integrated into the SNS instrument data acquisition and control system for remote operation (niedziela2017designandoperating pages 7-8). The system implements proportional-integral-derivative (PID) technology for the control loop, with a key innovation being dynamically switchable PID parameters based on operating temperature range, enabling precise control across different thermal regimes. PID tables can be programmed offline or adjusted in situ to enhance stability for specific experimental samples (niedziela2017designandoperating pages 7-8). The power supply includes a power-limiting feature typically set at 70% of maximum output (adjustable for extreme cases), and an integrated alarm system alerts staff to over-temperature trips, enabling rapid fault response (niedziela2017designandoperating pages 7-8). An emergency stop mechanism rapidly cuts power to heating elements when triggered (niedziela2017designandoperating pages 5-7).

More broadly, LabVIEW-based virtual instrument approaches to furnace temperature control have been explored in the applied engineering literature, including fuzzy-PID hybrid controllers for resistance furnaces and LabVIEW-interfaced assembly-line heating furnace control systems, though full-text access to many of these conference proceedings was limited during this review.

## 4. Non-Contact Temperature Measurement: Pyrometry and Infrared Thermography

For high-temperature furnace applications—particularly those involving induction heating, vacuum operation, or environments hostile to contact sensors—non-contact pyrometric feedback is essential. Several comprehensive reviews address the principles, challenges, and practical implementation of radiation thermometry.

Usamentiaga et al. (2014) provide a foundational and highly cited review of infrared thermography for temperature measurement. They describe how total infrared radiation received by a sensor comprises three components: object emission, reflected radiation from surroundings, and atmospheric emission, each requiring compensation for accurate temperature determination (usamentiaga2014infraredthermographyfor pages 10-13). The fundamental physics is grounded in Planck's law, Wien's displacement law, and the Stefan-Boltzmann relation (W = ε·σ·T⁴), with emissivity ε defined as the ratio of actual radiant energy to that of an ideal blackbody at the same temperature (usamentiaga2014infraredthermographyfor pages 5-8). The most commonly used infrared bands for temperature measurement are the mid-wavelength infrared (MWIR, 2–5 µm, preferred for high-temperature readings) and long-wavelength infrared (LWIR, 8–14 µm, preferred for ambient-range temperatures), selected to match atmospheric transmittance windows and peak emission wavelengths (usamentiaga2014infraredthermographyfor pages 8-10).

Grujić (2023) reviews radiation thermometry specifically for high-temperature molten material monitoring, detailing how commercial pyrometers use direct-reading calibration algorithms based on blackbody references and how different detector types—thermal detectors (e.g., bolometers, ~10–15 ms response) versus wavelength-sensitive photodetectors (microsecond response)—are selected based on the target application (grujic2023areviewof pages 2-4). A critical challenge in pyrometric furnace control is emissivity uncertainty: spectral emissivity varies with material composition, surface roughness, oxidation state, temperature, wavelength, and viewing geometry (grujic2023areviewof pages 6-8). To mitigate emissivity effects, techniques include creating mechanical cavities that approximate blackbody conditions, employing two-wavelength (ratio) radiation thermometry to eliminate unknown emissivity in graybody assumptions, and using purged sighting tubes to reduce atmospheric interference (grujic2023areviewof pages 6-8).

Liu et al. (2022) compare contact and non-contact surface thermometry methods, identifying three main radiation detector classes: disappearing-filament optical pyrometers (commercial accuracy ±61 °C at 775 °C), thermal detectors (bolometers, thermopiles, pyroelectric sensors), and quantum detectors (higher spectral detectivity, faster response) (liu2022reviewofdevelopment pages 12-13). They note that non-contact techniques are indispensable for high-temperature or chemically reactive environments where contact sensors would degrade (liu2022reviewofdevelopment pages 11-12).

Giulietti et al. (2025) provide a systematic review of spectral emissivity measurement at temperatures up to 2500 °C, covering both direct and indirect radiometric approaches and discussing uncertainties, vacuum-chamber-assisted measurement strategies (achieving uncertainties below 1%), and the important distinction between approaches suitable for low-emissivity versus high-emissivity materials (giulietti2025spectralemissivitymeasurement pages 9-10, giulietti2025spectralemissivitymeasurement pages 11-12). For molten metals, surface oxides evaporate near melting temperatures, creating specular surfaces that reflect surrounding radiation to the pyrometer; the modified Hagen-Rubens relationship can be used to estimate normal spectral emissivity if electrical resistivity data are available (grujic2023areviewof pages 16-18, grujic2023areviewof pages 14-16).

These reviews collectively indicate that closed-loop PID temperature control using pyrometer feedback in custom furnaces requires careful attention to emissivity characterization, blackbody calibration, detector selection matched to the temperature range, and compensation for reflected and atmospheric radiation.

## 5. Vacuum and Controlled-Atmosphere Chamber Integration

The integration of vacuum or controlled-atmosphere enclosures with laboratory furnaces is essential for high-temperature materials processing, crystal growth, and experiments sensitive to oxidation. The MICAS furnace described by Niedziela et al. (2017) exemplifies this integration, requiring vacuum pressures of approximately 10⁻⁴ Torr during operation, with a turbo pump controller and vacuum gauges incorporated directly into the control rack and linked to the safety interlock system (niedziela2017designandoperating pages 5-7). Active water cooling maintains outer wall temperatures near room temperature despite internal temperatures up to 1873 K (niedziela2017designandoperating pages 7-8). The temperature control system was tested and validated across a range of 540–1700 K with linear dependence on control temperature (niedziela2017designandoperating pages 7-8).

These design strategies—vacuum-rated chambers, active cooling, interlocked safety systems, and computer-monitored vacuum gauges—represent best practices that can be adapted to custom or retrofitted furnace systems at varying budget levels.

## 6. Open-Source Hardware for Scientific Instruments: Principles, Economics, and Design Methodology

The broader movement toward free and open-source hardware (FOSH) for scientific equipment provides a strong conceptual and practical foundation for publishing custom furnace designs. Oberloier and Pearce (2017) formalize a five-step design procedure for FOSH scientific equipment: (1) evaluate existing tools and proof of concepts, (2) design using open-source software while minimizing parts, complexity, and cost, maximizing digital manufacturing compatibility, creating parametric designs, and using readily available off-the-shelf components, (3) validate the design, (4) thoroughly document all aspects including source CAD files, and (5) share documentation openly (oberloier2017generaldesignprocedure pages 1-3). This procedure, when applied to furnace construction, ensures that custom designs are reproducible, customizable, and publishable. Their case study demonstrates cost reductions exceeding 300× compared to commercial alternatives (oberloier2017generaldesignprocedure pages 11-13).

Pearce (2020) reviews the economic evidence for FOSH in science, finding that open-source scientific hardware commonly reduces costs by 87% or more compared to proprietary equivalents, with specific examples including optics lab setups fabricated for $500 replacing $15,000 commercial equipment (pearce2020economicsavingsfor pages 13-14). Beyond direct savings, FOSH eliminates vendor lock-in, enables flexible budget reallocation during multi-year grants, and fosters collaborative innovation through share-alike licensing (pearce2020economicsavingsfor pages 12-13, pearce2020economicsavingsfor pages 13-14).

Wenzel (2023), writing in *PLOS Biology*, examines the global spread of open hardware and argues that DIY laboratory instruments should be understood as "appropriate technology"—designs compatible with local economic and infrastructural conditions—rather than simply cheap substitutes (wenzel2023openhardwarefrom pages 13-17). Local production via 3D printing and CNC workshops enables faster design turnaround and customization without reliance on expensive international logistics (wenzel2023openhardwarefrom pages 5-9). Wenzel categorizes ten types of open hardware with varying characteristics across local fabrication suitability, adaptability, cost, and accessibility, and recommends institutional policies that incentivize the release of custom designs created by departmental workshops (wenzel2023openhardwarefrom pages 9-13, wenzel2023openhardwarefrom pages 20-25).

Baden et al. (2015), in a landmark *PLOS Biology* article, demonstrate how affordable consumer 3D printers combined with open-source blueprints and off-the-shelf electronics (Arduino, Raspberry Pi) enable scientists to build sophisticated laboratory equipment—from micropipettes to thermocyclers to two-photon microscopes—at a fraction of commercial costs (baden2015openlabware3d pages 1-3). Their survey of open labware projects spans microscopy, molecular biology, electrophysiology, and other domains, with designs shared under open-source licenses through online repositories and peer-reviewed journals (baden2015openlabware3d pages 3-4, baden2015openlabware3d pages 4-7).

Doloi et al. (2025) review how low-cost fused deposition modeling (FDM) 3D printing, combined with Arduino and Raspberry Pi platforms, is democratizing laboratory automation by enabling creation of liquid handlers, robotic arms, imaging systems, and chemical reactionware at costs far below commercial alternatives ($10,000–$60,000 for commercial liquid handlers versus under $1,000 for open-source equivalents) (doloi2025democratizingselfdrivinglabs pages 1-2, doloi2025democratizingselfdrivinglabs pages 3-4, doloi2025democratizingselfdrivinglabs pages 8-9). These approaches are directly transferable to the design and publication of open furnace control interfaces, enclosures, and accessory hardware.

## 7. Instrument Retrofits and Modernization

For laboratories seeking to modernize existing furnaces or integrate legacy equipment into computer-controlled workflows, McDermott et al. (2024) present LabThings Retro, an open-source framework for retrofitting older laboratory instruments with modern Web-of-Things (WoT) standards (mcdermott2024usingoldlaboratory pages 1-2). The system uses ESP32-based microcontrollers with integrated WiFi and relay switches to control legacy devices, supporting both simple on/off actuation (e.g., heaters, stirrers) and complex serial communication with instruments using RS232/RS485 protocols (mcdermott2024usingoldlaboratorya pages 2-3). Their framework enables laboratories to reuse existing equipment in modern automated experimental pipelines—including closed-loop feedback control—without full replacement, thereby reducing cost, e-waste, and training overhead (mcdermott2024usingoldlaboratory pages 2-4). LabThings Retro demonstrates that furnace controller modernization need not require wholesale equipment replacement; instead, low-cost microcontroller-based intermediaries can bridge legacy hardware and modern DAQ/automation software (mcdermott2024usingoldlaboratorya pages 1-2, mcdermott2024usingoldlaboratorya pages 4-5).

## 8. Synthesis and Gaps

This review reveals that while high-quality published examples of custom furnace design with integrated computer control, PID regulation, vacuum integration, and detailed validation exist (most notably Niedziela et al., 2017), there remains a notable gap in the literature specifically addressing the publication of fully open-source, low-cost, high-temperature laboratory furnaces following FOSH best practices. The FOSH design methodology (Oberloier and Pearce, 2017), economic justification (Pearce, 2020), and retrofit frameworks (McDermott et al., 2024) are well developed, and the pyrometry and infrared thermography literature (Usamentiaga et al., 2014; Grujić, 2023; Giulietti et al., 2025; Liu et al., 2022) provides thorough guidance on implementing non-contact temperature feedback. However, a peer-reviewed, fully documented open-source high-temperature furnace project combining all these elements—analog/digital power control with DAQ integration, pyrometer-based closed-loop PID feedback, vacuum or controlled-atmosphere operation, open CAD files, and validation data—represents an important opportunity for contribution to the scientific literature.

## 9. BibTeX References

The complete bibliography in BibTeX format is provided below for direct use in manuscript preparation.

```bibtex
@article{niedziela2017designandoperating,
  author    = {Niedziela, J. L. and Mills, R. and Loguillo, M. J. and Skorpenske, H. D. and Armitage, D. and Smith, H. L. and Lin, J. Y. Y. and Lucas, M. S. and Stone, M. B. and Abernathy, D. L.},
  title     = {Design and operating characteristic of a vacuum furnace for time-of-flight inelastic neutron scattering measurements},
  journal   = {Review of Scientific Instruments},
  year      = {2017},
  volume    = {88},
  number    = {10},
  pages     = {105116},
  month     = oct,
  doi       = {10.1063/1.5007089},
  url       = {https://doi.org/10.1063/1.5007089}
}

@article{oberloier2017generaldesignprocedure,
  author    = {Oberloier, Shane and Pearce, Joshua M.},
  title     = {General Design Procedure for Free and Open-Source Hardware for Scientific Equipment},
  journal   = {Designs},
  year      = {2017},
  volume    = {2},
  number    = {1},
  pages     = {2},
  month     = dec,
  doi       = {10.3390/designs2010002},
  url       = {https://doi.org/10.3390/designs2010002}
}

@article{wenzel2023openhardwarefrom,
  author    = {Wenzel, Tobias},
  title     = {Open hardware: From DIY trend to global transformation in access to laboratory equipment},
  journal   = {PLOS Biology},
  year      = {2023},
  volume    = {21},
  number    = {1},
  pages     = {e3001931},
  month     = jan,
  doi       = {10.1371/journal.pbio.3001931},
  url       = {https://doi.org/10.1371/journal.pbio.3001931}
}

@article{pearce2020economicsavingsfor,
  author    = {Pearce, Joshua M.},
  title     = {Economic savings for scientific free and open source technology: A review},
  journal   = {HardwareX},
  year      = {2020},
  volume    = {8},
  pages     = {e00139},
  month     = oct,
  doi       = {10.1016/j.ohx.2020.e00139},
  url       = {https://doi.org/10.1016/j.ohx.2020.e00139}
}

@article{baden2015openlabware3d,
  author    = {Baden, Tom and Chagas, Andre Maia and Gage, Greg and Marzullo, Timothy and Prieto-Godino, Lucia L. and Euler, Thomas},
  title     = {Open Labware: 3-D Printing Your Own Lab Equipment},
  journal   = {PLOS Biology},
  year      = {2015},
  volume    = {13},
  number    = {3},
  pages     = {e1002086},
  month     = mar,
  doi       = {10.1371/journal.pbio.1002086},
  url       = {https://doi.org/10.1371/journal.pbio.1002086}
}

@article{mcdermott2024usingoldlaboratory,
  author    = {McDermott, Samuel and Kotar, Jurij and Collins, Joel and Mancini, Leonardo and Bowman, Richard and Cicuta, Pietro},
  title     = {Using old laboratory equipment with modern Web-of-Things standards: a smart laboratory with LabThings Retro},
  journal   = {Royal Society Open Science},
  year      = {2024},
  volume    = {11},
  number    = {8},
  month     = aug,
  doi       = {10.1098/rsos.240634},
  url       = {https://doi.org/10.1098/rsos.240634}
}

@article{grujic2023areviewof,
  author    = {Gruji{\'c}, Katarina},
  title     = {A Review of Thermal Spectral Imaging Methods for Monitoring High-Temperature Molten Material Streams},
  journal   = {Sensors},
  year      = {2023},
  volume    = {23},
  number    = {3},
  pages     = {1130},
  month     = jan,
  doi       = {10.3390/s23031130},
  url       = {https://doi.org/10.3390/s23031130}
}

@article{usamentiaga2014infraredthermographyfor,
  author    = {Usamentiaga, Rub{\'e}n and Venegas, Pablo and Guerediaga, Jon and Vega, Laura and Molleda, Julio and Bulnes, Francisco},
  title     = {Infrared Thermography for Temperature Measurement and Non-Destructive Testing},
  journal   = {Sensors},
  year      = {2014},
  volume    = {14},
  number    = {7},
  pages     = {12305--12348},
  month     = jul,
  doi       = {10.3390/s140712305},
  url       = {https://doi.org/10.3390/s140712305}
}

@article{giulietti2025spectralemissivitymeasurement,
  author    = {Giulietti, Nicola and Cosoli, Gloria and Napolitano, Rachele and Pandarese, Giuseppe and Revel, Gian Marco and Chiariotti, Paolo},
  title     = {Spectral emissivity measurement for high-temperature applications: a systematic review},
  journal   = {Acta IMEKO},
  year      = {2025},
  volume    = {14},
  number    = {1},
  pages     = {1--17},
  month     = mar,
  doi       = {10.21014/actaimeko.v14i1.1846},
  url       = {https://doi.org/10.21014/actaimeko.v14i1.1846}
}

@article{liu2022reviewofdevelopment,
  author    = {Liu, Siyu and Huang, Yu and He, Yong and Zhu, Yanqun and Wang, Zhihua},
  title     = {Review of Development and Comparison of Surface Thermometry Methods in Combustion Environments: Principles, Current State of the Art, and Applications},
  journal   = {Processes},
  year      = {2022},
  volume    = {10},
  number    = {12},
  pages     = {2528},
  month     = nov,
  doi       = {10.3390/pr10122528},
  url       = {https://doi.org/10.3390/pr10122528}
}

@article{doloi2025democratizingselfdrivinglabs,
  author    = {Doloi, Sayan and Das, Maloy and Li, Yujia and Cho, Zen Han and Xiao, Xingchi and Hanna, John V. and Osvaldo, Matthew and Tat, Leonard Ng Wei},
  title     = {Democratizing Self-Driving Labs: Advances in Low-Cost 3D Printing for Laboratory Automation},
  journal   = {Digital Discovery},
  year      = {2025},
  volume    = {4},
  number    = {7},
  pages     = {1685--1721},
  month     = jan,
  doi       = {10.1039/d4dd00411f},
  url       = {https://doi.org/10.1039/d4dd00411f}
}
```


*Code_block: This BibTeX block compiles the core sources used in the review, covering custom furnace design, open-source hardware methodology, instrument retrofits, and non-contact temperature measurement. It is useful as a ready-to-import bibliography for manuscript drafting or literature management.*


References

1. (niedziela2017designandoperating pages 7-8): J. L. Niedziela, R. Mills, M. J. Loguillo, H. D. Skorpenske, D. Armitage, H. L. Smith, J. Y. Y. Lin, M. S. Lucas, M. B. Stone, and D. L. Abernathy. Design and operating characteristic of a vacuum furnace for time-of-flight inelastic neutron scattering measurements. The Review of scientific instruments, 88 10:105116, Oct 2017. URL: https://doi.org/10.1063/1.5007089, doi:10.1063/1.5007089. This article has 28 citations.

2. (niedziela2017designandoperating pages 1-3): J. L. Niedziela, R. Mills, M. J. Loguillo, H. D. Skorpenske, D. Armitage, H. L. Smith, J. Y. Y. Lin, M. S. Lucas, M. B. Stone, and D. L. Abernathy. Design and operating characteristic of a vacuum furnace for time-of-flight inelastic neutron scattering measurements. The Review of scientific instruments, 88 10:105116, Oct 2017. URL: https://doi.org/10.1063/1.5007089, doi:10.1063/1.5007089. This article has 28 citations.

3. (niedziela2017designandoperating pages 5-7): J. L. Niedziela, R. Mills, M. J. Loguillo, H. D. Skorpenske, D. Armitage, H. L. Smith, J. Y. Y. Lin, M. S. Lucas, M. B. Stone, and D. L. Abernathy. Design and operating characteristic of a vacuum furnace for time-of-flight inelastic neutron scattering measurements. The Review of scientific instruments, 88 10:105116, Oct 2017. URL: https://doi.org/10.1063/1.5007089, doi:10.1063/1.5007089. This article has 28 citations.

4. (oberloier2017generaldesignprocedure pages 1-3): Shane Oberloier and Joshua Pearce. General design procedure for free and open-source hardware for scientific equipment. ArXiv, 2:2, Dec 2017. URL: https://doi.org/10.3390/designs2010002, doi:10.3390/designs2010002. This article has 141 citations.

5. (oberloier2017generaldesignprocedure pages 11-13): Shane Oberloier and Joshua Pearce. General design procedure for free and open-source hardware for scientific equipment. ArXiv, 2:2, Dec 2017. URL: https://doi.org/10.3390/designs2010002, doi:10.3390/designs2010002. This article has 141 citations.

6. (wenzel2023openhardwarefrom pages 5-9): Tobias Wenzel. Open hardware: from diy trend to global transformation in access to laboratory equipment. PLOS Biology, 21:e3001931, Jan 2023. URL: https://doi.org/10.1371/journal.pbio.3001931, doi:10.1371/journal.pbio.3001931. This article has 104 citations and is from a highest quality peer-reviewed journal.

7. (wenzel2023openhardwarefrom pages 9-13): Tobias Wenzel. Open hardware: from diy trend to global transformation in access to laboratory equipment. PLOS Biology, 21:e3001931, Jan 2023. URL: https://doi.org/10.1371/journal.pbio.3001931, doi:10.1371/journal.pbio.3001931. This article has 104 citations and is from a highest quality peer-reviewed journal.

8. (wenzel2023openhardwarefrom pages 13-17): Tobias Wenzel. Open hardware: from diy trend to global transformation in access to laboratory equipment. PLOS Biology, 21:e3001931, Jan 2023. URL: https://doi.org/10.1371/journal.pbio.3001931, doi:10.1371/journal.pbio.3001931. This article has 104 citations and is from a highest quality peer-reviewed journal.

9. (wenzel2023openhardwarefrom pages 20-25): Tobias Wenzel. Open hardware: from diy trend to global transformation in access to laboratory equipment. PLOS Biology, 21:e3001931, Jan 2023. URL: https://doi.org/10.1371/journal.pbio.3001931, doi:10.1371/journal.pbio.3001931. This article has 104 citations and is from a highest quality peer-reviewed journal.

10. (pearce2020economicsavingsfor pages 12-13): Joshua M. Pearce. Economic savings for scientific free and open source technology: a review. HardwareX, 8:e00139, Oct 2020. URL: https://doi.org/10.1016/j.ohx.2020.e00139, doi:10.1016/j.ohx.2020.e00139. This article has 182 citations and is from a peer-reviewed journal.

11. (pearce2020economicsavingsfor pages 13-14): Joshua M. Pearce. Economic savings for scientific free and open source technology: a review. HardwareX, 8:e00139, Oct 2020. URL: https://doi.org/10.1016/j.ohx.2020.e00139, doi:10.1016/j.ohx.2020.e00139. This article has 182 citations and is from a peer-reviewed journal.

12. (baden2015openlabware3d pages 1-3): Tom Baden, Andre Maia Chagas, Greg Gage, Timothy Marzullo, Lucia L. Prieto-Godino, and Thomas Euler. Open labware: 3-d printing your own lab equipment. PLOS Biology, 13:e1002086, Mar 2015. URL: https://doi.org/10.1371/journal.pbio.1002086, doi:10.1371/journal.pbio.1002086. This article has 421 citations and is from a highest quality peer-reviewed journal.

13. (baden2015openlabware3d pages 3-4): Tom Baden, Andre Maia Chagas, Greg Gage, Timothy Marzullo, Lucia L. Prieto-Godino, and Thomas Euler. Open labware: 3-d printing your own lab equipment. PLOS Biology, 13:e1002086, Mar 2015. URL: https://doi.org/10.1371/journal.pbio.1002086, doi:10.1371/journal.pbio.1002086. This article has 421 citations and is from a highest quality peer-reviewed journal.

14. (baden2015openlabware3d pages 4-7): Tom Baden, Andre Maia Chagas, Greg Gage, Timothy Marzullo, Lucia L. Prieto-Godino, and Thomas Euler. Open labware: 3-d printing your own lab equipment. PLOS Biology, 13:e1002086, Mar 2015. URL: https://doi.org/10.1371/journal.pbio.1002086, doi:10.1371/journal.pbio.1002086. This article has 421 citations and is from a highest quality peer-reviewed journal.

15. (mcdermott2024usingoldlaboratorya pages 4-5): Samuel McDermott, Jurij Kotar, Joel Collins, Leonardo Mancini, Richard Bowman, and Pietro Cicuta. Using old laboratory equipment with modern web-of-things standards: a smart laboratory with labthings retro. Royal Society Open Science, Aug 2024. URL: https://doi.org/10.1098/rsos.240634, doi:10.1098/rsos.240634. This article has 3 citations and is from a peer-reviewed journal.

16. (mcdermott2024usingoldlaboratory pages 1-2): Samuel McDermott, Jurij Kotar, Joel Collins, Leonardo Mancini, Richard Bowman, and Pietro Cicuta. Using old laboratory equipment with modern web-of-things standards: a smart laboratory with labthings retro. Royal Society Open Science, Nov 2024. URL: https://doi.org/10.48550/arxiv.2311.08200, doi:10.48550/arxiv.2311.08200. This article has 8 citations and is from a peer-reviewed journal.

17. (mcdermott2024usingoldlaboratory pages 7-9): Samuel McDermott, Jurij Kotar, Joel Collins, Leonardo Mancini, Richard Bowman, and Pietro Cicuta. Using old laboratory equipment with modern web-of-things standards: a smart laboratory with labthings retro. Royal Society Open Science, Nov 2024. URL: https://doi.org/10.48550/arxiv.2311.08200, doi:10.48550/arxiv.2311.08200. This article has 8 citations and is from a peer-reviewed journal.

18. (mcdermott2024usingoldlaboratorya pages 1-2): Samuel McDermott, Jurij Kotar, Joel Collins, Leonardo Mancini, Richard Bowman, and Pietro Cicuta. Using old laboratory equipment with modern web-of-things standards: a smart laboratory with labthings retro. Royal Society Open Science, Aug 2024. URL: https://doi.org/10.1098/rsos.240634, doi:10.1098/rsos.240634. This article has 3 citations and is from a peer-reviewed journal.

19. (mcdermott2024usingoldlaboratory pages 9-10): Samuel McDermott, Jurij Kotar, Joel Collins, Leonardo Mancini, Richard Bowman, and Pietro Cicuta. Using old laboratory equipment with modern web-of-things standards: a smart laboratory with labthings retro. Royal Society Open Science, Nov 2024. URL: https://doi.org/10.48550/arxiv.2311.08200, doi:10.48550/arxiv.2311.08200. This article has 8 citations and is from a peer-reviewed journal.

20. (mcdermott2024usingoldlaboratory pages 2-4): Samuel McDermott, Jurij Kotar, Joel Collins, Leonardo Mancini, Richard Bowman, and Pietro Cicuta. Using old laboratory equipment with modern web-of-things standards: a smart laboratory with labthings retro. Royal Society Open Science, Nov 2024. URL: https://doi.org/10.48550/arxiv.2311.08200, doi:10.48550/arxiv.2311.08200. This article has 8 citations and is from a peer-reviewed journal.

21. (mcdermott2024usingoldlaboratorya pages 5-6): Samuel McDermott, Jurij Kotar, Joel Collins, Leonardo Mancini, Richard Bowman, and Pietro Cicuta. Using old laboratory equipment with modern web-of-things standards: a smart laboratory with labthings retro. Royal Society Open Science, Aug 2024. URL: https://doi.org/10.1098/rsos.240634, doi:10.1098/rsos.240634. This article has 3 citations and is from a peer-reviewed journal.

22. (mcdermott2024usingoldlaboratorya pages 2-3): Samuel McDermott, Jurij Kotar, Joel Collins, Leonardo Mancini, Richard Bowman, and Pietro Cicuta. Using old laboratory equipment with modern web-of-things standards: a smart laboratory with labthings retro. Royal Society Open Science, Aug 2024. URL: https://doi.org/10.1098/rsos.240634, doi:10.1098/rsos.240634. This article has 3 citations and is from a peer-reviewed journal.

23. (grujic2023areviewof pages 2-4): Katarina Grujić. A review of thermal spectral imaging methods for monitoring high-temperature molten material streams. Sensors (Basel, Switzerland), 23:1130, Jan 2023. URL: https://doi.org/10.3390/s23031130, doi:10.3390/s23031130. This article has 38 citations.

24. (grujic2023areviewof pages 6-8): Katarina Grujić. A review of thermal spectral imaging methods for monitoring high-temperature molten material streams. Sensors (Basel, Switzerland), 23:1130, Jan 2023. URL: https://doi.org/10.3390/s23031130, doi:10.3390/s23031130. This article has 38 citations.

25. (grujic2023areviewof pages 16-18): Katarina Grujić. A review of thermal spectral imaging methods for monitoring high-temperature molten material streams. Sensors (Basel, Switzerland), 23:1130, Jan 2023. URL: https://doi.org/10.3390/s23031130, doi:10.3390/s23031130. This article has 38 citations.

26. (grujic2023areviewof pages 26-27): Katarina Grujić. A review of thermal spectral imaging methods for monitoring high-temperature molten material streams. Sensors (Basel, Switzerland), 23:1130, Jan 2023. URL: https://doi.org/10.3390/s23031130, doi:10.3390/s23031130. This article has 38 citations.

27. (grujic2023areviewof pages 14-16): Katarina Grujić. A review of thermal spectral imaging methods for monitoring high-temperature molten material streams. Sensors (Basel, Switzerland), 23:1130, Jan 2023. URL: https://doi.org/10.3390/s23031130, doi:10.3390/s23031130. This article has 38 citations.

28. (grujic2023areviewof pages 1-2): Katarina Grujić. A review of thermal spectral imaging methods for monitoring high-temperature molten material streams. Sensors (Basel, Switzerland), 23:1130, Jan 2023. URL: https://doi.org/10.3390/s23031130, doi:10.3390/s23031130. This article has 38 citations.

29. (usamentiaga2014infraredthermographyfor pages 10-13): Rubén Usamentiaga, Pablo Venegas, Jon Guerediaga, Laura Vega, Julio Molleda, and Francisco Bulnes. Infrared thermography for temperature measurement and non-destructive testing. Sensors, 14:12305-12348, Jul 2014. URL: https://doi.org/10.3390/s140712305, doi:10.3390/s140712305. This article has 1533 citations and is from a peer-reviewed journal.

30. (usamentiaga2014infraredthermographyfor pages 5-8): Rubén Usamentiaga, Pablo Venegas, Jon Guerediaga, Laura Vega, Julio Molleda, and Francisco Bulnes. Infrared thermography for temperature measurement and non-destructive testing. Sensors, 14:12305-12348, Jul 2014. URL: https://doi.org/10.3390/s140712305, doi:10.3390/s140712305. This article has 1533 citations and is from a peer-reviewed journal.

31. (usamentiaga2014infraredthermographyfor pages 3-5): Rubén Usamentiaga, Pablo Venegas, Jon Guerediaga, Laura Vega, Julio Molleda, and Francisco Bulnes. Infrared thermography for temperature measurement and non-destructive testing. Sensors, 14:12305-12348, Jul 2014. URL: https://doi.org/10.3390/s140712305, doi:10.3390/s140712305. This article has 1533 citations and is from a peer-reviewed journal.

32. (usamentiaga2014infraredthermographyfor pages 8-10): Rubén Usamentiaga, Pablo Venegas, Jon Guerediaga, Laura Vega, Julio Molleda, and Francisco Bulnes. Infrared thermography for temperature measurement and non-destructive testing. Sensors, 14:12305-12348, Jul 2014. URL: https://doi.org/10.3390/s140712305, doi:10.3390/s140712305. This article has 1533 citations and is from a peer-reviewed journal.

33. (giulietti2025spectralemissivitymeasurement pages 11-12): Nicola Giulietti, Gloria Cosoli, Rachele Napolitano, Giuseppe Pandarese, Gian Marco Revel, and Paolo Chiariotti. Spectral emissivity measurement for high-temperature applications: a systematic review. Acta IMEKO, 14:1-17, Mar 2025. URL: https://doi.org/10.21014/actaimeko.v14i1.1846, doi:10.21014/actaimeko.v14i1.1846. This article has 13 citations and is from a peer-reviewed journal.

34. (giulietti2025spectralemissivitymeasurement pages 9-10): Nicola Giulietti, Gloria Cosoli, Rachele Napolitano, Giuseppe Pandarese, Gian Marco Revel, and Paolo Chiariotti. Spectral emissivity measurement for high-temperature applications: a systematic review. Acta IMEKO, 14:1-17, Mar 2025. URL: https://doi.org/10.21014/actaimeko.v14i1.1846, doi:10.21014/actaimeko.v14i1.1846. This article has 13 citations and is from a peer-reviewed journal.

35. (giulietti2025spectralemissivitymeasurement pages 10-11): Nicola Giulietti, Gloria Cosoli, Rachele Napolitano, Giuseppe Pandarese, Gian Marco Revel, and Paolo Chiariotti. Spectral emissivity measurement for high-temperature applications: a systematic review. Acta IMEKO, 14:1-17, Mar 2025. URL: https://doi.org/10.21014/actaimeko.v14i1.1846, doi:10.21014/actaimeko.v14i1.1846. This article has 13 citations and is from a peer-reviewed journal.

36. (liu2022reviewofdevelopment pages 12-13): Siyu Liu, Yu Huang, Yong He, Yanqun Zhu, and Zhihua Wang. Review of development and comparison of surface thermometry methods in combustion environments: principles, current state of the art, and applications. Processes, 10:2528, Nov 2022. URL: https://doi.org/10.3390/pr10122528, doi:10.3390/pr10122528. This article has 25 citations.

37. (liu2022reviewofdevelopment pages 11-12): Siyu Liu, Yu Huang, Yong He, Yanqun Zhu, and Zhihua Wang. Review of development and comparison of surface thermometry methods in combustion environments: principles, current state of the art, and applications. Processes, 10:2528, Nov 2022. URL: https://doi.org/10.3390/pr10122528, doi:10.3390/pr10122528. This article has 25 citations.

38. (doloi2025democratizingselfdrivinglabs pages 1-2): Sayan Doloi, Maloy Das, Yujia Li, Zen Han Cho, Xingchi Xiao, John V. Hanna, Matthew Osvaldo, and Leonard Ng Wei Tat. Democratizing self-driving labs: advances in low-cost 3d printing for laboratory automation. Digital Discovery, 4:1685-1721, Jan 2025. URL: https://doi.org/10.1039/d4dd00411f, doi:10.1039/d4dd00411f. This article has 36 citations and is from a peer-reviewed journal.

39. (doloi2025democratizingselfdrivinglabs pages 3-4): Sayan Doloi, Maloy Das, Yujia Li, Zen Han Cho, Xingchi Xiao, John V. Hanna, Matthew Osvaldo, and Leonard Ng Wei Tat. Democratizing self-driving labs: advances in low-cost 3d printing for laboratory automation. Digital Discovery, 4:1685-1721, Jan 2025. URL: https://doi.org/10.1039/d4dd00411f, doi:10.1039/d4dd00411f. This article has 36 citations and is from a peer-reviewed journal.

40. (doloi2025democratizingselfdrivinglabs pages 8-9): Sayan Doloi, Maloy Das, Yujia Li, Zen Han Cho, Xingchi Xiao, John V. Hanna, Matthew Osvaldo, and Leonard Ng Wei Tat. Democratizing self-driving labs: advances in low-cost 3d printing for laboratory automation. Digital Discovery, 4:1685-1721, Jan 2025. URL: https://doi.org/10.1039/d4dd00411f, doi:10.1039/d4dd00411f. This article has 36 citations and is from a peer-reviewed journal.
