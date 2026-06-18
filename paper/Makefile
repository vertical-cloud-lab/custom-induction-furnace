# Build the HardwareX manuscript draft.
#
# The manuscript is written in LaTeX (paper.tex) using Elsevier's `elsarticle`
# document class — the class HardwareX submissions use. The class/template files
# and the HardwareX author guidelines are mirrored in ./template/.
#
# Requirements: a LaTeX engine with pdflatex. MiKTeX is recommended (it auto-installs
# the needed packages — elsarticle, hyphenat, gensymb, tabularx, booktabs, etc.):
#   sudo apt-get install -y miktex && sudo miktexsetup --shared=yes finish
#   sudo initexmf --admin --set-config-value '[MPM]AutoInstall=1'
#
# Usage:
#   make pdf     # build paper.pdf from paper.tex (runs pdflatex twice for refs)
#   make clean   # remove the compiled PDF and LaTeX aux files

PDFLATEX ?= pdflatex
SRC := paper.tex

.PHONY: all pdf clean
all: pdf

pdf: paper.pdf
paper.pdf: $(SRC) template/elsarticle.cls references.bib
	$(PDFLATEX) -interaction=nonstopmode $(SRC)
	-bibtex paper
	$(PDFLATEX) -interaction=nonstopmode $(SRC)
	$(PDFLATEX) -interaction=nonstopmode $(SRC)

clean:
	rm -f paper.pdf paper.aux paper.log paper.out paper.toc paper.bbl paper.blg paper.spl
