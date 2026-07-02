# Build the Review of Scientific Instruments manuscript draft.
#
# The manuscript is written in LaTeX (paper.tex) using REVTeX 4.2 with the AIP
# substyles (`aip,rsi` document-class options) — the class behind the official
# AIP Publishing template that RSI recommends. The template files and the
# RSI/AIP author guidelines are mirrored in ./template/rsi/.
# (The earlier HardwareX version, on Elsevier's elsarticle class, is archived
# in ./archive/ and builds against ./template/elsarticle.cls.)
#
# Requirements: a LaTeX engine with pdflatex. MiKTeX is recommended (it auto-installs
# the needed packages — revtex, gensymb, tabularx, booktabs, etc.):
#   sudo apt-get install -y miktex && sudo miktexsetup --shared=yes finish
#   sudo initexmf --admin --set-config-value '[MPM]AutoInstall=1'
#
# Usage:
#   make pdf     # build paper.pdf from paper.tex (pdflatex + bibtex + 2x pdflatex)
#   make clean   # remove the compiled PDF and LaTeX aux files
#   make figures # regenerate the validation/characterization/crucible figures

PDFLATEX ?= pdflatex
SRC := paper.tex

.PHONY: all pdf clean figures
all: pdf

# Regenerate the validation + characterization figures from the archived data.
figures:
	python3 build_validation_figures.py
	python3 build_characterization_crossref.py
	python3 build_schematic_figures.py
	python3 build_crucible_figure.py
	python3 build_crucible_dimensions_figure.py
	python3 build_crucible_assembly_figure.py

pdf: paper.pdf
paper.pdf: $(SRC) references.bib
	$(PDFLATEX) -interaction=nonstopmode $(SRC)
	-bibtex paper
	$(PDFLATEX) -interaction=nonstopmode $(SRC)
	$(PDFLATEX) -interaction=nonstopmode $(SRC)

clean:
	rm -f paper.pdf paper.aux paper.log paper.out paper.toc paper.bbl paper.blg paper.spl paperNotes.bib
