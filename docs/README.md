# Documentation

Files downloaded from the Box shared folder (including all subfolders):
https://byu.box.com/s/lh04mmpkhvhy4vtokpm4sol711xycrph

A total of **218 files** were downloaded, preserving the original folder
structure. One file in the shared folder is intentionally **not** included:
`data_log/IFrun041-060/IFrun043_extra/IFrun043_Ni4N5_028_endOfTest.mp4`
(≈122 MB), because it exceeds GitHub's 100 MB per-file limit. Use
`python ../download_box_docs.py --max-bytes 0` to fetch it locally.

## Top-level folders

| Folder | Files | Size |
|--------|------:|-----:|
| `CYSI/` | 9 | 7.0 MB |
| `KF Supplies/` | 1 | 74.2 KB |
| `LabVIEW/` | 11 | 3.8 MB |
| `MFC/` | 6 | 7.0 MB |
| `ThermalEvaporation/` | 4 | 2.0 MB |
| `Vent Valve/` | 2 | 1.6 MB |
| `data_log/` | 103 | 81.6 MB |
| `east-coast-induction/` | 6 | 21.0 MB |
| `lepel furnace pictures/` | 10 | 22.4 MB |
| `manual/` | 20 | 84.3 MB |
| `quotes/` | 14 | 2.7 MB |
| `temp-control-modification/` | 24 | 3.5 MB |

## Root files

| File | Description | Size |
|------|-------------|-----:|
| `induction-furnace-schematic.pptx` | Induction furnace schematic diagram | 70.3 KB |
| `induction_parts_list.xlsx` | Parts list and components | 18.9 KB |
| `coils-drawing.pdf` | Coil design drawings | 3.9 MB |
| `induction_order_corrections.pptx` | Order corrections and updates | 9.5 MB |
| `Picture1.png` | Image reference | 433.8 KB |
| `schematic.pptx` | Schematic presentation | 48.8 KB |
| `induction_SOP_200901.docx` | Standard Operating Procedure (Sept 2020) | 490.0 KB |
| `coils.oxps` | Coil design document | 144.4 KB |

## Re-downloading

To re-download every file from Box (subfolders included):

```bash
python ../download_box_docs.py
```
