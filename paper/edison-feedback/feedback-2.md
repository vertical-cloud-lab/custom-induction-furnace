<!-- Edison ANALYSIS task 6f4d2804-3c2d-4d53-b3b2-13bb0483bd5a (iteration 2) -->

# HardwareX review report: induction-annealing retrofit manuscript

## Bottom line

The manuscript has the right core story for *HardwareX*: a useful retrofit that turns an induction generator into a computer-controlled, vacuum-capable, pyrometer-feedback annealing platform. The draft already covers most required section headings, but it is **not submission-ready yet** because the reproducible package is still incomplete in four places: **repository/compliance metadata, BOM completeness, build reproducibility, and validation depth**.

The strongest publishable angle is **not** “we used an old furnace,” but **“we provide a transferable modernization stack for any induction generator with an analog power-control interface.”** Right now that claim is plausible, but it needs tighter evidence and tighter writing.

## 1. Completeness and quality versus HardwareX section requirements

### 1.1 Specifications table
**Current status:** Present, but still weak in several fields.

**What works now**
- Hardware name, subject area, hardware type, control input, max temperature, vacuum level, temperature measurement, chamber, crucible/susceptor, and coil geometry are all present in the draft (`paper.md`, lines 30–49).
- The table distinguishes the **current reproducible build** (CEIA Power Cube 6 kW + Master Controller v3+) from the **legacy LEPEL prototype**.

**What is missing or weak**
- **Open-source license** is still `[TODO]`.
- **Total cost** is still `[TODO]`.
- **Source file repository** is still `[TODO]` and currently does not have a DOI.
- The table would be stronger if it reported **control resolution/range** more explicitly, for example DAQ output range, analog input scaling, pyrometer range, and generator analog-input standard.
- If available, add **heating-rate envelope**, **maximum soak duration demonstrated**, and **sample envelope** (max crucible OD / max usable sample size).

**Action**
- Finalize the three compliance-critical entries: license, cost, DOI.
- Add 2–4 practical operating specs that matter to a reproducer, not just headline specs.

### 1.2 Hardware in context
**Current status:** Conceptually strong, but still under-cited and a bit too internal.

**What works now**
- The draft clearly states the application: reactive-metal annealing and grain growth near 1400–1500 °C under high vacuum (`paper.md`, lines 53–58).
- It makes the intended contribution explicit: remote power control, closed-loop temperature control, vacuum integration, and a graphite susceptor/crucible (`paper.md`, lines 60–76).
- It already frames the CEIA system as the reproducible build and LEPEL as historical prototype (`paper.md`, lines 78–88).

**What is weak**
- It needs a more formal **prior-art comparison**: what open hardware or commercial systems already exist, and exactly what gap this design fills.
- The sentence “the same control software, vacuum chamber, pyrometer feedback, crucible, and work-coil geometry transfer from one induction generator to another” is the manuscript’s biggest claim, but the paper currently shows only narrative support, not a compact technical argument.
- The cost claim “roughly an order of magnitude cheaper” needs either a cited commercial benchmark or a cautious rewrite.

**How to improve**
- Add a short comparison paragraph or table with 3 categories:
  1. commercial vacuum induction annealing furnaces,
  2. open furnace/annealing systems that are not induction-based,
  3. induction generators sold without integrated vacuum/feedback automation.
- State the exact reproducibility boundary: **this paper does not reproduce the RF generator internals; it reproduces the control, sensing, vacuum, fixturing, and sample-heating integration around a compatible generator**.
- Replace vague value language with testable criteria: “compatible generators must expose an analog power-control input with monotonic response over the usable power range and must support the chosen coil/chiller combination.”

### 1.3 Hardware description
**Current status:** Good skeleton, but the level of engineering detail is not yet enough for independent rebuilding.

**What works now**
- The five-subsystem structure is sensible and matches HardwareX expectations (`paper.md`, lines 97–125).
- The graphite crucible/susceptor section is important and should stay (`paper.md`, lines 127–138).
- The extracted schematics support the block-level description (`schematic_induction_furnace.md`; `schematic_support_stand.md`).

**What is weak**
- The hardware description still lacks dimensions, interfaces, and signal paths in enough detail.
- The control section mentions LabVIEW, DAQ, PID, and email alerts, but does not yet document the **actual control architecture**. Readers need a signal-flow description: setpoint source → AO scaling/current conversion → generator input → pyrometer output → AI scaling → controller logic.
- The vacuum section needs the actual connection stack in order: quartz tube → flange/window → bellows → gauge → T-station → vent/backfill branch.
- The crucible section needs the actual geometry drawing and support-stack dimensions.

**Action**
- Add one figure that is a clean system architecture diagram with labeled interfaces:
  - analog out to generator
  - pyrometer analog out to DAQ/PLC
  - cooling-water loop
  - vacuum line
  - optical path
- Add a small table of critical dimensions and interfaces.

### 1.4 Design files summary
**Current status:** Present, but not compliant yet.

**What works now**
- The draft lists the major design assets: LabVIEW VIs, MATLAB plotting script, coil drawing, schematics, temperature-control wiring, KF40 overpressure ring STEP file, and a placeholder for crucible drawings (`paper.md`, lines 140–154).

**What is missing or weak**
- Every license field is still `[TODO]`.
- The **graphite crucible machining drawing is missing**, which is a major reproducibility gap.
- The design file paths point to native/proprietary formats in several places (`.vi`, `.pptx`, `.oxps`) without open/exported counterparts.
- Non-LabVIEW readers cannot inspect the logic unless the VIs are exported to PDF/PNG.

**Action**
- For every proprietary source file, add one human-readable exported companion:
  - LabVIEW `.vi` → block diagram PDF/PNG
  - PPTX schematics → PDF or SVG
  - OXPS coil drawing → PDF
- Add the missing crucible drawing.
- Deposit all files in a DOI-minted repository and point the table there.

### 1.5 Bill of materials
**Current status:** Usable draft, but not reproducible enough for submission.

**What works now**
- The manuscript already adopts the HardwareX 7-column BOM format (`paper.md`, lines 156–181).
- The extracted parts list contains real vendor names and several prices for retrofit parts and consumables (`parts_list.md`).

**What is weak**
- The most important line items remain unresolved: generator, controller, chiller, DAQ, turbo pump, and several vacuum-hardware totals.
- Some entries are too grouped for reproducibility, especially “KF40 flanges, clamps, centering rings, optical window” as one set.
- Some sources are vague (“eBay / OEM”, “see parts list”, “—”).
- Currency and quote year are missing.
- The BOM does not yet distinguish **must-have** items from **alternatives/legacy options**.

**Action**
- Expand grouped entries into procurement-ready lines.
- Add manufacturer part numbers wherever possible.
- Separate “canonical reproducible build” from “acceptable substitutes.”

### 1.6 Build instructions
**Current status:** Present, but too condensed for a first-time builder.

**What works now**
- The six-step structure is logical (`paper.md`, lines 184–206).
- Coil geometry corrections and support-stand component counts are already captured in the supporting files.

**What is missing or weak**
- The build section still reads like a summary, not a build manual.
- There are no stepwise photographs yet.
- The control-wiring step is too compressed; for safety and reproducibility it needs a real wiring diagram with terminal names and scaling details.
- The coil-forming step needs tubing OD/wall, bend method, spacing method, and cooling connections.
- The quartz-tube/window sealing method currently offers multiple options (overpressure ring + clamp, or Torr-Seal) without a clear statement of which configuration is the **reference build**.

**Action**
- Pick one reference configuration and document it in full.
- Treat alternatives as side notes, not as equal first-class build paths.

### 1.7 Operation instructions
**Current status:** Solid starting point, derived from a real SOP.

**What works now**
- The operation sequence is credible and matches the extracted SOP (`SOP_induction_200901.md`).
- Important warnings, such as not venting while the turbo is spinning, are already captured in both the SOP and manuscript.

**What is weak**
- The operation section should distinguish **startup prerequisites**, **normal run**, **shutdown**, and **abort/emergency stop**.
- It should include the pyrometer lower detection limit noted in the alternate SOP: “pyrometer does not recognize temperatures < 700 °C” (`SOP_alternate.md`, lines 35–38), because this affects how ramp initiation is handled.
- It should define the operator checks before energizing RF: vacuum threshold, cooling flow confirmation, coil/sample alignment, chamber clearance, pyrometer alignment.

**Action**
- Convert the SOP prose into a concise numbered operational workflow with a separate boxed emergency procedure.

### 1.8 Validation and characterization
**Current status:** The weakest scientific section at present.

**What works now**
- The draft correctly identifies the needed validation classes: calibration, ramp/soak profile, control performance, SEM, and EBSD (`paper.md`, lines 228–253).
- The repository reportedly contains 100+ runs across multiple materials, which is a real strength if curated well.

**What is missing or weak**
- No actual validation figures or quantitative analysis are included yet.
- No uncertainty, repeatability, or control-performance statistics are reported.
- No direct linkage is made between a specific thermal history and a specific microstructure dataset.

**Action**
- This section needs real data reduction and figure production before submission. More detail below.

### 1.9 Safety
**Current status:** Good content, but it should be more systematic.

**What works now**
- High voltage/RF, vacuum, thermal, and lockout-tagout hazards are all mentioned (`paper.md`, lines 255–267).
- The SOP provides vivid operational hazard context, including conductive objects near the coil and turbo-pump venting risks.

**What is weak**
- Safety should explicitly include:
  - water/electricity interaction,
  - quartz implosion / fracture hazard,
  - inert-gas asphyxiation risk if used in enclosed spaces,
  - hot graphite and possible oxidation on venting,
  - sample melt-through / contamination of the pump line,
  - EMI risk to nearby electronics and instrumentation.
- Safety interlocks and recommended PPE are not summarized cleanly.

**Action**
- Add a hazard table with columns: hazard, failure mode, consequence, mitigation.

### 1.10 Ethics / declarations / closing matter
**Current status:** Incomplete.

**What works now**
- Ethics statement is present and adequate in principle (`paper.md`, lines 268–271).

**What is missing or weak**
- CRediT roles are still `[TODO]`.
- Competing interests are still `[TODO]`.
- Funding is incomplete.
- The data availability statement is weak until the repository has a DOI.

**Action**
- These are easy to finish but mandatory.

## 2. Is the retrofit/modernization framing convincing?

### Short answer
**Yes, mostly. But it becomes convincing only if you sharply define what is portable, what is not, and show at least one compact piece of evidence for transferability.**

### What already works
The draft makes the right strategic move by anchoring the reproducible build on the **current CEIA Power Cube 6 kW + Master Controller v3+** while retaining the **LEPEL** only as developmental history. That is the correct choice. If you lean too hard on the vintage LEPEL, the paper risks reading like a one-off resurrection project. HardwareX wants something another lab can actually reproduce.

The best part of the current framing is this implicit claim:
- the reproducible object is the **modernization layer**,
- not the generator internals.

That is a legitimate HardwareX contribution.

### Where the argument is still soft
Right now “generator-agnostic” is more asserted than demonstrated. A reviewer could reasonably ask:
- What exactly must a compatible generator provide?
- Does monotonic analog input suffice, or must the response be near-linear?
- How much retuning is needed when changing generators?
- Are the coil geometry and sample envelope really portable, or only portable within a narrow range of induction heads/frequencies?
- Is the pyrometer/control stack independent of generator frequency and EMI environment, or was it tuned for one setup?

### How to strengthen it
#### A. Define compatibility in engineering terms
Add a short boxed subsection or table titled **Generator compatibility requirements**. For example:
- external analog power-control input accepted by the generator/controller,
- monotonic mapping between analog command and delivered heating response over the usable range,
- water-cooled induction head/coil support for the documented coil dimensions,
- sufficient RF power to reach target temperatures for the documented crucible/sample stack,
- safe electrical isolation between DAQ/control path and generator interface,
- availability of cooling and line power required by the selected generator.

#### B. Explicitly define what must be recalibrated after porting
State that on a new generator, the following must be re-established:
- analog command scaling,
- power-to-temperature calibration,
- PID gains,
- coil/sample alignment,
- max safe ramp rate,
- any generator-specific interlock behavior.

This helps the generator-agnostic claim sound honest rather than magical.

#### C. Add one transferability figure or table
Best option: a simple 2-column comparison of the legacy LEPEL and current CEIA implementations:
- analog control interface,
- frequency range,
- max power,
- control signal scaling,
- same pyrometer? same chamber? same crucible? same support stand? same control concept?
- what changed during migration?

That table would make the portability argument concrete.

#### D. Tighten the title and phrasing
Current title is good, but consider language that emphasizes the portable layer. For example:
- **Retrofitting a commercial RF induction generator with open, computer-controlled vacuum annealing and pyrometer-feedback for reactive-metal grain growth**
- or
- **A transferable control, sensing, and vacuum retrofit for induction-generator-based annealing of reactive metals**

The second is less catchy but more aligned with the actual contribution.

## 3. Is the bill of materials reproducible? What is essential to fill in?

### Short answer
**Not yet.** It is close enough to rescue, but the current BOM would still frustrate a reproducer trying to buy parts.

### Essential missing items
These must be filled before submission:

1. **Generator package cost and source**
   - CEIA Power Cube 6 kW
   - Master Controller v3+
   - required heating head if separate
   - recirculating chiller
   - transformer, if required for local line voltage
   - quote year and whether price is quote, invoice, or estimate

2. **DAQ exact model and interface parts**
   - exact NI DAQ model
   - any current-loop interface hardware or resistor/shunt/signal conditioner used to produce/measure 4–20 mA
   - connector/terminal hardware

3. **Turbo-pump package**
   - exact pump/station model
   - gauge/controller if separate
   - bellows, adapters, and KF hardware needed for the documented configuration

4. **Optical path hardware**
   - exact pyrometer model used in the canonical build
   - lens / stand-off / mount details if relevant
   - optical window dimensions and material

5. **Quartz tube and crucible dimensions**
   - tube OD/ID/wall and cut length used in the reference build
   - graphite stock dimensions and resulting crucible dimensions

6. **Cooling-water hardware**
   - tubing, fittings, hose barbs, clamps, manifold pieces, and any flow requirements

7. **Consumables and wear parts**
   - O-rings, Torr-Seal, graphite cement, replacement quartz tube, spare window, graphite stock

### What needs structural improvement
#### A. Break out lumped vacuum entries
“KF40 flanges, clamps, centering rings, optical window” should become separate lines unless there is a fixed kit with a vendor SKU.

#### B. Add manufacturer part numbers
A HardwareX BOM is much stronger when it includes exact identifiers. Vendor name alone is not enough.

#### C. Mark substitutes cleanly
Use the BOM for the canonical build only. Put substitutes in notes or supplementary tables. Do not mix prototype, rejected import path, and reproducible build in one table.

#### D. Add costing conventions
State:
- all costs in USD,
- quote/invoice year,
- whether shipping/tax is included,
- whether institutional surplus/used prices were used.

### Suggested BOM split
- **Core purchased platform**: generator, controller, head, chiller, transformer.
- **Retrofit hardware**: DAQ, pyrometer, vacuum hardware, support stand, window hardware, fittings.
- **Fabricated/custom parts**: coil, crucible, mounts, brackets.
- **Consumables**: graphite stock, repair cement, quartz tube, O-rings, epoxy.

## 4. Validation: what analyses, figures, and controls make this publishable?

This is the section that will decide whether the paper feels like a hardware note or a publishable HardwareX article.

### 4.1 Minimum publishable validation package
I would aim for **five figure panels or five standalone figures**.

#### Figure 1. System overview figure
A labeled photograph or composite:
- generator/controller,
- chiller,
- coil,
- quartz chamber,
- pyrometer line-of-sight,
- vacuum station,
- DAQ/control computer.

This is partly descriptive, but HardwareX reviewers like a clean “what am I looking at?” figure.

#### Figure 2. Power-command to temperature calibration
Use the canonical generator/build.

**Recommended analysis**
- For a fixed sample/crucible geometry, measure steady-state temperature at several analog command values spanning the useful range.
- Repeat each setting at least **n = 3** independent runs if feasible.
- Report mean ± SD steady-state temperature.
- Fit a simple model only if justified by the data. Do not assume linearity if the curve bends.
- If a linear region is what matters operationally, show that region explicitly.

**What to include**
- x-axis: analog command (mA or scaled percent)
- y-axis: pyrometer temperature (°C)
- error bars: between-run SD
- optional second axis: inferred generator output power if available

**Controls / caveats**
- Keep coil geometry, crucible, optical alignment, vacuum level, and sample type fixed.
- State pyrometer lower valid temperature range and calibration assumptions.

#### Figure 3. Representative ramp/soak profile with control error
Take one representative anneal, probably Ni at ~1200 °C if that is your canonical process.

**Recommended analysis**
- Plot setpoint and measured temperature versus time.
- Show ramp segment, approach to setpoint, and soak.
- Quantify:
  - rise time,
  - overshoot,
  - settling time,
  - soak mean temperature,
  - soak SD or RMS error,
  - maximum absolute deviation during soak.

This turns “closed loop worked” into numbers.

#### Figure 4. Repeatability / reproducibility across runs
This is the missing control most drafts forget.

**Recommended analysis**
- Run the same programmed thermal profile at least 3 times on the same setup.
- Compare achieved soak temperature and integrated time-above-threshold.
- Overlay the temperature traces or summarize them in a table.

**Metrics**
- soak mean temperature across runs,
- between-run SD,
- coefficient of variation if useful,
- drift over long soaks if available.

If you can’t do 3 new runs, use archived runs only if they are truly same-profile, same geometry, same material, same sensor setup. Be explicit.

#### Figure 5. Scientific-use validation via microstructure
This is the key figure. The furnace exists to change microstructure, so show that.

**Recommended package**
- SEM as-received vs annealed micrographs.
- EBSD inverse pole figure map and grain-boundary map for at least one annealed condition.
- Grain-size distribution histograms or boxplots.
- A table linking each microstructure sample to its exact run ID, temperature profile, soak time, atmosphere/vacuum condition, and cooling mode.

### 4.2 Specific analyses to add for SEM/EBSD
#### A. Grain-size quantification
Do not stop at “bigger grains in the image.” Report:
- number of grains analyzed,
- equivalent-circle diameter or intercept-based grain size metric,
- median and IQR or mean ± SD,
- segmentation / cleanup criteria,
- minimum grain area threshold,
- whether twins are merged or separated.

#### B. Compare as-received vs annealed statistically
If you have multiple fields of view or replicate specimens, compare grain size distributions using an appropriate test.
- If per-specimen summary statistics are available and sample size is small, use specimen-level comparisons.
- If you only have pixel/feature-level distributions from one specimen per condition, do **not** overclaim inferential statistics; present them descriptively and state the limitation.

#### C. Correlate microstructure with thermal history
Even a small plot helps:
- grain size versus soak temperature,
- grain size versus soak duration,
- or two-condition comparison showing expected trend.

#### D. Show failure/limit cases if available
HardwareX papers get stronger when they define limits.
Examples:
- open-loop ramping had larger overshoot,
- too-fast heating caused quartz or support issues,
- below pyrometer threshold control must be staged differently.

### 4.3 Controls that would make reviewers trust the system
- **Open-loop versus closed-loop comparison** using the same target thermal cycle.
- **Vacuum versus inert-gas backfill mode** if both are intended operating modes.
- **Directly coupled metal sample versus graphite-susceptor-mediated ceramic heating** if you want to sell broader applicability.
- **Long-soak stability** over several hours, since grain growth work cares about soak integrity.

### 4.4 If you only have limited data
If new experiments are constrained, the best minimal publishable set is:
1. one calibration figure,
2. one closed-loop ramp/soak figure with stability metrics,
3. one repeatability figure from 3 nominally identical runs,
4. one SEM + EBSD figure pair with quantified grain-size change.

That is enough if executed cleanly.

## 5. Highest-priority gaps

These are the gaps most likely to block review or trigger major revision.

### Tier 1: must fix before submission
1. **Mint repository DOI and declare licenses.** Without this, the paper is not HardwareX-complete.
2. **Finish the canonical BOM.** Exact models, part numbers, costs, sources, year, and what belongs to the reproducible build.
3. **Add missing design files in accessible formats.** Especially crucible drawing and LabVIEW exports.
4. **Produce real validation figures from actual runs.** Right now the validation section is still a plan.
5. **Curate build figures/photos.** The build section needs a real visual sequence.

### Tier 2: high-value scientific improvements
6. **Strengthen the portability argument** with a generator-compatibility table and a migration table from LEPEL to CEIA.
7. **Quantify control performance** with overshoot, stability, and repeatability metrics.
8. **Link thermal runs to SEM/EBSD samples** using run IDs and a specimen table.

### Tier 3: polish that improves acceptance odds
9. **Add 3–5 bullet points in Hardware description** explaining who else can use this system and for what tasks. The accessible HardwareX template text asks for this.
10. **Expand the safety section into a hazard/mitigation table.**
11. **Clarify the software portability story** if LabVIEW is retained as the main implementation.

## 6. Ordered pre-submission checklist

### Compliance and repository
- [ ] Choose and add licenses at repo root.
  - Hardware drawings/CAD/schematics: preferably CERN-OHL-S or similar.
  - Code/scripts/VIs: MIT, GPL, or similar.
  - Documentation: CC-BY if you want separate doc licensing.
- [ ] Archive a release in an approved repository and mint a DOI.
  - HardwareX guidance, as captured in the accessible template text, points authors to **Zenodo, OSF, or Mendeley Data** for design files.
- [ ] Replace the placeholder repository field in the specifications table with the DOI.
- [ ] Fill CRediT roles, funding, competing interests, and final data availability statement.

### Reproducibility package
- [ ] Add the **graphite crucible/susceptor machining drawing**.
- [ ] Export **LabVIEW block diagrams** to PDF/PNG.
- [ ] Export PPTX schematics and coil drawings to non-proprietary reader-friendly formats.
- [ ] Decide and document the **reference build path** for the optical-window seal and vacuum-stack configuration.
- [ ] Add exact DAQ model and signal-conditioning details.

### BOM
- [ ] Fill generator/controller/chiller/transformer pricing and source.
- [ ] Break out grouped vacuum hardware into specific part lines or kits with SKU.
- [ ] Add part numbers, currency, quote year, and note whether used/surplus pricing was used.
- [ ] Separate canonical BOM from substitutes/legacy hardware.

### Build and operation
- [ ] Add photographed build sequence: stand, coil, crucible, vacuum integration, pyrometer alignment, control wiring.
- [ ] Add an interface/wiring schematic with terminal names and scaling.
- [ ] Rewrite operation into startup, run, shutdown, and emergency-stop subsections.
- [ ] Add operator preflight checklist.

### Validation
- [ ] Select canonical run IDs from the data logs.
- [ ] Generate command-to-temperature calibration figure with repeat points.
- [ ] Generate representative ramp/soak trace with setpoint, measured temperature, and control metrics.
- [ ] Quantify long-soak stability.
- [ ] Generate repeatability comparison across nominally identical runs.
- [ ] Add SEM and EBSD figures from actual annealed specimens.
- [ ] Quantify grain size and link each specimen to exact run conditions.

### Framing and writing
- [ ] Add a short prior-art comparison to commercial and open alternatives.
- [ ] Add a **generator compatibility requirements** table.
- [ ] Add a **legacy LEPEL vs current CEIA** migration table showing what changed and what transferred.
- [ ] Tighten claims about “order-of-magnitude cheaper” unless backed by citations or actual quotes.

## 7. HardwareX policy requirements that appear unsatisfied or at risk

Based on the draft and the accessible HardwareX guidance/template text, these policy items look incomplete:

1. **Open-source license declaration**
   - Still missing in the specifications table and design-file table.

2. **Design-file repository with persistent access**
   - Still missing DOI.
   - HardwareX guidance, as reflected in the accessible template/reference material, expects editable design files in a persistent repository such as **Zenodo, OSF, or Mendeley Data**.

3. **Editable design files**
   - Some files are present only in proprietary/native forms. Exported readable versions are needed.

4. **Design files summary completeness**
   - Missing crucible drawing.

5. **BOM completeness**
   - Required columns exist, but several critical rows still have placeholders.

6. **Validation and characterization completeness**
   - The paper currently proposes validation but does not yet present the core quantitative results.

7. **Declarations**
   - CRediT, competing interests, and funding not complete.

8. **Video / supplementary demonstration**
   - I could not directly scrape the live ScienceDirect guide page due to access failure, so I won’t overstate this as a verified hard requirement here. But the accessible HardwareX template ecosystem and search snippets show a dedicated **Videos** submission section and strong expectation for visual supplementary material. You should assume that an operation video will materially improve compliance and review.

9. **3–5 bullet points in the hardware description**
   - The accessible HardwareX template text explicitly asks for bullet points explaining how the hardware helps other researchers. Your draft does not currently include these.

## 8. Concrete writing suggestions

### Replace generic claims with bounded ones
Instead of:
> “the same control software, vacuum chamber, pyrometer feedback, crucible, and work-coil geometry transfer from one induction generator to another”

Use something like:
> “The transferable portion of the design is the control, sensing, vacuum, and sample-fixturing stack around the generator. Porting to a new generator requires only a compatible external analog power-control input, matched cooling and coil interfaces, and re-calibration of the command-to-temperature mapping and PID gains.”

That sounds much more reviewer-proof.

### Add explicit reuse bullets in Hardware description
Something like:
- enables closed-loop high-temperature annealing for reactive metals using an existing induction generator,
- extends induction heating to poorly coupling materials through a graphite susceptor/crucible,
- integrates vacuum or inert-gas operation using standard KF hardware,
- provides programmable ramp/soak control using commonly available DAQ hardware,
- offers a lower-cost upgrade path for labs that already own induction power hardware.

### Make the prototype/current-build boundary cleaner
A dedicated sentence early in the manuscript would help:
> “The LEPEL furnace served only as the development platform for the retrofit concept; the reproducible HardwareX build documented here is based on the CEIA Power Cube 6 kW platform and the shared open design files describe only the transferable retrofit components and interfaces.”

## 9. Final recommendation

The submission is promising and very salvageable. The manuscript already has the right **structure** and the right **story**. What it does not yet have is the fully documented reproducible package and the quantitative validation that *HardwareX* reviewers will expect.

If you do only three things before the next draft, do these:
1. **finish the canonical BOM + DOI + license package**,
2. **export and add the missing design files, especially the crucible and LabVIEW logic**,
3. **turn the validation plan into real figures with run IDs and microstructure quantification**.

Do that, and this stops looking like a lab-internal draft and starts looking like a credible HardwareX paper.

## Sources used for this review
- Draft manuscript: `paper.md`
- Project plan: `PLAN.md`
- Parts/BOM extract: `extracted-context/parts_list.md`
- SOP extracts: `extracted-context/SOP_induction_200901.md`, `extracted-context/SOP_alternate.md`
- Coil geometry notes: `extracted-context/order_corrections_coils.md`
- Schematic extracts: `extracted-context/schematic_induction_furnace.md`, `extracted-context/schematic_support_stand.md`
- East Coast Induction notes: `east-coast-induction-heater-notes.txt`
- Accessible HardwareX template/reference text fetched from:
  - Zenodo HardwareX template record: `https://zenodo.org/records/5078227`
  - Hacker Fab HardwareX template reference: `https://docs.hackerfab.org/home/templates-to-do/hardware-x-template-for-reference`
- ScienceDirect search snippets for the current HardwareX guide-for-authors page: `https://www.sciencedirect.com/journal/hardwarex/publish/guide-for-authors`

- Discretionary analytical decisions made during the analysis:
  - Anchored the review primarily to the draft manuscript and project plan, using supporting extracted files only to verify specific hardware details and gaps.
  - Treated the CEIA Power Cube 6 kW system as the canonical reproducible build and the LEPEL system as historical prototype, following the manuscript’s stated intent.
  - Used accessible secondary representations of HardwareX requirements (Zenodo template record, Hacker Fab template mirror, ScienceDirect search snippets) because direct scraping of the live guide-for-authors page failed with HTTP 422.
  - Did not claim any unverified quantitative performance metrics beyond those explicitly present in the draft or supporting documents.
  - Framed validation recommendations around a minimal publishable package of calibration, control, repeatability, and microstructure figures rather than a broader experimental campaign.
  - Recommended specimen-level statistical comparisons for grain-size validation when replicate specimens exist, and descriptive reporting only when data are limited to single-specimen image-derived distributions.
  - Recommended keeping proprietary LabVIEW source files while adding exported PDF/PNG logic views, rather than insisting on immediate reimplementation in open-source control software.