# custom-induction-furnace

Custom Induction Furnace project — documentation and resources for building and operating an induction furnace.

## Documentation

All documentation has been downloaded from the Box shared folder — including
every subfolder — into the [`docs/`](docs/) directory (218 files), preserving
the original folder structure. See [`docs/README.md`](docs/README.md) for a
per-folder breakdown.

**Box Shared Link:** https://byu.box.com/s/lh04mmpkhvhy4vtokpm4sol711xycrph

### Folders

| Folder | Files |
|--------|------:|
| [`docs/quotes/`](docs/quotes/) | 14 |
| [`docs/east-coast-induction/`](docs/east-coast-induction/) | 6 |
| [`docs/data_log/`](docs/data_log/) | 103 |
| [`docs/temp-control-modification/`](docs/temp-control-modification/) | 24 |
| [`docs/CYSI/`](docs/CYSI/) | 9 |
| [`docs/lepel furnace pictures/`](docs/lepel%20furnace%20pictures/) | 10 |
| [`docs/manual/`](docs/manual/) | 20 |
| [`docs/ThermalEvaporation/`](docs/ThermalEvaporation/) | 4 |
| [`docs/LabVIEW/`](docs/LabVIEW/) | 11 |
| [`docs/KF Supplies/`](docs/KF%20Supplies/) | 1 |
| [`docs/Vent Valve/`](docs/Vent%20Valve/) | 2 |
| [`docs/MFC/`](docs/MFC/) | 6 |

One file in the shared folder is intentionally omitted because it exceeds
GitHub's 100 MB per-file limit (`IFrun043_Ni4N5_028_endOfTest.mp4`, ≈122 MB).

### Re-downloading

To re-download every file from Box (subfolders included):

```bash
pip install requests
python download_box_docs.py
```

Downloaded files are saved to the `docs/` directory. To also fetch files
larger than 100 MB, pass `--max-bytes 0`.