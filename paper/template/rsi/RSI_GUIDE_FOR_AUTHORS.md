# Review of Scientific Instruments (RSI) — guide for authors (summary)

Summary of the official AIP Publishing / RSI author instructions as retrieved on
**2026-07-02**, for the manuscript in [`../../paper.tex`](../../paper.tex).
The full text of the official instructions page is mirrored verbatim in
[`aip-author-instructions-2026-07-02.txt`](aip-author-instructions-2026-07-02.txt).

> **Access note:** `pubs.aip.org` (the journal-site mirror of these pages) blocks
> automated access (HTTP 403 / Cloudflare). The canonical instructions live on
> `publishing.aip.org`, which is what is mirrored here; the RSI publication-charges
> page was mirrored via the Internet Archive
> ([`rsi-publication-charges-2026-07-02.txt`](rsi-publication-charges-2026-07-02.txt)).

## Official sources

| Resource | URL |
|---|---|
| AIP Publishing author instructions (incl. RSI-specific section) | <https://publishing.aip.org/resources/researchers/author-instructions/> |
| RSI journal home | <https://pubs.aip.org/aip/rsi> |
| RSI — Preparing Your Manuscript | <https://pubs.aip.org/aip/rsi/pages/manuscript> |
| RSI — Publication charges | <https://pubs.aip.org/aip/rsi/pages/charges> |
| RSI — Editorial policies | <https://pubs.aip.org/aip/rsi/pages/policies> |
| AIP Publishing LaTeX template (Overleaf) | <https://www.overleaf.com/latex/templates/template-for-submission-to-aip-journals/wdmsvzfjgvyj> |
| REVTeX 4.2 (CTAN) — the class the AIP template is built on | <https://ctan.org/pkg/revtex> |

## LaTeX template

- RSI recommends the **AIP Publishing template** (Overleaf link above), which is
  built on **REVTeX 4.2 with the AIP substyles**. The equivalent local files from
  the official REVTeX 4.2 CTAN distribution are mirrored in this directory:
  - [`aiptemplate.tex`](aiptemplate.tex) — the blank AIP template.
  - [`aipsamp.tex`](aipsamp.tex) / [`aipsamp.bib`](aipsamp.bib) /
    [`aipsamp.pdf`](aipsamp.pdf) — the worked AIP sample article.
  - [`aipguide4-2.pdf`](aipguide4-2.pdf) — *Author's Guide to the AIP Substyles
    for REVTeX 4.2* (official).
  - [`revtex4-2-authors-guide.pdf`](revtex4-2-authors-guide.pdf) — *REVTeX 4.2
    Author's Guide* (official).
- **RSI is an official journal substyle**: `\documentclass[aip,rsi,reprint]{revtex4-2}`
  (see Table 1 of `aipguide4-2.pdf`, "Rev. Sci. Instrum. → `rsi`").
- Numeric citations via the class's built-in natbib; with BibTeX the class selects
  the AIP numeric style (`aipnum4-2.bst`). `reprint` approximates the typeset
  two-column journal appearance; `preprint` gives one-column double-spaced.
- Initial submission format: a **single compiled manuscript PDF** (supplementary
  material as a separate PDF).

## Required manuscript order (AIP general guidelines)

1. Title, author(s), affiliation(s)
2. Abstract — **one paragraph, ≤ 250 words**, no equations/footnotes/references/figures
3. Text (with a **conclusion** section)
4. Supplementary material section (if any)
5. Acknowledgments
6. **Author declarations** — Conflict of Interest (required even if none), Ethics
   approval (if applicable), **Author Contributions (CRediT, NISO standard)**
7. **Data availability statement** (required; use one of AIP's templates)
8. Appendixes (if any)
9. References

Other general requirements: American English; motivation/results/conclusion stated
in nontechnical language for a broad audience; **alt text for all figures, tables,
and multimedia**; consecutive page numbers; accessible format.

## RSI-specific points

- **No length limit for regular contributed articles.** The only RSI-specific
  length limits are for *Conference Articles* (5 pages contributed / 9 pages
  invited; word-count equivalents: single-column figure ≈ 260 words, double-column
  ≈ 550 words).
- **Publication charges:** AIP Publishing does **not** require page or color
  charges for RSI. Optional open access ("Author Select") costs **$3,800 USD**;
  otherwise the article is subscription-access. Color figures are free online;
  they should also reproduce legibly in black & white print.
- **Preprints are allowed** — posting to a preprint server (e.g. arXiv) before
  submission is compatible with AIP policy (green OA / preprint route noted in
  the project plan).
- Scope: novel instrumentation and methods — an instrument/apparatus paper should
  describe the design, construction, and **quantified performance** of the
  instrument. (The furnace paper's validation section maps directly onto this.)

## Mapping from the HardwareX draft (what changed and why)

| HardwareX element | RSI treatment |
|---|---|
| Mandatory 7-row specifications table | **Removed** (no RSI equivalent); license/cost/repository moved into the Introduction and Data Availability |
| "Hardware in context" | Introduction |
| "Hardware description" | System design and description |
| "Design files summary" (mandated table) | Appendix (design-file inventory) + Data Availability |
| "Bill of materials summary" (mandated 7-column table) | Appendix (bill of materials) |
| "Build instructions" / "Operation instructions" | Construction and operation section (condensed) |
| "Validation and characterization" | Performance validation + microstructural validation sections |
| "Ethics statements" / "Declarations" | AIP "Author declarations" + "Data availability" sections |
| `elsarticle` class, `elsarticle-num` BibTeX style | `revtex4-2` class (`aip,rsi,reprint`), AIP numeric BibTeX style |
