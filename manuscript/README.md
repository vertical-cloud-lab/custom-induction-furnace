# RSI Manuscript — LaTeX Template

LaTeX source for a manuscript to be submitted to *Review of Scientific
Instruments* (RSI), based on the official
[AIP Publishing template for Overleaf](https://www.overleaf.com/latex/templates/template-for-submission-to-aip-journals/wdmsvzfjgvyj)
(REVTeX 4.1 with the AIP substyles).

## Files

| File | Purpose |
| --- | --- |
| `main.tex` | The RSI manuscript — **edit this one** |
| `references.bib` | Bibliography for `main.tex` |
| `aiptemplate.tex` | Pristine bare template from AIP (keep as reference) |
| `aipsamp.tex` / `aipsamp.bib` | AIP's annotated sample article showing all features |
| `aipguide4-1.pdf` | AIP's guide to using the substyles |
| `revtex4-1.cls`, `aip4-1.rtx`, `ltx*.sty`, `revsymb4-1.sty` | REVTeX 4.1 class and AIP substyle (bundled so compilation does not depend on the TeX distribution's REVTeX version) |
| `*.bst` | BibTeX styles — `aipnum4-1.bst` (numeric, default) and `aipauth4-1.bst` (author–year) |
| `fig_1.png`, `fig_2.eps` | Sample figures used by `aipsamp.tex` |

## Compiling

Requires a TeX distribution (TeX Live works; tested with TeX Live 2023):

```bash
sudo apt-get install texlive-latex-base texlive-latex-recommended \
  texlive-fonts-recommended texlive-publishers texlive-font-utils \
  latexmk ghostscript
```

Then:

```bash
cd manuscript
latexmk -pdf main.tex
```

`latexmk` handles the pdflatex/bibtex rerun cycle automatically. The same
files compile as-is on [Overleaf](https://www.overleaf.com).

## RSI-specific notes

- The document class is `\documentclass[aip,rsi,...]{revtex4-1}` — the `rsi`
  option selects the RSI substyle.
- Use `reprint` for two-column, journal-formatted output; use `preprint`
  for the one-column, double-spaced submission format.
- Page limits (Conference Articles): **5 pages** contributed, **9 pages**
  invited.
- Per AIP author instructions, include the *Author Declarations* (conflict
  of interest) and *Data Availability Statement* sections — `main.tex`
  already contains both.
- Abstract should be fewer than 250 words.
