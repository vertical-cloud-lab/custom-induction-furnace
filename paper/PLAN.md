# HardwareX manuscript plan — Custom Induction Furnace

A working plan for drafting a [HardwareX](https://www.sciencedirect.com/journal/hardwarex)
article from the material in this repository. HardwareX publishes reproducible,
open-source scientific hardware, so the manuscript must let a reader **rebuild and
operate the system** from the design files, bill of materials, and instructions
provided here.

This plan (1) frames the contribution, (2) maps every required HardwareX section
to the concrete repository files that feed it, and (3) lists the gaps that still
need to be filled before submission.

---

## 1. Framing the contribution

This project is **not** a from-scratch furnace. The contribution we lean into is
**retrofit and modernization**: turning a bare commercial RF induction generator into
a **computer-controlled, vacuum-integrated, pyrometer-feedback annealing system** for
grain-growth and reactive-metal heat treatment. The retrofit is deliberately
**generator-agnostic** — the same DAQ/LabVIEW control stack, vacuum chamber, optical
temperature sensing, crucible stack, and work-coil geometry port from one induction
generator to another. That portability *is* the reproducible result, and it is what makes
this useful to any lab with an induction generator that exposes an analog power input.

The modernization was first prototyped on a **~1970 LEPEL high-frequency induction
furnace** (owned by the BYU Mechanical Engineering department), which served as the
initial proof-of-concept platform. The **reproducible build documented for HardwareX —
including the bill of materials — is based on the lab's current, USA-sourced induction
heater** (a CEIA "Power Cube" 6 kW generator with a Master Controller v3+, procured
through East Coast Induction), with the LEPEL retrofit pointed out as the originating
prototype rather than the canonical build. The novel, reproducible hardware/firmware
contributions are:

1. **Remote power control** — replacing the front-panel "power control" knob with
   a LabVIEW + DAQ analog output (0–5 mA → off→full power), added Aug 2019.
   (Source: `docs/induction_SOP_200901.docx`, extracted to
   [`extracted-context/SOP_induction_200901.md`](extracted-context/SOP_induction_200901.md).)
2. **Closed-loop temperature control** — an optical/dual-wavelength pyrometer feeding
   a PLC / 0–5 V control path for setpoint ramping, replacing open-loop current ramps.
   (Source: `docs/temp-control-modification/`, including `0-5V PLC wire design.png`.)
3. **High-vacuum integration** — a quartz-tube chamber on a turbo-molecular pump
   (~1×10⁻⁶–10⁻⁸ Torr) with KF-flange optics and inert-gas venting to suppress
   oxidation of reactive metals (Ni, Fe).
4. **Custom water-cooled work coil** — corrected geometry (≈3″ tall, 2.5″ ID, 6.5 turns)
   matched to the sample/crucible stack.
   (Source: `docs/induction_order_corrections.pptx`, extracted to
   [`extracted-context/order_corrections_coils.md`](extracted-context/order_corrections_coils.md)
   and figures in [`extracted-context/figures/`](extracted-context/figures/).)
5. **Custom-machined graphite crucibles / susceptors** — graphite stock (Cotronics
   56L-3, 3000 °C grade) machined in-house into crucibles that double as RF susceptors,
   so that even poorly-coupling or non-conductive charges (e.g. YSZ ceramic) are heated
   indirectly by the inductively-heated graphite. Fractured crucibles are repaired with
   a graphite cement (Resbond 931). The crucible sits inside the quartz tube on a ceramic
   spacer / Teflon stack.
   (Source: `docs/induction_parts_list.xlsx`, extracted to
   [`extracted-context/parts_list.md`](extracted-context/parts_list.md).)
6. **Operational tooling** — LabVIEW VIs for ramping, manual control, PID tuning, and
   automated email alerts; a MATLAB heat-curve plotter. (Source: [`../code/`](../code/).)

> **Current status note:** the control/vacuum/pyrometer retrofit described above is
> furnace-agnostic. It was developed on the legacy LEPEL unit and is now being applied to
> a **new USA-sourced induction unit (East Coast Induction / CEIA)**; an earlier CYSI
> GP-15A (China) unit was evaluated but did not meet the lab's control requirements and is
> no longer used (see §3.1).

**Working title (draft):** *"Retrofitting a vintage high-frequency induction furnace
for computer-controlled, vacuum-integrated annealing of reactive metals."*

**Target subject area:** Materials science / mechanical engineering — thermal
processing and grain-growth annealing.

---

## 2. Specifications table (draft values)

To be finalized once measured values are confirmed from the data logs. The
**reproducible build column reflects the current USA-sourced generator (CEIA "Power
Cube" 6 kW via East Coast Induction)**; the legacy LEPEL values are retained only to
document the originating prototype.

| Property | Reproducible build (current, USA unit) | Initial prototype (LEPEL) | Source |
|----------|----------------------------------------|---------------------------|--------|
| Induction generator | CEIA "Power Cube" 6 kW, solid-state RF generator + Master Controller v3+ | LEPEL high-frequency tube furnace (~1970), up to ~35 kW | `docs/east-coast-induction/`, SOP |
| Power control input | analog setpoint (4–20 mA controller input; LabVIEW/DAQ) | 0–5 mA analog (LabVIEW/DAQ) → off→full power | heater-notes, SOP |
| RF frequency | solid-state (mid–high kHz, generator-set) | ~200–450 kHz | manuals, SOP |
| Line power | 3-phase (380–480 V), ~12 kW autotransformer-fed | single high-voltage tube supply | heater-notes |
| Max sample temperature | ~1400–1500 °C+ (Ni/Fe melting range) | ~1400–1500 °C+ | SOP / data logs |
| Vacuum level | ~1×10⁻⁶ to 1×10⁻⁸ Torr (Edwards T-Station 85 turbo pump) | same | SOP / equipment-reference |
| Temperature measurement | IMPAC ISR6 dual-wavelength ratio pyrometer (also LumaSens 800–2500 °C) | optical / dual-wavelength pyrometer | equipment-reference, parts list |
| Chamber | quartz tube with KF40 optical-window flange | same | SOP / parts list |
| Crucible / susceptor | in-house machined graphite (Cotronics 56L-3, 3000 °C) crucible-susceptor | same | parts list |
| Work coil | ~3″ tall, 2.5″ ID, ~6.5 turns, water-cooled copper (head-matched) | same (corrected geometry) | order corrections |
| Cooling | recirculating water chiller (generator) + facility water | recirculating chiller + facility water (~45° valve) | SOP / schematic |

---

## 3. Required HardwareX sections → repository sources

### 3.1 Hardware in context (Introduction)
- Motivation: only ME-department machine able to reach Ni/Fe melting temperatures;
  need controlled grain growth and oxidation-free annealing.
- Procurement history / alternative approaches: the lab evaluated commercial modern
  induction systems. A CYSI GP-15A (China) was purchased first but **did not meet the
  lab's needs** — the required analog (0–5 V / 4–20 mA) remote-control spec was lost
  across model substitutions (SP-AB-25 → SPZ-25 → SPZ-15) — so it was **abandoned and
  is no longer in use**. The lab has since moved to a **new USA-sourced unit (East Coast
  Induction / CEIA 6 kW)**, whose controller does provide the analog (4–20 mA) input.
  - Sources: `docs/east-coast-induction/` (`heater-notes.txt`, Master Controller v3+ /
    Power Cube manuals, pyrometer notes), `docs/quotes/`, and `docs/CYSI/`
    (order-issue chat log documenting the missing 0–5 V control spec on the GP-15A).
- **Angle:** the reproducible contribution remains the LabVIEW/DAQ + vacuum + pyrometer
  control retrofit, which is intentionally **furnace-agnostic** — it has been applied to
  the legacy LEPEL unit and ports to the new East Coast Induction generator (and could be
  reused by other labs with similar vintage or commercial induction hardware), rather than
  being locked to any single furnace vendor.

### 3.2 Hardware description
- System block diagram: pump (Edwards T-Station 85) → bellows → quartz-tube chamber →
  pyrometer + holder + quartz disc → induction heating head/coil → induction generator;
  support stand with clamps; recirculating chiller; DAQ.
  - Sources: `docs/induction-furnace-schematic.pptx` and `docs/schematic.pptx`
    (extracted: [`schematic_induction_furnace.md`](extracted-context/schematic_induction_furnace.md),
    [`schematic_support_stand.md`](extracted-context/schematic_support_stand.md)).
- Subsystems to describe: (a) RF generator + work coil, (b) vacuum + gas, (c) optical
  temperature sensing, (d) control/DAQ + LabVIEW, (e) mechanical support stand.

### 3.3 Design files
Populate the HardwareX *Design Files Summary* table from version-controlled artifacts:

| Design file | Type | License | Location |
|-------------|------|---------|----------|
| LabVIEW control VIs (`induction-furnace-control.vi`, `manual-induction-furnace-control.vi`, `pid-tuning.vi`, `pid-tuning-v2.vi`, `send-email.vi`) | LabVIEW `.vi` | (set repo license) | [`../code/induction-furnace-control-code/`](../code/induction-furnace-control-code/) |
| Manual ramping v5 VIs | LabVIEW `.vi` | (set) | [`../code/manual-ramping-v5/`](../code/manual-ramping-v5/) |
| `plotheatcurve.m` | MATLAB | (set) | [`../code/plotheatcurve.m`](../code/plotheatcurve.m) |
| Coil drawing | PDF/OXPS | (set) | `docs/coils-drawing.pdf`, `docs/coils.oxps` |
| System schematics | PPTX | (set) | `docs/*.pptx` (+ extracted text/figures) |
| Temp-control wiring | PNG | (set) | `docs/temp-control-modification/0-5V PLC wire design.png` |
| KF40 overpressure ring | STEP | (set) | `docs/KF Supplies/KF40_overpressureCenteringRing.step` |
| Graphite crucible/susceptor | machining drawing (to add) | (set) | machined from Cotronics 56L-3 3000 °C graphite (`extracted-context/parts_list.md`) |

- **Gap:** confirm an OSHW-compatible license is declared at the repo root (`LICENSE`).
  Export `.vi` block diagrams to PDF/PNG so non-LabVIEW readers can inspect logic.

### 3.4 Bill of materials
- The **reproducible BOM is anchored on the current USA-sourced generator** (CEIA "Power
  Cube" 6 kW + Master Controller v3+, via East Coast Induction) plus the retrofit parts
  the lab adds around any generator. Separate the BOM into three blocks so the
  "reproducible" portion is unambiguous:
  1. **Induction generator + controller** (current USA unit) — the legacy LEPEL is listed
     only as the prototype alternative, not the canonical line item.
  2. **Retrofit / control + vacuum + sensing** parts (the reproducible additions).
  3. **Consumables** (crucibles, quartz tube, gas).
- Primary source for the retrofit/consumable parts: `docs/induction_parts_list.xlsx`
  (extracted to [`extracted-context/parts_list.md`](extracted-context/parts_list.md)) —
  already lists vendors, quantities, prices, and rationale (Cotronics, QSI Quartz,
  McMaster-Carr, IdealVac, Mouser, eBay), e.g. **machined graphite crucible stock
  (Cotronics 56L-3, 3000 °C) and graphite repair cement (Resbond 931)**, quartz tube,
  KF40 vacuum parts, dual-wavelength pyrometer, vent valve, gas regulator, optical windows.
- **Action:** reshape into the HardwareX BOM schema (Designator, Component, Number,
  Cost/unit, Total, Source, Material type), add currency/date, and add the generator +
  controller + chiller line items (with East Coast Induction as the source).

### 3.5 Build instructions
- Mechanical: assemble support stand (8 short + 4 long sections, 12 corner braces,
  4 floor mounts — see `schematic.pptx` slide 2), mount generator/head, route coil.
- Coil: wind/water-cool to corrected geometry (3″ tall, 2.5″ ID, 6.5 turns) — use
  `induction_order_corrections.pptx` figures as the before/after reference.
- **Crucible/susceptor:** machine the graphite crucible from 3000 °C graphite stock to
  fit inside the quartz tube and accept the sample; this graphite crucible acts as the
  RF susceptor (it couples to the field and conducts heat to non/poorly-coupling charges
  such as YSZ). Repair cracks with graphite cement (Resbond 931). Seat it on the
  ceramic-cylinder/Teflon spacer stack described in the SOP.
- Vacuum: quartz tube + KF40 flange + optical window (Torr-Seal or O-ring bracket),
  bellows to Edwards T-Station 85 turbo pump, vent valve, gas line.
- Electrical/control: wire the DAQ analog out to the generator's analog power-control
  input (4–20 mA on the current USA controller; 0–5 mA on the legacy LEPEL); wire the
  pyrometer/PLC temperature-control path (`temp-control-modification/`).
- **Gap:** step-by-step photos exist mostly inside `data_log/.../IFrun036_*` and the
  pptx media — curate a clean build sequence; some steps need new photos.

### 3.6 Operation instructions
- **Strong existing source:** `docs/induction_SOP_200901.docx` is a complete SOP
  (load sample → pump down → cooling water → power-on sequence: solenoid/filament/
  overload-reset/plate/RF → run LabVIEW ramp → shutdown in reverse → vent).
  Extracted verbatim to
  [`extracted-context/SOP_induction_200901.md`](extracted-context/SOP_induction_200901.md);
  alternate SOP in [`SOP_alternate.md`](extracted-context/SOP_alternate.md).
- **Action:** condense the SOP into the HardwareX "Operation instructions" section and
  move the long safety narrative into a dedicated Safety subsection.

### 3.7 Validation and characterization
- Source: `docs/data_log/` — 100+ runs (IFrun001–100) across Ni200, Ni4N5, YSZ, and Pd
  thermal-evaporation experiments; temperatures 900–1400 °C; durations 5 min–40 h, each
  with `.xlsx`/`.txt`/`.lvm` traces and some photos (e.g. `IFRun078_PdRamping.PNG`).
- **Proposed validation figures:**
  1. Current→temperature calibration curve (linear correlation noted in SOP).
  2. Representative ramp/soak profile (e.g. 1200 °C/12 h Ni anneal) from a data log.
  3. Temperature stability / control performance before vs. after PID + pyrometer
     closed-loop modification.
  4. **Real microstructural results — SEM micrographs and EBSD orientation/grain-size
     maps** of annealed samples (e.g. Ni200 / Ni4N5), demonstrating the grain growth the
     system was built to achieve. Compare as-received vs. annealed grain size, and (where
     available) grain size vs. anneal temperature/time, to validate that the closed-loop
     thermal profile produces the intended microstructure.
     - **Action/gap:** locate and add the SEM/EBSD image files and the corresponding run
       IDs from `data_log/`; if not yet in the repo, request them from the student work
       (`docs/student-work/RyanWeber.pdf`) and add raw micrographs under `paper/figures/`.
- **Action:** pick canonical runs, parse logs (reuse `plotheatcurve.m` or a Python
  equivalent), and generate publication figures committed under `paper/figures/`.

### 3.8 Safety
- Extract from the SOP: high voltage/RF shock hazards near coils; keep conductive
  objects/electronics ≥6–12″ away; lockout-tagout for the internal transformer tap
  change; never open the manual vent valve while the turbo pump spins; nitrile gloves
  to avoid vacuum contamination; melt/drip and quartz-failure risks.

### 3.9 Closing matter
- Acknowledgements (BYU ME dept., Johnson group, K. Cole), CRediT author roles,
  declaration of interests, references (induction heating, eddy currents, ICP plasma,
  grain growth), and any data-availability statement pointing back to this repo.

---

## 4. Gap checklist before submission

- [ ] Confirm/declare an OSHW-compatible license at repo root and in the Design Files table.
- [ ] Export LabVIEW `.vi` logic to PDF/PNG for non-LabVIEW readers.
- [ ] Reformat `induction_parts_list.xlsx` into the HardwareX BOM schema (with date/currency).
- [ ] Curate a clean, photographed build sequence (coil, vacuum, control wiring).
- [ ] Select canonical validation runs from `data_log/` and generate figures.
- [ ] Add real **SEM and EBSD** micrographs / grain-size maps of annealed samples for the validation section.
- [ ] Document the **custom-machined graphite crucible/susceptor** (drawing, stock, machining steps) in Design files + Build.
- [ ] Anchor the BOM and specs on the **current USA generator** (CEIA Power Cube / East Coast Induction); keep LEPEL only as the prototype.
- [ ] Obtain/confirm measured specs (frequency, achievable T, vacuum, control resolution).
- [ ] Pull author list, affiliations, funding, and CRediT roles.
- [ ] Resolve the legacy-vs-retrofit boundary so the "reproducible" portion is unambiguous.

---

## 5. Extracted context committed alongside this plan

To make the binary source documents reviewable as version-controlled text/figures,
their content has been extracted into
[`extracted-context/`](extracted-context/) (see its
[`README.md`](extracted-context/README.md)) and
[`extracted-context/figures/`](extracted-context/figures/). The original binary files
in [`../docs/`](../docs/) remain the source of record.
