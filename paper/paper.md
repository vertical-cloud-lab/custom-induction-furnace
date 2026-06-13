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
| Power-control input | Analog setpoint via LabVIEW/DAQ → current-loop conditioner (4–20 mA on current controller; 0–5 mA on LEPEL) |
| Generator-input standard required | External analog power-control input with **monotonic** command→power response over the usable range |
| Control signal chain | DAQ analog output (0–5 V) → voltage-to-current (4–20 mA) loop conditioner → generator power-setpoint input; pyrometer analog output → DAQ analog input (scaled to °C) |
| Max sample temperature | ~1400–1500 °C+ (Ni/Fe melting range) |
| Pyrometer detection range | ~800–2500 °C (dual-wavelength ratio); does not report below ~700 °C |
| Demonstrated soak duration | minutes up to ~40 h (per `docs/data_log/` run logs) |
| Sample / crucible envelope | charge fits inside a 35 mm-ID quartz tube and a machined graphite crucible |
| Vacuum level | ~1×10⁻⁶ to 1×10⁻⁸ Torr (Edwards T-Station 85 turbo-molecular pump) |
| Temperature measurement | LumaSense IMPAC ISR 6 dual-wavelength ratio pyrometer (~800–2500 °C) |
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
only requirement a reader's generator must satisfy is an **analog power-control input with
a monotonic command→power response** over the usable range (e.g. 4–20 mA or 0–5 V / 0–5 mA);
near-linearity is convenient but not required, because the pyrometer feedback and PID
calibration absorb any nonlinearity. That portability is the reproducible result and is what
makes the design reusable by other labs that already own, or can buy, such an induction
generator.

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

Compared with commercial vacuum annealing furnaces, this approach has **substantially
lower capital cost** (the retrofit and consumables add roughly $1–2k on top of a generator
a lab already owns, versus $50k–$200k+ for turn-key systems), is repairable and modifiable
by the user, and is broadly reusable: any lab with an induction generator and an analog
power input can reproduce the
control, vacuum, and temperature-sensing additions described below.

## Reproducibility boundary

To be explicit about what this paper does and does not reproduce: **this work does not
reproduce the RF generator internals.** It reproduces the *modernization layer* built
around a compatible generator — the computer power control, optical (pyrometer) feedback,
high-vacuum quartz-tube chamber, machined graphite crucible/susceptor, work-coil geometry,
and the mechanical support fixturing. A reader supplies (or already owns) a compatible
generator and rebuilds the layer described here.

## Prior art and comparison

| Class | Examples | Limitation this design addresses |
|-------|----------|----------------------------------|
| Commercial vacuum induction annealing furnaces | turn-key systems ($50k–$200k+) | Cost; closed/non-modifiable; vendor lock-in |
| Open non-induction annealing systems | tube/box furnaces with resistive heating | Lower max temperature and slower ramp than induction; no RF-susceptor heating of non-coupling charges |
| Induction generators sold bare | CEIA, Ambrell, etc. | Ship without integrated vacuum, optical feedback, or computer setpoint control — exactly the layer added here |

## Generator compatibility requirements

The control/sensing/vacuum layer transfers to any generator that meets these criteria:

- Exposes an **external analog power-control input** (e.g. 4–20 mA or 0–5 V/0–5 mA).
- The command→delivered-power response is **monotonic over the usable range** (near-linear
  is convenient but not required, since the pyrometer feedback closes the loop).
- Supports a **water-cooled induction head/coil** matching the documented coil dimensions.
- Delivers **enough RF power** to reach the target temperature for the documented
  crucible/sample stack.
- Allows **safe electrical isolation** between the DAQ/control path and the generator input.
- Has the required cooling and line power for the selected generator.

When porting to a new generator, the following must be re-established: analog-command
scaling, power-to-temperature calibration, PID gains, coil/sample alignment, maximum safe
ramp rate, and any generator-specific interlock behavior.

## Transferability: LEPEL prototype → CEIA reproducible build

| Aspect | LEPEL prototype (~1970) | CEIA reproducible build (current) | Transferred? |
|--------|-------------------------|-----------------------------------|--------------|
| Analog control interface | 0–5 mA | 4–20 mA (Master Controller v3+) | Concept yes; scaling re-set |
| Frequency | ~200–450 kHz tube | solid-state (generator-set) | n/a (generator internal) |
| Max power | up to ~35 kW | 6 kW | Re-tuned for charge |
| Pyrometer / optical feedback | dual-wavelength | same dual-wavelength stack | Yes |
| Vacuum chamber / quartz tube | quartz + KF40 | same | Yes |
| Graphite crucible/susceptor | machined graphite | same | Yes |
| Support stand / fixturing | bolted stand | same | Yes |
| LabVIEW/DAQ control concept | manual + ramp/PID VIs | same VIs | Yes |

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
   venting/backfilling to suppress oxidation of reactive metals. The vacuum connection
   stack, in order, is: **quartz tube → KF40 flange + optical window → flexible bellows →
   vacuum gauge → Edwards T-Station 85 → vent / inert-gas backfill branch.**

3. **Optical temperature sensing.** A dual-wavelength (ratio) pyrometer (the canonical unit
   is a LumaSense IMPAC ISR 6, 800–2500 °C; the IMPAC brand is LumaSense's) views the
   sample through a KF40 optical window, providing a non-contact temperature signal that is
   robust to emissivity changes and to the RF field that would corrupt thermocouples.

4. **Control / DAQ + LabVIEW.** A LabVIEW DAQ analog output sets generator power; the
   pyrometer signal is read back for closed-loop ramp/soak control. The VIs implement
   manual control, automated ramping, PID tuning, and email alerts
   (see [`../code/`](../code/)). In the CEIA build the DAQ outputs **0–5 V** to a
   **voltage-to-current loop conditioner** that converts the command to the controller's
   **4–20 mA** power-setpoint input (the LEPEL prototype instead took a 0–5 mA command
   directly). The closed-loop **signal flow** is therefore: **LabVIEW setpoint → DAQ
   analog output (0–5 V) → V→I conditioner (4–20 mA) → generator power → sample/crucible
   heating → pyrometer optical reading → DAQ analog input (scaled to °C) → PID controller →
   updated analog command.** The same path runs **open-loop** (direct command ramp) while
   the temperature is below the pyrometer's ~700 °C detection floor; once the pyrometer
   reports a **sustained valid reading above that floor**, control hands over to
   **closed-loop** PID on the optical temperature.

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

## Who can use this system

- Materials labs needing **oxidation-free grain-growth anneals** of reactive metals
  (Ni, Fe) near their melting points.
- Labs that own a **bare induction generator** and want to add computer setpoint control,
  optical feedback, and vacuum integration without buying a turn-key furnace.
- Groups processing **poorly- or non-coupling charges** (e.g. YSZ ceramic) that can be
  heated indirectly through the graphite susceptor.
- Teaching/maker contexts wanting a **repairable, modifiable** high-temperature vacuum
  furnace built from documented, open design files.

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

HardwareX requires a single 7-column BOM table. Groupings are denoted by the designator
prefix: **GEN** = induction generator + controller (the current USA reproducible build;
the legacy LEPEL is the prototype alternative, not a line item), **RETRO** = the
reproducible retrofit (control / vacuum / sensing) parts, and **CONS** = consumables.
Full vendor/price detail for the RETRO and CONS parts is in
[`extracted-context/parts_list.md`](extracted-context/parts_list.md) (extracted from
`docs/induction_parts_list.xlsx`).

**Costing conventions:** all costs are in **USD**; prices are the lab's purchase records
(quote year ~2019–2021), several from used/surplus/eBay sources as noted; shipping and tax
are excluded unless stated. The table below is the **canonical reproducible build only** —
legacy LEPEL and the rejected CYSI import path are documented in the text, not the BOM.

| Designator | Component | Number | Cost per unit | Total cost | Source of materials | Material type |
|------------|-----------|-------:|---------------|-----------:|---------------------|---------------|
| GEN-1 | CEIA "Power Cube" 6 kW solid-state RF generator | 1 | `[TODO]` | `[TODO]` | East Coast Induction (USA) | — |
| GEN-2 | Master Controller v3+ | 1 | `[TODO]` | `[TODO]` | East Coast Induction (USA) | — |
| GEN-3 | Recirculating water chiller | 1 | `[TODO]` | `[TODO]` | `[TODO]` | — |
| RETRO-1 | LabVIEW-compatible DAQ with analog out + in (e.g. NI USB-6001/6009-class, 0–5 V AO) `[confirm exact model]` | 1 | `[TODO]` | `[TODO]` | National Instruments | — |
| RETRO-2 | Dual-wavelength ratio pyrometer (LumaSense IMPAC ISR 6, 800–2500 °C) | 1 | $241 (used) | $241 | eBay / OEM | — |
| RETRO-3 | 24 V linear power supply for pyrometer (International Power) | 1 | $51 | $51 | Mouser | — |
| RETRO-4 | Voltage-to-current (0–5 V → 4–20 mA) loop conditioner for the generator power-setpoint input | 1 | `[TODO]` | `[TODO]` | `[TODO: signal-conditioning vendor]` | — |
| RETRO-5 | Edwards T-Station 85 turbo-molecular pump + gauge | 1 | `[TODO]` | `[TODO]` | Edwards | — |
| RETRO-6 | Edwards TAV5 vent valve | 1 | $59 | $59 | eBay | — |
| RETRO-7 | Inert-gas regulator (Fisher FS-50) | 1 | $38 | $38 | Fisher Scientific | — |
| RETRO-8 | KF40 overpressure centering ring | 1 | $19 | $19 | IdealVac | aluminum |
| RETRO-9 | KF40 plastic quick vacuum clamp | 1 | $23 | $23 | IdealVac | polymer |
| RETRO-10 | Optical window, quartz disc 55 mm × 1.5 mm (1 used; buy 3 for spares) | 3 | $18 | $54 | McMaster-Carr (custom) | fused quartz |
| RETRO-11 | Ultra-high-temperature quartz disc 2″ × 1/16″ | 1 | $19 | $19 | McMaster-Carr | fused quartz |
| RETRO-12 | Inert-gas plumbing (BSPT/KF adapters, barbs, tee, 10 psi relief valve McMaster 4772K4) | 1 set | see parts list | ~$66 | McMaster-Carr / BMotionTech | brass / steel |
| CONS-1 | Quartz tube, 4′ × 35 mm ID, cut to length | 2 | $67 | $134 | QSI Quartz | fused quartz |
| CONS-2 | Graphite stock for machined crucible/susceptor (56L-3, 3000 °C, 1″×6″×6″) | 1 | $99 | $99 | Cotronics | graphite |
| CONS-3 | Graphite repair cement (Resbond 931-1, 3000 °C) | 1 | $108 | $108 | Cotronics | graphite |
| CONS-4 | Alumina crucible stock (RTC-60-2, 1787 °C, 10 lb) | 1 | $91 | $91 | Cotronics | alumina |
| CONS-5 | Zirconia crucible stock (760-1, 2204 °C, 10 lb) | 1 | $124 | $124 | Cotronics | zirconia |
| CONS-6 | Torr-Seal high-vacuum epoxy / O-rings | 1 set | $57 | $57 | Varian / McMaster | epoxy / elastomer |

`[TODO: confirm GEN-1/2/3, RETRO-1/4/5 pricing, the exact NI DAQ model, and the V→I
loop-conditioner model; the GEN line items dominate total cost and must be filled from the
East Coast Induction quote before submission.]`

# Build instructions

1. **Support stand.** Assemble the bolted stand (8 short + 4 long sections, 12 corner
   braces, 4 floor mounts) and mount the generator/heating head and pyrometer holder.
2. **Work coil.** Form/water-cool the copper coil to the corrected geometry (~3″ tall,
   2.5″ ID, ~6.5 turns); connect to the generator head and the cooling-water circuit. Use
   the before/after figures from `induction_order_corrections.pptx` as the reference.
   `[TODO: state the exact copper-tube OD/wall, bend radius/spacing method, and
   cooling-connection fittings from the coil drawing (docs/coils-drawing.pdf).]`
3. **Graphite crucible/susceptor.** Machine the crucible from 3000 °C graphite stock to
   fit inside the quartz tube and accept the sample. Seat it on the ceramic-cylinder /
   Teflon spacer stack. Repair any cracks with graphite cement.
4. **Vacuum chamber.** Mount the quartz tube with the KF40 flange and optical window. The
   **reference build** seats a 55 mm quartz window on the overpressure KF40 centering ring
   and secures it with the plastic quick-clamp (reusable, no adhesive); a Torr-Seal'd blank
   flange is documented as an alternative for a permanent seal. Connect the flexible bellows
   to the Edwards T-Station 85 turbo pump; install the manual vent valve and inert-gas line.
5. **Control wiring.** Wire the DAQ analog output (0–5 V) through the voltage-to-current
   loop conditioner to the generator's analog power-control input (4–20 mA on the current
   CEIA controller; the LEPEL prototype took 0–5 mA directly). Wire the pyrometer output
   into the DAQ analog input and, for closed-loop ramping, the pyrometer/PLC
   temperature-control path (`docs/temp-control-modification/`). Maintain electrical
   isolation between the DAQ/control path and the generator interface.
6. **Software.** Deploy the LabVIEW VIs from [`../code/`](../code/) and configure the DAQ
   channels; verify manual control before enabling automated ramp/soak.

`[TODO: curate a clean, photographed build sequence — candidate photos exist in
docs/data_log/.../IFrun036_* and the PPTX media.]`

# Operation instructions

Condensed from the lab SOP
([`extracted-context/SOP_induction_200901.md`](extracted-context/SOP_induction_200901.md)).

## Preflight checklist (before energizing RF)

- [ ] Chamber at high vacuum (~1×10⁻⁶ Torr or better) or backfilled to the intended
      inert atmosphere.
- [ ] Cooling-water flow confirmed at the coil/generator (no leaks).
- [ ] Coil/sample alignment and chamber clearance verified.
- [ ] Pyrometer aligned and sighted on the sample/crucible.
- [ ] No conductive objects (jewelry, watches, phones, tools) within ≥6–12″ of the coil.

## Startup

1. **Load the sample.** With the chamber vented to atmosphere (never open the vent valve
   while the turbo pump is spinning), stack sample → optional alumina plate → ceramic
   cylinder → Teflon spacer inside the graphite crucible, insert into the quartz tube, and
   clamp the KF40 flange finger-tight with the O-ring.
2. **Pump down.** Close the vent valve, start the roughing/turbo pumps, and wait for high
   vacuum (~1×10⁻⁶ Torr or better).
3. **Cooling water.** Open the facility cooling-water valve (~45°, half open) and the
   generator chiller; check for leaks and confirm flow before applying RF power.

## Normal run

4. **Power on.** Bring up the generator per its sequence, then run the LabVIEW ramp/soak
   profile. Below the pyrometer's ~700 °C detection floor the VI ramps **open-loop** on the
   analog command; once the pyrometer returns a **sustained valid reading above the ~700 °C
   floor** (the handoff criterion), control switches to **closed-loop** PID on the optical
   temperature.
5. **Anneal.** Hold the temperature/time profile (e.g. ~1200 °C for several hours for Ni
   grain growth); the VI can email status alerts.

## Shutdown

6. **Ramp down.** Ramp power down and stop RF, then turn off cooling water, allow the
   sample to cool under vacuum, and vent only after the turbo pump has fully stopped.

## Abort / emergency stop

- **Loss of cooling water or chiller alarm:** immediately command power to zero / stop RF,
  then investigate; do not re-energize until flow is restored.
- **Vacuum loss or quartz-tube fracture:** stop RF immediately; do not vent against a
  spinning turbo pump.
- **Arcing, smoke, or runaway temperature:** zero the analog command, kill RF at the
  generator, and lock out before inspecting.

# Validation and characterization

The repository contains 100+ logged runs (`docs/data_log/`, IFrun001–100) across Ni200,
Ni4N5, YSZ, and Pd thermal-evaporation experiments, with temperatures of ~900–1400 °C and
soak durations from minutes to ~40 h, each with `.xlsx`/`.txt`/`.lvm` traces and some
photos. The minimum publishable validation package targets five figures, each with
quantitative metrics rather than qualitative claims.

**Figure 1 — System overview.** A labeled photograph/composite of generator, controller,
chiller, coil, quartz chamber, pyrometer line-of-sight, vacuum station, and control
computer.

**Figure 2 — Power-command → temperature calibration.** For a fixed sample/crucible
geometry, steady-state temperature at several analog command values spanning the useful
range, ideally n ≥ 3 runs per setpoint reported as mean ± SD. Plot analog command (mA /
scaled %) vs. pyrometer temperature (°C) with between-run error bars; fit a model only if
the data justify it, and show the operationally linear region explicitly. Hold coil
geometry, crucible, optical alignment, vacuum level, and sample type fixed; state the
pyrometer's valid range and calibration assumptions.

**Figure 3 — Representative ramp/soak with control error.** One representative anneal
(e.g. Ni at ~1200 °C) plotting setpoint and measured temperature vs. time, parsed from a
data log via `plotheatcurve.m` or a Python equivalent. Quantify **rise time, overshoot,
settling time, soak mean temperature, soak SD/RMS error, and maximum absolute deviation
during soak.**

**Figure 4 — Repeatability across runs.** The same programmed profile run ≥ 3 times on the
same setup; overlay the traces and report soak mean temperature, between-run SD,
coefficient of variation, and any long-soak drift. Use archived runs only if they are
truly same-profile/geometry/material/sensor, and state this explicitly.

**Figure 5 — Microstructural validation (SEM + EBSD).** The furnace exists to change
microstructure, so the key validation is **real microstructural data**: SEM micrographs of
as-received vs. annealed samples (e.g. Ni200 / Ni4N5) and EBSD inverse-pole-figure and
grain-boundary maps for at least one annealed condition. Quantify grain size properly:
number of grains analyzed, equivalent-circle-diameter or intercept metric, median + IQR
(or mean ± SD), segmentation/cleanup criteria, minimum-grain-area threshold, and whether
twins are merged or separated. Compare as-received vs. annealed descriptively (and
statistically only where replicate specimens justify it), and, where multiple runs exist,
plot grain size vs. soak temperature/time.

**Suggested controls** that build reviewer trust: open-loop vs. closed-loop on the same
target cycle; vacuum vs. inert-gas backfill mode; directly-coupled metal vs.
susceptor-mediated ceramic heating; and long-soak (multi-hour) stability.

**Specimen ↔ thermal-history linkage.** Each microstructure specimen will be tied to its
exact run via a table:

| Specimen | Material | Run ID | Soak T (°C) | Soak time | Atmosphere / vacuum | Cooling mode | Grain size (as-received → annealed) |
|----------|----------|--------|------------:|-----------|---------------------|--------------|-------------------------------------|
| `[TODO]` | `[TODO]` | `[TODO]` | `[TODO]` | `[TODO]` | `[TODO]` | `[TODO]` | `[TODO]` |

`[TODO: select canonical run IDs from docs/data_log/; add the SEM/EBSD image files (source
candidate micrographs from docs/student-work/RyanWeber.pdf) and the parsed thermal traces
under paper/figures/.]`

# Safety

The system combines high voltage/RF, high vacuum, high temperature, and water cooling; the
principal hazards and mitigations are summarized below.

| Hazard | Failure mode | Consequence | Mitigation |
|--------|--------------|-------------|------------|
| High voltage / RF field | Contact with coil or induced currents in nearby conductors | Electric shock, burns | Keep conductive objects/electronics ≥6–12″ from the coil while powered; isolate DAQ/control path |
| Lockout-tagout | Internal transformer-tap change (LEPEL prototype) | Shock during service | Follow LOTO before opening the generator |
| Vacuum / quartz | Venting against a spinning turbo pump; quartz fracture/implosion | Pump destruction; flying glass | Never vent while the turbo spins; handle quartz/gauge carefully; use eye protection |
| Water + electricity | Coil/chiller leak near energized hardware | Shock, equipment damage | Confirm flow and check for leaks before RF; route water away from electronics |
| Thermal | Sample melt-through; hot graphite oxidizing on vent | Pump-line contamination, burns | Cool under vacuum; let cool before venting; nitrile gloves when loading/unloading |
| Inert gas | Backfill/venting in an enclosed space | Asphyxiation | Adequate ventilation; do not backfill in confined areas |
| EMI | RF coupling into nearby instruments | Data corruption, instrument damage | Shield/separate sensitive electronics; keep them clear of the coil |

**PPE / shielding.** Operators should wear safety glasses (quartz-fracture/implosion risk),
clean nitrile gloves when handling vacuum components, and remove all conductive personal
items before approaching the energized coil; keep sensitive instrumentation outside the RF
near-field.

# Ethics statements

This work did not involve human participants, human data, or animal subjects. There are
no associated ethical considerations.

# Declarations

- **CRediT author roles:** `[TODO: confirm]` — provisional: Sterling G. Baird
  (conceptualization, software, investigation, writing); Kevin Cole (methodology,
  resources, supervision); additional authors to be confirmed.
- **Acknowledgements:** BYU Mechanical Engineering Department; the Johnson group;
  Kevin Cole. `[TODO: funding sources.]`
- **Declaration of competing interests:** `[TODO]` — provisional: the authors declare no
  competing interests.
- **Data availability:** design files, logs, and extracted context are in this repository
  (`vertical-cloud-lab/custom-induction-furnace`); a permanent DOI will be minted (Zenodo)
  before submission and listed in the specifications table.

# References

`[TODO: add the formatted reference list before submission. Anticipated citations:
(1) a general induction-heating / eddy-current reference (e.g. Davies, *Conduction and
Induction Heating*) for the physics of RF coupling and susceptor heating; (2) a grain-growth
/ recrystallization reference (e.g. Humphreys & Hatherly, *Recrystallization and Related
Annealing Phenomena*) motivating the annealing study; (3) a ratio/dual-wavelength pyrometry
reference for the non-contact temperature measurement; (4) the HardwareX author guidelines;
and (5) any prior open-source furnace-control hardware papers used for comparison. Confirm
exact citations and DOIs.]`
