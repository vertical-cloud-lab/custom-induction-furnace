# Manuscript moved to LaTeX (now targeting RSI)

The manuscript is maintained in **LaTeX**, and as of 2026-07-02 targets
**Review of Scientific Instruments** (AIP Publishing) rather than HardwareX —
RSI is the better venue fit (see the PR #3 discussion).

- **Canonical manuscript:** [`paper.tex`](paper.tex) — REVTeX 4.2 with the
  official AIP `rsi` journal substyle (`\documentclass[aip,rsi,reprint]{revtex4-2}`).
- **Compiled PDF:** [`paper.pdf`](paper.pdf) — build with `make pdf` (pdflatex / MiKTeX).
- **Template + author guidelines:** [`template/rsi/`](template/rsi/) — mirrored
  REVTeX/AIP template files and the official RSI/AIP author instructions.
- **Archived HardwareX version:** [`archive/`](archive/) (Elsevier `elsarticle`
  class, with its template files retained in [`template/`](template/)).

The previous Markdown draft of this manuscript is preserved in the repository's git
history; all of its content was ported into `paper.tex`.
