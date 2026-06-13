---
title: "Retrofitting a commercial RF induction generator into a computer-controlled, vacuum-integrated annealing system for reactive-metal grain growth"
subtitle: "HardwareX manuscript draft"
author:
  - Sterling G. Baird
  - Kevin Cole
  - "[additional authors — to confirm]"
date: 2026-06-13
keywords:
  - induction furnace
  - grain growth
  - vacuum annealing
  - LabVIEW
  - pyrometer
  - open-source hardware
---

> **Status:** working draft generated from the repository's design files, standard
> operating procedure, parts list, schematics, and run logs. Bracketed `[TODO]` markers
> flag values or figures that still need to be confirmed or added before submission. The
> reproducible build and bill of materials are anchored on the lab's **current,
> USA-sourced induction generator** (CEIA "Power Cube" 6 kW, procured through East Coast
> Induction); the ~1970 LEPEL furnace is documented only as the originating prototype.
>
> An independent review of this draft against the HardwareX section requirements, and the
> resulting action checklist, are recorded in [`edison-feedback/`](edison-feedback/); its
> highest-priority items have been folded into the BOM, specifications table, and the
> plan's gap checklist.

# Specifications table

| Property | Value |
|----------|-------|
| Hardware name | Computer-controlled, vacuum-integrated induction annealing system |
| Subject area | Materials science; mechanical engineering (thermal processing / grain growth) |
| Hardware type | Heat-treatment / annealing furnace; vacuum system; instrument control |
| Closest commercial analog | Vacuum induction annealing furnace (turn-key systems cost $50k–$200k+) |
| Open-source license | `[TODO: proposed — CERN-OHL-S v2 for hardware/design files + MIT for code; add a LICENSE file at the repo root before submission]` |
| Cost of hardware | `[TODO: total; retrofit + consumables ≈ $1–2k on top of the generator]` |
| Source file repository | `[TODO: mint a permanent DOI — e.g. Zenodo — for the repository; HardwareX does not accept a bare GitHub URL]` |
| Induction generator (reproducible build) | CEIA "Power Cube" 6 kW solid-state RF generator + Master Controller v3+ (East Coast Induction, USA) |
| Induction generator (prototype) | LEPEL high-frequency tube furnace (~1970), up to ~35 kW |
| Power-control input | Analog setpoint via LabVIEW/DAQ (4–20 mA on current controller; 0–5 mA on LEPEL) |
| Max sample temperature | ~1400–1500 °C+ (Ni/Fe melting range) |
| Vacuum level | ~1×10⁻⁶ to 1×10⁻⁸ Torr (Edwards T-Station 85 turbo-molecular pump) |
| Temperature measurement | IMPAC ISR6 dual-wavelength ratio pyrometer (range ~800–2500 °C) |
| Chamber | Quartz tube, KF40 optical-window flange, inert-gas vent |
| Crucible / susceptor | In-house machined graphite (3000 °C grade) crucible-susceptor |
| Work coil | Water-cooled copper, ~3″ tall, 2.5″ ID, ~6.5 turns |

# Hardware in context

High-temperature annealing near a metal's melting point drives controlled **grain
growth**, which is central to studying microstructure–property relationships in metals
such as nickel and iron. Doing this without oxidizing the sample requires both high
temperature (~1400–1500 °C) and high vacuum (or inert atmosphere). Commercial vacuum
induction annealing furnaces that meet these requirements are expensive turn-key systems,
which puts them out of reach for many academic labs.

This work takes the opposite approach: rather than building or buying a complete furnace,
we **retrofit and modernize a bare RF induction generator** into a full annealing system
by adding (1) computer power control, (2) closed-loop optical temperature control, (3) a
high-vacuum quartz-tube chamber, and (4) a machined graphite crucible/susceptor. The
emphasis of the contribution is the **modernization stack itself**, which is deliberately
**generator-agnostic**: the same control software, vacuum chamber, pyrometer feedback,
crucible, and work-coil geometry transfer from one induction generator to another. The
only requirement a reader's generator must satisfy is an **analog power-control input that
maps roughly linearly to output power** (e.g. 4–20 mA or 0–5 V / 0–5 mA). That
portability is the reproducible result and is what makes the design reusable by other labs
that already own, or can buy, such an induction generator.

A second feature that broadens the system's applicability is the **machined graphite
crucible/susceptor**: because graphite couples strongly to the RF field and heats the
charge indirectly by conduction and radiation, the furnace is not limited to electrically
conductive samples — it can also process poorly- or non-coupling materials such as YSZ
ceramic. This makes the same build useful well beyond reactive-metal annealing.

The modernization was first prototyped on a ~1970 LEPEL high-frequency induction furnace
owned by the BYU Mechanical Engineering department — at the time the only departmental
machine able to reach the Ni/Fe melting range. A "remote control" capability was added in
August 2019 to drive the generator's power from a computer instead of the front-panel
knob. The lab subsequently moved the same stack onto a current, USA-sourced solid-state
generator (CEIA "Power Cube" 6 kW via East Coast Induction), whose Master Controller v3+
accepts a standard analog (4–20 mA) power setpoint. An intermediate, separately-purchased
import generator (CYSI GP-15A) was evaluated but did not meet the lab's control
requirements — the required analog remote-control input was lost across vendor model
substitutions — and was retired. The reproducible build documented here therefore targets
the current USA generator, with the LEPEL retrofit retained as historical context.

Compared with commercial vacuum annealing furnaces, this approach is roughly an
order of magnitude cheaper, is repairable and modifiable by the user, and is broadly
reusable: any lab with an induction generator and an analog power input can reproduce the
control, vacuum, and temperature-sensing additions described below.

# Hardware description

The system comprises five subsystems (see the schematics in
[`extracted-context/schematic_induction_furnace.md`](extracted-context/schematic_induction_furnace.md)
and [`extracted-context/schematic_support_stand.md`](extracted-context/schematic_support_stand.md)):

1. **RF generator + work coil.** A solid-state induction generator (current build: CEIA
   Power Cube 6 kW) drives a water-cooled copper work coil. The coil carries both the
   oscillating current and cooling water. Coil geometry (~3″ tall, 2.5″ ID, ~6.5 turns)
   was tuned to the sample/crucible stack (see
   [`extracted-context/order_corrections_coils.md`](extracted-context/order_corrections_coils.md)).

2. **Vacuum + gas.** A quartz tube forms the chamber and is connected through a KF40
   flange and flexible bellows to an Edwards T-Station 85 turbo-molecular pump
   (~1×10⁻⁶–10⁻⁸ Torr). A manual vent valve and an inert-gas regulator allow controlled
   venting/backfilling to suppress oxidation of reactive metals.

3. **Optical temperature sensing.** A dual-wavelength (ratio) pyrometer (IMPAC ISR6; also
   a LumaSens 800–2500 °C unit) views the sample through a KF40 optical window, providing
   a non-contact temperature signal that is robust to emissivity changes and to the RF
   field that would corrupt thermocouples.

4. **Control / DAQ + LabVIEW.** A LabVIEW DAQ analog output sets generator power; the
   pyrometer signal is read back for closed-loop ramp/soak control. The VIs implement
   manual control, automated ramping, PID tuning, and email alerts
   (see [`../code/`](../code/)).

5. **Mechanical support stand + crucible.** A bolted support stand (8 short + 4 long
   sections, 12 corner braces, 4 floor mounts) positions the chamber, coil, pyrometer
   holder, and quartz disc. An **in-house machined graphite crucible** holds the sample
   and acts as the RF susceptor.

## Custom-machined graphite crucible / susceptor

Because some charges of interest couple poorly to the RF field (e.g. YSZ ceramic) or must
be physically contained, the sample is held in a **graphite crucible machined in-house
from 3000 °C-grade graphite stock** (Cotronics 56L-3). The graphite couples strongly to
the induction field and acts as a **susceptor**, transferring heat to the contained charge
by conduction/radiation; this makes the same furnace usable for conductive metals (direct
coupling) and for non/poorly-coupling materials (indirect, susceptor-driven heating).
Crucibles are machined to fit inside the quartz tube and seat on a ceramic-cylinder /
Teflon spacer stack. Cracked crucibles are repaired with a 3000 °C graphite cement
(Resbond 931) rather than discarded. `[TODO: add the crucible machining drawing and
photos to paper/figures/.]`

# Design files summary

| Design file | File type | Open source license | Location of the file |
|-------------|-----------|---------------------|----------------------|
| LabVIEW control VIs (furnace control, manual control, PID tuning v1/v2, email alert) | LabVIEW `.vi` | MIT (proposed) | [`../code/induction-furnace-control-code/`](../code/induction-furnace-control-code/) |
| Manual ramping v5 VIs | LabVIEW `.vi` | MIT (proposed) | [`../code/manual-ramping-v5/`](../code/manual-ramping-v5/) |
| `plotheatcurve.m` (heat-curve plotter) | MATLAB | MIT (proposed) | [`../code/plotheatcurve.m`](../code/plotheatcurve.m) |
| Work-coil drawing | PDF / OXPS | CERN-OHL-S (proposed) | `docs/coils-drawing.pdf`, `docs/coils.oxps` |
| System schematics | PPTX (+ extracted text/figures) | CERN-OHL-S (proposed) | `docs/*.pptx`, [`extracted-context/`](extracted-context/) |
| Temperature-control wiring | PNG | CERN-OHL-S (proposed) | `docs/temp-control-modification/0-5V PLC wire design.png` |
| KF40 overpressure centering ring | STEP | CERN-OHL-S (proposed) | `docs/KF Supplies/KF40_overpressureCenteringRing.step` |
| Graphite crucible/susceptor machining drawing | `[TODO: add]` | CERN-OHL-S (proposed) | `[TODO]` |

`[TODO: export the LabVIEW .vi block diagrams to PDF/PNG so non-LabVIEW readers can
inspect the control logic.]`

# Bill of materials summary

HardwareX requires a single 7-column BOM table; groupings are denoted by the designator
prefix: **GEN** = induction generator + controller (the current USA reproducible build;
the legacy LEPEL is the prototype alternative, not a line item), **RETRO** = the
reproducible retrofit (control / vacuum / sensing) parts, and **CONS** = consumables.
Full vendor/price detail for the RETRO and CONS parts is in
[`extracted-context/parts_list.md`](extracted-context/parts_list.md) (extracted from
`docs/induction_parts_list.xlsx`).

| Designator | Component | Number | Cost per unit | Total cost | Source of materials | Material type |
|------------|-----------|-------:|---------------|-----------:|---------------------|---------------|
| GEN-1 | CEIA "Power Cube" 6 kW solid-state RF generator | 1 | `[TODO]` | `[TODO]` | East Coast Induction (USA) | — |
| GEN-2 | Master Controller v3+ | 1 | `[TODO]` | `[TODO]` | East Coast Induction (USA) | — |
| GEN-3 | Recirculating water chiller | 1 | `[TODO]` | `[TODO]` | `[TODO]` | — |
| RETRO-1 | LabVIEW-compatible DAQ (analog out + in), e.g. NI USB-6009 `[confirm model]` | 1 | `[TODO]` | `[TODO]` | National Instruments | — |
| RETRO-2 | Dual-wavelength pyrometer (IMPAC ISR6 / LumaSens) | 1 | ~$241 (used) | ~$241 | eBay / OEM | — |
| RETRO-3 | Edwards T-Station 85 turbo-molecular pump | 1 | `[TODO]` | `[TODO]` | Edwards | — |
| RETRO-4 | Edwards TAV5 vent valve | 1 | ~$59 | ~$59 | eBay | — |
| RETRO-5 | Inert-gas regulator (Fisher FS-50) | 1 | ~$38 | ~$38 | Fisher Scientific | — |
| RETRO-6 | KF40 flanges, clamps, centering rings, optical window | 1 set | see parts list | `[TODO]` | IdealVac / McMaster | aluminum / quartz |
| CONS-1 | Quartz tube (35 mm ID), cut to length | 1–2 | ~$67 | ~$134 | QSI Quartz | fused quartz |
| CONS-2 | Graphite stock for machined crucible/susceptor (56L-3, 3000 °C) | 1 | ~$99 | ~$99 | Cotronics | graphite |
| CONS-3 | Graphite repair cement (Resbond 931) | 1 | ~$108 | ~$108 | Cotronics | graphite |
| CONS-4 | Torr-Seal epoxy / O-rings | 1 set | see parts list | `[TODO]` | — | epoxy / elastomer |

`[TODO: confirm GEN-1/2/3 and RETRO-1/3 pricing; add currency (USD) and quote year.]`

# Build instructions

1. **Support stand.** Assemble the bolted stand (8 short + 4 long sections, 12 corner
   braces, 4 floor mounts) and mount the generator/heating head and pyrometer holder.
2. **Work coil.** Form/water-cool the copper coil to the corrected geometry (~3″ tall,
   2.5″ ID, ~6.5 turns); connect to the generator head and the cooling-water circuit. Use
   the before/after figures from `induction_order_corrections.pptx` as the reference.
3. **Graphite crucible/susceptor.** Machine the crucible from 3000 °C graphite stock to
   fit inside the quartz tube and accept the sample. Seat it on the ceramic-cylinder /
   Teflon spacer stack. Repair any cracks with graphite cement.
4. **Vacuum chamber.** Mount the quartz tube with the KF40 flange and optical window
   (set the window with the overpressure centering ring + clamp, or Torr-Seal). Connect
   the flexible bellows to the Edwards T-Station 85 turbo pump; install the manual vent
   valve and inert-gas line.
5. **Control wiring.** Wire the DAQ analog output to the generator's analog power-control
   input (4–20 mA on the current controller; 0–5 mA on the LEPEL prototype). Wire the
   pyrometer output into the DAQ analog input and, for closed-loop ramping, the
   pyrometer/PLC temperature-control path (`docs/temp-control-modification/`).
6. **Software.** Deploy the LabVIEW VIs from [`../code/`](../code/) and configure the DAQ
   channels; verify manual control before enabling automated ramp/soak.

`[TODO: curate a clean, photographed build sequence — candidate photos exist in
docs/data_log/.../IFrun036_* and the PPTX media.]`

# Operation instructions

Condensed from the lab SOP
([`extracted-context/SOP_induction_200901.md`](extracted-context/SOP_induction_200901.md)):

1. **Load the sample.** Vent the chamber (confirm atmospheric pressure; never open the
   vent valve while the turbo pump is spinning). Stack sample → optional alumina plate →
   ceramic cylinder → Teflon spacer inside the graphite crucible, insert into the quartz
   tube, and clamp the KF40 flange finger-tight with the O-ring.
2. **Pump down.** Close the vent valve, start the roughing/turbo pumps, and wait for
   high vacuum (~1×10⁻⁶ Torr or better).
3. **Cooling water.** Open the facility cooling-water valve (~45°, half open) and the
   generator chiller; check for leaks and confirm flow before applying RF power.
4. **Power on.** Bring up the generator per its sequence, then run the LabVIEW ramp/soak
   profile (analog setpoint to the generator; pyrometer feedback for closed-loop control).
5. **Anneal.** Hold the temperature/time profile (e.g. ~1200 °C for several hours for Ni
   grain growth); the VI can email status alerts.
6. **Shutdown.** Ramp power down, stop RF, then turn off cooling water, allow the sample
   to cool under vacuum, and vent only after the turbo pump has stopped.

# Validation and characterization

**Thermal performance.** The repository contains 100+ logged runs (`docs/data_log/`,
IFrun001–100) across Ni200, Ni4N5, YSZ, and Pd thermal-evaporation experiments, with
temperatures of ~900–1400 °C and soak durations from minutes to ~40 h, each with
`.xlsx`/`.txt`/`.lvm` traces and some photos. Proposed thermal validation figures:

1. **Power-setpoint → temperature calibration** curve (the SOP notes an approximately
   linear current↔temperature correlation).
2. **Representative ramp/soak profile** (e.g. a 1200 °C multi-hour Ni anneal) parsed from
   a data log via `plotheatcurve.m` or a Python equivalent.
3. **Control performance**: temperature stability before vs. after adding PID + pyrometer
   closed-loop control.

**Microstructural validation (SEM + EBSD).** The intended outcome of the furnace is
controlled grain growth, so the key validation is **real microstructural data**:

- **SEM micrographs** of as-received vs. annealed samples (e.g. Ni200 / Ni4N5) showing the
  increase in grain size produced by the anneal.
- **EBSD orientation and grain-size maps** quantifying grain-size distribution (and, where
  multiple runs are available, grain size vs. anneal temperature/time), confirming that
  the closed-loop thermal profile yields the targeted microstructure.

`[TODO: add the SEM and EBSD image files and identify the corresponding data_log run IDs;
source candidate micrographs from docs/student-work/RyanWeber.pdf and add raw images under
paper/figures/.]`

# Safety

- **High voltage / RF.** Lethal voltages and strong RF fields are present near the coil.
  Keep conductive objects, jewelry, watches, phones, and electronics ≥6–12″ from the coil
  while powered; nearby conductive hardware can deliver a shock.
- **Lockout-tagout.** Changing the generator's internal transformer tap (to adjust max
  power, LEPEL prototype) requires a lockout-tagout procedure.
- **Vacuum.** Never open the manual vent valve while the turbo pump is spinning — this can
  destroy the pump. Handle the vacuum gauge and quartz tube carefully (both are fragile
  and costly).
- **Thermal.** Samples reach ~1400–1500 °C; melt/drip and quartz-tube failure are risks.
  Wear clean nitrile gloves when loading/unloading to avoid contaminating the vacuum.

# Ethics statements

This work did not involve human participants, human data, or animal subjects. There are
no associated ethical considerations.

# Declarations

- **CRediT author roles:** `[TODO]`
- **Acknowledgements:** BYU Mechanical Engineering Department; the Johnson group;
  Kevin Cole. `[TODO: funding sources.]`
- **Declaration of competing interests:** `[TODO]`
- **Data availability:** design files, logs, and extracted context are in this repository
  (`vertical-cloud-lab/custom-induction-furnace`).

# References

`[TODO: add the formatted reference list before submission. Anticipated citations:
(1) a general induction-heating / eddy-current reference (e.g. Davies, *Conduction and
Induction Heating*) for the physics of RF coupling and susceptor heating; (2) a grain-growth
/ recrystallization reference (e.g. Humphreys & Hatherly, *Recrystallization and Related
Annealing Phenomena*) motivating the annealing study; (3) a ratio/dual-wavelength pyrometry
reference for the non-contact temperature measurement; (4) the HardwareX author guidelines;
and (5) any prior open-source furnace-control hardware papers used for comparison. Confirm
exact citations and DOIs.]`
