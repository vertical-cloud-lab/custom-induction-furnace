# HardwareX — Guide for Authors (working summary)

This is a working, version-controlled summary of the
[HardwareX](https://www.sciencedirect.com/journal/hardwarex) author requirements,
collected so the manuscript can be checked against them offline. **The authoritative
source is the journal's official Guide for Authors** — verify against it before
submission:

- Guide for Authors: <https://www.elsevier.com/journals/hardwarex/2468-0672/guide-for-authors>
- Elsevier LaTeX instructions: <https://www.elsevier.com/researcher/author/policies-and-guidelines/latex-instructions>
- Submission portal (Editorial Manager): <https://www.editorialmanager.com/hardwarex/>

## Article type and class

HardwareX is an Elsevier journal and uses the **`elsarticle` LaTeX document class**.
Submit the **full LaTeX source project** (the `.tex`, `.bib`, figures, and any class/style
files) — **do not** submit only a compiled PDF as the manuscript source. The compiled PDF
is built by the production system; a locally compiled PDF is fine for review/preview.

The template files are mirrored in this directory:

- [`elsarticle.cls`](elsarticle.cls) — Elsevier article class (LPPL).
- [`elsarticle-num.bst`](elsarticle-num.bst) — numbered-reference bibliography style.
- [`elsarticle-template-num.tex`](elsarticle-template-num.tex) — the official starter template.
- [`elsarticle-user-documentation.pdf`](elsarticle-user-documentation.pdf) — the `elsdoc` class manual.

## Required manuscript sections (in order)

A HardwareX "Hardware" article must contain, in this order:

1. **Title, authors, affiliations, corresponding author**
2. **Abstract**
3. **Keywords**
4. **Specifications table** (mandatory; see below) — placed right after the abstract
5. **Hardware in context** (motivation, prior art, who benefits)
6. **Hardware description** (what it is and what it does)
7. **Design files summary** — a table listing every design file with: *Design file name,
   File type, Open source license, Location of the file* (deposited in a permanent
   open-access repository)
8. **Bill of materials summary** — a single table with the columns: *Designator,
   Component, Number, Cost per unit, Total cost, Source of materials, Material type*.
   Costs in a single currency; the BOM should also be provided as a separate
   `.csv`/`.xlsx`.
9. **Build instructions** (step-by-step, with photos)
10. **Operation instructions**
11. **Validation and characterization** (quantitative evidence the hardware works)
12. **Ethics statements** (if applicable)
13. **Declarations** — CRediT author statement, Declaration of competing interest,
    Acknowledgements, funding
14. **References**

## Specifications table — required rows

The mandatory specifications table includes at least:

| Field | Notes |
|-------|-------|
| Hardware name | |
| Subject area | Choose from the journal's list (e.g. *Engineering and materials science*) |
| Hardware type | |
| Closest commercial analog | Or "No commercial analog is available." |
| Open source license | e.g. CERN-OHL, MIT, GPL, CC-BY |
| Cost of hardware | Excluding taxes; single currency |
| Source file repository | A **permanent DOI** (e.g. Zenodo / OSF / Mendeley Data) — a bare GitHub URL is *not* accepted as the archival location |

## Mandatory policies / deliverables

- **Open hardware license** required for the design files (e.g. CERN-OHL-S, CERN-OHL-W);
  software/code under an OSI license (e.g. MIT, GPL).
- **Permanent repository with a DOI** for all design files and the BOM — GitHub alone is
  not sufficient for the archival deposit; mint a DOI (Zenodo can archive a GitHub release).
- **Design files** must be openly editable formats where possible (e.g. native CAD plus a
  neutral export such as STEP/STL; source code, not only compiled binaries).
- **Figures**: high resolution; vector (PDF/EPS) for line art, ≥300 dpi raster (TIFF/PNG)
  for photos.
- **Validation**: quantitative characterization (not just "it works") demonstrating the
  hardware meets its stated specifications.

## LaTeX submission checklist

- [ ] Main `\documentclass[5p]{elsarticle}` (or `[preprint,review,12pt]` for review).
- [ ] `\begin{frontmatter}` with `\title`, `\author`, `\affiliation`, `\begin{abstract}`,
      `\begin{keyword}`.
- [ ] Numbered references via `\bibliographystyle{elsarticle-num}` + `.bib`.
- [ ] Submit the LaTeX **source project as a zip** (not the PDF as the source).
- [ ] BOM and design-file tables present in the text **and** the BOM also as a separate
      `.csv`/`.xlsx`.
- [ ] DOI'd repository link in the specifications table and Data availability.

*Source: HardwareX Guide for Authors and the Elsevier `elsarticle` documentation,
summarized {2026}. Re-verify against the official pages above before submitting.*
