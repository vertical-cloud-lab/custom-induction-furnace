# AI-edit review findings (to be spot-checked)

Review of `real_person_paper.tex` + `SI.tex` at repo commit c149c59, produced by
running `ai_edit_review_prompt.md` (uploaded alongside this file) against the
manuscript and supplementary-information (SI) LaTeX sources. Line numbers (e.g.
"L327–331") refer to the LaTeX sources; when verifying against the uploaded
PDFs, match by the verbatim quotes instead. Severity levels: `referee-flag`
(a journal reviewer would catch it), `confusing`, `polish`.

Summary: 43 findings — 11 factual contradictions (7 referee-flag), 8 garbled
sentences, 12 author-check questions, and the rest terminology/style.

## 1. Factual contradictions

**No. 1 — referee-flag (NEW): "all ran under this continuous flow" is contradicted by the SI's own table.**
Main text L327–331: "a constant argon flow of 20 SCCM was then maintained… The
nickel grain-growth anneals reported below all ran under this continuous flow."
But SI Table S1 marks all four calibration runs (IFrun039/040/038/032) and the
Fig. 4(a) EBSD specimen's run (Ni4N5_034, IFrun049) as "no-flow." A referee
comparing the table to this sentence catches it immediately. Action: restrict
the claim to the cohorts it's true for (representative, repeatability,
long-soak), or explain the no-flow runs.

**No. 2 — referee-flag (still open): YSZ starting grain size, 10 vs. 20 µm.**
Body L645–647: "grain growth from approximately 10 µm to 90 µm required 228 h"
vs. Fig. 7 caption L677–678: "coarsened the grains from approximately 20 to
90 µm." Author question: did the box-furnace and induction specimens start at
different sizes? If yes, say so; if no, reconcile against the micrograph data.

**No. 3 — referee-flag (NEW): the abstract says grooves span the sheet thickness; the body (correctly) says grain boundaries do.**
Abstract L194–196: "deep thermal grooves, several spanning the full sheet
thickness" vs. body L548–549: "Several grain boundaries traverse the full sheet
thickness." An author already ruled on exactly this ("the grooves don't go
through the thickness") and the Conclusions were fixed — the abstract kept the
wrong attribution. Action: "…deep thermal grooves; several grain boundaries
span the full sheet thickness."

**No. 4 — referee-flag (NEW): which contact does the BN barrier separate? Body and figure disagree.**
Body L653–668: graphite–alumina contact "was eliminated by introducing a boron
nitride diffusion barrier between the two materials. Alternatively, replacing
the graphite with tantalum avoids this compatibility issue" — implying the Ta
route needs no BN. But the Fig. 8 caption (and the schematic itself) put the BN
stub in the tantalum configuration, "prevent[ing] reaction between the tantalum
and the alumina." Author question: was BN used in the graphite configuration at
all, or only ever as the Ta–alumina barrier? Reword the body's "Alternatively…"
sentence accordingly.

**No. 5 — referee-flag (NEW): 2500 °C is claimed four times; the hottest committed evidence is 2344 °C.**
Claims in abstract L201, L369, L648, Conclusions L729–730. Best data shown: SI
Fig. S9 — ramp to 2344 °C (interlock-terminated) and a steady hold at
~2000 °C. Table S1 contains no YSZ rows, so the headline 2500 °C / 45 min
anneal has no trace or run-log linkage anywhere in the paper set. Action: add
that run's trace and a Table S1 row, or state the temperature basis for the
45 min anneal explicitly.

**No. 6 — referee-flag (still open): 1400–1500 °C claimed, 1400 °C demonstrated.**
L228–229 and L367–368 claim the 1400–1500 °C range; the hottest logged runs
shown are 1400 °C (Table S1, IFrun032/IFrun072). Action: soften to "up to
1400 °C demonstrated," or cite a hotter run.

**No. 7 — referee-flag (still open): the calibration current is impossible for a 4–20 mA loop.**
T = 931 + 632 I (L477) implies commands of 0.43–0.74 mA — confirmed on the
Fig. S4 axis (0.45–0.75 mA) — below the 4 mA live-zero of the loop described at
L348–353. New clue: SI Fig. S9 states commands in percent (33 %, 17 %). If the
logged quantity is the fractional command (0–1), then 0.43–0.74 → 43–74 %,
which is physically sensible and unit-consistent with S9. Author question: what
is I actually — fractional command, DAQ volts, or loop mA? Relabel the fit, the
figure axis, and the S4 caption to match.

**No. 8 — confusing: "only requirement" vs. the four requirements.**
Abstract L186, Intro L244, and Conclusions L708–709 say the *only* requirement
is a monotonic analog input, while L370–374 lists four (analog input,
liquid-cooled head/coil, sufficient RF power, electrical isolation). Action:
say "only interface requirement," and see repetition item No. 39.

**No. 9 — referee-flag: the linkage promise overstates.**
Fig. 4 caption L580–581: "The supplementary material links each specimen to its
furnace run" — yet Table S1's row for the Fig. 4(b) specimen (Ni4N5_069) reads
"— (log not in parsed set)," and Fig. 3's specimen has no row at all (No. 22).
Same for L470–471 "links each result below." Action: "…links the specimens to
their furnace runs where the log survives."

**No. 10 — confusing: "not attached to any of these flanges… resting on a retaining ring of a KF40 flange."**
L363–365 reads self-contradictory in adjacent sentences, and the crucible
section gives a different load path (alumina tube → teflon tube at the KF40
fitting, L392–395). This is a known open question for an author — once
answered, merge into one description.

**No. 11 — referee-flag (NEW): coil dimensions don't match the SI's own drawing.**
L306–307: "approximately 3 in tall with a 2.5 in inner diameter." The Fig. S2
drawing (docs/coils-drawing.pdf) is dimensioned 86.2 mm (3.4 in) tall,
Ø59.85 mm (2.36 in) ID. 3 vs. 3.4 in is beyond "approximately," and a referee
can open the drawing. Action: quote the drawing's mm values in the text (which
also fixes the mixed-units issue, No. 42).

## 2. Nonsensical or garbled sentences

- **No. 12 — confusing** L382–383: "a cup body and a lidded cap with a central
  bore" — a cap that has a lid? Everywhere else the second piece is just "the
  lid." → "a cup body and a lid with a central bore."
- **No. 13 — confusing** L388–390: "increase transmittance in the wavelength
  ranges emitted from the sample relative to the pyrometer" — the
  pyrometry→pyrometer swap kept the dangling "relative to"; the sentence still
  doesn't parse. Suggest "…in the wavelength bands the pyrometer measures."
- **No. 14 — confusing** L360–363: "The quartz tube and the vacuum hardware
  below it are joined by KF40 flanges to the pyrometer housing" — says both
  join the housing; the Fig. 1 caption has the correct topology (tube→housing
  above, tube→vacuum hardware below). Align.
- **No. 15 — polish** L634: "grains to coarsen on refractory ceramics" → "in."
- **No. 16 — polish** L227–229: "Growing grains without oxidizing the sample
  requires temperatures of 1400 to 1500 °C along with high vacuum" — the
  temperature is required for growth, the atmosphere for avoiding oxidation; as
  written the temperature seems needed to avoid oxidation.
- **No. 17 — polish** L466–468: "analogous to a stainless-steel designation
  such as SS316" reads as comparing the alloys, not the naming scheme; and
  "Ni (4N5…) nickel charges" says nickel twice.
- **No. 18 — polish** L309–310: "The coil is modular, and this geometry was
  chosen to fit our sample geometry" — repeated word, and "modular" is
  unexplained for a coil (interchangeable?).
- **No. 19 — confusing** L602: "the microstructure such an anneal produces" —
  the anneal just discussed is 1200 °C/12 h, but Fig. 6's is 1300 °C/20 h.

## 3. Author-check questions

- **No. 20 — referee-flag (NEW)** SI BOM row RETRO-1: "DAQ with analog out + in
  (0–5 V AO): NI USB-6000" — per NI's published specs the USB-6000 has no
  analog outputs (the USB-6001/6002 do). Verify the model against the actual
  unit.
- **No. 21 — referee-flag (NEW)** SI BOM row RETRO-4: "NI-9265 input module +
  NI-9203 output module" — the labels look swapped (the 9265 is a
  current-output module, the 9203 a current-input module). Deeper question: a
  cDAQ-9174 chassis is USB-commanded, so how does the DAQ's "0–5 V analog
  output drive" it (L350–353)? Please describe the actual signal chain — this
  ties directly to the command-units puzzle (No. 7).
- **No. 22** Fig. 3 provenance: `fig_kikuchi_raw.jpg` is byte-identical to
  `reg1a_x4100y1628.jpg` from early-campaign specimen Ni_003b1a, which has no
  Table S1 row and no documented prep state. Confirm it was annealed in this
  furnace and truly unprepared; consider naming the specimen in the caption.
- **No. 23** The grooving specimen was "cleaned only ultrasonically"
  (L545–546) while the EBSD specimens "went straight from the furnace to the
  SEM" (L513–515). Were the EBSD specimens cleaned at all? State it either way.
- **No. 24** L255: "modern, USA-sourced… generator" — CEIA is an Italian
  manufacturer; East Coast Induction is the US distributor. Intended claim?
- **No. 25** 0.5 psi relief-valve cracking pressure (L437–438, SI Fig. S3) —
  still unconfirmed for the project-support-center valve actually used.
- **No. 26** "two 25.5 mm tantalum susceptor blocks" (L688) — the schematic
  shows 25.5 mm as the block width; the caption doesn't say which dimension.
- **No. 27** SI Fig. S10(a): "YSZ after a 1700 °C / 10 h anneal" — which
  furnace? It matches neither the 1600 °C box furnace nor any described
  induction run. Unexplained provenance.
- **No. 28** SI Fig. S8(b): "SEM live view at 70,068×" — overprecise; verify
  against the microscope metadata (and consider rounding).
- **No. 29** "Every failure mode was a contact reaction…" (L724–725) — the
  paper describes only the graphite–alumina reaction; the universal claim rests
  on the unpublished configuration survey. Fine if the authors stand behind it.
- **No. 30** SI Fig. S1 caption: "Fully assembled the crucible stands 13 mm
  tall" — this exact claim was removed from the main text as implying one fixed
  configuration, but survives in the SI (and the stated part heights don't
  obviously sum to 13 mm). Keep or cut deliberately.
- **No. 31** The MFC is listed as "optional" (SI BOM RETRO-6A) yet every
  reported nickel anneal ran "a constant argon flow of 20 SCCM" — reproducing
  the reported results effectively requires it.
- For the record (all remaining physical-configuration claims, which read
  consistent with prior author statements but only the authors can verify):
  pyrometer housing suspended from the ceiling by cables with the vacuum column
  hanging from it; coolant series path chiller→generator→heating head→coil→
  chiller; roughing-pump vibration decoupled through a flexible hose only;
  graphite subliming onto the chamber walls under vacuum-only heating; the
  55 mm quartz disc (not the printed housing) sealing against an O-ring.

## 4. Terminology and cross-references

- **No. 32 — polish** One part, three names: "alumina discs" (L386), "alumina
  sample-surrounding sheets" / "alumina sheets" (Fig. 2 caption), "alumina
  spacer disc" (SI Fig. S1).
- **No. 33 — polish** "turbo pumping station" / "turbopump" / "turbo pump"
  drift (L316, L325, L453, L459); "pressure sensor" (Fig. 1 caption) vs.
  "wide-range vacuum gauge" (L440) vs. "the gauge."
- **No. 34 — polish (still open)** KF40 first appears in the Fig. 1 caption
  before its in-text gloss at L315–316; floats can render above the defining
  text.
- **No. 35 — decision, not defect:** the title still uses "RF" (before the
  abstract defines it) and "reactive-metal" while the demonstrations are nickel
  and a ceramic; earlier title recommendations (including "into"→"for") remain
  unadopted.
- **No. 36 — polish** "teflon" lowercase (L395, L693) — Teflon (trademark) or
  PTFE.
- **No. 37 — checks that PASSED** (so you don't re-do them): SI figure count
  "S1–S10" OK; hard-coded S4–S7 pointers OK; SI→main "Fig. 8" OK; the
  Sec. SI–SVII listing matches SI.tex order OK; GEN line items sum to $16,487
  vs. "~$16.5k" OK; the repeatability stats recompute exactly from Table S1
  (mean 1201.2, SD 1.3, CV 0.11 %) OK; representative-soak and microstructure
  temperatures match their Table S1 rows OK.
- **No. 38 — repo-level (old item, partially fixed):** paper/README.md still
  describes `paper.tex`, `archive/`, `PLAN.md`, `supplementary/`, "Table S3,"
  and "figures S1–S12," none of which exist on this branch; the Makefile's
  `make pdf`/`make draft`/`make figures` targets reference `paper.tex` and ten
  build scripts that aren't here.

## 5. Style / repetition

- **No. 39 — polish** "only requirement … monotonic analog" still appears 4×
  (abstract, Intro, Sec. II variant, Conclusions).
- **No. 40 — polish** The no-prep phrasing ("no grinding, polishing, or
  etching" + "pulled directly from the furnace chamber and placed directly into
  the EBSD chamber") appears near-verbatim 4× (Sec. V, Fig. 3 caption,
  Conclusions, SI Fig. S8). The emphasis was requested — but consider varying
  the wording so it doesn't read templated. "The grooves have deepened enough
  that they delineate the grain structure on their own" is verbatim in both
  body and Fig. 5 caption.
- **No. 41 — polish (still open)** "10⁻⁶ to 10⁻⁸ Torr" reads backwards, twice
  (L318, L436–437).
- **No. 42 — polish (still open)** Mixed units: coil in inches, relief valve in
  psi, everything else metric — fixing No. 11 with the drawing's mm values
  resolves the coil half.
- **No. 43 — polish** "hand-tightened clamps"/"hand-clamped" 3× (Fig. 1
  caption, L435, Conclusions) — trim one.

## Completeness note (from the reviewing model)

Swept: `real_person_paper.tex`, `SI.tex`, `paper/README.md`, `paper/Makefile`,
plus visual inspection of `fig_calibration.png`, `fig_grain_growth.png`,
`fig_ysz_stack.png`, and `docs/coils-drawing.pdf`, and file-hash provenance for
`fig_kikuchi_raw.jpg`. Not performed: pixel-level caption-vs-content checks for
the remaining nine figure images; verification of the raw run logs; citation
content checks beyond previously verified references; and the NI part
specifications in No. 20/21 are from published-spec knowledge, not a datasheet
pulled fresh.
