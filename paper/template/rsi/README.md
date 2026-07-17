# RSI / AIP Publishing template and author guidelines

Mirrored template files for the **Review of Scientific Instruments** manuscript
(`../../paper.tex`), plus the official author instructions. See
[`RSI_GUIDE_FOR_AUTHORS.md`](RSI_GUIDE_FOR_AUTHORS.md) for the summary and the
list of official source URLs.

| File | What it is |
|---|---|
| `aiptemplate.tex` | Blank AIP Publishing article template (REVTeX 4.2, official) |
| `aipsamp.tex` / `aipsamp.bib` / `aipsamp.pdf` | Worked AIP sample article (official) |
| `aipguide4-2.pdf` | *Author's Guide to the AIP Substyles for REVTeX 4.2* (official) |
| `revtex4-2-authors-guide.pdf` | *REVTeX 4.2 Author's Guide* (official) |
| `revtex4-2.cls`, `ltx*.sty`, `revsymb4-2.sty` | REVTeX 4.2f class + support files (v4.2f, 2022-06-05) |
| `aip4-2.rtx` | AIP journal substyles — provides the `rsi` document-class option |
| `aipnum4-2.bst` | AIP numeric BibTeX style (selected automatically by the class) |
| `aip-author-instructions-2026-07-02.txt` | Full text of the official AIP Publishing author instructions (incl. the RSI-specific section), retrieved 2026-07-02 |
| `rsi-publication-charges-2026-07-02.txt` | RSI publication-charges page (no page/color charges; optional $3,800 open access) |

Source: REVTeX 4.2f distribution from CTAN (<https://ctan.org/pkg/revtex>) —
the same class behind the AIP Publishing Overleaf template that RSI recommends;
instructions from <https://publishing.aip.org/resources/researchers/author-instructions/>.

The build does **not** compile against these mirrored copies — MiKTeX/TeX Live
provide the installed `revtex` package; the mirror is for provenance and for
readers without the package.
