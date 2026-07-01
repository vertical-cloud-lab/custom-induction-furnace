# Repository agent guide

This file captures durable, **throughout-the-document** conventions for the HardwareX
manuscript in `paper/` (and related artifacts), distilled from PR review feedback.
When a reviewer flags something "that applies throughout" and points at one example,
the rule is recorded here so it is applied consistently and recognized in future
sessions. See also `.github/copilot-instructions.md` for tooling/environment notes.

## Manuscript authoring conventions (`paper/paper.tex`)

These apply to the **whole manuscript**, not just the line a reviewer happened to mark.

1. **Write to the reader, not to "us" as the authors.** Address the potential reader
   who will reproduce the build. Avoid first-person lab narration where it should be
   reader-facing instruction.
   - Bad: "the VI we wrote emails *us* status alerts."
   - Good: "the VI can email status alerts."

2. **Use actual figures wherever they exist.** Prefer real figures (rendered
   schematics, hardware photos, software screenshots) over prose placeholders. Source
   schematics live as editable PowerPoint in `docs/` (e.g.
   `docs/induction-furnace-schematic.pptx`) and are rendered by
   `paper/build_schematic_figures.py`; real screenshots/photos live under `docs/`
   (e.g. `docs/equipment-reference/frontPanel_200219.PNG`). Only when no real figure
   exists, use a proper `figure` environment placeholder **with a real, descriptive
   caption** (not a bare "planned" sentence). This applies throughout.

3. **Remove BYU-/facility-specific detail unhelpful to a general reader.** Strip
   hyperspecific local details that a reader cannot use.
   - Removed example: "Open the facility cooling-water valve (~45°, half open)" →
     "Check for leaks and confirm flow before applying RF power."
   - Legitimate exceptions: author affiliation, acknowledgements, and brief historical
     origin context.

4. **Anchor the reproducible design + BOM on the current USA induction heater.** The
   reproducible build is the CEIA "Power Cube" (model PW3-90/50) + Power Controller
   C-V3 Plus, procured through East Coast Induction (quote `210203AP`, in
   `docs/quotes/EastCoastInduction-CEIA.docx`). The ~1970 LEPEL furnace is the
   *originating prototype* and the rejected CYSI/GP-15A import is documented only as
   historical context — neither is a BOM line item.

5. **Specifications table = HardwareX's 7 mandatory rows only.** The mandatory
   specifications table has exactly: Hardware name, Subject area, Hardware type,
   Closest commercial analog, Open source license, Cost of hardware, Source file
   repository. Do **not** add machine-/build-dependent rows (e.g. "vacuum level",
   temperatures, coil geometry) there — those are build-specific and belong in the
   "Technical specifications" table in the Hardware description.

6. **Use the minted Zenodo DOI for the archival deposit; keep the GitHub link too.**
   Wherever a permanent DOI is required (specifications table, Data availability), use
   `https://doi.org/10.5281/zenodo.20878017`, and keep the development repository link
   `https://github.com/vertical-cloud-lab/custom-induction-furnace` in appropriate
   places. A bare GitHub URL is not accepted by HardwareX as the archival location.

7. **Mark used/eBay-sourced BOM items as "used" with an approximate/estimated cost,
   and prefer verifiable part numbers.** For items bought used (eBay, surplus), label
   them "used" and give an estimated cost (re-check a current listing, or fall back to
   the recorded quote price), e.g. the LumaSense ISR 6 pyrometer was $241 used vs.
   ~$5,500 new list (quote `00161403`). Prefer catalog part numbers where they exist
   (e.g. McMaster-Carr `1357T12` for the 2"×1/16" ultra-high-temperature quartz disc;
   McMaster stocks only imperial sizes, so the 55 mm metric disc is a custom-cut part
   with a vendor not recorded in the parts list).

## Build

- Build the manuscript with `make pdf` in `paper/` (pdflatex × multiple passes +
  bibtex; Elsevier `elsarticle` class). Always rebuild `paper/paper.pdf` after editing
  `paper/paper.tex`.
- Regenerate figures with `make figures` in `paper/` (validation + characterization +
  schematic/photo figures).
