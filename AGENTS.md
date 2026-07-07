# Repository agent guide

This file captures durable, **throughout-the-document** conventions for the journal
manuscript in `paper/` (and related artifacts), distilled from PR review feedback.
The manuscript targets **Review of Scientific Instruments (RSI)** as of 2026-07-02
(REVTeX 4.2, `aip,rsi`); it was previously drafted for HardwareX, and that version
is archived in `paper/archive/`.
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

5. **Follow the AIP/RSI manuscript structure, not HardwareX's.** RSI has no
   mandatory specifications table or design-files/BOM sections; the bill of
   materials and design-file inventory live in **appendices**, and the required
   AIP order is: title → abstract (≤250 words, one paragraph) → text (ending in a
   Conclusions section) → Supplementary Material → Acknowledgments → Author
   Declarations (Conflict of Interest, Ethics, CRediT Author Contributions) →
   Data Availability → appendices → references. Build-dependent values (vacuum
   level, temperatures, coil geometry) belong in the "Technical specifications"
   table in the System design section. See `paper/template/rsi/RSI_GUIDE_FOR_AUTHORS.md`.

6. **Use the minted Zenodo DOI for the archival deposit; keep the GitHub link too.**
   Wherever a permanent DOI is required (Data availability, Supplementary material),
   use `https://doi.org/10.5281/zenodo.20878017`, and keep the development repository
   link `https://github.com/vertical-cloud-lab/custom-induction-furnace` in
   appropriate places. A bare GitHub URL is not an acceptable archival location.

7. **Mark used/eBay-sourced BOM items as "used" with an approximate/estimated cost,
   and prefer verifiable part numbers.** For items bought used (eBay, surplus), label
   them "used" and give an estimated cost (re-check a current listing, or fall back to
   the recorded quote price), e.g. the LumaSense ISR 6 pyrometer was $241 used vs.
   ~$5,500 new list (quote `00161403`). Prefer catalog part numbers where they exist
   (e.g. McMaster-Carr `1357T12` for the 2"×1/16" ultra-high-temperature quartz disc;
   McMaster stocks only imperial sizes, so the 55 mm metric disc is a custom-cut part
   with a vendor not recorded in the parts list).

8. **Match the prose-first style of published RSI articles.** RSI apparatus
   papers describe construction with labeled schematics/photographs plus prose
   explaining how the parts are connected --- not numbered step-by-step build
   recipes or checklists --- and they use tables sparingly, only to relay data
   (specifications, per-run results, inventories). Rhetorical or comparative
   content (prior art, hazards/mitigations, migration history) belongs in prose,
   not tables. (Requested by R. Guymon in PR #3, 2026-07-06, after comparing the
   draft against recent RSI publications, e.g.
   https://pubs.aip.org/aip/rsi/article/97/6/063303/3394533.)

9. **At most one data table in the main text; no BOM or specs tables.** The
   exemplar RSI publication R. Guymon provided (Rev. Sci. Instrum. 97, 063303
   (2026), doi:10.1063/5.0299443) has exactly one table, presented while
   discussing the data, and no bill-of-materials table. The manuscript
   currently has **zero** main-text tables: the specimen ↔ thermal-history
   linkage moved to `paper/supplementary/specimen-run-linkage.md` (Table S1)
   per S. Baird's PDF annotations (PR #3, 2026-07-07). Technical
   specifications are prose in the System design
   section; the itemized bill of materials and design-file inventory live in
   `paper/supplementary/bill-of-materials.md` and
   `paper/supplementary/design-file-inventory.md` (referenced from the
   Supplementary Material section), NOT as manuscript appendices. Outstanding
   BOM corrections are tracked in the supplementary BOM file. (Requested by
   R. Guymon in PR #3, 2026-07-06.)

10. **No rhetorical bolding in the manuscript body.** `\textbf{}` is not used
    for emphasis in prose (S. Baird: "There's way too much bolded text here").
    Bold remains only in the CRediT author-contribution names and the
    draft-only status box. Use plain prose (or sparing `\emph{}`).

11. **No bullet or numbered lists in the manuscript body.** S. Baird: "All of
    these numbered lists are distracting and look weird" / "Stop with all the
    bullet points." Subsystem descriptions, audience statements, portability
    criteria, etc. are written as flowing prose paragraphs.

12. **No run-ID (`IFrunNNN`) level detail in the main text or figures.**
    S. Baird: run/specimen-ID-level detail "could be supporting information as
    long as the raw data is made available or hyperlinked." Run IDs live only
    in `paper/supplementary/specimen-run-linkage.md` (Table S1), whose rows
    hyperlink to the raw logs; the manuscript references that cross-reference.
    Specimen IDs (`Ni4N5_###`) may appear where needed to key the
    characterization figures, but without their run IDs. Figure builders label
    plots by nominal condition / chronological run number, not run ID.

13. **The mass flow controller is optional equipment.** Everywhere the MFC is
    mentioned, describe it as optional (a regulator + needle valve suffices in
    a minimal build); the MFC photo panel was removed from the vacuum-details
    figure. (S. Baird, PR #3, 2026-07-07.)

14. **Do not reinsert the LabVIEW front-panel screenshot as a figure.** The
    archived screenshot (`fig_control_panel.png` /
    `docs/equipment-reference/frontPanel_200219.PNG`) shows the old LEPEL-era
    interface; the original LabVIEW files were lost and no current-interface
    screenshot exists. The front panel is described in prose only.
    (S. Baird, PR #3, 2026-07-07.)

15. **Clean vs. draft PDFs.** `make pdf` builds the clean `paper.pdf` (no
    status box, no red \todo markers — the shareable version); `make draft`
    builds `paper-draft.pdf` with the notes rendered (`\DRAFTNOTES` toggle in
    the preamble). Keep both in sync when editing. (S. Baird, PR #3,
    2026-07-07.)

16. **Kevin Cole is acknowledged, not an author.** (S. Baird, PR #3,
    2026-07-06/07-07.) The LEPEL prototype is historical context and is not
    mentioned in the abstract.

17. **Never fabricate a reference.** Only cite entries already present in
    `paper/references.bib`, which is compiled and validated from the Edison
    literature-query artifacts in `literature-search/`. (S. Baird, PR #3,
    2026-07-07.)

## Physical-configuration facts (from lab feedback)

- **The vacuum chamber has no support stand.** The chamber stack is joined by KF40
  flanges to the pyrometer housing, which is suspended from the ceiling by cables —
  the vertical stack hangs from above. The bolted support stand (8 short + 4 long
  sections, 12 corner braces, 4 floor mounts) carries the generator's **heating
  head/work coil**, not the chamber. Any text, caption, or schematic implying a
  stand-supported chamber or a "stand-mounted pyrometer holder" is wrong.
  (R. Guymon, PR #3, 2026-07-07.)
- **Three ceiling cables physically; draw two.** The pyrometer housing hangs from
  **three** cables to the ceiling. In the v2 overview schematic, however, only two
  are drawn — the third attachment sits behind the pyrometer in the flat side view
  and an angled third line read poorly, so it is deliberately omitted for clarity.
  Do not "fix" the schematic back to three. (R. Guymon, PR #3, 2026-07-07.)
- **Cooling water is a series loop**: chiller → heating head/work coil → generator →
  back to the chiller. (R. Guymon, PR #3, 2026-07-07.)
- **Overpressure relief valve** (0.5 psi cracking) hangs at the bottom of the chamber
  stack, at the KF40 cross where the bellows connects; every KF40 joint in the stack
  seals on an elastomer O-ring carried on its centering ring. (R. Guymon, PR #3,
  2026-07-07.)

## Build

- Build the manuscript with `make pdf` in `paper/` (pdflatex × multiple passes +
  bibtex; REVTeX 4.2 class with the `aip,rsi` options); `make draft` builds the
  notes-visible `paper-draft.pdf`. Always rebuild both `paper/paper.pdf` and
  `paper/paper-draft.pdf` after editing `paper/paper.tex`.
- REVTeX 4.2f predates the 2023+ LaTeX kernel/array table internals; `paper.tex`
  disables REVTeX's begin-document tabular patching (see the commented
  `\switch@tabular` override in the preamble) — do not remove it, and do not use
  REVTeX's `ruledtabular` environment (use booktabs, as the manuscript already does).
- Regenerate figures with `make figures` in `paper/` (validation + characterization +
  schematic/photo figures).
