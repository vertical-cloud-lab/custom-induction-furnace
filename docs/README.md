# Documentation

Files downloaded from the Box shared folder (including all subfolders):
https://byu.box.com/s/lh04mmpkhvhy4vtokpm4sol711xycrph

Additional files merged from the main branch (removed duplicates).

A total of **227 files** are included, preserving the original folder structure
and removing internal duplicates. One file in the Box shared folder is intentionally
**not** included: `data_log/IFrun041-060/IFrun043_extra/IFrun043_Ni4N5_028_endOfTest.mp4`
(≈122 MB), because it exceeds GitHub's 100 MB per-file limit. Use
`python ../download_box_docs.py --max-bytes 0` to fetch it locally.

## Top-level folders

| Folder | Files |
|--------|------:|
| `data_log/` | 102 |
| `manual/` | 20 |
| `temp-control-modification/` | 24 |
| `quotes/` | 14 |
| `LabVIEW/` | 12 |
| `lepel furnace pictures/` | 10 |
| `CYSI/` | 9 |
| `east-coast-induction/` | 6 |
| `MFC/` | 6 |
| `equipment-reference/` | 7 |
| `ThermalEvaporation/` | 4 |
| `Vent Valve/` | 2 |
| `KF Supplies/` | 1 |
| `student-work/` | 1 |

## Root files (Induction Furnace specific)

| File | Description |
|------|-------------|
| `induction-furnace-schematic.pptx` | Induction furnace schematic diagram |
| `induction_parts_list.xlsx` | Parts list and components |
| `coils-drawing.pdf` | Coil design drawings |
| `induction_order_corrections.pptx` | Order corrections and updates |
| `Picture1.png` | Image reference |
| `schematic.pptx` | Schematic presentation |
| `induction_SOP_200901.docx` | Standard Operating Procedure (Sept 2020) |
| `coils.oxps` | Coil design document |
| `SOP.docx` | Alternative Standard Operating Procedure |

## Re-downloading

To re-download every file from Box (subfolders included):

```bash
python ../download_box_docs.py
```
