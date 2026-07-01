<!-- Edison ANALYSIS task f10579bb-4cbc-45bb-9761-373dbd7754d9 (iteration 3) -->

# Follow-up HardwareX review: revised induction-annealing manuscript

## Bottom line

This revision is better. The manuscript now fixes several of the structural problems from the first round: the **retrofit boundary is clearer**, the **generator-agnostic claim is framed more honestly**, the **BOM is in a single 7-column table**, the **safety section is much stronger**, and the **operation section reads like a real workflow instead of lab notes**.

It is still **not submission-ready**, but the remaining blockers are narrower now. The highest-priority problems are:

1. **compliance metadata still missing**: license, DOI, final references, final declarations,
2. **the BOM is still not procurement-complete** for the generator/DAQ/pump core,
3. **validation is still a plan, not results**, and
4. **the revised control description introduces one important reproducibility inconsistency**: the manuscript now centers a **4–20 mA generator input**, but the DAQ line item appears to be an **NI USB-6009**, which does not natively output 4–20 mA.

That last point is the main new technical weakness I’d fix next.

---

## 1. What is now resolved versus the previous review

These earlier issues are substantially addressed in the current draft:

### Resolved or mostly resolved
- **Retrofit / modernization framing is much clearer.**
  - The new **Reproducibility boundary** subsection is good and reviewer-proof.
  - The paper now clearly states that it reproduces the **control, sensing, vacuum, fixturing, and susceptor layer**, not the RF generator internals.
- **Generator-agnostic claim is better bounded.**
  - The new **Generator compatibility requirements** section is a real improvement.
  - The new **LEPEL prototype → CEIA reproducible build** table is exactly the kind of bridge the first draft lacked.
- **Prior-art/context framing is better.**
  - The comparison table is concise and useful.
- **Hardware description is stronger.**
  - The control signal path is now explicit.
  - The vacuum stack order is now explicit.
- **BOM format is improved.**
  - The manuscript now uses a single **7-column HardwareX-style BOM**.
  - The distinction between **GEN / RETRO / CONS** is helpful.
  - Costing conventions are stated.
- **Build/operation sections are better organized.**
  - Preflight, startup, normal run, shutdown, and abort are now separated.
  - The pyrometer low-temperature limitation is now acknowledged.
- **Safety section is improved.**
  - The hazard table is a clear upgrade.
- **Ethics section is now present.**
- **Graphite crucible/susceptor framing is much better.**
  - It now reads as a genuine enabling hardware element, not an aside.
- **Reuse bullets are present.**
  - The “Who can use this system” section solves a previous weakness.

So the revision did real work. Good.

---

## 2. What is still weak, with emphasis on the next blockers

## A. Submission blockers that remain

### A1. Compliance items are still placeholders
These are still immediate blockers for HardwareX submission:

- **Open-source license** in the specifications table is still `[TODO]`.
- **Source repository DOI** is still `[TODO]`.
- **Total cost of hardware** is still `[TODO]`.
- **CRediT roles** are still provisional.
- **Competing interests** are still provisional.
- **Funding** is still `[TODO]`.
- **References** are still entirely `[TODO]`.

These are not polish items anymore. They are final-package requirements.

### A2. Validation is still entirely prospective
The validation section is well planned, but it still describes what the authors *intend* to include rather than what they *show*.

Right now the manuscript still lacks:
- actual calibration data,
- actual ramp/soak traces,
- actual repeatability statistics,
- actual SEM/EBSD figures,
- actual specimen-to-run mapping.

For review, this is the biggest remaining scientific gap.

### A3. Design-file package is still incomplete
Still missing:
- **graphite crucible machining drawing**,
- **LabVIEW block-diagram exports** for non-LabVIEW readers,
- likely a cleaner exported schematic package tied to the repository DOI.

This remains a reproducibility gap, not just a formatting issue.

---

## 3. New or newly visible weaknesses introduced by the revision

These are the most important things I would fix now because the revised draft makes them visible.

### B1. DAQ choice and 4–20 mA control path are inconsistent
This is the biggest new technical problem.

The manuscript now says the reproducible CEIA build uses a **4–20 mA analog power setpoint**. But the BOM lists:

- **RETRO-1: “LabVIEW-compatible DAQ ... e.g. NI USB-6009 [confirm model]”**

An NI USB-6009 does **not** natively provide a 4–20 mA current-loop output. It provides voltage output. If the actual system drives a 4–20 mA CEIA input, then one of these must be true:

1. the DAQ model is not USB-6009,
2. there is an external **voltage-to-current converter / signal conditioner / PLC/current controller**, or
3. the CEIA controller is actually being driven in voltage mode, not current mode.

Right now the manuscript does not resolve that.

**Why this matters:** this is not a minor detail. It affects the exact reproducible control interface.

**Action:**
- name the exact DAQ model,
- name the exact analog-output standard used in the CEIA build,
- if a V→I converter is used, add it to the BOM and wiring description,
- add one sentence in the hardware description that states the physical signal chain precisely.

Example of the needed sentence:
> “In the CEIA build, the DAQ outputs 0–5 V to a current-loop conditioner, which converts the command to the controller’s 4–20 mA power-setpoint input.”

Or, if not true, state the real arrangement.

### B2. The canonical pyrometer is still ambiguous
The draft names:
- **IMPAC ISR6** in the specifications table,
- **IMPAC ISR6; also a LumaSens 800–2500 °C unit** in the hardware description,
- **LumaSens / IMPAC ISR6** in the BOM.

That leaves the canonical build unclear.

**Action:** pick one as the reproducible line item and treat the other as an alternative or historical substitute.

### B3. A few BOM lines now contain internal inconsistencies
I found at least two concrete issues:

- **RETRO-9 optical window**: the BOM says `Number = 1 (3 incl. spares)`, `Cost per unit = $18`, `Total = $54`.
  - That math implies **3 units**, not 1.
- **RETRO-10 source attribution looks wrong**:
  - the BOM cites `McMaster-Carr (4772K-series)` for the quartz disc,
  - but in the extracted parts list, **4772K4** is the **10 psi relief valve**, not the quartz disc.

These are small, but reviewers notice BOM sloppiness fast.

### B4. The build section is clearer, but still not rebuildable end-to-end
The build section improved structurally, but it still omits a few practical details that matter:

- exact **coil tubing OD / wall / material spec**,
- bending/forming method,
- cooling connection details,
- critical crucible dimensions,
- the exact electrical interface hardware for the control signal,
- terminal-level or connector-level wiring detail.

I would not expand this into a full manual in the paper, but the paper should point to the exact design files that contain those details. At the moment some of those files still do not exist in the package.

### B5. The “order of magnitude cheaper” claim is still vulnerable
The statement remains, but there is still no direct citation or cost comparison table supporting it.

Because the current hardware-cost row is also still `[TODO]`, this claim is exposed.

**Action:** either:
- support it with a cited commercial comparison, or
- soften it to something like “substantially lower capital cost than turn-key commercial systems.”

---

## 4. Section-by-section follow-up assessment

## 4.1 Specifications table
**Status:** improved, still not complete.

### Better now
- More operationally relevant than before.
- Includes pyrometer range, soak duration, sample envelope, vacuum, coil.
- Includes the analog-input requirement explicitly.

### Still weak
- **License, cost, DOI** still missing.
- **Control resolution / range** is still vague rather than numeric.
- The table would be stronger if it gave the actual command interface numerically, for example:
  - DAQ output type and range,
  - current-loop conditioner model if present,
  - pyrometer output signal type,
  - analog input scaling,
  - command resolution.

### Next fix
Replace descriptive wording with exact I/O specs.

---

## 4.2 Hardware in context / framing
**Status:** much better.

### Better now
- The portability claim is more believable.
- The reproducibility boundary is explicit.
- The transferability table helps a lot.

### Still weak
- The phrase “maps roughly linearly to output power” is not necessary and may overconstrain the argument. Since you already say monotonic response is enough under feedback, keep the standard to **monotonic** unless you actually require linearity for the open-loop startup segment.
- The commercial-cost comparison is still unsupported.

### Next fix
Tighten one sentence so the logic is consistent:
- compatibility requires **monotonic command response**,
- calibration and PID tuning absorb nonlinearity.

---

## 4.3 Hardware description
**Status:** improved and close, but not done.

### Better now
- Signal path and vacuum path are explicit.
- The five-subsystem breakdown works.

### Remaining issue
The control description is now good enough conceptually, but not yet electrically reproducible because the **actual output-conditioning hardware is still unspecified**.

### Next fix
State the exact chain at the hardware level:
- DAQ model,
- output voltage/current range,
- any current-loop driver,
- pyrometer analog output type,
- input module or scaling path.

---

## 4.4 Design files summary
**Status:** still incomplete.

### Better now
- The design-file inventory is more explicit.

### Still missing
- crucible machining drawing,
- exported LabVIEW logic views,
- final DOI-backed repository location,
- final licenses.

### Next fix
This is still a must-finish section, not optional polish.

---

## 4.5 Bill of materials
**Status:** format fixed, reproducibility still incomplete.

### Better now
- The table is now in the right schema.
- The split between generator, retrofit, and consumables is helpful.

### Still missing
The critical unresolved rows are still the same ones that dominate cost and reproducibility:
- **GEN-1** CEIA generator cost,
- **GEN-2** Master Controller cost,
- **GEN-3** chiller exact model/cost,
- **RETRO-1** exact DAQ model/cost,
- **RETRO-4** T-Station 85 exact cost/source.

### New cleanup needed
- Fix the **RETRO-9 quantity/total mismatch**.
- Fix the **RETRO-10 wrong SKU/source note**.
- Decide whether the BOM should list **spares** in the Number column or move them to Notes/text.
- If a current-loop conditioner exists, it must become its own BOM row.

### Judgment
The BOM is improved, but still **not yet procurement-ready**.

---

## 4.6 Build instructions
**Status:** improved, still short of fully reproducible.

### Better now
- Reference build path for the optical-window seal is now chosen.
- The sequence is cleaner.

### Still weak
- No photographed build sequence yet.
- No exact crucible dimensions yet.
- No coil fabrication dimensions beyond coarse geometry.
- No wiring terminals or current-conditioning details.

### Next fix
At this point, the fastest path is probably:
1. add the missing drawing(s),
2. add 3–6 labeled build photos,
3. add one wiring/interface figure.

---

## 4.7 Operation instructions
**Status:** substantially improved.

This section is now in decent shape.

### Minor remaining issue
The open-loop-to-closed-loop handoff is mentioned, but the **handoff criterion** is not defined. If the control behavior depends on pyrometer acquisition, say what event triggers handoff.

For example:
- sustained valid pyrometer signal above a threshold,
- operator-confirmed acquisition,
- or a specific temperature band.

That would make the control logic sound less ad hoc.

---

## 4.8 Validation and characterization
**Status:** still the main scientific blocker.

The section is better organized than before, but still reads as a work plan.

### What now looks right
The figure logic is good. I would keep the five-figure structure.

### What must happen next
To reach submission quality, the next draft needs actual numbers and actual figures for at least these four elements:

1. **Calibration**
   - command vs. temperature,
   - replicate points if possible,
   - mean ± SD.
2. **Closed-loop control performance**
   - one ramp/soak trace,
   - rise time, overshoot, settling time, soak RMS error / SD.
3. **Repeatability**
   - at least 3 nominally matched runs,
   - between-run soak-temperature SD and drift.
4. **Microstructural outcome**
   - SEM and EBSD,
   - quantified grain-size change,
   - explicit specimen ↔ run-ID linkage.

### A reviewer-sensitive point
Do not claim inferential statistics unless there are true biological/material replicates at the specimen level. If there is one specimen per condition with many EBSD grains, keep the comparison descriptive unless justified.

---

## 4.9 Safety
**Status:** good enough for submission once the rest is finished.

This section is much better than before. The only thing I’d consider adding is one line on **PPE / shielding expectations** if those are standardized in the lab.

---

## 4.10 Declarations and references
**Status:** still incomplete.

This is now a straightforward completion task. Finish it.

---

## 5. Highest-priority next changes

Here is the shortest path from current draft to submission-quality draft.

### Priority 1: fix the control-interface reproducibility gap
This is the most important new action.

- Resolve the **DAQ vs. 4–20 mA** inconsistency.
- Name the exact interface hardware.
- Add any missing signal conditioner/current-loop driver to the BOM and wiring description.
- Pick one canonical pyrometer model.

### Priority 2: convert validation from plan to evidence
- Insert at least one real figure for each of:
  - calibration,
  - ramp/soak performance,
  - repeatability,
  - SEM/EBSD outcome.
- Populate the specimen/run linkage table with real IDs.

### Priority 3: finish the compliance package
- add final license,
- mint DOI,
- complete declarations,
- add final references.

### Priority 4: finish the missing design files
- crucible machining drawing,
- LabVIEW exports,
- cleaned figure/design-file bundle for repository deposition.

### Priority 5: clean the BOM and minor consistency issues
- fill GEN-1/2/3, RETRO-1/4,
- fix RETRO-9 quantity math,
- fix RETRO-10 source/SKU note,
- provide exact total cost.

---

## 6. Concise pre-submission checklist for this revision round

### Must fix before submission
- [ ] Resolve the **actual analog control chain** for the CEIA build: DAQ model, output standard, and any V→I/current-loop hardware.
- [ ] Choose and declare the final **licenses**.
- [ ] Mint and insert the **repository DOI**.
- [ ] Fill the missing **GEN-1/2/3, RETRO-1/4** BOM details and total hardware cost.
- [ ] Add the **crucible machining drawing**.
- [ ] Export **LabVIEW block diagrams** to reader-accessible PDF/PNG.
- [ ] Replace the validation plan with **actual figures and quantitative metrics**.
- [ ] Populate the **specimen ↔ run-ID** table.
- [ ] Add the **final references list**.
- [ ] Finalize **CRediT, funding, and competing interests**.

### Strongly recommended before submission
- [ ] Add a photographed build sequence.
- [ ] Fix the pyrometer-model ambiguity.
- [ ] Fix RETRO-9 quantity/total mismatch.
- [ ] Fix RETRO-10 source/SKU attribution.
- [ ] Tighten the “order-of-magnitude cheaper” claim unless directly supported.
- [ ] Define the open-loop → closed-loop handoff criterion.

---

## 7. Final judgment on this round

This revision did address a lot of the first-round feedback. The manuscript is now better framed and much easier to review as a HardwareX paper.

What remains is less about structure and more about **closing the package**:
- exact interface hardware,
- completed BOM/compliance metadata,
- real validation data,
- final design-file exports.

If the authors fix the **DAQ/current-loop inconsistency** and replace the validation placeholders with actual results, the paper will move much closer to submission quality.

- Discretionary analytical decisions made during the analysis:
  - Focused this round on verifying resolution of previously flagged issues and only highlighted unresolved or newly introduced weaknesses rather than repeating the full first-round review.
  - Treated the revised `paper.md` as the primary source of truth and used `REVIEW.md`, `PLAN.md`, and `extracted-context/parts_list.md` only to verify whether prior concerns were addressed and to check internal consistency.
  - Interpreted HardwareX readiness primarily through manuscript-completeness and reproducibility criteria rather than attempting to re-scrape journal policy pages in this follow-up round.
  - Flagged the DAQ-versus-4–20 mA issue as a major reproducibility gap because the revised manuscript now makes the analog interface more specific, making that mismatch materially important.
  - Treated the pyrometer-model ambiguity and BOM arithmetic/source inconsistencies as higher priority than stylistic edits because they directly affect procurement and reproducibility.
  - Recommended retaining the five-figure validation structure from the revised draft because it is scientifically appropriate; the problem is absence of actual data, not the planned figure set.
  - Suggested descriptive rather than inferential grain-size comparisons unless replicate specimens exist, to avoid overstating evidence from image-derived feature distributions.