## Task 1. Verification of the 43 findings

I checked the two text extractions and visually inspected the downloaded compiled PDFs, including Figs. 1–8 and S1–S10. For external hardware facts, I used current National Instruments product documentation: [USB-6000](https://www.ni.com/docs/en-US/bundle/usb-6000-specs/page/specs.html), [NI-9265](https://www.ni.com/en/shop/hardware/current/model-ni-9265), [NI-9203](https://www.ni.com/docs/en-US/bundle/ni-9203-specs/page/specs.html), and [cDAQ-9174](https://www.ni.com/en/shop/hardware/compactdaq-chassis/model-cdaq-9174). I also recomputed the repeatability statistics from Table S1.

### Compact verdict table

| No. | Verdict | One-line justification |
|---:|---|---|
| 1 | **CONFIRMED** | Main p. 2 says all reported nickel anneals used continuous flow, while Table S1 lists calibration and characterized nickel runs as “no-flow.” |
| 2 | **CONFIRMED** | Main p. 5 gives “approximately 10 μm to 90 μm”; Fig. 7 says “approximately 20 to 90 μm” for the YSZ comparison. |
| 3 | **CONFIRMED** | The abstract attributes full-thickness spanning to “deep thermal grooves,” while the body and Fig. 5 attribute it to grain boundaries. |
| 4 | **CONFIRMED** | Main p. 5 describes BN as a graphite–alumina barrier; Fig. 8 visibly places BN between tantalum and the alumina support. |
| 5 | **CONFIRMED** | The documents repeatedly claim a 2500 °C/45 min run, but the highest supplied trace reaches 2344 °C and Table S1 has no YSZ linkage. |
| 6 | **CONFIRMED** | The text claims 1400–1500 °C for metal charges, while the documented nickel data stop at 1400 °C. |
| 7 | **CONFIRMED** | The fit and Fig. S4 label values of 0.43–0.74 as mA, impossible as the stated 4–20 mA loop current; the plotted quantity is evidently mislabeled or differently scaled. |
| 8 | **OVERSTATED/MISJUDGED** | “Only requirement” is imprecise, but the later four-item list mixes an interface requirement with ordinary capacity/configuration constraints rather than presenting four equivalent retrofit requirements. |
| 9 | **CONFIRMED** | “Links each specimen/result” is false: one Fig. 4 specimen lacks a surviving log, and the Fig. 3 specimen is not linked in Table S1. |
| 10 | **CONFIRMED** | “Not attached to any of these flanges” followed by “resting on a retaining ring of a KF40 flange” is confusing and conflicts with the later alumina-tube/PTFE support description. |
| 11 | **CONFIRMED** | The SI drawing visibly specifies 86.2 mm height and 59.85 mm ID, versus “approximately 3 in” and “2.5 in” in the main text. |
| 12 | **CONFIRMED** | “A cup body and a lidded cap” is malformed terminology for the visibly separate crucible body and lid. |
| 13 | **CONFIRMED** | “Relative to the pyrometer” has no coherent comparison target in the sapphire-transmittance sentence. |
| 14 | **CONFIRMED** | The sentence grammatically joins both the quartz tube and lower vacuum hardware to the upper pyrometer housing; Fig. 1 shows the intended two-ended topology. |
| 15 | **CONFIRMED** | “Grains to coarsen on refractory ceramics” uses the wrong preposition. |
| 16 | **OVERSTATED/MISJUDGED** | The sentence is compressed but interpretable: high temperature enables growth, while vacuum/inert gas prevents oxidation; this is wording ambiguity, not nonsense. |
| 17 | **CONFIRMED** | The comparison is between naming conventions but reads as an alloy comparison, and “Ni … nickel charges” is redundant. |
| 18 | **OVERSTATED/MISJUDGED** | Repeated “geometry” is clumsy, but “modular” is later defined through an interchangeable coil/sample assembly context; not a substantive defect. |
| 19 | **CONFIRMED** | “Such an anneal” immediately follows discussion of 1200 °C/12 h, but Fig. 6 is 1300 °C/20 h. |
| 20 | **CONFIRMED** | NI specifies the USB-6000 as 8 analog inputs, 4 digital I/O, and no analog-output channels; it cannot supply the stated 0–5 V AO. |
| 21 | **CONFIRMED** | NI identifies the 9265 as a current-output module and the 9203 as a current-input module; the BOM reverses them, and the USB-commanded cDAQ signal chain is not coherently described. |
| 22 | **NOT CHECKABLE** | The quoted Fig. 3 provenance issue cannot be established from the PDFs alone; verification needs the original image file, alleged source file, hashes, specimen metadata, and run/preparation records. |
| 23 | **CONFIRMED** | The documents explicitly state ultrasonic cleaning for Fig. 5 but only “straight from the furnace” for EBSD samples, leaving EBSD cleaning ambiguous. |
| 24 | **OVERSTATED/MISJUDGED** | “USA-sourced” can accurately mean bought from East Coast Induction in the USA; it does not necessarily claim that CEIA manufactured the generator in the USA. |
| 25 | **NOT CHECKABLE** | The 0.5 psi statement is present, but the photo does not establish cracking pressure; the valve model/datasheet or a calibration record is needed. |
| 26 | **CONFIRMED** | Fig. 8 visibly labels the block width as 25.5 mm, while the caption’s “two 25.5 mm … blocks” leaves the measured dimension unstated. |
| 27 | **CONFIRMED** | Fig. S10(a) gives 1700 °C/10 h without identifying the furnace or linking it to a run; it matches neither documented comparison condition. |
| 28 | **OVERSTATED/MISJUDGED** | “70,068×” is conspicuously precise, but exact SEM displayed magnification can legitimately come from instrument metadata; it is not defective absent evidence that it was invented. |
| 29 | **NOT CHECKABLE** | The universal “Every failure mode” claim cannot be tested from the reported examples; it requires the complete configuration survey/failure log. |
| 30 | **NOT CHECKABLE** | “Fully assembled … 13 mm tall” is present, but photographs and listed partial dimensions do not determine the seating depth reliably; direct measurement or a dimensioned section is needed. |
| 31 | **NOT CONFIRMED** | Its rationale says every reported nickel anneal used flow, but Table S1 itself shows multiple no-flow runs; optionality is therefore not contradicted in the claimed way. |
| 32 | **CONFIRMED** | The same circular alumina pieces are called “discs,” “sample-surrounding sheets,” “sheets,” and “spacer disc.” |
| 33 | **OVERSTATED/MISJUDGED** | “Turbo pumping station,” “turbopump,” and “roughing pump” need not be synonyms, and “gauge” is a normal short form; only “pressure sensor” versus “vacuum gauge” merits a minor consistency check. |
| 34 | **NOT CONFIRMED** | In the compiled main PDF, the in-text KF40 gloss occurs on p. 2 before the Fig. 1 caption in normal reading order; the hypothesized float-order defect did not occur. |
| 35 | **NOT CONFIRMED** | This item calls itself a “decision, not defect”; RF in a technical title and a broad application-oriented title are editorial choices, not demonstrated inconsistencies. |
| 36 | **CONFIRMED** | Lowercase “teflon” appears twice; use the trademark “Teflon” or, preferably, the material name PTFE if accurate. |
| 37 | **CONFIRMED** | The listed passed checks do pass: figure/section counts and pointers agree, the GEN subtotal is $16,487, and the repeatability values recompute to mean 1201.1875 °C, sample SD 1.3282 °C, CV 0.1106%. |
| 38 | **CONFIRMED** | At commit c149c59, the README names absent `paper.tex`, `archive/`, `PLAN.md`, `supplementary/`, Table S3, and S1–S12; all but one of the Makefile’s listed figure scripts return 404 at those paths. |
| 39 | **CONFIRMED** | The “only requirement … monotonic analog” claim appears in the abstract, introduction, system description, and conclusion. |
| 40 | **OVERSTATED/MISJUDGED** | The no-preparation claim is repeated heavily, but repetition between body and captions is partly necessary because captions should stand alone; it is mainly an editorial compression opportunity. |
| 41 | **CONFIRMED** | “10⁻⁶ to 10⁻⁸ Torr” is decreasing numerical order and reads awkwardly; “10⁻⁸ to 10⁻⁶ Torr” is clearer. |
| 42 | **OVERSTATED/MISJUDGED** | Mixed SI and US customary units are not inherently erroneous for US-sourced hardware, although adding metric equivalents would improve reproducibility. |
| 43 | **CONFIRMED** | The hand-clamp claim occurs in Fig. 1, construction, and conclusions; one non-caption occurrence could be removed. |

### Notes on verdicts other than CONFIRMED

**No. 8.** The defect is real but less stark than “one versus four requirements.” The sentence “Because its only requirement is a monotonic analog power-control input” plainly needs qualification. However, the later list includes adequate RF power, liquid cooling, and isolation, which are compatibility and implementation conditions rather than alternative signal-interface requirements. “Its only generator-control interface requirement…” would resolve it.

**No. 16.** I would edit this, but not label it nonsensical. Suggested logic: “Grain growth requires temperatures of 1400–1500 °C; high vacuum or an inert atmosphere is used to suppress oxidation.”

**No. 18.** “The coil is modular” is not self-explanatory, but the article later uses “modular” for hand-clamped vacuum hardware and interchangeable assemblies. Ask whether the coil itself is interchangeable; otherwise delete that adjective.

**No. 20.** The manufacturer evidence is decisive. NI’s current USB-6000 specification identifies eight analog-input channels and no analog outputs. The closest model names with analog output include USB-6001/6002/6003 and the older USB-6008/6009 families. The actual unit/model must be checked, not silently guessed.

**No. 21.** NI’s module directions are unambiguous: NI-9265 is a four-channel current **output** module; NI-9203 is an eight-channel current **input** module. Also, the cDAQ-9174 is a USB chassis controlled by a host computer. Thus “the DAQ device’s 0–5 V analog output drives” this cDAQ set is not a sufficient or plausible description of the documented chain. A wiring diagram identifying the command source, conversion stage, module channels, external loop supply, and logged variable is needed.

**No. 22.** I could verify that the displayed Fig. 3 is a Kikuchi pattern, but not its specimen identity, anneal history, or byte identity. Those are file-level provenance claims outside the supplied document set.

**No. 24.** CEIA is an Italian company, but Table S2 names East Coast Induction (USA) as the source. Replace “USA-sourced” with “purchased from a US distributor” if that is the intended economic/procurement point.

**No. 25.** The photograph confirms a component at the stated location, not its cracking pressure. The BOM also says the valve used in the build came from the BYU project support center, so supplier/model traceability is especially important.

**No. 28.** Retain 70,068× only if copied from the acquisition metadata and meaningful for the exported image. Otherwise report a rounded nominal magnification and rely on the 1 μm scale bar, which is the metrologically useful quantity.

**No. 29.** The conclusion generalizes beyond the evidence shown. If the complete adverse-reaction survey supports it, cite/link that survey directly; otherwise use “The failures we documented were contact reactions…”.

**No. 30.** The stated body height is 6.5 mm, while lid dimensions include 4 and 6 mm stepped heights, but those numbers cannot simply be summed because the lid seats inside the body. A section view with assembled overall height would settle it.

**No. 31.** There may still be a reproducibility problem for the explicitly flow-controlled cohorts, but that is different from the finding’s claim. The BOM should distinguish “optional for vacuum-only operation” from “required for controlled continuous-flow protocols.”

**No. 33.** Keep distinctions among the pumping station, turbopump, and roughing pump. Standardize only labels that refer to the same device. Fig. 1’s “pressure sensor” and the body’s “wide-range vacuum gauge” appear to denote the same item and should be reconciled.

**No. 34.** The source-level concern is theoretically possible with LaTeX floats, but verification was requested against the compiled documents. The compiled ordering is acceptable.

**No. 35.** “Reactive-metal” may overstate the demonstrated material scope, but nickel annealing under oxygen-controlled conditions and a ceramic extension can motivate a broader title. That is a scope/framing decision, not an internally provable defect.

**No. 40.** Preserve complete information in captions. Reduce nearby body/conclusion duplication rather than making captions dependent on surrounding prose.

**No. 42.** The better recommendation is not “metric only,” but “give SI first and parenthetical source-unit equivalents,” especially for the coil and relief pressure.

---

## Task 2. Defects the review missed

### 1. Unresolved editorial placeholder in the author-contribution statement

- **Location:** Main text, p. 7, Author Contributions.
- **Quote:** “— provisional: Sterling G. Baird: Conceptualization, Software, Investigation, Writing – original draft.”
- **Why it matters:** “Provisional” is visibly unfinished submission text. The LaTeX source at the reviewed commit also contains `\todo{confirm CRediT roles}` immediately before it, although the TODO is suppressed in the clean PDF. Finalize all Contributor Roles Taxonomy roles and delete the placeholder and leading dash.

### 2. Literal placeholder journal in reference 17

- **Location:** Main text, p. 7, reference 17.
- **Quote:** “F. Suleiman, ‘Improving pyrometry of advanced high strength steels during intercritical annealing,’ Unknown journal (2025).”
- **Why it matters:** “Unknown journal” cannot remain in a submitted bibliography. The title resolves to a University of Waterloo repository item, so the correct document type, institution, year, and persistent URL/identifier should replace the fabricated journal field.

### 3. Two books are misclassified as ArXiv articles

- **Location:** Main text, pp. 7–8, references 8 and 20.
- **Quotes:**
  - “V. Rudnev, D. Loveless, R. L. Cook, and M. Black, ‘Handbook of induction heating,’ ArXiv (2017), 10.1201/9781420028904.”
  - “E. Rapoport and Y. Pleshivtseva, ‘Optimal control of induction heating processes,’ ArXiv (2006), 10.1201/9781420019490.”
- **Why it matters:** Both DOI landing records identify CRC Press books, not ArXiv papers. Reference 8 also appears to have the wrong year: the DOI is associated with the 2002 *Handbook of Induction Heating*. These are concrete bibliography-type errors that a citation-integrity pass should catch.

### 4. “High-purity annealing environment” is claimed without a purity measurement

- **Location:** Main p. 6, Conclusions; related description on p. 2.
- **Quotes:** “The full system and workflow deliver a high-purity annealing environment.” / “This helped avoid oxidation during heating.”
- **Why it matters:** The manuscript reports pressure, nominal argon flow, and successful EBSD, but no residual-gas analysis, oxygen partial pressure, argon grade/purity, leak rate, or post-anneal composition. EBSD indexability is evidence of a sufficiently clean surface, not a quantitative demonstration of environmental “high purity.” Use “low-oxygen annealing environment” if supported, or add a defined purity metric.

### 5. The cost comparison changes denominator and is not a “small fraction” at the low end

- **Location:** Main pp. 1 and 6; SI pp. 11–12.
- **Quotes:** “Commercial vacuum induction furnaces that meet these requirements are closed, turn-key systems costing $50k to $200k or more.” / “This is a small fraction of turn-key cost…” / “directly reusable at a small fraction of turn-key cost.”
- **Why it matters:** From Table S2, the required listed generator package is $16,487 and the non-optional listed retrofit/consumable items total approximately $21,249, for approximately **$37,736** before shipping, tax, unpriced tantalum/BN, and optional flow control. That is about **75% of $50,000**, not naturally a “small fraction,” although it is about 19% of $200,000. The text sometimes appears to compare the $16.5k generator package alone and elsewhere the full system. State the actual as-built total and define what is excluded.

### 6. The ratio-pyrometer emissivity claim is too broad and conflicts with the later qualification

- **Location:** Main pp. 2 and 4.
- **Quotes:** “This provides a non-contact signal that is robust to emissivity changes…” / “By extension, absolute specimen temperature still depends on emissivity and surface condition.”
- **Why it matters:** Two-color pyrometry reduces sensitivity to absolute emissivity only under assumptions about the emissivity ratio at the two wavelengths, optical transmission, and target filling. The second sentence acknowledges some limitation, but the first reads as unconditional. Replace “robust to emissivity changes” with a qualified statement such as “less sensitive than single-wavelength pyrometry to gray-body emissivity changes, subject to wavelength-dependent emissivity and optical-path assumptions.” The manufacturer describes the ISR 6 as a ratio pyrometer; that alone does not justify emissivity independence.

### 7. The claimed 90 μm YSZ grain size is not quantitatively demonstrated in Fig. 7

- **Location:** Main p. 5, body and Fig. 7.
- **Quotes:** “grain growth from approximately 10 μm to 90 μm…” / “coarsened the grains from approximately 20 to 90 μm. The red traces are the microscope software’s multi-grain size measurements.”
- **Why it matters:** The visible red line annotations are approximately 384–866 μm multi-grain intercepts, not individual 90 μm grain measurements. No intercept count, conversion method, number of fields, sample size, mean, dispersion, or uncertainty is reported. Even after resolving the 10-versus-20 μm contradiction, the figure does not by itself substantiate “90 μm.” Report the grain-size method and summary statistics or soften the numeric claim.

### 8. The opening claim of “more than one hundred logged anneals” is not auditable from the supplied linkage

- **Location:** Main p. 4; SI pp. 9–10.
- **Quotes:** “The furnace has completed more than one hundred logged anneals…” / “Table S1: Specimen ↔ thermal-history linkage for the runs used in the manuscript’s validation sections.”
- **Why it matters:** Table S1 is explicitly selective and contains fewer than two dozen rows, including missing logs. The claim may be true, but the provided manuscript set gives no run index or count supporting “more than one hundred.” Link a complete run manifest or state that Table S1 is a selected subset and cite the manifest.

### 9. Fig. S10’s plural wording implies unsupported common provenance

- **Location:** SI p. 8, Fig. S10 caption.
- **Quote:** “(a) YSZ after a 1700 °C / 10 h anneal. (b) An induction-annealed YSZ specimen, showing the equiaxed grain structure. The tantalum-susceptor sample assembly used for these anneals is drawn in the main text (Fig. 8).”
- **Why it matters:** “These anneals” grammatically says both panels used the tantalum-susceptor assembly, but panel (a)’s furnace is unidentified and its condition matches neither the stated 1600 °C/228 h box-furnace comparison nor the 2500 °C/45 min induction run. This extends existing finding 27: the caption itself makes an unsupported shared-configuration claim. Identify each panel’s furnace, specimen, run, and role separately.

I did **not** count two tempting but invalid “misses”: the 1204.2 °C repeatability point is not a statistical contradiction because it was retained and the reported sample SD/CV are correct; and IFrun080/081 numbering does not prove chronological order unless the authors define run IDs that way.

---

## Task 3. Critique of `ai_edit_review_prompt.md`

### (a) What it does well

1. **It forces document-wide reconciliation.** The extract-and-reconcile tables are the strongest part. They successfully surfaced the flow contradiction, 10-versus-20 μm discrepancy, mislabeled command units, and claimed-versus-demonstrated temperature limits.
2. **It demands verbatim evidence and locations.** That makes findings auditable and allowed this independent check without the LaTeX line numbers.
3. **It distinguishes knowable corrections from author questions.** “Never guess at facts only the authors can know” is good scientific-integrity guidance.
4. **It explicitly includes captions, SI, and cross-references.** Many high-value defects occurred at those boundaries rather than within isolated body paragraphs.
5. **It asks for a completeness note.** The original report appropriately disclosed missing raw-log and citation-content checks.

### (b) Blind spots

1. **Submission residue and placeholders.** The prompt catches sentence artifacts but does not explicitly search for `TODO`, “provisional,” “TBD,” “Unknown,” draft notes, suppressed clean/draft differences, or placeholder metadata. It missed both “provisional” and “Unknown journal.”
2. **Bibliographic integrity.** “Citation fit” asks whether a source supports a claim, but not whether each reference’s authors, title, venue, year, DOI, and document type agree with authoritative metadata. It missed two books labeled “ArXiv” and the incomplete thesis citation.
3. **Claim operationalization.** It checks claimed-versus-demonstrated maxima, but not whether qualitative claims such as “high-purity,” “low-cost,” “robust,” or “more than one hundred” have a defined metric and auditable denominator.
4. **Statistical reporting sufficiency.** It checks arithmetic but not whether grain-size measurements report method, sample size, uncertainty, field selection, or the distinction between a multi-grain intercept and individual grain diameter.
5. **Cost-accounting consistency.** Cost is a numeric quantity, but the prompt does not require reconciling subtotal versus full-system cost, optional/unpriced items, tax/shipping exclusions, and the denominator behind comparative language.
6. **Source-versus-compiled-output checks.** The prompt does not explicitly require comparing draft and clean builds for hidden TODOs or checking whether float-order concerns actually occur in the compiled PDF. That contributed to false positive No. 34 and the missed suppressed TODO before “provisional.”

### (c) Ambiguous, redundant, or false-positive-prone instructions

- **“Read every sentence in isolation”** is useful for syntax but encourages false positives when meaning depends on the preceding sentence. No. 16 is an example.
- **“Err on the side of reporting: a false alarm costs the author ten seconds”** undervalues review burden and encourages speculative findings such as No. 28, No. 33, and No. 42.
- **“List them ALL as author-check questions” for physical configurations** produces a large unactionable inventory and dilutes actual contradictions. Ask only when configuration is inconsistent, consequential, unsupported by a figure/BOM, or required for reproduction.
- **“Suspiciously specific details”** risks treating legitimate instrument metadata as AI invention. Precision should be checked against provenance and significant figures, not flagged merely because it is specific.
- **“Flag bare ‘see supplementary material’ where a figure number is checkable”** is too categorical. A broad SI pointer is appropriate when several sections or files support a statement.
- Pass 2 numbers and Pass 3 contradiction sweep overlap substantially. That redundancy is acceptable operationally, but the prompt should say Pass 3 is a targeted independent recheck rather than another unrestricted contradiction search.

### (d) Few-shot examples: helpful, but overfit

The examples help by making subtle failure modes concrete, especially “relative to the pyrometry,” 4–20 mA scaling, full-thickness grooves, and figure-count drift. They clearly improved recall on this manuscript.

They also overfit the reviewer. Several reported findings closely reproduce the examples rather than arising from a neutral audit, while generic defects were missed: “provisional,” “Unknown journal,” books labeled ArXiv, undefined “high-purity,” and incomplete cost accounting. The prompt advertises repository-specific examples as “real defects,” which anchors the model toward finding those exact motifs. For reuse, retain two or three examples from unrelated scientific domains and label them as illustrations, not calibration targets.

### (e) Six wording-level prompt edits

1. **Replace lines 23–25:**

> Produce an evidence-ranked findings report. Report a candidate only when you can quote the relevant text and explain a concrete failure mode. Separate verified defects from author-verification questions; do not inflate the defect count with merely unusual wording.

2. **Replace the opening instruction of Pass 1:**

> Read every sentence first in context, then test whether it remains grammatically and logically coherent. Flag an isolated reading only when the local context does not resolve the ambiguity.

3. **Add after Pass 1:**

> **Submission-residue check.** Search source and compiled outputs for TODO/TBD/FIXME markers, “draft,” “provisional,” “unknown,” placeholder citations or identifiers, commented author queries, dummy values, suppressed notes, and differences between clean and draft builds. Treat visible unresolved metadata as high priority.

4. **Replace “Citation fit” with:**

> **Citation and bibliography integrity.** For every citation, check both claim support and bibliographic identity. Resolve the DOI, PMID, ISBN, or repository record where available and compare authors, title, venue or document type, year, volume, pages, and identifier. Flag placeholders, retracted sources, books labeled as articles/preprints, and citations whose source type or metadata is wrong. State when full-text support could not be checked.

5. **Replace the physical-configuration instruction:**

> Extract physical-configuration claims, but report only those that (i) contradict another passage, figure, BOM, or drawing; (ii) omit a connection or component needed for reproduction or safety; or (iii) cannot be reconciled with the supplied evidence. Put any remaining author-verification checklist in an appendix, not in the prioritized defect count.

6. **Add to claimed-versus-demonstrated checks:**

> For qualitative claims such as “high-purity,” “low-cost,” “robust,” “accurate,” “reproducible,” and “more than N,” identify the operational definition, denominator, exclusions, measurement method, sample size, uncertainty, and best supporting artifact. For image-derived quantities, verify that the displayed annotations and stated measurement method actually yield the reported statistic.

### Limitations

This was a document and figure audit, not a validation of the raw run logs, microscopy metadata, gas purity, valve calibration, specimen identities, or complete configuration survey. Manufacturer documentation resolves the NI module-direction and USB-6000 capability issues, but the actual installed model and wiring still require inspection. No inferential statistical test was appropriate; the only numerical reanalysis was direct arithmetic from Table S1.

### Discretionary analytical decisions

- Treated the compiled PDFs as controlling for layout/float-order findings and the text extractions as searchable copies.
- Used four verdict classes exactly as requested; assigned **OVERSTATED/MISJUDGED** when a wording issue existed but the reported interpretation or severity was too strong.
- Counted an author-check item as **CONFIRMED** only when the quoted ambiguity or evidence gap was itself demonstrable; otherwise used **NOT CHECKABLE**.
- Used current NI manufacturer documentation as the authoritative source for device capabilities and module direction.
- Recomputed repeatability with the sample standard deviation and conventional coefficient of variation, matching the manuscript’s reported values.
- Did not treat a visually unusual point as an “outlier defect” without a prespecified outlier rule or evidence of exclusion.
- Consolidated closely related new issues, such as full-system cost denominator changes, rather than multiplying findings by every occurrence.