Question: For induction heating systems that use susceptors to heat electrically non-conductive or poorly coupling charges (e.g., ceramics such as yttria-stabilized zirconia), review the literature on graphite and refractory-metal (e.g., tantalum) susceptor design and use: RF coupling efficiency, susceptor geometry and placement, heat transfer to the charge by conduction/radiation, achievable temperatures and operating limits at 1700-2500 C, and susceptor vapor deposition / contamination of the charge. Cite high-quality sources with bibtex.

# Susceptor Design and Use in Induction Heating Systems for Electrically Non-Conductive Ceramics

## 1. Introduction and Rationale

Electrically non-conductive or poorly coupling materials such as yttria-stabilized zirconia (YSZ), alumina, and other advanced ceramics cannot be directly heated by induction because they do not support the eddy currents required for electromagnetic-to-thermal energy conversion. The standard solution is to employ a conductive susceptor—typically graphite or a refractory metal such as tantalum or tantalum carbide (TaC)—that couples with the RF field of the induction coil, absorbs electromagnetic power, and transfers heat to the ceramic charge by radiation and conduction (kuzmichev2011evaporatorswithinduction pages 3-6, kuzmichev2011evaporatorswithinduction pages 6-9). This review synthesizes literature on the design, performance, and limitations of such susceptor-based induction heating systems, with emphasis on operation in the 1700–2500 °C range.

## 2. RF Coupling Efficiency and Skin Depth Considerations

The fundamental electromagnetic design rule for an induction-heated susceptor is that its wall thickness should be at least equal to the skin depth at the operating frequency. The skin depth δ in a conductor is given by δ = 1/√(πμ₀μᵣσf), where σ is the electrical conductivity and f is the frequency. For a graphite crucible operating at 15 kHz, Patidar et al. measured and modeled a skin depth of approximately 10 mm, and accordingly selected a crucible wall thickness of 10 mm to maximize electromagnetic coupling; their system achieved coil efficiencies exceeding 90% at approximately 14 kHz (patidar2018modellingandexperimental pages 5-5, patidar2018modellingandexperimental pages 5-8). The workpiece effective resistance was shown to increase more rapidly with frequency than the coil resistance, contributing to improved energy transfer at higher frequencies (patidar2018modellingandexperimental pages 5-8). The temperature-dependent electrical conductivity of graphite was modeled as a fourth-order polynomial, reflecting the significant variation of resistivity with temperature that affects coupling at high temperatures (patidar2018modellingandexperimental pages 4-5).

When the susceptor wall thickness exceeds the skin depth, it fully absorbs electromagnetic energy and electromagnetically shields the charge from the inductor field, preventing turbulence in molten charges and ensuring that the quantity and volume of the charge do not affect AC generator operation (kuzmichev2011evaporatorswithinduction pages 3-6). Kuzmichev and Tsybulsky emphasize that the susceptor wall thickness must be "larger than the skin-layer thickness at operation frequency" for effective shielding, and that both configuration and composition should be selected to "absorb the maximum amount of RF energy and convert it into heat" (kuzmichev2011evaporatorswithinduction pages 9-11, kuzmichev2011evaporatorswithinduction pages 6-9).

For RF dielectric heating of carbon-based susceptors at lower frequencies (1–200 MHz), Vashisth et al. showed that the heating response depends on the bulk electrical conductivity of the susceptor material and the electric field magnitude and frequency, with an optimum conductivity window—too low and insufficient energy absorption occurs, too high and the field is reflected (vashisth2021radiofrequencyheating pages 2-3, vashisth2021radiofrequencyheating pages 1-2).

## 3. Susceptor Geometry and Placement

Graphite susceptors are most commonly fabricated in cylindrical or cup-shaped geometries that surround the dielectric crucible containing the charge. Kuzmichev and Tsybulsky describe an external hollow cylindrical susceptor made from high-purity graphite that surrounds a pyrolytic boron nitride (BN) crucible (kuzmichev2011evaporatorswithinduction pages 6-9). In another design, a solid columnar block of graphite carbon 3.5 cm in diameter and 1.3 cm in height supports and heats a Mo crucible containing copper (kuzmichev2011evaporatorswithinduction pages 9-11). The susceptor assembly is typically surrounded by thermally insulating components—pyrolytic BN heat shields and silica or quartz spacers—that are refractory, transparent to radio frequencies, and have low thermal conductivity, thereby concentrating heat at the charge location while minimizing parasitic absorption of RF energy (kuzmichev2011evaporatorswithinduction pages 9-11).

In SiC chemical vapor deposition (CVD) reactors, the graphite susceptor takes the form of a long rectangular or cylindrical hot-wall element upon which substrates are placed. In the chimney (vertical hot-wall) reactor described by Ellison et al., substrates are placed along both inner walls of the RF-induction-heated graphite susceptor, and the hot-wall geometry establishes uniform heat distribution and low temperature gradients in the vicinity of the substrate (ellison1999hightemperaturecvd pages 2-4, ellison1999hightemperaturecvd pages 4-5). In horizontal CVD reactors, substrates sit directly on the inductively heated graphite susceptor surface, with a free height of approximately 22 mm between the substrate and the upper reactor wall (rottner1994graphiteascarbon pages 1-3, rottner1994graphiteascarbon pages 3-4).

For induction evaporators used in microelectronics, an inductor-concentrator design acts as a step-down RF transformer, with the concentrator body serving as a one-turn inductor that heats the graphite susceptor disposed within its central hole. This arrangement minimizes working voltage and stray magnetic fields, effectively transporting RF power to the susceptor (kuzmichev2011evaporatorswithinduction pages 13-16).

## 4. Heat Transfer from Susceptor to Charge

Heat transfer from the susceptor to the non-conductive charge occurs primarily by thermal radiation and conduction. Kuzmichev and Tsybulsky state that the graphite susceptor "heats the non-conducting crucible due to heat radiation and heat conductivity," and that the susceptor's mass and receptivity to RF frequencies "assures that the charge contained within the crucible is quickly heated in controllable manner" (kuzmichev2011evaporatorswithinduction pages 3-6, kuzmichev2011evaporatorswithinduction pages 9-11). In the evaporator design described in the Phinney and Strippe patent, the susceptor "begins to heat and transfer this heat by a radiation and conduction process into the charge in the crucible" (kuzmichev2011evaporatorswithinduction pages 11-13).

The pyrolytic BN inner heat shield serves a dual purpose: it prevents infrared radiation from escaping from the susceptor and crucible area, thereby retaining heat, while simultaneously shielding the outer heat shield from direct radiative transfer (kuzmichev2011evaporatorswithinduction pages 9-11). Radiation dominates heat transfer at the extreme temperatures relevant to ceramic processing (>1700 °C), following the Stefan-Boltzmann T⁴ relationship.

In ultrafast high-temperature sintering (UHS), graphite felts serve as both heaters and thermal insulators. Their low thermal conductivity and heat capacity enable efficient heat concentration at the sample location, with the sample being heated primarily at its surface through radiative heat transfer from the hot graphite (karacasulu2025sinteringunderhigh pages 9-11, karacasulu2025sinteringunderhigh pages 11-12, luo2603ultrafastsintering pages 4-7).

## 5. Achievable Temperatures and Operating Limits

Graphite susceptors in induction heating systems routinely operate in the range of 1500–1900 °C for evaporation applications. In one documented system, the susceptor and crucible reached a peak temperature of 1900 °C during a fractionation phase, with steady-state deposition at 1500 °C (kuzmichev2011evaporatorswithinduction pages 11-13). For SiC CVD, graphite susceptors are heated to growth temperatures of 1400–2100 K (1127–1827 °C) in the horizontal reactor configuration (rottner1994graphiteascarbon pages 1-3), and up to 2000–2300 °C in the stagnant-flow high-temperature CVD configuration (ellison1999hightemperaturecvd pages 2-4, ellison1999hightemperaturecvd pages 4-5).

Graphite-based UHS systems can exceed 2500 °C and have been used to densify refractory ceramics including SiC, Si₃N₄, ZrB₂, and ZrC (karacasulu2025sinteringunderhigh pages 9-11, karacasulu2025sinteringunderhigh pages 11-12). Wu et al. report that UHS using graphite powder beds can reach up to 3000 °C (wu2024innovationsinelectric pages 19-20). However, at temperatures above approximately 2000 °C, graphite reactivity and sublimation become significant concerns, particularly in the presence of reactive gases.

For TaC-based systems, Sumathi reported bulk crystal growth of AlN at 1800–1900 °C in TaC crucibles within an inductively heated reactor (sumathi2021commonissuesin pages 2-4). Wellmann notes that the establishment of high-temperature growth processes above 2000 °C for SiC was a key milestone, and that tantalum or tantalum carbide crucibles are specifically suited for growth above 2000 °C where carbon species control is critical (wellmann2018reviewofsic pages 3-5, wellmann2018reviewofsic pages 5-6, wellmann2018reviewofsic pages 1-3). The peritectic decomposition temperature of SiC (2830 °C in inert atmosphere) defines the upper limit for SiC-related processing, with PVT growth typically carried out between 1900 °C and 2400 °C (wellmann2018reviewofsic pages 5-6).

Luo introduced induction ultrafast sintering (IUS) that operates in both field-coupled direct (d-IUS) and field-decoupled susceptor-heating (s-IUS) modes, enabling rapid densification of ceramics including YSZ without the need to pass current through the specimen (luo2603ultrafastsintering pages 4-7).

## 6. Susceptor Vapor Deposition and Contamination of the Charge

### 6.1 Graphite Contamination

Carbon contamination from graphite susceptors is a well-documented concern at high temperatures. Rottner and Helbig showed that graphite reacts with hydrogen at temperatures up to 2100 K to produce hydrocarbon species (primarily methane below 1900 K and acetylene above 1900 K), and that above approximately 1700 K the carbon generation rate becomes thermodynamically limited rather than kinetically limited. At these temperatures, the amount of hydrocarbon formed by the graphite susceptor can exceed the concentration of intentionally supplied carbon precursors, making the gas-phase composition largely independent of external carbon input (rottner1994graphiteascarbon pages 1-3, rottner1994graphiteascarbon pages 4-6, rottner1994graphiteascarbon pages 3-4). This is particularly problematic for CVD processes where stoichiometric control is essential.

When partly coated graphite susceptors are used in SiC epitaxial growth, impurities such as Al, B, and Ti may be incorporated into the growing film from exposed graphite surfaces. Ellison et al. demonstrated that using fully SiC-coated susceptors eliminates this impurity incorporation and provides better doping control, with residual nitrogen doping as low as 2×10¹⁴ cm⁻³ achievable on fully coated susceptors (ellison1999hightemperaturecvd pages 2-4). The growth rate difference between partly coated (10–40 mm/h) and fully coated susceptors (5–15 mm/h) reflects the substantial contribution of exposed graphite to carbon supply (ellison1999hightemperaturecvd pages 2-4).

In the evaporator context, Kuzmichev and Tsybulsky note that pyrolytic BN is selected as an interface material because it "does not interact with the carbon of the susceptor at the high temperatures at which evaporator operates" (kuzmichev2011evaporatorswithinduction pages 9-11). Self-fractionation procedures, in which impurities are driven to the crucible walls by controlled temperature ramping, provide an additional contamination mitigation strategy (kuzmichev2011evaporatorswithinduction pages 11-13).

### 6.2 TaC as a Contamination Barrier

TaC coatings on graphite susceptors serve as a chemically inert barrier that prevents direct graphite-gas interactions. Zhang describes TaC-coated graphite susceptors in hot-wall MOCVD reactors for nitride growth, where the TaC layer prevents carbon contamination of the growing film (zhang2021hotwallmocvdof pages 1-9). In the SiC PVT growth context, Wellmann explains that when tantalum or TaC is used as growth cell material instead of graphite, the materials system changes from SiC+C to SiC+Si, because TaC getters carbon species from the gas phase, fundamentally altering the gas-phase composition and enabling better stoichiometric control (wellmann2018reviewofsic pages 5-6).

For AlN crystal growth, Sumathi used TaC crucibles within inductively heated reactors at 1800–1900 °C, with the main remaining contamination concern being Si and C incorporation from decomposition of SiC substrates rather than from the crucible material itself (sumathi2021commonissuesin pages 2-4, sumathi2021commonissuesin pages 1-2). This demonstrates that TaC effectively mitigates susceptor-originating contamination, though other sources of contamination remain relevant at very high temperatures.

## 7. Summary Comparison

The following table provides a comparative overview of graphite and TaC-based susceptor materials for induction heating of non-conductive ceramics:

| Material | Max Operating Temperature | RF Coupling Characteristics | Typical Geometry | Heat Transfer Mode | Key Contamination Issues | Mitigation Strategies |
|---|---:|---|---|---|---|---|
| High-purity graphite | Commonly demonstrated to ~1900–2000 °C in induction evaporators; graphite-based ultrafast heater/susceptor systems can exceed 2500 °C, but this is a practical upper regime where graphite reactivity/vaporization concerns become important rather than a benign continuous operating range (kuzmichev2011evaporatorswithinduction pages 11-13, karacasulu2025sinteringunderhigh pages 9-11, karacasulu2025sinteringunderhigh pages 11-12) | Strong RF susceptor because of good electrical conductivity; coupling is improved by matching wall thickness to skin depth. For a graphite crucible at 15 kHz, skin depth was selected at ~10 mm to match a 10 mm wall; coil efficiency exceeded 90% near 14 kHz in one modeled/validated system (patidar2018modellingandexperimental pages 5-5, patidar2018modellingandexperimental pages 5-8). For shielding applications, susceptor wall thickness should be larger than skin depth to prevent direct RF coupling to the charge (kuzmichev2011evaporatorswithinduction pages 6-9) | External hollow cylindrical susceptor around a dielectric crucible; cup-shaped graphite susceptor around pyrolytic BN crucibles; also solid columnar graphite blocks used under crucibles (e.g., 3.5 cm diameter × 1.3 cm height) (kuzmichev2011evaporatorswithinduction pages 6-9, kuzmichev2011evaporatorswithinduction pages 9-11, kuzmichev2011evaporatorswithinduction pages 13-16) | Primarily radiation + conduction from susceptor to crucible/charge; susceptor also acts as RF shield to decouple melt/charge from magnetic stirring and direct field interaction (kuzmichev2011evaporatorswithinduction pages 3-6, kuzmichev2011evaporatorswithinduction pages 9-11, kuzmichev2011evaporatorswithinduction pages 11-13, kuzmichev2011evaporatorswithinduction pages 6-9) | Carbon contamination from graphite-hydrogen reaction at high temperature can dominate gas chemistry; hydrocarbon generation can exceed intentionally supplied carbon precursor, and exposed graphite can contribute impurity incorporation (including Al, B, Ti in SiC epitaxy contexts). Thin pyrolytic graphite coatings may also be consumed (rottner1994graphiteascarbon pages 1-3, rottner1994graphiteascarbon pages 4-6, rottner1994graphiteascarbon pages 8-9, ellison1999hightemperaturecvd pages 2-4) | Use fully SiC-coated graphite susceptors rather than partly coated/exposed graphite; isolate graphite from reactive gas with BN or ceramic barriers; use high purity graphite; operate in inert/vacuum atmospheres where possible; employ heat shields and geometry that minimize line-of-sight deposition and uncontrolled reactions (kuzmichev2011evaporatorswithinduction pages 9-11, ellison1999hightemperaturecvd pages 2-4, kuzmichev2011evaporatorswithinduction pages 13-16) |
| Tantalum / TaC / TaC-coated graphite | TaC crucibles are reported for AlN sublimation growth at 1800–1900 °C; tantalum or TaC are specifically identified as suitable materials for growth systems above 2000 °C, especially where carbon gettering or carbon-control is needed (sumathi2021commonissuesin pages 2-4, wellmann2018reviewofsic pages 3-5, wellmann2018reviewofsic pages 1-3) | Less direct induction-specific coupling data were retrieved than for graphite, but tantalum/TaC are identified as susceptor/crucible materials for high-temperature growth cells; in SiC PVT, tantalum or TaC alter the effective gas-species balance by gettering carbon species, unlike carbon containers (wellmann2018reviewofsic pages 3-5, wellmann2018reviewofsic pages 5-6). TaC is also used as a thin protective coating on graphite susceptors to preserve RF-heated graphite benefits while changing surface chemistry (zhang2021hotwallmocvdof pages 1-9) | TaC crucibles for sublimation growth; TaC-coated graphite susceptors in hot-wall reactors; tantalum/TaC used as growth-cell construction materials or coated susceptor surfaces rather than only bulk standalone shapes in the retrieved literature (sumathi2021commonissuesin pages 2-4, zhang2021hotwallmocvdof pages 1-9, wellmann2018reviewofsic pages 3-5) | Same indirect-heating architecture as graphite-based systems when used as crucible/surface material: susceptor/crucible is RF-heated and transfers heat by radiation/conduction to the ceramic or crystal-growth charge; coatings mainly modify surface chemistry and contamination behavior (sumathi2021commonissuesin pages 2-4, zhang2021hotwallmocvdof pages 1-9, wellmann2018reviewofsic pages 3-5) | Main benefit is reduced carbon contamination relative to bare graphite. Remaining contamination risks come from substrate/crucible interactions at very high temperature (e.g., Si and C incorporation from decomposing SiC substrates in AlN growth), rather than hydrocarbon generation from the susceptor surface itself (sumathi2021commonissuesin pages 2-4, sumathi2021commonissuesin pages 1-2, rottner1994graphiteascarbon pages 8-9) | Use TaC-coated graphite susceptors to combine good RF heating with a chemically more inert surface; use TaC crucibles where carbon control is critical; select source/crucible/substrate combinations to avoid decomposition-driven Si/C contamination; employ high-purity materials and controlled thermal gradients (sumathi2021commonissuesin pages 2-4, zhang2021hotwallmocvdof pages 1-9, wellmann2018reviewofsic pages 3-5) |


*Table: This table compares graphite and tantalum/TaC-based susceptors for induction heating of poorly coupling ceramic charges. It highlights practical temperature ranges, RF-coupling design rules, typical geometries, and the main contamination-control tradeoffs relevant to 1700–2500 °C processing.*

## 8. BibTeX References

The following BibTeX entries correspond to the key sources cited in this review:

> @article{kuzmichev2011evaporatorswithinduction,
>   author = {Kuzmichev, Anatoly and Tsybulsky, Leonid},
>   title = {Evaporators with Induction Heating and Their Applications},
>   journal = {ArXiv},
>   year = {2011},
>   month = {Feb},
>   doi = {10.5772/13934},
>   url = {https://doi.org/10.5772/13934}
> }
>
> @article{patidar2018modellingandexperimental,
>   author = {Patidar, Bhupendra and Hussain, Md. Mozahir and Jha, Sanjeev K. and Dikshit, Biswaranjan and Sharma, Archana},
>   title = {Modelling and Experimental Demonstration of a Litz Coil-Based High-Temperature Induction Heating System for Melting Application},
>   journal = {IET Electric Power Applications},
>   volume = {12},
>   number = {2},
>   pages = {161--168},
>   year = {2018},
>   month = {Feb},
>   doi = {10.1049/iet-epa.2017.0256},
>   url = {https://doi.org/10.1049/iet-epa.2017.0256}
> }
>
> @article{rottner1994graphiteascarbon,
>   author = {Rottner, Kurt and Helbig, Reinhard},
>   title = {Graphite as Carbon Source in Chemical Vapor Deposition of {$\alpha$}-Silicon Carbide},
>   journal = {Journal of Crystal Growth},
>   volume = {144},
>   number = {3-4},
>   pages = {258--266},
>   year = {1994},
>   month = {Dec},
>   doi = {10.1016/0022-0248(94)90465-0},
>   url = {https://doi.org/10.1016/0022-0248(94)90465-0}
> }
>
> @article{ellison1999hightemperaturecvd,
>   author = {Ellison, A. and Zhang, Jie and Peterson, J. and Henry, A. and Wahab, Q. and Bergman, J. and Makarov, Y. and Vorob'ev, A. N. and Vehanen, A. and Janz{\'e}n, E.},
>   title = {High Temperature CVD Growth of SiC},
>   journal = {Materials Science and Engineering B: Advanced Functional Solid-State Materials},
>   volume = {61},
>   pages = {113--120},
>   year = {1999},
>   month = {Jul},
>   doi = {10.1016/S0921-5107(98)00482-6},
>   url = {https://doi.org/10.1016/S0921-5107(98)00482-6}
> }
>
> @article{sumathi2021commonissuesin,
>   author = {Sumathi, R. Radhakrishnan},
>   title = {Common Issues in the Hetero-Epitaxial Seeding on SiC Substrates in the Sublimation Growth of AlN Crystals},
>   journal = {Applied Physics A},
>   volume = {127},
>   number = {8},
>   year = {2021},
>   month = {Jul},
>   doi = {10.1007/s00339-021-04770-9},
>   url = {https://doi.org/10.1007/s00339-021-04770-9}
> }
>
> @article{wellmann2018reviewofsic,
>   author = {Wellmann, Peter J.},
>   title = {Review of SiC Crystal Growth Technology},
>   journal = {Semiconductor Science and Technology},
>   volume = {33},
>   number = {10},
>   pages = {103001},
>   year = {2018},
>   month = {Sep},
>   doi = {10.1088/1361-6641/aad831},
>   url = {https://doi.org/10.1088/1361-6641/aad831}
> }
>
> @article{zhang2021hotwallmocvdof,
>   author = {Zhang, Hengfang},
>   title = {Hot-Wall MOCVD of N-Polar Group-III Nitride Materials},
>   journal = {Link{"o}ping Studies in Science and Technology. Licentiate Thesis},
>   year = {2021},
>   month = {Jun},
>   doi = {10.3384/lic.diva-175502},
>   url = {https://doi.org/10.3384/lic.diva-175502}
> }
>
> @article{vashisth2021radiofrequencyheating,
>   author = {Vashisth, Aniruddh and Upama, Shegufta T. and Anas, Muhammad and Oh, Ju-Hyun and Patil, Nutan and Green, Micah J.},
>   title = {Radio Frequency Heating and Material Processing Using Carbon Susceptors},
>   journal = {Nanoscale Advances},
>   volume = {3},
>   number = {18},
>   pages = {5255--5264},
>   year = {2021},
>   month = {Jul},
>   doi = {10.1039/D1NA00217A},
>   url = {https://doi.org/10.1039/D1NA00217A}
> }
>
> @article{karacasulu2025sinteringunderhigh,
>   author = {Karacasulu, Levent and Mani{\`e}re, Charles and Vakifahmetoglu, Cekdar and Marinel, Sylvain and Biesuz, Mattia},
>   title = {Sintering Under High Heating Rates},
>   journal = {Annual Review of Materials Research},
>   volume = {55},
>   number = {1},
>   pages = {203--230},
>   year = {2025},
>   month = {Jul},
>   doi = {10.1146/annurev-matsci-080323-042441},
>   url = {https://doi.org/10.1146/annurev-matsci-080323-042441}
> }
>
> @article{wu2024innovationsinelectric,
>   author = {Wu, Jiajia and Wu, Xiaohu and Gao, Yan and Yan, Zilin},
>   title = {Innovations in Electric Current-Assisted Sintering for SOFC: A Review of Advances in Flash Sintering and Ultrafast High-Temperature Sintering},
>   journal = {Applied Sciences},
>   volume = {14},
>   number = {10},
>   pages = {3953},
>   year = {2024},
>   month = {May},
>   doi = {10.3390/app14103953},
>   url = {https://doi.org/10.3390/app14103953}
> }
>
> @article{luo2025ultrafastsintering,
>   author = {Luo, J.},
>   title = {Ultrafast Sintering},
>   journal = {ArXiv},
>   year = {2025},
>   doi = {10.48550/arXiv.2603.23423},
>   url = {https://doi.org/10.48550/arXiv.2603.23423}
> }
>
> (kuzmichev2011evaporatorswithinduction pages 3-6, rottner1994graphiteascarbon pages 1-3, ellison1999hightemperaturecvd pages 2-4, sumathi2021commonissuesin pages 2-4, zhang2021hotwallmocvdof pages 1-9, vashisth2021radiofrequencyheating pages 1-2, wellmann2018reviewofsic pages 3-5, karacasulu2025sinteringunderhigh pages 9-11, wu2024innovationsinelectric pages 19-20, luo2603ultrafastsintering pages 4-7)


*Blockquote: This artifact provides a ready-to-use BibTeX list for the principal sources supporting the review of graphite and refractory-metal susceptors. It is useful for directly importing the most relevant references into a manuscript or literature review.*

## 9. Conclusions

The design of susceptor-based induction heating systems for non-conductive ceramics involves a tradeoff between electromagnetic coupling efficiency, achievable temperature, and contamination risk. Graphite remains the most widely used susceptor material due to its excellent electrical conductivity, thermal stability to approximately 2500 °C under inert conditions, ease of machining, and low cost. The primary design rule is that susceptor wall thickness must equal or exceed the electromagnetic skin depth at the operating frequency—approximately 10 mm for graphite at 15 kHz—to ensure efficient power absorption and electromagnetic shielding of the charge (patidar2018modellingandexperimental pages 5-5, kuzmichev2011evaporatorswithinduction pages 6-9). Coil efficiencies exceeding 90% have been demonstrated with optimized litz-wire coils and graphite susceptors (patidar2018modellingandexperimental pages 5-8).

However, graphite susceptors generate significant carbon contamination at temperatures above 1700 K, particularly in hydrogen-containing atmospheres where graphite-hydrogen reactions produce hydrocarbons at rates that can dominate over intentionally supplied precursors (rottner1994graphiteascarbon pages 1-3). TaC coatings on graphite susceptors, or standalone TaC crucibles, provide a chemically more inert surface that mitigates carbon contamination while preserving the RF coupling advantages of graphite (zhang2021hotwallmocvdof pages 1-9, wellmann2018reviewofsic pages 5-6). For the most demanding high-temperature applications (>2000 °C) involving sensitive ceramic or semiconductor charges, TaC-coated graphite or TaC crucibles within inductively heated systems represent the current state of the art for balancing thermal performance, electromagnetic coupling, and charge purity (sumathi2021commonissuesin pages 2-4, wellmann2018reviewofsic pages 3-5).

References

1. (kuzmichev2011evaporatorswithinduction pages 3-6): Anatoly Kuzmichev and Leonid Tsybulsky. Evaporators with induction heating and their applications. ArXiv, Feb 2011. URL: https://doi.org/10.5772/13934, doi:10.5772/13934. This article has 16 citations.

2. (kuzmichev2011evaporatorswithinduction pages 6-9): Anatoly Kuzmichev and Leonid Tsybulsky. Evaporators with induction heating and their applications. ArXiv, Feb 2011. URL: https://doi.org/10.5772/13934, doi:10.5772/13934. This article has 16 citations.

3. (patidar2018modellingandexperimental pages 5-5): Bhupendra Patidar, Md. Mozahir Hussain, Sanjeev K. Jha, Biswaranjan Dikshit, and Archana Sharma. Modelling and experimental demonstration of a litz coil-based high-temperature induction heating system for melting application. Iet Electric Power Applications, 12:161-168, Feb 2018. URL: https://doi.org/10.1049/iet-epa.2017.0256, doi:10.1049/iet-epa.2017.0256. This article has 15 citations and is from a peer-reviewed journal.

4. (patidar2018modellingandexperimental pages 5-8): Bhupendra Patidar, Md. Mozahir Hussain, Sanjeev K. Jha, Biswaranjan Dikshit, and Archana Sharma. Modelling and experimental demonstration of a litz coil-based high-temperature induction heating system for melting application. Iet Electric Power Applications, 12:161-168, Feb 2018. URL: https://doi.org/10.1049/iet-epa.2017.0256, doi:10.1049/iet-epa.2017.0256. This article has 15 citations and is from a peer-reviewed journal.

5. (patidar2018modellingandexperimental pages 4-5): Bhupendra Patidar, Md. Mozahir Hussain, Sanjeev K. Jha, Biswaranjan Dikshit, and Archana Sharma. Modelling and experimental demonstration of a litz coil-based high-temperature induction heating system for melting application. Iet Electric Power Applications, 12:161-168, Feb 2018. URL: https://doi.org/10.1049/iet-epa.2017.0256, doi:10.1049/iet-epa.2017.0256. This article has 15 citations and is from a peer-reviewed journal.

6. (kuzmichev2011evaporatorswithinduction pages 9-11): Anatoly Kuzmichev and Leonid Tsybulsky. Evaporators with induction heating and their applications. ArXiv, Feb 2011. URL: https://doi.org/10.5772/13934, doi:10.5772/13934. This article has 16 citations.

7. (vashisth2021radiofrequencyheating pages 2-3): Aniruddh Vashisth, Shegufta T. Upama, Muhammad Anas, Ju-Hyun Oh, Nutan Patil, and Micah J. Green. Radio frequency heating and material processing using carbon susceptors. Nanoscale Advances, 3:5255-5264, Jul 2021. URL: https://doi.org/10.1039/d1na00217a, doi:10.1039/d1na00217a. This article has 59 citations and is from a peer-reviewed journal.

8. (vashisth2021radiofrequencyheating pages 1-2): Aniruddh Vashisth, Shegufta T. Upama, Muhammad Anas, Ju-Hyun Oh, Nutan Patil, and Micah J. Green. Radio frequency heating and material processing using carbon susceptors. Nanoscale Advances, 3:5255-5264, Jul 2021. URL: https://doi.org/10.1039/d1na00217a, doi:10.1039/d1na00217a. This article has 59 citations and is from a peer-reviewed journal.

9. (ellison1999hightemperaturecvd pages 2-4): A. Ellison, Jie Zhang, J. Peterson, A. Henry, Q. Wahab, J. Bergman, Y. Makarov, A. N. Vorob'ev, A. Vehanen, and E. Janzén. High temperature cvd growth of sic. Materials Science and Engineering B-advanced Functional Solid-state Materials, 61:113-120, Jul 1999. URL: https://doi.org/10.1016/s0921-5107(98)00482-6, doi:10.1016/s0921-5107(98)00482-6. This article has 126 citations.

10. (ellison1999hightemperaturecvd pages 4-5): A. Ellison, Jie Zhang, J. Peterson, A. Henry, Q. Wahab, J. Bergman, Y. Makarov, A. N. Vorob'ev, A. Vehanen, and E. Janzén. High temperature cvd growth of sic. Materials Science and Engineering B-advanced Functional Solid-state Materials, 61:113-120, Jul 1999. URL: https://doi.org/10.1016/s0921-5107(98)00482-6, doi:10.1016/s0921-5107(98)00482-6. This article has 126 citations.

11. (rottner1994graphiteascarbon pages 1-3): Kurt Rottner and Reinhard Helbig. Graphite as carbon source in chemical vapor deposition of α-silicon carbide. Journal of Crystal Growth, 144:258-266, Dec 1994. URL: https://doi.org/10.1016/0022-0248(94)90465-0, doi:10.1016/0022-0248(94)90465-0. This article has 23 citations and is from a peer-reviewed journal.

12. (rottner1994graphiteascarbon pages 3-4): Kurt Rottner and Reinhard Helbig. Graphite as carbon source in chemical vapor deposition of α-silicon carbide. Journal of Crystal Growth, 144:258-266, Dec 1994. URL: https://doi.org/10.1016/0022-0248(94)90465-0, doi:10.1016/0022-0248(94)90465-0. This article has 23 citations and is from a peer-reviewed journal.

13. (kuzmichev2011evaporatorswithinduction pages 13-16): Anatoly Kuzmichev and Leonid Tsybulsky. Evaporators with induction heating and their applications. ArXiv, Feb 2011. URL: https://doi.org/10.5772/13934, doi:10.5772/13934. This article has 16 citations.

14. (kuzmichev2011evaporatorswithinduction pages 11-13): Anatoly Kuzmichev and Leonid Tsybulsky. Evaporators with induction heating and their applications. ArXiv, Feb 2011. URL: https://doi.org/10.5772/13934, doi:10.5772/13934. This article has 16 citations.

15. (karacasulu2025sinteringunderhigh pages 9-11): Levent Karacasulu, Charles Manière, Cekdar Vakifahmetoglu, Sylvain Marinel, and Mattia Biesuz. Sintering under high heating rates. Annual Review of Materials Research, 55:203-230, Jul 2025. URL: https://doi.org/10.1146/annurev-matsci-080323-042441, doi:10.1146/annurev-matsci-080323-042441. This article has 16 citations and is from a domain leading peer-reviewed journal.

16. (karacasulu2025sinteringunderhigh pages 11-12): Levent Karacasulu, Charles Manière, Cekdar Vakifahmetoglu, Sylvain Marinel, and Mattia Biesuz. Sintering under high heating rates. Annual Review of Materials Research, 55:203-230, Jul 2025. URL: https://doi.org/10.1146/annurev-matsci-080323-042441, doi:10.1146/annurev-matsci-080323-042441. This article has 16 citations and is from a domain leading peer-reviewed journal.

17. (luo2603ultrafastsintering pages 4-7): J Luo. Ultrafast sintering. ArXiv, 2603. URL: https://doi.org/10.48550/arxiv.2603.23423, doi:10.48550/arxiv.2603.23423.

18. (wu2024innovationsinelectric pages 19-20): Jiajia Wu, Xiaohu Wu, Yan Gao, and Zilin Yan. Innovations in electric current-assisted sintering for sofc: a review of advances in flash sintering and ultrafast high-temperature sintering. Applied Sciences, 14:3953, May 2024. URL: https://doi.org/10.3390/app14103953, doi:10.3390/app14103953. This article has 37 citations.

19. (sumathi2021commonissuesin pages 2-4): R. Radhakrishnan Sumathi. Common issues in the hetero-epitaxial seeding on sic substrates in the sublimation growth of aln crystals. Applied Physics A, Jul 2021. URL: https://doi.org/10.1007/s00339-021-04770-9, doi:10.1007/s00339-021-04770-9. This article has 3 citations.

20. (wellmann2018reviewofsic pages 3-5): Peter J Wellmann. Review of sic crystal growth technology. Semiconductor Science and Technology, 33:103001, Sep 2018. URL: https://doi.org/10.1088/1361-6641/aad831, doi:10.1088/1361-6641/aad831. This article has 220 citations and is from a peer-reviewed journal.

21. (wellmann2018reviewofsic pages 5-6): Peter J Wellmann. Review of sic crystal growth technology. Semiconductor Science and Technology, 33:103001, Sep 2018. URL: https://doi.org/10.1088/1361-6641/aad831, doi:10.1088/1361-6641/aad831. This article has 220 citations and is from a peer-reviewed journal.

22. (wellmann2018reviewofsic pages 1-3): Peter J Wellmann. Review of sic crystal growth technology. Semiconductor Science and Technology, 33:103001, Sep 2018. URL: https://doi.org/10.1088/1361-6641/aad831, doi:10.1088/1361-6641/aad831. This article has 220 citations and is from a peer-reviewed journal.

23. (rottner1994graphiteascarbon pages 4-6): Kurt Rottner and Reinhard Helbig. Graphite as carbon source in chemical vapor deposition of α-silicon carbide. Journal of Crystal Growth, 144:258-266, Dec 1994. URL: https://doi.org/10.1016/0022-0248(94)90465-0, doi:10.1016/0022-0248(94)90465-0. This article has 23 citations and is from a peer-reviewed journal.

24. (zhang2021hotwallmocvdof pages 1-9): Hengfang Zhang. Hot-wall mocvd of n-polar group-iii nitride materials. Linköping Studies in Science and Technology. Licentiate Thesis, Jun 2021. URL: https://doi.org/10.3384/lic.diva-175502, doi:10.3384/lic.diva-175502. This article has 2 citations.

25. (sumathi2021commonissuesin pages 1-2): R. Radhakrishnan Sumathi. Common issues in the hetero-epitaxial seeding on sic substrates in the sublimation growth of aln crystals. Applied Physics A, Jul 2021. URL: https://doi.org/10.1007/s00339-021-04770-9, doi:10.1007/s00339-021-04770-9. This article has 3 citations.

26. (rottner1994graphiteascarbon pages 8-9): Kurt Rottner and Reinhard Helbig. Graphite as carbon source in chemical vapor deposition of α-silicon carbide. Journal of Crystal Growth, 144:258-266, Dec 1994. URL: https://doi.org/10.1016/0022-0248(94)90465-0, doi:10.1016/0022-0248(94)90465-0. This article has 23 citations and is from a peer-reviewed journal.
