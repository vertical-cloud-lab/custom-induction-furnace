# Assessment

Your observation is physically credible. The most economical explanation is a **conjunction**, not a single mechanism: (i) the prolonged near-solidus anneal recrystallized the sheet and eliminated the mechanically damaged near-surface layer that polishing ordinarily must remove; (ii) the hot, graphite-enclosed environment maintained a sufficiently low oxygen potential that no thick NiO scale formed; and (iii) rapid high-temperature surface transport locally smoothed or faceted the free surface. The result is unusual mainly because these conditions were achieved accidentally as the final processing step, not because EBSD fundamentally requires polishing.

| Candidate mechanism | Assessment/rank | Literature-supported basis | Key caveat/test |
|---|---|---|---|
| Removal of deformation by recrystallization/annealing | **Most likely primary cause** | EBSD/channeling is dominated by the near-surface region (~10–100 nm), and successful patterns require a flat surface free of mechanically damaged layers; polishing is normally needed mainly to remove the deformed/Beilby layer. A long soak near the Ni melting point should annihilate dislocations and consume any prior surface deformation, leaving a diffraction-quality skin if oxidation/topography are not severe. (goldstein2018characterizingcrystallinematerials pages 5-6) | Strong claim is justified, but only if the starting surface was not deeply roughened or chemically altered. Test by comparing EBSD quality before vs after a light intentional abrasion, followed by identical anneal; cross-check near-surface strain with HR-EBSD/ECCI if available. |
| Low oxygen potential / NiO suppression or reduction in graphite/CO environment | **Very likely co-primary cause** | Metallic Ni is thermodynamically favored over NiO under sufficiently reducing gas ratios; bulk-Ni oxidation requires high oxidant/reductant ratios, and graphite-containing hot zones can plausibly buffer oxygen via CO/CO2. Literature on Ni surface evolution also shows that residual oxygen strongly affects faceting and transport, so suppressing oxide is important for preserving an EBSD-active metallic surface. (wolf2021thermodynamicassessmentof pages 5-6, wolf2021thermodynamicassessmentof pages 4-5, thompson2012solidstatedewettingof pages 23-25) | Your exact crucible pO2 and CO/CO2 were not measured, so phrase this as a plausible thermodynamic explanation rather than a demonstrated atmosphere composition. No universal NiO thickness cutoff is defensible from the available literature; pattern loss depends on beam energy, oxide structure, continuity, and roughness. Test with XPS/AES depth profiling, Raman for NiO, and controlled graphite-vs-non-graphite or static-vacuum-vs-flowing-Ar comparisons. |
| High-temperature surface diffusion, faceting, and possible evaporation-condensation smoothing | **Likely important secondary cause** | Ni surface atom mobility is high far above the Tammann temperature, and literature on Ni at high temperature shows atmosphere-sensitive surface transport, faceting, and shape evolution. Near-melting anneals can therefore remove small-scale asperities or reorganize the topmost surface into locally low-energy facets that still diffract well, even if the macroscopic surface is not metallographically polished. (wolf2021thermodynamicassessmentof pages 8-9, thompson2012solidstatedewettingof pages 23-25) | Faceting can help or hurt: local flat terraces may improve patterns, but large facet tilts can change effective EBSD geometry. Distinguishing surface-diffusion smoothing from evaporation-condensation requires morphology data. Test with AFM/white-light profilometry before/after anneal, and vary temperature/time to look for transport-controlled scaling. |
| Thermal desorption / sublimation cleaning of adsorbates | **Plausible auxiliary factor** | High-temperature vacuum/inert annealing will desorb weakly bound contaminants and reduce adventitious surface species, which can improve EBSD indirectly by exposing cleaner metallic Ni. This is consistent with general vacuum-surface practice, though the direct evidence retrieved here is weaker than for deformation removal and oxide suppression. (thompson2012solidstatedewettingof pages 23-25) | Likely not sufficient by itself if an oxide film or damaged layer remains. Test by measuring surface C/O with XPS/AES immediately after anneal and after air exposure; compare direct-transfer vs deliberate air-aging before EBSD. |
| Adverse thermal grooving / topography at grain boundaries | **Important caveat, not an enabling mechanism** | EBSD is highly sensitive to topography, and thermal grooving is expected during long high-temperature anneals by capillarity-driven surface transport. Literature on annealed Ni/Ni-alloy tapes explicitly links grain-boundary misorientation and thermal grooving, consistent with your observed deep grooves outlining grains. (goldstein2018characterizingcrystallinematerials pages 5-6) | Grooves can cause local shadowing, variable effective tilt, band blurring, and unindexed points or boundary-position bias. Quantify with AFM/profilometry or cross-sectional SEM/FIB; report that indexing may be preferentially lost at grooves and that boundary traces may be topographic as well as crystallographic. |
| Native/grown oxide thickness tolerance | **Constraint to acknowledge, not rankable as a single mechanism** | Available evidence supports that nanometre-scale surface films can degrade channeling/EBSD, but the retrieved literature does not justify a single critical NiO thickness applicable to all instruments and beam conditions. Surface condition, crystallinity, continuity, and roughness all matter. (goldstein2018characterizingcrystallinematerials pages 5-6) | Best practice is to avoid a hard cutoff claim. Recommend XPS/AES + Raman to identify oxide state/thickness qualitatively, and correlate those data with pattern quality under fixed SEM voltage/current/binning. |
| Crucible/atmosphere comparison strategy | **Recommended discriminating experiment** | Because both oxygen potential and surface transport are atmosphere-sensitive, side-by-side anneals can separate mechanisms more cleanly than post hoc interpretation alone. Graphite is expected to change both chemistry and transport relative to alumina-only or metal foil enclosures. (thompson2012solidstatedewettingof pages 23-25, wolf2021thermodynamicassessmentof pages 5-6) | Run controlled comparisons: graphite crucible vs non-graphite enclosure; dynamic Ar vs sealed vacuum; deliberate O2/H2O leakage; shorter vs longer soak. Pair EBSD with XPS/AES, Raman, and AFM/profilometry to link chemistry/topography directly to pattern quality. |


*Table: This table ranks the most plausible reasons your as-annealed nickel surfaces produced directly indexable EBSD patterns and pairs each mechanism with the strongest literature basis and the most useful validation tests. It also highlights the main caveats, especially oxide uncertainty and thermal-groove-induced mapping bias.*

## 1. Mechanisms

### (a) Removal of near-surface deformation — primary mechanism

This is the strongest explanation. EBSD/channeling information is generated in only a shallow near-surface volume—approximately 10–100 nm, depending on beam energy and material. Surface condition is therefore critical: abrasive preparation can leave a plastically deformed or “Beilby” layer that suppresses diffraction and normally must be removed chemically or electrochemically. Surface topography likewise competes with weak crystallographic contrast. A 12–40 h treatment at 1200–1325 °C will recrystallize Ni and provide ample recovery time to annihilate near-surface dislocations, leaving an undeformed crystalline skin without requiring a subsequent polish (Goldstein et al., DOI **10.1007/978-1-4939-6676-9_29**). (goldstein2018characterizingcrystallinematerials pages 5-6)

This mechanism explains why the observation is compatible with coarse 8×8 detector binning: the relevant surface volume is not merely “smooth enough,” but highly crystalline, strain-relieved, and composed of large grains, so the bands and zone axes remain strong. The equiaxed grains and annealing twins expected in recrystallized Ni are consistent with this interpretation.

### (b) Low oxygen potential and suppression/removal of NiO — co-primary mechanism

Vacuum followed by nominally pure flowing Ar does not, by itself, prove an oxide-free surface: ppm-level O₂/H₂O in Ar and outgassing can oxidize hot Ni. The **closed graphite crucible**, however, is important. Hot carbon scavenges oxygen-bearing species and establishes CO/CO₂ equilibria; when CO₂/CO and H₂O/H₂ ratios are sufficiently low, metallic Ni is thermodynamically favored over NiO. Thermodynamic calculations for bulk Ni show that oxidation requires strongly oxidizing gas ratios—reported values are on the order of CO₂/CO or H₂O/H₂ above roughly 50–60 under the studied high-temperature reforming conditions—whereas more reducing mixtures stabilize Ni⁰ (Wolf, DOI **10.1039/D1RA01856F**). (wolf2021thermodynamicassessmentof pages 5-6, wolf2021thermodynamicassessmentof pages 4-5)

Thus, pre-existing NiO may have dissociated or been reduced by carbon/CO, while new scale growth was suppressed. This is a plausible inference, not a demonstrated furnace-gas composition: the local oxygen fugacity inside the crucible was not measured, and the published equilibrium calculations concern specified reforming mixtures rather than your exact Ar–graphite–alumina enclosure.

A thin native oxide formed during transfer through air is not inconsistent with excellent patterns. EBSD electrons can traverse nanometre-scale films, although the oxide adds diffuse scattering and can itself diffract if crystalline. There is **no defensible universal critical NiO thickness**: tolerance depends on accelerating voltage, oxide continuity and crystallinity, roughness, detector sensitivity, and the required indexing confidence. Dorri et al. demonstrated EBSD/channeling through amorphous nano-thick oxide layers on 316L steel, illustrating that a nanometre film need not eliminate crystallographic contrast (DOI **10.1017/S1431927616011612**). Avoid assigning a numerical NiO cutoff without direct thickness–pattern-quality measurements.

### (c) Surface diffusion, faceting, and evaporation–condensation — likely secondary mechanism

At your temperatures, Ni surface mobility is enormous. The bulk-Ni Tammann temperature is about 581 °C, far below the 900–1400 °C treatments; atom transport is therefore rapid. Classic measurements directly established Ni surface self-diffusion and its relationship to surface energy (Maiya and Blakely, DOI **10.1063/1.1709399**). High-temperature Ni-film studies further show that surface-diffusion anisotropy, residual oxygen, and atmosphere control edge retraction and facet development (Thompson, DOI **10.1146/annurev-matsci-070511-155048**). (thompson2012solidstatedewettingof pages 23-25, wolf2021thermodynamicassessmentof pages 8-9)

Capillarity-driven surface diffusion can erase short-wavelength asperities and produce broad, locally flat low-energy terraces. Evaporation–condensation may contribute near the melting point, especially during 12–40 h soaks, but should be described cautiously unless mass loss, redeposition, or vapor-pressure calculations are presented. Faceting is not synonymous with global planarization: a faceted surface can give excellent local EBSD while having substantial height and slope variation over longer distances.

### (d) Desorption and other effects

High-temperature vacuum/inert annealing will remove water, hydrocarbons, and other weakly bound adsorbates. This is a reasonable auxiliary “thermal cleaning” mechanism, but it cannot by itself remove a plastically damaged layer or a stable thick oxide. Prefer **thermal desorption/cleaning** over “sublimation cleaning” unless measurable Ni or contaminant sublimation is demonstrated.

Contact with alumina discs may also help mechanically by shielding the faces from gas-borne deposits and suppressing macroscopic distortion. Conversely, it could cause local alumina transfer or reactions at contact points, so face-to-face differences should be checked.

## 2. Precedent and degree of novelty

There is substantial **adjacent precedent**, although the precise claim “bulk Ni removed from a furnace and mapped by EBSD with literally no grinding, polishing, etching, or ion cleaning” is sparsely documented.

* In-situ heating EBSD necessarily reuses an exposed surface through annealing cycles. Nakamichi, Humphreys, and Brough mapped recrystallization in IF steel by in-situ EBSD (DOI **10.1111/j.1365-2818.2008.02006.x**). This demonstrates that an EBSD-capable surface can survive annealing, although the initial surface had been prepared.
* Wu et al. performed in-situ EBSD on recrystallizing Ni–5W coated-conductor substrate material (DOI **10.1017/S143192762002485X**). Again, this is close Ni-alloy precedent but not proof of zero initial preparation.
* Annealed, cube-textured Ni and Ni-alloy tapes are routinely characterized by EBSD in coated-conductor research. Gladstone et al. specifically correlated grain-boundary misorientation with thermal grooving in cube-textured Ni/Ni–Cr tape (DOI **10.1109/77.919674**), directly paralleling your grooves. Reviews of textured Ni substrate processing include EBSD-based characterization after high-temperature recrystallization annealing (Bhattacharjee et al., DOI **10.1007/s10853-006-1416-6**).
* Vannozzi et al. characterized annealed cube-textured Ni–Cu–Co substrates by EBSD (DOI **10.1016/j.actamat.2009.10.006**), another close materials precedent, although conventional papers often do not state with enough precision whether any final cleaning or polishing preceded EBSD.

Accordingly, the defensible claim is: **direct EBSD from an annealed metallic surface has clear precedent, including Ni-alloy tapes and in-situ annealing experiments, but furnace-out, completely preparation-free bulk Ni appears unusual and is rarely highlighted as a surface-preparation result.** Do not call it unprecedented without a broader systematic review; “not commonly reported” or “not generally relied upon” is safer.

## 3. Limits and caveats

### Oxide and air exposure

* Do not equate a good Ni-indexed pattern with a chemically oxide-free surface. A discontinuous or nanometre-scale native oxide can transmit enough electrons for the underlying Ni pattern.
* Conversely, a thicker, rough, crystalline, or compositionally variable NiO scale will increase diffuse scattering, reduce band contrast, and may generate overlapping NiO patterns. The practical limit must be calibrated on your instrument.
* Because specimens were exposed to air between furnace and SEM, describe the surface as **free of an EBSD-obscuring oxide scale**, not necessarily oxide-free.
* Useful measurements are angle-resolved XPS or AES depth profiling, Raman spectroscopy for NiO, and pattern-quality versus controlled air-aging time. Direct inert/vacuum transfer would distinguish furnace condition from the post-exposure native film.

### Carbon and crucible contamination

Graphite can lower oxygen potential but can also supply carbonaceous vapor or particulates. Ni catalyzes carbon reactions, and carbon can dissolve at high temperature and segregate during cooling. A thin amorphous-carbon film may merely attenuate EBSD; graphite particles, carbide-like reaction products, or carbon-induced roughness can cause local non-indexing. Check C 1s by XPS/AES, Raman D/G bands, EDS at deposits, and—if bulk uptake matters—combustion analysis or SIMS. Ni–C equilibrium and cooling history should be considered before claiming chemically pristine Ni.

### Thermal grooving and map bias

The deep grooves are expected from capillarity-driven grain-boundary grooving, with kinetics controlled by surface diffusion and possibly evaporation–condensation. They are both evidence of strong surface transport and a limitation. EBSD is sensitive to competing topographic contrast and local geometry (Goldstein et al., DOI **10.1007/978-1-4939-6676-9_29**). (goldstein2018characterizingcrystallinematerials pages 5-6)

At grooves and steep facets:

* the effective specimen tilt and pattern center vary;
* incident electrons or emitted backscatter electrons can be shadowed;
* patterns may be blurred, displaced, or absent;
* two neighboring grains can contribute near a boundary;
* apparent boundary position can shift relative to the true boundary;
* cleanup routines may incorrectly fill unindexed groove pixels from the adjacent majority grain.

Consequently, maps can preferentially omit boundary-adjacent material, underestimate boundary length or small-grain area, inflate apparent grain size, and bias boundary-character distributions if poor-quality boundaries are systematically excluded. Report the raw indexing rate, band contrast/pattern quality, confidence metric, and unindexed-pixel distribution before cleanup. Overlaying the map on forescatter or secondary-electron images is particularly important.

Grooves spanning a substantial fraction of a nominal 100 µm thickness also raise a separate issue: they may no longer be passive surface markers but may alter sheet connectivity or indicate incipient grain-boundary separation. Cross-sectional SEM/FIB and profilometry should distinguish an equilibrium groove from a crack, void, or liquid-assisted penetration feature.

### Faceting and orientation bias

Facets can enhance local pattern quality by presenting atomically smoother terraces, but facets with unfavorable slopes can move out of the detector’s optimal angular range. If facet type correlates with crystallographic orientation, indexing success becomes orientation-dependent, biasing texture measurements. Test this by plotting indexing rate and pattern quality against orientation and by measuring local slopes with AFM, confocal microscopy, or white-light interferometry.

### Palladium

The same general argument applies to Pd—recrystallization, low oxygen affinity, and rapid high-temperature surface transport—but Pd is nobler and less prone to stable bulk oxide formation than Ni under these conditions. Therefore, successful preparation-free Pd EBSD is not, by itself, evidence that the Ni surfaces were oxide-free.

## 4. Suggested manuscript wording

> The strong EBSD patterns obtained without post-anneal metallographic preparation are attributed to the combined effects of recrystallization and thermal surface conditioning. Because electron-channeling information is generated within only approximately 10–100 nm of the surface, the prolonged near-solidus anneal removes the mechanically damaged near-surface layer that polishing ordinarily must eliminate, while the low oxygen potential established by the evacuated, Ar-flowing, graphite-enclosed environment plausibly suppresses an EBSD-obscuring NiO scale (Goldstein et al., DOI 10.1007/978-1-4939-6676-9_29; Wolf, DOI 10.1039/D1RA01856F). (goldstein2018characterizingcrystallinematerials pages 5-6, wolf2021thermodynamicassessmentof pages 5-6, wolf2021thermodynamicassessmentof pages 4-5)
>
> At these temperatures rapid Ni surface diffusion can additionally smooth short-wavelength roughness and produce low-energy facets, although the associated grain-boundary grooving introduces local tilt and shadowing that can reduce indexing immediately adjacent to boundaries (Maiya and Blakely, DOI 10.1063/1.1709399; Thompson, DOI 10.1146/annurev-matsci-070511-155048; Gladstone et al., DOI 10.1109/77.919674). (thompson2012solidstatedewettingof pages 23-25, wolf2021thermodynamicassessmentof pages 8-9)

## Key references

1. Goldstein, J. I. et al., *Characterizing Crystalline Materials in the SEM*, in **Scanning Electron Microscopy and X-Ray Microanalysis**. DOI: **10.1007/978-1-4939-6676-9_29**.
2. Wolf, M., “Thermodynamic assessment of the stability of bulk and nanoparticulate cobalt and nickel during dry and steam reforming of methane,” *RSC Advances* 11, 18187–18197 (2021). DOI: **10.1039/D1RA01856F**.
3. Thompson, C. V., “Solid-State Dewetting of Thin Films,” *Annual Review of Materials Research* 42, 399–434 (2012). DOI: **10.1146/annurev-matsci-070511-155048**.
4. Maiya, P. S. and Blakely, J. M., “Surface Self-Diffusion and Surface Energy of Nickel,” *Journal of Applied Physics* 38, 698–704 (1967). DOI: **10.1063/1.1709399**.
5. Gladstone, T. A. et al., “Grain boundary misorientation and thermal grooving in cube-textured Ni and Ni–Cr tape,” *IEEE Transactions on Applied Superconductivity* 11, 2923–2926 (2001). DOI: **10.1109/77.919674**.
6. Dorri, M. et al., “Characterization of amorphous oxide nano-thick layers on 316L stainless steel by electron channeling contrast imaging and electron backscatter diffraction,” *Microscopy and Microanalysis* 22, 997–1006 (2016). DOI: **10.1017/S1431927616011612**.
7. Nakamichi, H., Humphreys, F. J. and Brough, I., “Recrystallization phenomena in an IF steel observed by in situ EBSD experiments,” *Journal of Microscopy* 230, 464–471 (2008). DOI: **10.1111/j.1365-2818.2008.02006.x**.
8. Wu, X. et al., “In situ EBSD study on the microstructural transformation of the Ni5W substrate for coated conductors,” *Microscopy and Microanalysis* 27, 36–43 (2021). DOI: **10.1017/S143192762002485X**.
9. Bhattacharjee, P. P., Ray, R. K. and Upadhyaya, A., “Nickel base substrate tapes for coated superconductor applications,” *Journal of Materials Science* 42, 1984–2001 (2007). DOI: **10.1007/s10853-006-1416-6**.
10. Vannozzi, A. et al., “Development and characterization of cube-textured Ni–Cu–Co substrates for YBCO-coated conductors,” *Acta Materialia* 58, 910–918 (2010). DOI: **10.1016/j.actamat.2009.10.006**.