# Design-file inventory (supplementary)

Open design files in the repository (paths relative to the repository root).
Per the RSI manuscript style (single data table — see `AGENTS.md`), this
inventory lives here as supplementary material rather than as a manuscript
appendix table; the paper's Supplementary Material section points here and to
the archived Zenodo deposit (10.5281/zenodo.20878017).

| Design file | File type | License | Location |
| --- | --- | --- | --- |
| LabVIEW control VIs (furnace control, manual control, PID tuning v1/v2, email alert) | LabVIEW `.vi` | MIT (proposed) | `code/induction-furnace-control-code/` |
| Manual ramping v5 VIs | LabVIEW `.vi` | MIT (proposed) | `code/manual-ramping-v5/` |
| `plotheatcurve.m` (heat-curve plotter) | MATLAB | MIT (proposed) | `code/plotheatcurve.m` |
| Work-coil drawing | PDF / OXPS | CERN-OHL-S (proposed) | `docs/coils-drawing.pdf`, `docs/coils.oxps` |
| System schematics | PPTX (+ extracted text/figures) | CERN-OHL-S (proposed) | `docs/*.pptx`, `paper/extracted-context/` |
| Temperature-control wiring | PNG | CERN-OHL-S (proposed) | `docs/temp-control-modification/0-5V PLC wire design.png` |
| KF40 overpressure centering ring | STEP | CERN-OHL-S (proposed) | `docs/KF Supplies/KF40_overpressureCenteringRing.step` |
| YSZ / tantalum-susceptor stack: schematic, heat-curve workbook, configuration survey, compatibility notes | PNG / XLSX / PDF / DOCX | CERN-OHL-S (proposed) | `docs/YSZ/` |
| Graphite crucible/susceptor machining drawing | **TODO: add** | CERN-OHL-S (proposed) | TODO (measured dimensions are in the manuscript's crucible figure) |

**TODO:** export the LabVIEW `.vi` block diagrams to PDF/PNG so non-LabVIEW
readers can inspect the control logic.
