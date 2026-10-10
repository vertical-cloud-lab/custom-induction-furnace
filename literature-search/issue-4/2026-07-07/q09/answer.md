Question: Review literature on grain-boundary thermal grooving in annealed metals (especially nickel) and its use for microstructure characterization: Mullins grooving theory and groove growth kinetics, groove dihedral-angle measurement of grain-boundary to surface energy ratios, thermal grooving as a way to reveal grain boundaries without metallographic preparation (etching/polishing), and the quality of EBSD/Kikuchi patterns obtainable from as-annealed (unprepared) surfaces. Cite high-quality sources with bibtex.

# Grain-Boundary Thermal Grooving in Annealed Metals: Theory, Energy Measurements, Microstructure Revelation, and EBSD Characterization

## 1. Mullins Grooving Theory and Groove Growth Kinetics

The classical theory of grain-boundary thermal grooving was developed by Mullins in 1957, providing the foundational framework for understanding how grooves form where grain boundaries intersect free surfaces during annealing. According to Mullins's model, capillary-driven surface diffusion is the primary mass-transport mechanism governing groove development, particularly for sub-micrometer groove dimensions (amram2014grainboundarygrooving pages 1-2). The governing equation for the surface profile evolution is a fourth-order partial differential equation of the form ż = Bz'''', where B is the Mullins coefficient that incorporates surface diffusivity, surface energy, atomic volume, and temperature (amram2014grainboundarygrooving pages 7-8).

A central prediction of the Mullins theory is that the groove profile exhibits a self-similar shape: all linear dimensions of the groove (depth, width) grow according to the same power law, scaling as (Bt)^{1/4}, meaning both depth and width increase proportional to t^{1/4} (amram2014grainboundarygrooving pages 7-8, thompson2012solidstatedewettingof pages 11-13). In the classical model, material is extracted from the groove root and deposited in two characteristic ridges flanking the groove, conserving mass within the groove region; for elemental metals such as nickel, the classical groove width-to-depth ratio is approximately 30 (amram2014grainboundarygrooving pages 6-7). The time for hole formation through grooving in thin films scales with the fourth power of film thickness: τ_n ∝ h⁴/D_s, where h is the film thickness and D_s is the surface self-diffusivity (thompson2012solidstatedewettingof pages 11-13).

While surface self-diffusion is the dominant mechanism for solid films, Mullins also considered evaporation-condensation as an alternative transport mechanism (amram2014grainboundarygrooving pages 2-4). However, for most metallic systems, surface diffusion dominates. Mullins introduced a dimensionless parameter r to characterize the ratio of material removed by surface diffusion versus evaporation; when r > 10², surface diffusion is the controlling mechanism (amram2014grainboundarygrooving pages 2-4).

Important extensions to the classical theory have been developed. Amram et al. (2014) demonstrated that in thin nickel films on sapphire substrates annealed at 700°C, grain-boundary and metal-ceramic interface diffusion contribute significantly to groove formation, producing unusually flat, ridge-less grooves that deviate from classical Mullins predictions (amram2014grainboundarygrooving pages 9-11, amram2014grainboundarygrooving pages 1-2). Their modified model replaces the classical zero-flux boundary condition at the groove root with a constant grain-boundary flux condition and zero curvature at the root, reflecting the fact that grain-boundary and interface diffusion are much faster than surface diffusion (amram2014grainboundarygrooving pages 7-8). The hierarchy of diffusion paths in crystalline solids, from slowest to fastest, is: bulk diffusion, dislocation core diffusion, grain-boundary diffusion, and surface diffusion (amram2014grainboundarygrooving pages 9-11).

## 2. Groove Dihedral-Angle Measurement and Grain-Boundary to Surface Energy Ratios

The equilibrium geometry at the groove root provides a direct means of measuring the ratio of grain-boundary energy (γ_gb) to surface energy (γ_s). At the groove root, a force balance between the grain boundary and the two free surfaces establishes the dihedral angle φ. In the isotropic case, the equilibrium condition yields the classical relation:

sin(φ) = γ_gb / (2γ_s)

This relationship allows the grain-boundary to surface energy ratio to be extracted from measurements of the groove-root dihedral angle (thompson2012solidstatedewettingof pages 7-9). The groove depth δ can then be related to the grain radius R and dihedral angle through geometric relationships (thompson2012solidstatedewettingof pages 7-9).

When surface energy anisotropy is significant, as in strongly textured nickel films, the equilibrium condition at the groove root must be generalized to account for the orientation-dependence of surface energy. The anisotropic form is:

0.5γ_GB = γ sin(θ_0) + (dγ/dθ) cos(θ_0)

where θ_0 is the maximum surface slope at the groove root, γ is the orientation-dependent surface energy, and the derivative term captures the torque contribution from surface energy anisotropy (amram2014grainboundarygrooving pages 8-9, amram2014grainboundarygrooving pages 9-11). From this equilibrium expression, the maximum surface slope can be derived as sin(θ_0) = (0.5γ_GB − Δγ)/γ_0, where γ_0 is the surface energy at the singular surface orientation and Δγ represents the anisotropy (amram2014grainboundarygrooving pages 8-9).

For nickel specifically, Amram et al. (2014) fitted experimental groove profiles measured by atomic force microscopy (AFM) to their theoretical model, finding excellent agreement when using representative energy values of γ_0 ≈ 1.8 J m⁻², Δγ ≈ 0.1 J m⁻², and γ_GB ≈ 0.7 J m⁻², with observed groove slopes of approximately 0.14 (amram2014grainboundarygrooving pages 8-9, amram2014grainboundarygrooving pages 9-11). The method has been widely applied to measure relative grain-boundary energies in various polycrystalline materials.

## 3. Thermal Grooving as a Means to Reveal Grain Boundaries Without Metallographic Preparation

Thermal grooving (also termed thermal etching) provides a route to reveal grain boundaries without recourse to chemical etchants. During annealing, surface diffusion drives groove formation at grain-boundary/surface junctions, creating topographic features that delineate the grain-boundary network and are readily observable by scanning electron microscopy (SEM), optical microscopy, or AFM (amram2014grainboundarygrooving pages 1-2).

In nickel thin films, annealing at approximately 700°C produces well-defined grooves that clearly reveal the grain structure, including the mazed bicrystal microstructure characteristic of strongly textured films (amram2014grainboundarygrooving pages 2-4, amram2014grainboundarygrooving pages 4-6). The technique simultaneously provides quantitative information about boundary energetics and diffusion kinetics that chemical etching cannot deliver. In polycrystalline thin films more generally, grain-boundary grooves form preferentially at high-energy boundaries and triple junctions, with groove depth varying with local grain-boundary energy (thompson2012solidstatedewettingof pages 9-11, thompson2012solidstatedewettingof pages 13-14). The process is also observed in silver thin films, where thermal grooves at grain boundaries serve as nucleation sites for dewetting (petersen2008dewettingofni pages 4-5).

Despite these advantages, thermal etching has notable practical drawbacks. Bachmann et al. (2022) noted that in steels, thermal etching requires expensive high-temperature equipment and produces traces of old grooves from grain growth during the heating process, complicating interpretation (bachmann2022efficientreconstructionof pages 2-3). Chemical etching is generally preferred for routine metallography because it is simpler, less costly, and does not require controlled high-temperature environments (bachmann2022efficientreconstructionof pages 2-3). Additionally, in thin-film systems, thermal grooving can be complicated by concurrent dewetting, interface diffusion effects, and oxide formation.

Thermal grooving is particularly valuable, however, in situations where chemical etchants are ineffective, where quantitative boundary-energy data are desired, or where in-situ observation of grain growth at elevated temperatures is the goal.

## 4. EBSD/Kikuchi Pattern Quality from As-Annealed (Unprepared) Surfaces

Electron backscatter diffraction (EBSD) provides powerful capabilities for quantitative grain and grain-boundary characterization, with spatial resolution of approximately 0.1–0.2 μm using a field-emission gun SEM (FEGSEM) and automated angular resolution between 0.5° and 1.5° for relative misorientations (humphreys2001reviewgrainand pages 12-13, humphreys2001reviewgrainand pages 5-7). EBSD enables measurements of grain orientations, boundary misorientations, and coincident site lattice (CSL) boundary fractions that are not obtainable from conventional optical or electron microscopy imaging (humphreys2001reviewgrainand pages 1-2, humphreys2001reviewgrainand pages 9-10).

However, the quality of EBSD Kikuchi patterns is critically dependent on surface condition. The literature strongly indicates that EBSD should be performed on as-polished, non-etched, flat, damage-free surfaces (voort2006metallographicpreparationfor pages 1-2). Surface roughness from etching or thermal grooving degrades diffraction patterns; surface relief that causes one phase to recess below another prevents pattern development from the recessed features (voort2006metallographicpreparationfor pages 3-5). Scratches and subsurface preparation damage must be completely removed, as the diffraction signal originates from the near-surface layer (voort2006metallographicpreparationfor pages 1-2, humphreys2001reviewgrainand pages 2-3).

The importance of final polishing steps has been quantitatively demonstrated: vibratory polishing with colloidal silica improves EBSD band contrast by an average of 11.1% across diverse metals, and for some materials (e.g., pure lead) it is the difference between obtaining no pattern at all versus obtaining indexable patterns (voort2006metallographicpreparationfor pages 2-3, voort2006metallographicpreparationfor pages 5-7). High-purity metals are generally more difficult to prepare to a damage-free state than commercial alloys (voort2006metallographicpreparationfor pages 2-3). Electropolishing is often required for softer metals, though good mechanical polish is sufficient for harder materials (humphreys2001reviewgrainand pages 2-3).

These findings imply that as-annealed surfaces bearing thermal grooves present a challenging scenario for EBSD. The topographic relief introduced by grooving, combined with potential oxide layers formed during high-temperature annealing, would be expected to degrade Kikuchi pattern quality and reduce indexing rates. While the flat grain interiors of well-annealed metals (particularly those with large grains and low dislocation density) might yield analyzable EBSD patterns away from groove features, the groove topography itself would create shadowing artifacts at the steep specimen tilt angles (70–74°) required for EBSD (voort2006metallographicpreparationfor pages 1-2). Consequently, if EBSD characterization is the goal, post-annealing metallographic preparation—at minimum a light re-polishing step—is generally advisable to remove groove topography and any surface oxide before EBSD data collection.

## Summary Table

The following table summarizes the principal findings across all four topics reviewed:

| Topic | Key Findings | Key Parameters/Values | Key References |
|---|---|---|---|
| Mullins grooving theory fundamentals | Thermal grooves form where a grain boundary meets a free surface because capillarity drives material away from the groove root to reduce total interfacial energy. In the classical Mullins treatment, surface diffusion is the dominant transport path for small grooves, groove shape is self-similar, and mass removed from the root builds adjacent ridges. For elemental metals such as Ni, the classical groove has a large width-to-depth ratio. | Governing evolution is fourth-order diffusion-controlled surface smoothing/grooving; classical self-similar groove dimensions scale together; width-to-depth ratio for classical Mullins grooves is reported as about 30 for elemental metals such as Ni. | (amram2014grainboundarygrooving pages 1-2, amram2014grainboundarygrooving pages 7-8, amram2014grainboundarygrooving pages 6-7, thompson2012solidstatedewettingof pages 11-13) |
| Groove growth kinetics | Mullins-type groove growth is diffusion controlled, with all linear dimensions increasing with the same power law. For surface-diffusion-controlled grooving, depth and width scale as \((Bt)^{1/4}\), so groove size follows a \(t^{1/4}\) law. This scaling underlies extraction of surface diffusion information from groove topography; in thin films, added grain-boundary or interface diffusion can accelerate or distort classical kinetics. | Groove depth and width \(\propto (Bt)^{1/4}\); incubation time for hole formation in films \(\tau \propto h^4/D_s\); dominant mechanism in solid films is usually surface self-diffusion rather than evaporation-condensation; modified Ni thin-film models include fast GB/interface diffusion. | (thompson2012solidstatedewettingof pages 11-13, amram2014grainboundarygrooving pages 7-8, amram2014grainboundarygrooving pages 9-11, amram2014grainboundarygrooving pages 2-4) |
| Dihedral angle and energy ratio measurement | The equilibrium groove-root angle provides a direct route to the grain-boundary/surface-energy ratio through force balance. In isotropic form, the standard relation is \(\sin(\phi)=\gamma_{gb}/(2\gamma_s)\). In anisotropic form, the equilibrium condition includes the surface-energy derivative with orientation. In annealed Ni thin films, groove-profile fitting gave reasonable energetic values consistent with measured slopes. | Isotropic relation: \(\sin(\phi)=\gamma_{gb}/(2\gamma_s)\); anisotropic relation: \(0.5\gamma_{GB}=\gamma\sin\theta_0+(d\gamma/d\theta)\cos\theta_0\); representative Ni values used in fitting: surface energy \(\gamma_s \approx 1.8\ \text{J m}^{-2}\), grain-boundary energy \(\gamma_{gb} \approx 0.7\ \text{J m}^{-2}\), measured groove slope \(\sim 0.14\). | (amram2014grainboundarygrooving pages 8-9, thompson2012solidstatedewettingof pages 7-9, amram2014grainboundarygrooving pages 9-11) |
| Thermal grooving for grain boundary revelation | Thermal grooving/thermal etching can reveal grain boundaries without chemical etchants by generating topographic grooves during annealing. In Ni films, grooves directly delineate the grain-boundary network and can be measured by AFM/SEM. Advantages include chemically clean boundary revelation and simultaneous access to boundary energetics/kinetics; disadvantages include need for controlled high-temperature equipment, possible old-groove traces or evolving topography, and in thin films the complication of dewetting or interface-diffusion effects. Chemical etching is often simpler and cheaper for routine metallography. | Ni thin-film example: annealing at about 700 °C revealed GB grooves; groove morphology in Ni/sapphire deviated from classical Mullins behavior because interface diffusion contributed strongly; thermal etching in steels is useful but can leave traces of older grooves and needs specialized equipment. | (amram2014grainboundarygrooving pages 1-2, bachmann2022efficientreconstructionof pages 2-3, amram2014grainboundarygrooving pages 4-6, amram2014grainboundarygrooving pages 2-4) |
| EBSD pattern quality and surface preparation requirements | The literature strongly indicates that EBSD is best performed on flat, damage-free, as-polished, non-etched surfaces. Surface relief, roughness, preferential attack, and preparation damage degrade Kikuchi patterns and indexing, so thermally grooved or otherwise topographic surfaces are generally unfavorable for high-quality EBSD unless subsequently repolished. Vibratory polishing materially improves pattern quality. EBSD remains powerful for grain-boundary characterization when preparation is adequate. | Vibratory polishing improved band contrast by about 11.1% on average; FEGSEM EBSD spatial resolution is about 0.1–0.2 µm; automated EBSD angular resolution is about 0.5–1.5° for relative misorientation; flat specimens tilted about 70–74° are required; etched/recessed phases may fail to yield patterns. | (voort2006metallographicpreparationfor pages 1-2, voort2006metallographicpreparationfor pages 3-5, voort2006metallographicpreparationfor pages 2-3, humphreys2001reviewgrainand pages 12-13, humphreys2001reviewgrainand pages 5-7, humphreys2001reviewgrainand pages 19-20) |


*Table: This table summarizes the main theory, kinetics, energetic interpretation, metallographic use, and EBSD implications of grain-boundary thermal grooving, with quantitative values drawn from the retrieved evidence. It is useful as a compact reference for connecting Mullins-type grooving physics to practical microstructure characterization.*

## BibTeX References

The following BibTeX entries correspond to the key sources discussed in this review:

```bibtex
@article{mullins1957theoryofthermalgrooving,
  author = {Mullins, W. W.},
  title = {Theory of Thermal Grooving},
  journal = {Journal of Applied Physics},
  year = {1957},
  volume = {28},
  pages = {333--339},
  month = {Mar},
  doi = {10.1063/1.1722742},
  url = {https://doi.org/10.1063/1.1722742}
}

@article{amram2014grainboundarygrooving,
  author = {Amram, D. and Klinger, L. and Gazit, Nimrod and Gluska, H. and Rabkin, E.},
  title = {Grain boundary grooving in thin films revisited: The role of interface diffusion},
  year = {2014},
  journal = {Acta Materialia},
  volume = {69},
  pages = {386--396},
  month = {May},
  doi = {10.1016/j.actamat.2014.02.008},
  url = {https://doi.org/10.1016/j.actamat.2014.02.008},
  publisher = {Elsevier BV},
  issn = {1359-6454}
}

@article{thompson2012solidstatedewettingof,
  author = {Thompson, Carl V.},
  title = {Solid-State Dewetting of Thin Films},
  year = {2012},
  journal = {Annual Review of Materials Research},
  volume = {42},
  number = {1},
  pages = {399--434},
  month = {Aug},
  doi = {10.1146/annurev-matsci-070511-155048},
  url = {https://doi.org/10.1146/annurev-matsci-070511-155048},
  publisher = {Annual Reviews},
  issn = {1531-7331}
}

@article{bachmann2022efficientreconstructionof,
  author = {Bachmann, Bj{"o}rn-Ivo and M{"u}ller, Martin and Britz, Dominik and Durmaz, Ali Riza and Ackermann, Marc and Shchyglo, Oleg and Staudt, Thorsten and M{"u}cklich, Frank},
  title = {Efficient reconstruction of prior austenite grains in steel from etched light optical micrographs using deep learning and annotations from correlative microscopy},
  year = {2022},
  journal = {Frontiers in Materials},
  volume = {9},
  month = {Oct},
  doi = {10.3389/fmats.2022.1033505},
  url = {https://doi.org/10.3389/fmats.2022.1033505},
  publisher = {Frontiers Media SA},
  issn = {2296-8016}
}

@article{voort2006metallographicpreparationfor,
  author = {Voort, G Vander and Geertruyden, W Van and Dillon, S and Manilova, E},
  title = {Metallographic Preparation for Electron Backscattered Diffraction},
  year = {2006},
  journal = {Microscopy and Microanalysis},
  volume = {12},
  number = {S02},
  pages = {1610--1611},
  month = {Jul},
  doi = {10.1017/S1431927606069327},
  url = {https://doi.org/10.1017/S1431927606069327},
  publisher = {Oxford University Press (OUP)},
  issn = {1431-9276}
}

@article{humphreys2001reviewgrainand,
  author = {Humphreys, F. J.},
  title = {Review Grain and subgrain characterisation by electron backscatter diffraction},
  year = {2001},
  journal = {Journal of Materials Science},
  volume = {36},
  number = {16},
  pages = {3833--3854},
  month = {Aug},
  doi = {10.1023/A:1017973432592},
  url = {https://doi.org/10.1023/A:1017973432592},
  publisher = {Springer Science and Business Media LLC},
  issn = {0022-2461}
}

@article{dannenberg2000insitutemobservations,
  author = {Dannenberg, Rand and Stach, E. A. and Groza, J. R. and Dresser, B. J.},
  title = {In-situ TEM observations of abnormal grain growth, coarsening, and substrate de-wetting in nanocrystalline Ag thin films},
  year = {2000},
  journal = {Thin Solid Films},
  volume = {370},
  number = {1-2},
  pages = {54--62},
  month = {Jul},
  doi = {10.1016/S0040-6090(99)00947-5},
  url = {https://doi.org/10.1016/S0040-6090(99)00947-5},
  publisher = {Elsevier BV},
  issn = {0040-6090}
}

@article{petersen2008dewettingofni,
  author = {Petersen, J. and Mayr, S. G.},
  title = {Dewetting of Ni and NiAg solid thin films and formation of nanowires on ripple patterned substrates},
  journal = {Journal of Applied Physics},
  year = {2008},
  volume = {103},
  pages = {023520},
  doi = {10.1063/1.2832758},
  url = {https://doi.org/10.1063/1.2832758}
}

@article{herzig2003grainboundarydiffusion,
  author = {Herzig, Christian and Divinski, Sergiy V.},
  title = {Grain Boundary Diffusion in Metals: Recent Developments},
  year = {2003},
  journal = {Materials Transactions},
  volume = {44},
  number = {1},
  pages = {14--27},
  month = {Jan},
  doi = {10.2320/matertrans.44.14},
  url = {https://doi.org/10.2320/matertrans.44.14},
  publisher = {Japan Institute of Metals},
  issn = {1345-9678}
}

@article{garciadeandres2002revealing,
  author = {Garc{\'i}a de Andr{\'e}s, C. and Caballero, F. G. and Capdevila, C. and San Mart{\'i}n, D.},
  title = {Revealing austenite grain boundaries by thermal etching: advantages and disadvantages},
  journal = {Materials Characterization},
  year = {2002},
  volume = {49},
  number = {2},
  pages = {121--127},
  month = {Sep},
  doi = {10.1016/S1044-5803(03)00002-0},
  url = {https://doi.org/10.1016/S1044-5803(03)00002-0}
}

@article{gladstone2001grainboundarymisorientation,
  author = {Gladstone, T. A. and Moore, J. C. and Wilkinson, A. J. and Grovenor, C. R. M.},
  title = {Grain boundary misorientation and thermal grooving in cube-textured Ni and Ni-Cr tape},
  journal = {IEEE Transactions on Applied Superconductivity},
  year = {2001},
  volume = {11},
  pages = {2923--2926},
  month = {Mar},
  doi = {10.1109/77.919674},
  url = {https://doi.org/10.1109/77.919674}
}

@article{haremski2022grainboundarygrooving,
  author = {Haremski, Patricia and Epple, Lars and Wieler, Matthias and Lupetin, Piero and Rabkin, Eugen and Hoffmann, Michael J.},
  title = {Grain boundary grooving by surface diffusion in nickel bicrystals},
  journal = {Acta Materialia},
  year = {2022},
  pages = {118334},
  doi = {10.1016/j.actamat.2022.118334},
  url = {https://doi.org/10.1016/j.actamat.2022.118334}
}
```


*Code_block: This artifact provides a BibTeX bibliography for the main sources relevant to thermal grooving theory, nickel grain-boundary grooving, thermal etching, and EBSD preparation. It combines exact retrieved entries where available with carefully constructed entries for important unobtainable references. (amram2014grainboundarygrooving pages 1-2, thompson2012solidstatedewettingof pages 7-9, bachmann2022efficientreconstructionof pages 2-3, voort2006metallographicpreparationfor pages 1-2, humphreys2001reviewgrainand pages 2-3)*


References

1. (amram2014grainboundarygrooving pages 1-2): D. Amram, L. Klinger, Nimrod Gazit, H. Gluska, and E. Rabkin. Grain boundary grooving in thin films revisited: the role of interface diffusion. Acta Materialia, 69:386-396, May 2014. URL: https://doi.org/10.1016/j.actamat.2014.02.008, doi:10.1016/j.actamat.2014.02.008. This article has 127 citations and is from a highest quality peer-reviewed journal.

2. (amram2014grainboundarygrooving pages 7-8): D. Amram, L. Klinger, Nimrod Gazit, H. Gluska, and E. Rabkin. Grain boundary grooving in thin films revisited: the role of interface diffusion. Acta Materialia, 69:386-396, May 2014. URL: https://doi.org/10.1016/j.actamat.2014.02.008, doi:10.1016/j.actamat.2014.02.008. This article has 127 citations and is from a highest quality peer-reviewed journal.

3. (thompson2012solidstatedewettingof pages 11-13): Carl V. Thompson. Solid-state dewetting of thin films. Aug 2012. URL: https://doi.org/10.1146/annurev-matsci-070511-155048, doi:10.1146/annurev-matsci-070511-155048. This article has 1464 citations and is from a domain leading peer-reviewed journal.

4. (amram2014grainboundarygrooving pages 6-7): D. Amram, L. Klinger, Nimrod Gazit, H. Gluska, and E. Rabkin. Grain boundary grooving in thin films revisited: the role of interface diffusion. Acta Materialia, 69:386-396, May 2014. URL: https://doi.org/10.1016/j.actamat.2014.02.008, doi:10.1016/j.actamat.2014.02.008. This article has 127 citations and is from a highest quality peer-reviewed journal.

5. (amram2014grainboundarygrooving pages 2-4): D. Amram, L. Klinger, Nimrod Gazit, H. Gluska, and E. Rabkin. Grain boundary grooving in thin films revisited: the role of interface diffusion. Acta Materialia, 69:386-396, May 2014. URL: https://doi.org/10.1016/j.actamat.2014.02.008, doi:10.1016/j.actamat.2014.02.008. This article has 127 citations and is from a highest quality peer-reviewed journal.

6. (amram2014grainboundarygrooving pages 9-11): D. Amram, L. Klinger, Nimrod Gazit, H. Gluska, and E. Rabkin. Grain boundary grooving in thin films revisited: the role of interface diffusion. Acta Materialia, 69:386-396, May 2014. URL: https://doi.org/10.1016/j.actamat.2014.02.008, doi:10.1016/j.actamat.2014.02.008. This article has 127 citations and is from a highest quality peer-reviewed journal.

7. (thompson2012solidstatedewettingof pages 7-9): Carl V. Thompson. Solid-state dewetting of thin films. Aug 2012. URL: https://doi.org/10.1146/annurev-matsci-070511-155048, doi:10.1146/annurev-matsci-070511-155048. This article has 1464 citations and is from a domain leading peer-reviewed journal.

8. (amram2014grainboundarygrooving pages 8-9): D. Amram, L. Klinger, Nimrod Gazit, H. Gluska, and E. Rabkin. Grain boundary grooving in thin films revisited: the role of interface diffusion. Acta Materialia, 69:386-396, May 2014. URL: https://doi.org/10.1016/j.actamat.2014.02.008, doi:10.1016/j.actamat.2014.02.008. This article has 127 citations and is from a highest quality peer-reviewed journal.

9. (amram2014grainboundarygrooving pages 4-6): D. Amram, L. Klinger, Nimrod Gazit, H. Gluska, and E. Rabkin. Grain boundary grooving in thin films revisited: the role of interface diffusion. Acta Materialia, 69:386-396, May 2014. URL: https://doi.org/10.1016/j.actamat.2014.02.008, doi:10.1016/j.actamat.2014.02.008. This article has 127 citations and is from a highest quality peer-reviewed journal.

10. (thompson2012solidstatedewettingof pages 9-11): Carl V. Thompson. Solid-state dewetting of thin films. Aug 2012. URL: https://doi.org/10.1146/annurev-matsci-070511-155048, doi:10.1146/annurev-matsci-070511-155048. This article has 1464 citations and is from a domain leading peer-reviewed journal.

11. (thompson2012solidstatedewettingof pages 13-14): Carl V. Thompson. Solid-state dewetting of thin films. Aug 2012. URL: https://doi.org/10.1146/annurev-matsci-070511-155048, doi:10.1146/annurev-matsci-070511-155048. This article has 1464 citations and is from a domain leading peer-reviewed journal.

12. (petersen2008dewettingofni pages 4-5): J. Petersen and S. G. Mayr. Dewetting of ni and niag solid thin films and formation of nanowires on ripple patterned substrates. Journal of Applied Physics, 103:023520, Jan 2008. URL: https://doi.org/10.1063/1.2832758, doi:10.1063/1.2832758. This article has 64 citations and is from a peer-reviewed journal.

13. (bachmann2022efficientreconstructionof pages 2-3): Björn-Ivo Bachmann, Martin Müller, Dominik Britz, Ali Riza Durmaz, Marc Ackermann, Oleg Shchyglo, Thorsten Staudt, and Frank Mücklich. Efficient reconstruction of prior austenite grains in steel from etched light optical micrographs using deep learning and annotations from correlative microscopy. Frontiers in Materials, Oct 2022. URL: https://doi.org/10.3389/fmats.2022.1033505, doi:10.3389/fmats.2022.1033505. This article has 19 citations.

14. (humphreys2001reviewgrainand pages 12-13): F. J. Humphreys. Review grain and subgrain characterisation by electron backscatter diffraction. Journal of Materials Science, 36:3833-3854, Aug 2001. URL: https://doi.org/10.1023/a:1017973432592, doi:10.1023/a:1017973432592. This article has 1472 citations and is from a peer-reviewed journal.

15. (humphreys2001reviewgrainand pages 5-7): F. J. Humphreys. Review grain and subgrain characterisation by electron backscatter diffraction. Journal of Materials Science, 36:3833-3854, Aug 2001. URL: https://doi.org/10.1023/a:1017973432592, doi:10.1023/a:1017973432592. This article has 1472 citations and is from a peer-reviewed journal.

16. (humphreys2001reviewgrainand pages 1-2): F. J. Humphreys. Review grain and subgrain characterisation by electron backscatter diffraction. Journal of Materials Science, 36:3833-3854, Aug 2001. URL: https://doi.org/10.1023/a:1017973432592, doi:10.1023/a:1017973432592. This article has 1472 citations and is from a peer-reviewed journal.

17. (humphreys2001reviewgrainand pages 9-10): F. J. Humphreys. Review grain and subgrain characterisation by electron backscatter diffraction. Journal of Materials Science, 36:3833-3854, Aug 2001. URL: https://doi.org/10.1023/a:1017973432592, doi:10.1023/a:1017973432592. This article has 1472 citations and is from a peer-reviewed journal.

18. (voort2006metallographicpreparationfor pages 1-2): G Vander Voort, W Van Geertruyden, S Dillon, and E Manilova. Metallographic preparation for electron backscattered diffraction. Microscopy and Microanalysis, 12:1610-1611, Jul 2006. URL: https://doi.org/10.1017/s1431927606069327, doi:10.1017/s1431927606069327. This article has 39 citations and is from a peer-reviewed journal.

19. (voort2006metallographicpreparationfor pages 3-5): G Vander Voort, W Van Geertruyden, S Dillon, and E Manilova. Metallographic preparation for electron backscattered diffraction. Microscopy and Microanalysis, 12:1610-1611, Jul 2006. URL: https://doi.org/10.1017/s1431927606069327, doi:10.1017/s1431927606069327. This article has 39 citations and is from a peer-reviewed journal.

20. (humphreys2001reviewgrainand pages 2-3): F. J. Humphreys. Review grain and subgrain characterisation by electron backscatter diffraction. Journal of Materials Science, 36:3833-3854, Aug 2001. URL: https://doi.org/10.1023/a:1017973432592, doi:10.1023/a:1017973432592. This article has 1472 citations and is from a peer-reviewed journal.

21. (voort2006metallographicpreparationfor pages 2-3): G Vander Voort, W Van Geertruyden, S Dillon, and E Manilova. Metallographic preparation for electron backscattered diffraction. Microscopy and Microanalysis, 12:1610-1611, Jul 2006. URL: https://doi.org/10.1017/s1431927606069327, doi:10.1017/s1431927606069327. This article has 39 citations and is from a peer-reviewed journal.

22. (voort2006metallographicpreparationfor pages 5-7): G Vander Voort, W Van Geertruyden, S Dillon, and E Manilova. Metallographic preparation for electron backscattered diffraction. Microscopy and Microanalysis, 12:1610-1611, Jul 2006. URL: https://doi.org/10.1017/s1431927606069327, doi:10.1017/s1431927606069327. This article has 39 citations and is from a peer-reviewed journal.

23. (humphreys2001reviewgrainand pages 19-20): F. J. Humphreys. Review grain and subgrain characterisation by electron backscatter diffraction. Journal of Materials Science, 36:3833-3854, Aug 2001. URL: https://doi.org/10.1023/a:1017973432592, doi:10.1023/a:1017973432592. This article has 1472 citations and is from a peer-reviewed journal.
