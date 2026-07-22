# YSZ (yttria-stabilized zirconia) high-temperature configuration

Materials for the ceramic (YSZ) grain-growth extension of the furnace: the
tantalum-susceptor charge stack that replaces the graphite crucible for
soak temperatures beyond ~1700 °C (demonstrated 2000–2344 °C).

| File | Content |
| --- | --- |
| `ysz-stack-schematic.png` | Hand schematic of the YSZ heating stack contributed by R. Guymon (PR #3, July 2026): inside a new ~35 mm-ID quartz tube, the YSZ specimen is sandwiched between two tantalum susceptor blocks (25.5 mm), seated in a 28 mm MgO crucible on a new alumina support rod, positioned in the work coil. |
| `Tantalum-Heat-Curve.xlsx` | Lab workbook (R. Guymon, PR #3, July 2026): pyrometer temperature vs. generator power command for one and two stacked Ta susceptor blocks (original and replacement power controller), plus two timed two-block ramp/soak logs — a >1 h hold at ~2000 °C at a constant 17 % command, and a ramp to **2344 °C at 33 %** ended by the chamber pressure interlock ("Test Failed: Pressure Limit Reached"). Rendered into the manuscript's Ta heat-curve figure by `paper/build_ysz_figures.py`. |
| `Induction-Furnace-Key-Takeaways.pdf` | Configuration survey (R. Guymon): four crucible-stack variants for YSZ at 2000–2500 °C (Ta/BN/alumina 2500 °C 8 h — grain growth successful but Ta deposited on YSZ; graphite stack 2000 °C 168 h — YSZ consumed by carbon; double-Ta 2130 °C 80.4 h — reaction shell around Ta; untried graphite-in-BN concept), the known-chemical-reactions list, and micrographs. Key results: ~90 µm clean YSZ grains in 45 min (runs >3 h contaminated); above ~2200 °C use a carbon susceptor not touching the YSZ. |
| `Observed-Adverse-Chemical-Reactions.docx` | Standalone list of the observed adverse chemical reactions between YSZ, tantalum, graphite/carbon, alumina, MgO, BN, quartz, and oxygen at 1800–2500 °C. |
| `key-takeaways-images/` | Micrographs/photos extracted from the Key Takeaways PDF: `ysz-grain-measurements.png` (optical micrograph with in-image feature measurements, 100 µm scale bar), `ysz-pellet-in-susceptor.png`, `specimen-macro-cracked.png`, `reaction-product-iridescent.png`, `crucible-and-specimen-after-reaction.png`. |

Remaining gaps (tracked as a `\todo` in `paper/paper.tex`): which logged
`IFrun` IDs the heat curves and the 2500/2130/2000 °C configuration tests
correspond to, and which generator (LEPEL vs. CEIA) the tantalum heat curves
were recorded on.

The larger YSZ dataset lives in a BYU Box folder
(`https://byu.app.box.com/folder/298111707639?s=roeft0d7ejgj322vuaoviqx82c1cur2f`)
whose shared link currently **requires BYU login** (it redirects to
`byu.account.box.com/login`), so it could not be mirrored here the way
`docs/SEM/` and `docs/optical/` were. Once the link is switched to open
("People with the link") access, it can be pulled with:

```bash
python download_box_docs.py --shared-link <link> --output-dir docs/YSZ --max-bytes 0
```

Committed YSZ optical micrographs from the existing optical archive:

- `docs/optical/CB121/1908##_SS_etc/190823_YSZ/YSZ_1700C_10h.JPG` (after 1700 °C / 10 h)
- `docs/optical/CB121/1909##_Ni_YSZ_Pd/190909_YSZ/YSZ_induction1_multiplyScaleBy2_.JPG` (induction-annealed)
