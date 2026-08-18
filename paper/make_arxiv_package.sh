#!/usr/bin/env bash
# Build the arXiv submission package for the induction-furnace manuscript.
#
# arXiv compiles the LaTeX source itself. When a pre-built .bbl is included,
# arXiv uses it instead of running a bib compiler (per info.arxiv.org/help/
# submit_tex.html, which also requires the .bbl name to match the main .tex),
# so the package carries the pre-built real_person_paper.bbl alongside the .tex.
# The supplementary material goes in anc/ (arXiv's ancillary-file directory,
# listed on the abstract page but not compiled).
#
# Usage (from paper/):  bash make_arxiv_package.sh
# Output:               paper/arxiv_submission.tar.gz
#
# Requirements: pdflatex + bibtex with revtex4-2 (TeX Live: texlive-publishers).

set -euo pipefail
cd "$(dirname "$0")"

# 1. Fresh full build so the .bbl matches the current .tex and .bib.
make real
make si

# 2. Stage exactly what arXiv needs.
STAGE=arxiv_stage
rm -rf "$STAGE" arxiv_submission.tar.gz
mkdir -p "$STAGE/figures" "$STAGE/anc"

cp real_person_paper.tex real_person_paper.bbl "$STAGE/"

# Only the figures the manuscript actually includes.
for f in $(grep -o 'includegraphics\[[^]]*\]{[^}]*}' real_person_paper.tex \
           | sed 's/.*{\(.*\)}/\1/'); do
  cp "figures/$f" "$STAGE/figures/"
done

# Supplementary material as an ancillary file (not compiled by arXiv).
cp SI.pdf "$STAGE/anc/"

# 3. Verify the staged package compiles standalone the way arXiv will
#    (pdflatex only, no bibtex — the .bbl must satisfy all citations).
(
  cd "$STAGE"
  pdflatex -interaction=nonstopmode real_person_paper.tex > /dev/null
  pdflatex -interaction=nonstopmode real_person_paper.tex > /dev/null
  if grep -q "Citation .* undefined\|LaTeX Error" real_person_paper.log; then
    echo "ERROR: staged package did not compile cleanly; see $STAGE/real_person_paper.log" >&2
    exit 1
  fi
  rm -f real_person_paper.aux real_person_paper.log real_person_paper.out \
        real_person_paper.pdf real_person_paperNotes.bib
)

# 4. Tar it up (contents at the archive root, as arXiv expects).
tar -czf arxiv_submission.tar.gz -C "$STAGE" .
rm -rf "$STAGE"

echo "Wrote $(pwd)/arxiv_submission.tar.gz:"
tar -tzf arxiv_submission.tar.gz
