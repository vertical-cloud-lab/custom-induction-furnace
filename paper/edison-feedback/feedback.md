<!-- Edison ANALYSIS task d6b87bcc-813a-45e6-8405-f05dc7a72398 (iteration 4) -->

# Follow-up HardwareX review: revised induction-annealing manuscript

## Bottom line

This revision fixes several of the issues from the last round. The **control-interface story is now much clearer**, the **DAQ-to-4–20 mA gap is mostly addressed**, the **pyrometer naming is consistent**, the **BOM math bug around the optical window is fixed**, and the **open-loop → closed-loop handoff is now described**. The manuscript is closer to a real HardwareX submission.

It is still **not submission-ready**. The biggest remaining blockers are now:

1. **validation is still only a plan, not evidence**,
2. **compliance metadata are still placeholders**,
3. **the design-file package is still incomplete**, and
4. **the BOM is improved but still not procurement-complete, and one source attribution still looks wrong**.

The revision did good work. What remains is mostly package-closing work, not conceptual reframing.

---

## 1. What is now resolved from the previous review

### Resolved or substantially improved

- **Retrofit boundary is clear.**
  - The new **Reproducibility boundary** subsection does the job.
  - The paper now clearly says the contribution is the modernization layer around a compatible generator, not the RF generator internals.

- **Generator-agnostic claim is better argued.**
  - The new **Generator compatibility requirements** section is much better.
  - The manuscript now uses the right standard: **monotonic command→power response** is required; strict linearity is not.

- **The DAQ / analog-interface inconsistency is mostly fixed.**
  - The new text explicitly states the CEIA chain as:
    **DAQ 0–5 V → voltage-to-current conditioner → 4–20 mA generator input**.
  - Adding **RETRO-4** to the BOM was the right fix.

- **Pyrometer ambiguity is resolved.**
  - The manuscript now consistently uses **LumaSense IMPAC ISR 6** and explains the branding.

- **Open-loop to closed-loop handoff is now described.**
  - The paper now says control switches after a **sustained valid pyrometer reading above the ~700 °C floor**.

- **The BOM cleanup is partly real, not cosmetic.**
  - The previous **RETRO-9 quantity/total mismatch** is fixed.
  - The optical-window row is now separated more clearly.

- **The cost-comparison language is safer.**
  - “Order-of-magnitude cheaper” has been softened to **substantially lower capital cost**, which is easier to defend.

---

## 2. What is still weak now

## A. Remaining submission blockers

### A1. Validation is still prospective
This is still the main scientific problem.

The validation section is organized well, but it still reads as a **figure plan** rather than a **results section**. It still lacks:

- actual calibration data,
- actual ramp/soak traces,
- actual repeatability metrics,
- actual SEM images,
- actual EBSD maps,
- actual specimen ↔ run-ID linkage.

For HardwareX, this is the biggest remaining gap because the hardware still isn’t shown doing the thing it was built to do.

### A2. Compliance metadata are still placeholders
Still unresolved:

- **Open-source license** is still `[TODO]`.
- **Repository DOI** is still `[TODO]`.
- **Total hardware cost** is still `[TODO]`.
- **CRediT roles** are still provisional.
- **Funding** is still `[TODO]`.
- **Competing interests** are still provisional.
- **References** are still entirely `[TODO]`.

These are not minor edits. They are required submission-package items.

### A3. Design-file package is still incomplete
Still missing or incomplete:

- **graphite crucible machining drawing**,
- **exported LabVIEW logic/block diagrams** for non-LabVIEW readers,
- likely a more polished design-file bundle tied to the eventual DOI.

That is still a reproducibility gap.

---

## 3. New or still-unresolved technical weaknesses

These are the next changes I would make.

### B1. The control chain is conceptually fixed, but still not exact enough for rebuild
The revised manuscript now correctly introduces the **0–5 V to 4–20 mA conditioner**, which fixes the big inconsistency from the prior round.

What is still missing:

- the **exact DAQ model**,
- the **exact loop-conditioner model/vendor**,
- the **exact pyrometer output format and scaling path into the DAQ**.

Right now the reader understands the architecture, but not yet the exact parts list needed to rebuild it.

**What to do next**
- Replace `NI USB-6001/6009-class` with the exact DAQ used.
- Name the exact **V→I loop conditioner**.
- State the pyrometer analog output type and scaling explicitly in the hardware description or a wiring table.

### B2. RETRO-10 source attribution still looks unsupported
The BOM now fixes the arithmetic, but the source line for the 55 mm quartz disc still looks shaky.

In the extracted parts list, the **55 mm × 1.5 mm custom quartz disc** appears in the old purchase list near the Mouser block, but I do **not** see support for the manuscript’s current source label:

- **RETRO-10 source in paper:** `McMaster-Carr (custom)`

That source attribution is not clearly supported by `extracted-context/parts_list.md`.

**What to do next**
- Verify the actual vendor from the original purchase record.
- If vendor is uncertain, say so and fix it before submission.
- Do not leave a probably-wrong vendor in the canonical BOM.

### B3. The canonical build is clear, but a few spec/BOM rows still mix prototype and final build details
The manuscript is much better about separating **LEPEL prototype** from **CEIA reproducible build**, but a few cells still blend them more than necessary.

Examples:
- Specifications row for **Power-control input** includes both the CEIA 4–20 mA and LEPEL 0–5 mA detail in one value.
- Build step 5 also includes both canonical and prototype wiring details.

This is not wrong, but it weakens the “canonical build” feel.

**What to do next**
- Keep the main specs/build instructions **CEIA-only**.
- Move LEPEL details to a short note or comparison table.

### B4. Compatibility wording still has a small clarity problem
The manuscript now correctly emphasizes monotonic response, but the phrasing:

- `4–20 mA or 0–5 V / 0–5 mA`

is a little awkward.

**What to do next**
Rewrite as something like:
- `e.g. 4–20 mA, 0–5 V, or 0–5 mA`

Small thing, but cleaner.

---

## 4. Section-by-section follow-up assessment

## 4.1 Specifications table
**Status:** improved, still incomplete.

### Fixed since last round
- Analog-input requirement is now explicit.
- Control chain is now described.
- Canonical pyrometer identity is now cleaner.

### Still weak
- **License, DOI, and total hardware cost** still missing.
- Some rows still mix canonical CEIA and prototype LEPEL details.
- Control I/O specs still need more exactness.

### Next fix
Add exact numbers/models for:
- DAQ,
- loop conditioner,
- pyrometer analog output,
- command scaling.

---

## 4.2 Hardware in context / framing
**Status:** strong enough conceptually.

This section now works. The modernization-layer argument is convincing, and the reproducibility boundary is much more reviewer-proof.

### Small remaining improvement
The cost comparison would be safer if supported by either:
- a brief cited commercial comparison, or
- slightly more restrained wording.

The current wording is probably acceptable, but it would be stronger with one citation.

---

## 4.3 Hardware description
**Status:** much better, close to good.

### Fixed since last round
- Signal path is now explicit.
- Vacuum path is explicit.
- Control loop is described coherently.

### Still needed
- Exact interface hardware details.
- Possibly a compact wiring table or one polished wiring diagram figure.

---

## 4.4 Design files summary
**Status:** still incomplete.

### What remains missing
- crucible machining drawing,
- exported LabVIEW diagrams,
- final licenses,
- DOI-backed repository link.

This remains a must-finish section.

---

## 4.5 Bill of materials
**Status:** improved, but still not procurement-ready.

### Fixed since last round
- Single 7-column BOM remains in place.
- The **RETRO-9 mismatch** is fixed.
- The **V→I conditioner** is now present as a real row, which is a meaningful correction.

### Still missing
The important incomplete rows are still:
- **GEN-1** generator cost,
- **GEN-2** controller cost,
- **GEN-3** chiller model/cost,
- **RETRO-1** exact DAQ model/cost,
- **RETRO-4** exact loop-conditioner model/cost,
- **RETRO-5** pump/gauge cost.

### Still incorrect or uncertain
- **RETRO-10 vendor/source** still needs verification.

### Judgment
The BOM is better, but still not complete enough for a reader to price and source the build with confidence.

---

## 4.6 Build instructions
**Status:** structurally better, still not fully rebuildable.

### Better now
- The control-wiring description is much improved.
- The reference optical-window build path is clear.

### Still needed
- exact coil tubing OD/wall/material,
- bend/spacing method,
- cooling fittings,
- crucible machining drawing,
- cleaner build photos,
- exact wiring/interface parts.

The paper does not need a machine-shop manual, but it does need to point to the design files that carry those details.

---

## 4.7 Operation instructions
**Status:** good.

This section is now in decent shape for submission.

The handoff criterion is described well enough for manuscript purposes. If the authors want to strengthen it, they can define “sustained valid reading” numerically, but that is no longer a major issue.

---

## 4.8 Validation and characterization
**Status:** still the main blocker.

The planned validation package is sensible. Keep that structure. What is missing is the data.

### Minimum publishable validation package
The next draft should contain actual results for at least these four elements:

1. **Calibration**
   - analog command vs. steady-state temperature,
   - replicate runs if available,
   - mean ± SD.

2. **Closed-loop control performance**
   - one representative ramp/soak trace,
   - rise time,
   - overshoot,
   - settling time,
   - soak mean,
   - soak SD or RMS error,
   - maximum absolute soak deviation.

3. **Repeatability**
   - at least 3 matched runs,
   - between-run SD,
   - coefficient of variation,
   - long-soak drift if relevant.

4. **Microstructural validation**
   - SEM as-received vs. annealed,
   - EBSD maps for at least one annealed condition,
   - grain-size quantification with explicit image-analysis criteria,
   - direct linkage of each specimen to its furnace run.

### Controls that would help most
The suggested controls in the draft are good. If the authors cannot do all of them, the highest-value ones are:

- **open-loop vs. closed-loop** on the same target profile,
- **repeatability across matched runs**,
- **metal direct coupling vs. graphite-susceptor heating** if they want to support the broader applicability claim.

### Statistical caution
If there is only one specimen per condition, do not oversell EBSD grain counts as independent replicate samples. Report the grain-size distributions clearly, but only use inferential statistics if there are true specimen-level replicates.

---

## 4.9 Safety
**Status:** good enough.

This section is now solid and reads like a proper hardware paper section rather than inherited SOP text.

---

## 4.10 Declarations and references
**Status:** still incomplete.

This is straightforward completion work now. It just has to be done.

---

## 5. Is the retrofit / modernization framing now convincing?

Yes, mostly.

The paper now makes the right argument:
- the contribution is the **modernization stack**,
- it was first shown on LEPEL,
- the **reproducible build** is the current CEIA system,
- portability depends on a compatible analog-input generator, not on copying a particular RF power supply.

That is a credible HardwareX framing.

### How to strengthen it one more step
Two additions would make it tighter:

1. **Add one explicit sentence that the paper’s build instructions and BOM are canonical for the CEIA system only.**
   - Keep LEPEL in the transferability/comparison table, not in the main build logic.

2. **Add one figure or schematic panel showing the modernization layer abstractly.**
   - Generator input
   - coil/chamber
   - pyrometer
   - DAQ/LabVIEW
   - vacuum station

That would make the portability argument visual, not just textual.

---

## 6. Highest-priority next changes

Here is the shortest path to submission quality.

### Priority 1: replace validation placeholders with actual results
- Insert real calibration data.
- Insert one real representative ramp/soak trace with quantitative control metrics.
- Insert repeatability data from matched runs.
- Insert SEM + EBSD with specimen ↔ run mapping.

### Priority 2: finish the compliance package
- choose and declare final licenses,
- mint repository DOI,
- complete declarations,
- add formatted references,
- fill total hardware cost.

### Priority 3: finish the exact rebuild details for the control chain
- exact DAQ model,
- exact V→I conditioner model,
- pyrometer analog output/scaling details,
- one clean wiring figure or table.

### Priority 4: complete the missing design files
- crucible machining drawing,
- exported LabVIEW logic views,
- any final figure/design-file bundle for deposition.

### Priority 5: final BOM cleanup
- fill GEN-1/2/3 and RETRO-1/4/5 pricing,
- verify RETRO-10 vendor,
- compute total hardware cost.

---

## 7. Ordered pre-submission checklist

### Must fix before submission
- [ ] Replace the validation plan with **actual figures and quantitative results**.
- [ ] Fill the **specimen ↔ run-ID** table with real specimen IDs and furnace runs.
- [ ] Choose and declare final **licenses**.
- [ ] Mint and insert the **repository DOI**.
- [ ] Add the **formatted reference list**.
- [ ] Finalize **CRediT, funding, acknowledgements, and competing interests**.
- [ ] Name the exact **DAQ model**.
- [ ] Name the exact **0–5 V → 4–20 mA loop conditioner**.
- [ ] Add the **graphite crucible machining drawing**.
- [ ] Export **LabVIEW block diagrams** to a reader-accessible format.
- [ ] Fill missing BOM pricing/model details for **GEN-1/2/3, RETRO-1/4/5**.
- [ ] Verify the true vendor/source for **RETRO-10**.
- [ ] Fill the **total hardware cost** line in the specifications table.

### Strongly recommended before submission
- [ ] Keep main build/spec text **CEIA-canonical** and move prototype detail to notes/tables.
- [ ] Add a clean wiring/interface figure.
- [ ] Add 3–6 build photos.
- [ ] Tighten the compatible-input wording to `4–20 mA, 0–5 V, or 0–5 mA`.
- [ ] Add one citation or table to support the commercial-cost comparison.

---

## 8. Final judgment on this follow-up round

This revision did address several of the previous review’s important issues. The manuscript is now more coherent, more reproducible in concept, and less vulnerable to reviewer pushback on the retrofit framing.

The remaining problems are now concentrated in four places:
- **no real validation results yet**,
- **unfinished compliance metadata**,
- **missing design-file exports**,
- **unfinished exact BOM/interface details**.

If the authors now focus on those package-closing tasks, especially the **validation figures/results** and the **exact control-interface hardware**, the manuscript should move much closer to submission quality.

- Discretionary analytical decisions made during the analysis:
  - Treated `paper.md` as the primary source of truth for the revised manuscript and used `PLAN.md` and `extracted-context/parts_list.md` only to verify whether previously flagged issues were actually resolved.
  - Focused the review on changes relative to the prior round, emphasizing resolved items, still-open blockers, and newly visible inconsistencies rather than repeating the full first-pass critique.
  - Considered the prior DAQ-versus-4–20 mA inconsistency substantially resolved because the revised manuscript now explicitly includes a 0–5 V to 4–20 mA conditioner in both the prose and BOM, while still flagging missing exact model details as an unresolved reproducibility gap.
  - Treated the pyrometer naming issue as resolved because the revised draft consistently identifies the canonical unit as a LumaSense IMPAC ISR 6 and explains the branding relationship.
  - Flagged RETRO-10 source attribution as still uncertain because the extracted parts list supports the price/quantity but not the manuscript’s specific vendor label `McMaster-Carr (custom)`.
  - Judged validation to be the main remaining scientific blocker because the section still contains planned figure descriptions and TODO placeholders rather than actual quantitative results.
  - Recommended descriptive rather than inferential comparison for EBSD-derived grain-size results unless true specimen-level replication exists, to avoid overstating evidence from within-sample grain distributions.