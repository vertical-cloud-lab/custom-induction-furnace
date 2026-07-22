# Emissivity and Pyrometry Uncertainty During Induction Heating and Annealing of Metallic Samples: A Literature Review

## 1. Introduction

Non-contact temperature measurement via radiation pyrometry is essential for controlling induction heating and annealing of metallic samples, particularly steel and nickel-based superalloys. However, the accuracy of pyrometric temperature retrieval is fundamentally limited by uncertainty in the spectral emissivity of the target surface, which is itself a function of temperature, wavelength, surface condition, and processing atmosphere (suleiman2025improvingpyrometryofa pages 63-66, suleiman2023effectofdewa pages 9-10). This review summarizes the principal sources of emissivity uncertainty, the resulting pyrometry errors, and the calibration and correction methods documented in the literature.

## 2. Sources of Emissivity Uncertainty

### 2.1 Intrinsic Material Properties

The spectral emissivity of metals is governed by their electrical conductivity through the Drude model and Hagen–Rubens relations, which predict both wavelength and temperature dependence. A crossover (X-point) wavelength exists where the sign of the temperature coefficient of emissivity changes (suleiman2025improvingpyrometryofa pages 63-66, suleiman2025improvingpyrometryof pages 63-66). For nickel-based superalloys such as Inconel 625, Inconel 718, and Waspaloy, emissivity depends strongly on alloy composition, surface roughness, and the spectral range of the pyrometer. Experimental studies have confirmed that emissivity varies with temperature and that surface oxidation at elevated temperatures produces an oxide matte that modifies radiative properties (kieruj2016determinationofemissivity pages 1-2, kieruj2016determinationofemissivity pages 2-4).

### 2.2 Surface Oxidation and Thin-Film Interference

During annealing, selective oxidation of alloying elements (Mn, Si, Cr, Al) produces oxide layers of varying composition, morphology, and thickness (typically 40–320 nm for advanced high-strength steels). When the oxide film thickness is comparable to or smaller than the pyrometry wavelength, thin-film interference (constructive and destructive interference at film interfaces) produces wavelength-dependent oscillations in spectral emissivity (suleiman2025improvingpyrometryof pages 63-66, suleiman2025improvingpyrometryofa pages 63-66). The effect is strongest at shorter wavelengths (below ~2 μm) and for uniform, low-refractive-index films. At longer wavelengths where λ >> d, surface roughness and nodular oxide morphology dominate via random scattering, generally increasing emissivity (suleiman2023effectofdew pages 2-5, suleiman2023effectofdewa pages 2-5). The annealing atmosphere (dew point) controls the extent of oxidation; higher dew points promote thicker oxides and higher emissivity, particularly below 2 μm (suleiman2023effectofdew pages 2-5, suleiman2023effectofdewa pages 2-5). For austenitic stainless steels, short anneals produce thin chromium oxide layers while longer times yield iron oxide deposits over a protective sublayer, with emissivity increasing with both temperature and holding time (lassila2023effectofscale pages 64-69, lassila2023effectofscalea pages 64-69).

### 2.3 Surface Roughness and Topography

Surface roughness relative to the measurement wavelength (σ/λ) enhances multiple scattering and increases effective emissivity. This effect compounds with oxide morphology changes during processing and makes emissivity spatially and temporally variable (suleiman2025improvingpyrometryofa pages 63-66, suleiman2025improvingpyrometryof pages 63-66).

### 2.4 Environmental and Instrumental Factors

Reflected radiation from hot furnace surroundings, atmospheric absorption and emission along the optical path, incomplete filling of the pyrometer field of view, and viewing-angle dependence (significant above ~75°) all introduce additional measurement errors (grujic2023areviewof pages 4-6, giulietti2025spectralemissivitymeasurement pages 10-11). At temperatures below ~300 °C, background and reflected radiation can dominate the signal (giulietti2025spectralemissivitymeasurement pages 11-12).

## 3. Quantitative Uncertainty Estimates

Reported uncertainties depend strongly on the method and surface conditions. For steel processing, Bayesian pyrometry credibility intervals range from ±14 K to ±31 K depending on annealing dew point—far larger than the industrial targets of ±2–4 °C desired by steelmakers (suleiman2025improvingpyrometryof pages 156-160, suleiman2025improvingpyrometryofa pages 156-160). Discrepancies between ex situ and in situ emissivity measurements can produce relative temperature errors up to ~10% (suleiman2025improvingpyrometryofa pages 156-160). For general pyrometer instruments, reported measurement uncertainties are typically 1–3% (giulietti2025spectralemissivitymeasurement pages 11-11), while emissivity measurement uncertainties for specific materials can reach 3–14% for steel and up to 18% expanded uncertainty for nickel sheet (giulietti2025spectralemissivitymeasurement pages 10-11). For carbon steel Q235, emissivity uncertainty due to surface oxidation alone contributes 1.5–7.1% uncertainty in emissivity and 1.7–5.8 K uncertainty in temperature (Shi et al. 2015). At 2000 K, a surface assumed to have emissivity 0.5 must actually lie between 0.45 and 0.55 for 1% temperature accuracy (cunnington1973developmentoftechniques pages 56-61). For 316L powder steel, emissivity varied from 0.33 to 0.58 over 59–900 °C, with maximum relative combined temperature measurement uncertainty not exceeding 5.5% (Cullinan et al. 2025).

## 4. Calibration and Correction Methods

The following table summarizes the principal calibration and correction methods identified in the literature:

| Method | Principle | Advantages | Limitations | Key References |
|---|---|---|---|---|
| Blackbody reference calibration | Calibrate pyrometers/IR systems against a traceable blackbody or blackbody-equivalent source; instrument response factors are folded into calibration constants, and reflected/background radiation can be corrected if surroundings are characterized. | Traceable baseline; standard industrial practice; improves absolute accuracy; supports periodic recalibration and uncertainty control. | Does not solve process-time emissivity drift from oxidation/roughness; field conditions can differ from lab calibration; background reflections and alignment still matter. | (suleiman2025improvingpyrometryof pages 53-57, giulietti2025spectralemissivitymeasurement pages 11-12, giulietti2025spectralemissivitymeasurement pages 10-11) |
| Thermocouple cross-calibration | Adjust pyrometer emissivity or correction curves until non-contact readings match embedded or attached thermocouple temperatures under controlled conditions. | Simple and widely used; practical for alloy- and surface-specific emissivity tuning; useful for furnace and annealing trials. | Thermocouples perturb the specimen and may not represent true surface temperature during fast transients or induction heating; contact methods are difficult on moving/rotating parts. | (kieruj2016determinationofemissivity pages 2-4, kieruj2016determinationofemissivity pages 1-2, lassila2023effectofscale pages 64-69) |
| Ratio / dual-wavelength pyrometry | Infer temperature from the ratio of radiances at two wavelengths so common factors partly cancel; accuracy depends on a stable or known emissivity ratio between the two bands. | Less sensitive than single-color pyrometry to absolute emissivity, attenuation, and partial field-of-view filling; fast and practical for dynamic heating. | Not truly emissivity-independent if emissivity ratio changes with oxide growth or wavelength spacing; errors increase when surfaces are non-gray or rapidly evolving. | (suleiman2025improvingpyrometryof pages 60-63, narayanan2023aninvestigationinto pages 36-40, ren2019emissivitycalibrationmethod pages 6-8, giulietti2025spectralemissivitymeasurement pages 11-12) |
| Multi-wavelength pyrometry with polynomial emissivity models | Use 3+ wavelengths and fit temperature simultaneously with emissivity represented by linear/log-linear/polynomial/exponential wavelength functions, often by least squares. | Can compensate evolving wavelength dependence better than ratio pyrometry; can estimate both emissivity trend and temperature; suitable for complex metallic surfaces. | Sensitive to noise, model-form error, and overfitting; performance degrades when oxidation/roughness causes behavior outside the assumed emissivity model. | (narayanan2023aninvestigationinto pages 36-40, suleiman2025improvingpyrometryof pages 60-63, grujic2023areviewof pages 9-10) |
| Bayesian / stochastic pyrometry | Treat emissivity, calibration coefficients, and noise probabilistically; infer posterior temperature with MAP estimate and credibility intervals using ex situ, in situ, or conditional emissivity priors. | Explicit uncertainty quantification; handles poorly known emissivity; adaptable to dew point, alloy, and process state; can outperform deterministic methods when emissivity varies strongly. | Strongly dependent on prior quality; wide intervals remain when emissivity is weakly constrained; computationally heavier and may still miss industrial accuracy targets. | (suleiman2025improvingpyrometryof pages 156-160, suleiman2023effectofdew pages 7-9, suleiman2025improvingpyrometryofa pages 160-163, suleiman2025improvingpyrometryof pages 111-115) |
| Graphite coating method | Apply a thin high-emissivity coating with known spectral emissivity so radiometric temperature retrieval is less sensitive to the substrate’s unknown emissivity. | Effective way to impose a near-known emissivity; useful in induction-heated high-temperature metrology; simplifies inversion and uncertainty analysis. | Coating can degrade or spall at high temperature; may alter thermal behavior; not always acceptable for process samples or production parts. | (urban2022dynamicmeasurementof pages 1-4, urban2022dynamicmeasurementof pages 4-8, urban2022dynamicmeasurementof pages 14-16) |
| Virtual blackbody (wedge) method | Use a wedge/cavity geometry on the sample or fixture to create an effective emissivity near unity, providing a local blackbody-like reference for calibration or validation. | Reduces emissivity uncertainty without coating; useful for industrial strip/coil practice; provides an internal reference. | Sensitive to alignment and geometry; may be difficult to implement in compact or moving induction setups; only samples local geometry. | (narayanan2023aninvestigationinto pages 36-40) |
| Neural network / AI approaches | Use multispectral data-driven inversion to recognize emissivity behavior and estimate temperature/emissivity without prescribing a fixed analytical emissivity model. | Can capture nonlinear emissivity behavior and automate model selection; promising for online monitoring and process control. | Requires representative training data; limited interpretability; robustness outside the training domain is uncertain. | (grujic2023areviewof pages 9-10, grujic2023areviewof pages 26-27) |
| Thin-film optics / geometric optics modeling | Model emissivity changes from oxide-film thickness, refractive index, roughness, nodules, and scattering using thin-film interference, geometric optics, or hybrid ray-tracing approaches. | Physically grounded correction path for annealing steels where oxide growth dominates emissivity; explains wavelength-dependent oscillations and atmosphere effects. | Requires optical constants, oxide morphology/thickness, and often process-specific validation; difficult to use as a standalone real-time correction. | (suleiman2025improvingpyrometryof pages 63-66, suleiman2025improvingpyrometryofa pages 63-66, suleiman2023effectofdew pages 2-5, suleiman2023effectofdewa pages 2-5) |


*Table: This table summarizes the main calibration and correction approaches used to manage emissivity-driven uncertainty in pyrometry during induction heating and annealing of metals. It compares how each method works, where it helps most, and its practical limitations.*

### 4.1 Blackbody Reference Calibration

Pyrometers are calibrated against traceable blackbody sources prior to deployment, with instrument response factors grouped into a calibration constant. Periodic recalibration is standard industrial practice. The measurement model accounts for emitted, reflected, and extraneous radiation components, with reflected furnace radiation correctable if surroundings temperature is known (suleiman2025improvingpyrometryof pages 53-57).

### 4.2 Thermocouple Cross-Calibration

A direct and widely used approach involves adjusting the pyrometer emissivity setting until its reading matches a thermocouple reference temperature measured on the same sample. This method was employed for Inconel 625, Inconel 718, and Waspaloy using embedded thermocouples in blind holes (kieruj2016determinationofemissivity pages 2-4, kieruj2016determinationofemissivity pages 1-2). For annealing furnace applications, matching pyrometer and thermocouple readings provides in situ emissivity calibration (lassila2023effectofscale pages 64-69).

### 4.3 Ratio (Dual-Wavelength) Pyrometry

Two-color pyrometry estimates temperature from the ratio of spectral irradiances at two wavelengths, canceling common factors such as atmospheric absorption and partial field-of-view filling (suleiman2025improvingpyrometryof pages 60-63). Methods such as TRACE build experimentally derived reciprocal emissivity functions to improve accuracy. However, the method requires a known, stable emissivity ratio between the two wavelengths, and oxide growth can violate this assumption (narayanan2023aninvestigationinto pages 36-40).

### 4.4 Multi-Wavelength Pyrometry

Using three or more wavelengths, emissivity is modeled as a polynomial, exponential, or log-linear function of wavelength. Temperature and emissivity model coefficients are solved simultaneously using least-squares methods. The approach requires n ≥ m+2 wavelengths (where m is the polynomial order) to avoid overfitting (narayanan2023aninvestigationinto pages 36-40, grujic2023areviewof pages 9-10). Multi-wavelength methods are robust for uncontaminated surfaces but can fail when emissivity behavior is complex or rapidly evolving due to oxidation (suleiman2025improvingpyrometryof pages 60-63, suleiman2025improvingpyrometryofa pages 63-66).

### 4.5 Bayesian (Stochastic) Pyrometry

A Bayesian framework treats emissivity, calibration coefficients, and measurement noise as random variables with prior distributions. Temperature is inferred as a maximum a posteriori (MAP) estimate with credibility intervals that explicitly quantify uncertainty (suleiman2025improvingpyrometryof pages 156-160, suleiman2025improvingpyrometryofa pages 160-163, suleiman2025improvingpyrometryof pages 111-115). Multivariate normal (MVN) priors for emissivity can be constructed from ex situ or in situ measurements. In situ-based priors yielded ±21 °C credibility intervals for peak annealing temperature estimates, while conditional emissivity priors that condition on dew point and equivalent blackbody temperature vectors have been proposed to further narrow posterior widths (suleiman2023effectofdew pages 7-9, suleiman2025improvingpyrometryofa pages 160-163). Stage-specific priors (different for heating vs. soaking) are recommended to balance robustness and precision (suleiman2023effectofdew pages 7-9, suleiman2023effectofdewa pages 7-9).

### 4.6 Graphite Coating Method

Applying a thin graphite spray coating with known high emissivity (ε ≈ 0.97 ± 0.03 at 1064 nm below 2250 K) simplifies radiometric temperature retrieval in induction-heating setups by imposing a near-known emissivity boundary condition (urban2022dynamicmeasurementof pages 4-8). This approach has been used at PTB for dynamic specific-heat and emissivity measurements up to ~2000 K, though coating degradation above ~2000 K limits the usable range (urban2022dynamicmeasurementof pages 1-4, urban2022dynamicmeasurementof pages 14-16).

### 4.7 Virtual Blackbody (Wedge) Method

In industrial continuous annealing and galvanizing lines, a wedge geometry creates a virtual blackbody with effective emissivity near unity, providing an internal calibration reference. While effective, this approach is sensitive to alignment and geometric precision (narayanan2023aninvestigationinto pages 36-40).

### 4.8 Neural Network and AI Approaches

Back-propagation neural networks have been applied to multi-wavelength pyrometry data to automatically recognize linear and nonlinear emissivity models without assuming a specific functional form (grujic2023areviewof pages 9-10, grujic2023areviewof pages 26-27). Expert-system approaches using knowledge representation and decision logic have also been documented. For advanced high-strength steel coils, artificial neural networks have been used to predict spectral emissivity variations from pre-annealing surface properties, enabling on-line emissivity prediction and pyrometry updates (narayanan2023aninvestigationinto pages 36-40).

### 4.9 Physics-Based Emissivity Modeling

Thin-film optics models (using complex refractive indices and film thickness), geometric optics approximation (GOA) ray-tracing, and hybrid approaches have been developed to predict emissivity changes arising from oxide scale growth during annealing. These models can explain wavelength-dependent emissivity oscillations and atmosphere-dependent emissivity evolution, providing physics-based correction factors for pyrometry (suleiman2025improvingpyrometryof pages 63-66, suleiman2025improvingpyrometryofa pages 63-66, suleiman2023effectofdewa pages 9-10, suleiman2023effectofdew pages 9-10). Parabolic oxidation kinetics with Arrhenius-derived parameters have been coupled to emissivity regression models to predict scale growth and its effect on emissivity during stainless steel annealing (lassila2023effectofscale pages 64-69, lassila2023effectofscalea pages 64-69).

## 5. Induction Heating Specific Considerations

Induction heating introduces particular challenges and opportunities for pyrometry. The electromagnetic coupling can produce non-uniform temperature distributions, and the rapid heating rates require fast-response pyrometers. At PTB, a dedicated induction heating system (Ambrell EASYHEAT, max 6 kW, 240 kHz) was implemented for dynamic emissivity measurements with controlled drift below 150 mK/min at 1250 K, using v-grooved Nextel-painted chamber walls to reduce stray reflections (urban2022dynamicmeasurementof pages 4-8). Graphite susceptor rings can assist heating of poorly inductive samples (urban2022dynamicmeasurementof pages 4-8). The uncertainty evaluation employed adaptive Monte Carlo methods, and the dominant uncertainty contribution was from coating emissivity (~80% of the total specific heat uncertainty) (urban2022dynamicmeasurementof pages 14-16).

## 6. References (BibTeX)

The following BibTeX entries compile the key references identified in this review:

```bibtex
@article{suleiman2025improvingpyrometryof,
  author = {Suleiman, F. K.},
  title = {Improving Pyrometry of Advanced High Strength Steels During Intercritical Annealing},
  year = {2025},
  journal = {Unknown journal}
}

@article{suleiman2023effectofdew,
  author = {Suleiman, F. K. and Narayanan, N. S. and Daun, K. J.},
  title = {Effect of dew point on the evolving spectral emissivity of advanced high strength steel during intercritical annealing},
  year = {2023},
  journal = {Unknown journal}
}

@article{giulietti2025spectralemissivitymeasurement,
  author = {Giulietti, Nicola and Cosoli, Gloria and Napolitano, Rachele and Pandarese, Giuseppe and Revel, Gian Marco and Chiariotti, Paolo},
  title = {Spectral emissivity measurement for high-temperature applications: a systematic review},
  journal = {Acta IMEKO},
  year = {2025},
  volume = {14},
  number = {1},
  pages = {1--17},
  month = {Mar},
  doi = {10.21014/actaimeko.v14i1.1846},
  url = {https://doi.org/10.21014/actaimeko.v14i1.1846},
  issn = {2221-870X},
  publisher = {IMEKO International Measurement Confederation}
}

@article{urban2022dynamicmeasurementof,
  author = {Urban, David and Anhalt, Klaus},
  title = {Dynamic Measurement of Specific Heat Above 1000 K},
  journal = {International Journal of Thermophysics},
  year = {2022},
  volume = {43},
  number = {5},
  month = {Mar},
  doi = {10.1007/s10765-022-03005-0},
  url = {https://doi.org/10.1007/s10765-022-03005-0},
  issn = {0195-928X},
  publisher = {Springer Science and Business Media LLC}
}

@misc{cullinan2025methodologyfordetermination,
  author = {Cullinan, Michael and Vasilevskyi, Oleksandr and Allison, Jared},
  title = {Methodology for determination of the emissivity of metal powders and uncertainty quantification using an infrared camera and thermocouples},
  journal = {Measurement Science and Technology},
  year = {2025},
  volume = {36},
  number = {2},
  pages = {025013},
  month = {Jan},
  doi = {10.1088/1361-6501/ada4c6},
  url = {https://doi.org/10.1088/1361-6501/ada4c6},
  issn = {0957-0233},
  publisher = {IOP Publishing}
}

@article{kieruj2016determinationofemissivity,
  author = {Kieruj, Piotr and Przestacki, Damian and Chwalczuk, Tadeusz},
  title = {Determination of emissivity coefficient of heat-resistant super alloys and cemented carbide},
  journal = {Archives of Mechanical Technology and Materials},
  year = {2016},
  volume = {36},
  number = {1},
  pages = {30--34},
  month = {Dec},
  doi = {10.1515/amtm-2016-0006},
  url = {https://doi.org/10.1515/amtm-2016-0006},
  issn = {2450-9469},
  publisher = {Walter de Gruyter GmbH}
}

@article{ren2019emissivitycalibrationmethod,
  author = {Ren, Chi-Guang and Lo, Yu-Lung and Tran, Hong-Chuong and Lee, Min-Hsun},
  title = {Emissivity calibration method for pyrometer measurement of melting pool temperature in selective laser melting of stainless steel 316L},
  journal = {The International Journal of Advanced Manufacturing Technology},
  year = {2019},
  volume = {105},
  number = {1--4},
  pages = {637--649},
  month = {Aug},
  doi = {10.1007/s00170-019-04193-0},
  url = {https://doi.org/10.1007/s00170-019-04193-0},
  issn = {0268-3768},
  publisher = {Springer Science and Business Media LLC}
}

@article{shi2015effectofsurface,
  author = {Shi, Deheng and Zou, Fenghui and Zhu, Zunlue and Sun, Jinfeng},
  title = {Effect of Surface Oxidization on the Normal Spectral Emissivity of Straight Carbon Steel at 800--1100 K in Air},
  journal = {ISIJ International},
  year = {2015},
  volume = {55},
  number = {3},
  pages = {697--705},
  month = {Mar},
  doi = {10.2355/isijinternational.55.697},
  url = {https://doi.org/10.2355/isijinternational.55.697},
  issn = {0915-1559},
  publisher = {Iron and Steel Institute of Japan}
}

@article{lassila2023effectofscale,
  author = {Lassila, E.},
  title = {Effect of scale formation on the emissivity of austenitic stainless steels in an annealing furnace},
  year = {2023},
  journal = {Unknown journal}
}

@article{grujic2023areviewof,
  author = {Gruji{\'c}, Katarina},
  title = {A Review of Thermal Spectral Imaging Methods for Monitoring High-Temperature Molten Material Streams},
  journal = {Sensors},
  year = {2023},
  volume = {23},
  number = {3},
  pages = {1130},
  month = {Jan},
  doi = {10.3390/s23031130},
  url = {https://doi.org/10.3390/s23031130},
  issn = {1424-8220},
  publisher = {MDPI AG}
}

@article{narayanan2023aninvestigationinto,
  author = {Narayanan, N. S.},
  title = {An Investigation into Radiative Property Variations across Pre-Annealed Advanced High Strength Steel Coils},
  year = {2023},
  journal = {Unknown journal}
}

@article{belikov2024fastmultiwavelengthpyrometer,
  author = {Belikov, R. and Merges, D. and Varentsov, D. and Major, Zs. and Neumayer, P. and Hesselbach, Ph. and Schanz, M. and Winkler, B.},
  title = {Fast Multi-Wavelength Pyrometer for Dynamic Temperature Measurements},
  journal = {International Journal of Thermophysics},
  year = {2024},
  volume = {45},
  number = {2},
  pages = {1--12},
  month = {Feb},
  doi = {10.1007/s10765-023-03323-x},
  url = {https://doi.org/10.1007/s10765-023-03323-x},
  issn = {0195-928X},
  publisher = {Springer Science and Business Media LLC}
}

@article{ham2016insituspectralemissivity,
  author = {Ham, S. H. and Ferte, M. and Fricout, G. and Depalo, L. and Carteret, C.},
  title = {In-situ spectral emissivity measurement of alloy steels during annealing in controlled atmosphere},
  journal = {Quantitative InfraRed Thermography},
  year = {2016},
  month = {Jan},
  doi = {10.21611/qirt.2016.041},
  url = {https://doi.org/10.21611/qirt.2016.041},
  publisher = {QIRT Council}
}

@article{tapetado2016twocolorpyrometerfor,
  author = {Tapetado, Alberto and Diaz-Alvarez, Jose and Miguelez, Maria Henar and Vazquez, Carmen},
  title = {Two-Color Pyrometer for Process Temperature Measurement During Machining},
  journal = {Journal of Lightwave Technology},
  year = {2016},
  volume = {34},
  number = {4},
  pages = {1380--1386},
  month = {Feb},
  doi = {10.1109/JLT.2015.2513158},
  url = {https://doi.org/10.1109/JLT.2015.2513158},
  issn = {0733-8724},
  publisher = {Institute of Electrical and Electronics Engineers (IEEE)}
}

@article{hiramoto1999thebehaviorof,
  author = {Hiramoto, Kazuo and Uematsu, Chihiro and Tamura, Yoichi},
  title = {The Behavior of Spectral Emissivity of Metal in Oxidation Process},
  journal = {Tetsu To Hagane-journal of The Iron and Steel Institute of Japan},
  year = {1999},
  volume = {85},
  number = {12},
  pages = {863--869},
  month = {Dec},
  doi = {10.2355/tetsutohagane1955.85.12_863},
  url = {https://doi.org/10.2355/tetsutohagane1955.85.12_863},
  issn = {0021-1575},
  publisher = {Iron and Steel Institute of Japan}
}
```


*Code_block: This BibTeX block compiles the principal papers identified for emissivity and pyrometry uncertainty in steel and nickel-alloy heating and annealing. It is useful as a ready-to-import reference set for the literature review bibliography. (giulietti2025spectralemissivitymeasurement pages 10-11, giulietti2025spectralemissivitymeasurement pages 11-12, grujic2023areviewof pages 26-27, kieruj2016determinationofemissivity pages 1-2, kieruj2016determinationofemissivity pages 2-4, giulietti2025spectralemissivitymeasurement pages 7-8, urban2022dynamicmeasurementof pages 1-4, urban2022dynamicmeasurementof pages 4-8, lassila2023effectofscale pages 64-69)*

## 7. Conclusions

Emissivity uncertainty remains the dominant source of pyrometry error during induction heating and annealing of steel and nickel alloys. The primary physical mechanisms driving emissivity variability are surface oxidation (including thin-film interference), roughness evolution, and the intrinsic temperature-wavelength dependence of metallic emissivity. A range of calibration and correction methods are available, from traditional approaches (blackbody calibration, thermocouple cross-referencing) to advanced techniques (Bayesian inference, multi-wavelength pyrometry with emissivity compensation, neural networks). The most promising recent developments combine physics-based emissivity models with stochastic frameworks (Bayesian pyrometry with conditional priors) to provide both improved temperature estimates and explicit uncertainty quantification. However, achieving industrial accuracy targets (±2–4 °C) remains challenging, particularly when surface conditions evolve rapidly during processing.
