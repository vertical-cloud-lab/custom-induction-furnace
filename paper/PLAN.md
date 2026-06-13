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

This project is **not** a from-scratch furnace. It is the **retrofit and
modernization of a ~1970 LEPEL high-frequency induction furnace** (owned by the
BYU Mechanical Engineering department) into a **computer-controlled, vacuum-integrated
annealing system** for grain-growth and thin-film studies. The novel, reproducible
hardware/firmware contributions are:

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
5. **Operational tooling** — LabVIEW VIs for ramping, manual control, PID tuning, and
   automated email alerts; a MATLAB heat-curve plotter. (Source: [`../code/`](../code/).)

**Working title (draft):** *"Retrofitting a vintage high-frequency induction furnace
for computer-controlled, vacuum-integrated annealing of reactive metals."*

**Target subject area:** Materials science / mechanical engineering — thermal
processing and grain-growth annealing.

---

## 2. Specifications table (draft values)

To be finalized once measured values are confirmed from the data logs.

| Property | Value (draft) | Source |
|----------|---------------|--------|
| Furnace base unit | LEPEL high-frequency induction furnace (~1970) | SOP |
| RF frequency | ~200–450 kHz | SOP |
| Max RF power | up to ~35 kW | SOP |
| Power control input | 0–5 mA analog (LabVIEW/DAQ) → off→full power | SOP |
| Max sample temperature | ~1400–1500 °C+ (Ni/Fe melting range) | SOP |
| Vacuum level | ~1×10⁻⁶ to 1×10⁻⁸ Torr (turbo-molecular pump) | SOP |
| Temperature measurement | optical / dual-wavelength pyrometer (e.g. LumaSens 800–2500 °C) | parts list |
| Chamber | quartz tube with KF40 optical-window flange | SOP / parts list |
| Work coil | ~3″ tall, 2.5″ ID, ~6.5 turns, water-cooled copper | order corrections |
| Cooling | recirculating water chiller + facility water (~45° valve) | SOP / schematic |

---

## 3. Required HardwareX sections → repository sources

### 3.1 Hardware in context (Introduction)
- Motivation: only ME-department machine able to reach Ni/Fe melting temperatures;
  need controlled grain growth and oxidation-free annealing.
- Prior/alternative approaches: commercial modern induction systems quoted but costly
  (East Coast Induction / CEIA 6 kW; CYSI GP-15A purchased with control-spec issues).
  - Sources: `docs/east-coast-induction/` (`heater-notes.txt`, manuals, quotes),
    `docs/quotes/`, `docs/CYSI/` (`order_issues.txt`,
    [`extracted-context/...`] QIN ERIC chat log showing the missing 0–5 V control spec).
- **Angle:** modernizing legacy equipment is far cheaper and is broadly reusable by
  other labs with similar vintage induction hardware.

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

- **Gap:** confirm an OSHW-compatible license is declared at the repo root (`LICENSE`).
  Export `.vi` block diagrams to PDF/PNG so non-LabVIEW readers can inspect logic.

### 3.4 Bill of materials
- Primary source: `docs/induction_parts_list.xlsx` (extracted to
  [`extracted-context/parts_list.md`](extracted-context/parts_list.md)) — already lists
  vendors, quantities, prices, and rationale (Cotronics, QSI Quartz, McMaster-Carr,
  IdealVac, Mouser, eBay), e.g. crucible ceramics, quartz tube, KF40 vacuum parts,
  dual-wavelength pyrometer, vent valve, gas regulator, relief valves, optical windows.
- **Action:** reshape into the HardwareX BOM schema (Designator, Component, Number,
  Cost/unit, Total, Source, Material type), add currency/date, and split "furnace base
  unit" (legacy) from "retrofit components" (reproducible additions).

### 3.5 Build instructions
- Mechanical: assemble support stand (8 short + 4 long sections, 12 corner braces,
  4 floor mounts — see `schematic.pptx` slide 2), mount generator/head, route coil.
- Coil: wind/water-cool to corrected geometry (3″ tall, 2.5″ ID, 6.5 turns) — use
  `induction_order_corrections.pptx` figures as the before/after reference.
- Vacuum: quartz tube + KF40 flange + optical window (Torr-Seal or O-ring bracket),
  bellows to turbo pump, vent valve, gas line.
- Electrical/control: wire DAQ analog out to the furnace power-control input; wire the
  0–5 V pyrometer/PLC temperature-control path (`temp-control-modification/`).
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
  4. Microstructure/grain-growth outcome (if available from student work,
     `docs/student-work/RyanWeber.pdf`).
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
