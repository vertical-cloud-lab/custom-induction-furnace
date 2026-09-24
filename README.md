# custom-induction-furnace

[![arXiv](https://img.shields.io/badge/arXiv-2609.22118-b31b1b.svg)](https://arxiv.org/abs/2609.22118)

Custom Induction Furnace project — documentation and resources for building and operating an induction furnace. See the preprint at https://arxiv.org/abs/2609.22118 and the [Citation](#citation) section below.

![Animated overview of the custom induction furnace preprint](https://github.com/vertical-cloud-lab/custom-induction-furnace/blob/main/linkedin_preprint_option_4_story%20(2).gif)

(xref: [LinkedIn](https://lnkd.in/p/gpVekxN4))

<!--- source GIF in case I need to make changes: https://chatgpt.com/share/e/6ab596ff-3c4c-83e8-a1e9-2f8f8b9f92bf --->

## Citation

If you use this work, please cite the preprint:

> Baird, S. G., Weber, R., Nyborg, C., Guymon, R., Erickson, G., & Johnson, O. K. (2026). *Retrofitting a commercial RF induction generator into a computer-controlled, vacuum and gas integrated annealing system for reactive-metal grain growth*. arXiv preprint arXiv:2609.22118. https://doi.org/10.48550/arXiv.2609.22118

```bibtex
@misc{baird2026retrofitting,
  title         = {Retrofitting a commercial RF induction generator into a computer-controlled, vacuum and gas integrated annealing system for reactive-metal grain growth},
  author        = {Baird, Sterling G. and Weber, Ryan and Nyborg, Christopher and Guymon, Ronald and Erickson, Gage and Johnson, Oliver K.},
  year          = {2026},
  eprint        = {2609.22118},
  archivePrefix = {arXiv},
  primaryClass  = {physics.ins-det},
  doi           = {10.48550/arXiv.2609.22118},
  url           = {https://arxiv.org/abs/2609.22118}
}
```

## Documentation

All documentation has been downloaded from the Box shared folder — including
every subfolder — into the [`docs/`](docs/) directory (227 files), preserving
the original folder structure. Additional files have been merged from the main
branch with duplicates removed. See [`docs/README.md`](docs/README.md) for a
per-folder breakdown.

**Box Shared Link:** https://byu.box.com/s/lh04mmpkhvhy4vtokpm4sol711xycrph

### Folders

| Folder | Files |
|--------|------:|
| [`docs/data_log/`](docs/data_log/) | 102 |
| [`docs/manual/`](docs/manual/) | 20 |
| [`docs/temp-control-modification/`](docs/temp-control-modification/) | 24 |
| [`docs/quotes/`](docs/quotes/) | 14 |
| [`docs/LabVIEW/`](docs/LabVIEW/) | 12 |
| [`docs/lepel furnace pictures/`](docs/lepel%20furnace%20pictures/) | 10 |
| [`docs/CYSI/`](docs/CYSI/) | 9 |
| [`docs/east-coast-induction/`](docs/east-coast-induction/) | 6 |
| [`docs/MFC/`](docs/MFC/) | 6 |
| [`docs/equipment-reference/`](docs/equipment-reference/) | 7 |
| [`docs/ThermalEvaporation/`](docs/ThermalEvaporation/) | 4 |
| [`docs/Vent Valve/`](docs/Vent%20Valve/) | 2 |
| [`docs/KF Supplies/`](docs/KF%20Supplies/) | 1 |
| [`docs/student-work/`](docs/student-work/) | 1 |

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
