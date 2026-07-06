# Bill of materials (supplementary)

Itemized bill of materials for the reproducible CEIA-anchored build. Per the
RSI manuscript style (single data table, no BOM table — see `AGENTS.md`), this
inventory lives here as supplementary material rather than in the manuscript;
the paper's Construction section cites the package-level cost and points to
this file and to the archived repository.

Groupings by designator prefix: **GEN** = induction generator + controller
(the current USA reproducible build; the legacy LEPEL is the prototype
alternative, not a line item), **RETRO** = the reproducible retrofit
(control / vacuum / sensing) parts, **CONS** = consumables. Full vendor/price
detail for the RETRO and CONS parts is in
`paper/extracted-context/parts_list.md` (extracted from
`docs/induction_parts_list.xlsx`).

**Costing conventions:** all costs in **USD**; prices are the lab's purchase
records (quote year ~2019–2021), several from used/surplus/eBay sources as
noted; shipping and tax excluded unless stated. The bill of materials is
canonical for the CEIA system only; the legacy LEPEL prototype and the
rejected CYSI import path are documented in the manuscript text, not here.

| Desig. | Component | No. | Unit $ | Total | Source | Material |
| --- | --- | --- | --- | --- | --- | --- |
| GEN-1 | CEIA "Power Cube" PW3-90/50 solid-state RF generator (V3000-0070) | 1 | $8,240 | $8,240 | East Coast Induction (USA) | — |
| GEN-2 | Power Controller C-V3 Plus (V3000-0414) | 1 | $1,670 | $1,670 | East Coast Induction (USA) | — |
| GEN-3 | Recirculating water chiller (MIL043008 air-cooled closed-loop, V1650-0060) | 1 | $1,575 | $1,575 | East Coast Induction (USA) | — |
| GEN-4 | Heating head + 3 m cable and water lines (PWH-13-12-30/50, V3000-0300); 1 coil made to spec at no charge with a complete unit | 1 | $3,337 | $3,337 | East Coast Induction (USA) | copper |
| GEN-5 | Line auto-transformer, 12 kVA / 3PH / 480×380 V with taps (V049-0508; facility-dependent) | 1 | $1,665 | $1,665 | East Coast Induction (USA) | — |
| RETRO-1 | LabVIEW-compatible DAQ with analog out + in (0–5 V AO): NI USB-6000 DAQ | 1 | $281.00 | $281.00 | National Instruments | — |
| RETRO-2 | Dual-wavelength ratio pyrometer (LumaSense IMPAC ISR 6, 800–2500 °C), used | 1 | $385.00 (used) | $385.00 | eBay — used listing (new list ~$5,500, LumaSense quote 00161403) | — |
| RETRO-3 | 24 V linear power supply for pyrometer (International Power) | 1 | $51 | $51 | Mouser | — |
| RETRO-4 | Voltage-to-current (0–5 V → 4–20 mA) loop conditioner set for generator power-setpoint input (NI-9265 input module + NI-9203 output module + NI cDAQ-9174 chassis) | 1 set | $3,755.00 | $3,755.00 | National Instruments | — |
| RETRO-5 | Edwards nEXT T-Station 85H Dry turbo pumping station (1Ph 100–120 V, 50/60 Hz, DN 40 ISO-KF) | 1 | $13,573.65 | $13,573.65 | Edwards Vacuum | — |
| RETRO-5A | Wide-range vacuum gauge D14701000 (36 V, 2 W); discontinued, replaced by D3G0021100 | 1 | $1,543.29 | $1,543.29 | Chemtech Scientific | — |
| RETRO-6 | Edwards TAV5 vent valve (new) | 1 | $652.80 | $652.80 | Edwards Vacuum | — |
| RETRO-6A | Sierra SmartTrak 100L mass flow controller | 1 | $550–$1,000 (quote range) | $550–$1,000 | Sierra / distributor quote | — |
| RETRO-7 | Inert-gas regulator (Fisher FS-50) | 1 | $38 | $38 | Fisher Scientific | — |
| RETRO-8 | KF40 overpressure centering ring | 1 | $19 | $19 | IdealVac | aluminum |
| RETRO-9 | KF40 plastic quick vacuum clamp | 1 | $23 | $23 | IdealVac | polymer |
| RETRO-10 | Optical window, custom quartz disc 55 mm × 1.5 mm (1 used; buy 3 for spares) | 3 | $18 (est.) | $54 | Custom-cut metric disc — vendor not recorded in parts list; price approximate (McMaster stocks only imperial sizes) | fused quartz |
| RETRO-11 | Ultra-high-temperature quartz disc 2 in × 1/16 in (McMaster 1357T12) | 1 | $19 | $19 | McMaster-Carr | fused quartz |
| RETRO-12 | Inert-gas plumbing (BSPT/KF adapters, barbs, tee, 10 psi relief valve McMaster 4772K4) | 1 set | see parts list | ~$66 | McMaster-Carr / BMotionTech | brass / steel |
| CONS-1 | Quartz tube, 4 ft × 35 mm ID, cut to length | 2 | $67 | $134 | QSI Quartz | fused quartz |
| CONS-2 | Graphite stock for machined crucible/susceptor (56L-3, 3000 °C, 1×6×6 in) | 1 | $99 | $99 | Cotronics | graphite |
| CONS-3 | Graphite repair cement (Resbond 931-1, 3000 °C) | 1 | $108 | $108 | Cotronics | graphite |
| CONS-4 | Alumina crucible stock (RTC-60-2, 1787 °C, 10 lb) | 1 | $91 | $91 | Cotronics | alumina |
| CONS-5 | Zirconia crucible stock (760-1, 2204 °C, 10 lb) | 1 | $124 | $124 | Cotronics | zirconia |
| CONS-6 | Torr-Seal high-vacuum epoxy / O-rings | 1 set | $57 | $57 | Varian / McMaster | epoxy / elastomer |

For the high-temperature ceramic (YSZ) configuration, the graphite crucible
stack is exchanged for tantalum susceptor blocks and a compatible ceramic
crucible (MgO / BN / alumina, per the compatibility findings in the
manuscript's YSZ section and `docs/YSZ/`); vendor records for the tantalum
blocks and BN crucibles are **TODO** (not in the archived parts list).

**Co-author (R. Guymon) corrections incorporated in this revision:**
NI USB-6000 pricing, NI-9265/NI-9203/cDAQ-9174 loop-conditioner component
pricing, Edwards nEXT T-Station 85H pricing, wide-range gauge D14701000
pricing and replacement part number, TAV5 new-price update, pyrometer used
price update, and inclusion of the Sierra SmartTrak 100L MFC as a RETRO line
item. GEN line items remain from East Coast Induction quote 210203AP (3 Feb
2021; generator + heating head + controller + chiller + line transformer total
$16,487).
