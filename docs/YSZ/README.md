# YSZ (yttria-stabilized zirconia) high-temperature configuration

Materials for the ceramic (YSZ) grain-growth extension of the furnace.

| File | Content |
| --- | --- |
| `ysz-stack-schematic.png` | Hand schematic of the YSZ heating stack contributed by R. Guymon (PR #3, July 2026): inside a new ~35 mm-ID quartz tube, the YSZ specimen is sandwiched between two tantalum susceptor blocks (25.5 mm), seated in a 28 mm MgO crucible on a new alumina support rod, positioned in the work coil. |

The quantitative YSZ grain-growth dataset lives in a BYU Box folder
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
