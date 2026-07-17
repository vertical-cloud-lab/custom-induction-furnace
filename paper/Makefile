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
#   make pdf     # build the clean paper.pdf (no status box / \todo notes)
#   make draft   # build paper-draft.pdf with the status box + red \todo markers
#   make real    # build real_person_paper.pdf (restyled variant, same content)
#   make si      # build SI.pdf (the AIP-required separate supplementary-material PDF)
#   make clean   # remove the compiled PDFs and LaTeX aux files
#   make figures # regenerate the validation/characterization/crucible figures

PDFLATEX ?= pdflatex
SRC := paper.tex

.PHONY: all pdf draft real si clean figures
all: pdf draft real si

# Regenerate the validation + characterization figures from the archived data.
figures:
	python3 build_validation_figures.py
	python3 build_characterization_crossref.py
	python3 build_schematic_figures.py
	python3 build_crucible_figure.py
	python3 build_crucible_dimensions_figure.py
	python3 build_crucible_assembly_figure.py
	python3 build_photo_figures.py
	python3 build_ysz_figures.py
	python3 build_grooving_figure.py
	python3 extract_uploaded_figures.py

pdf: paper.pdf
paper.pdf: $(SRC) references.bib
	$(PDFLATEX) -interaction=nonstopmode $(SRC)
	-bibtex paper
	$(PDFLATEX) -interaction=nonstopmode $(SRC)
	$(PDFLATEX) -interaction=nonstopmode $(SRC)

# Draft build: predefines \DRAFTNOTES so the status box and \todo markers render.
draft: paper-draft.pdf
paper-draft.pdf: $(SRC) references.bib
	$(PDFLATEX) -interaction=nonstopmode -jobname=paper-draft "\def\DRAFTNOTES{1}\input{$(SRC)}"
	-bibtex paper-draft
	$(PDFLATEX) -interaction=nonstopmode -jobname=paper-draft "\def\DRAFTNOTES{1}\input{$(SRC)}"
	$(PDFLATEX) -interaction=nonstopmode -jobname=paper-draft "\def\DRAFTNOTES{1}\input{$(SRC)}"

# "Real person" restyled variant (R. Guymon, PR #3, 2026-07-14): same content
# as paper.tex, prose rewritten in the Extension-to-ceramics style (no \sim
# approximations, short declarative sentences). Does not replace paper.pdf.
real: real_person_paper.pdf
real_person_paper.pdf: real_person_paper.tex references.bib
	$(PDFLATEX) -interaction=nonstopmode real_person_paper.tex
	-bibtex real_person_paper
	$(PDFLATEX) -interaction=nonstopmode real_person_paper.tex
	$(PDFLATEX) -interaction=nonstopmode real_person_paper.tex

# Supplementary material: AIP requires SI as a single separate PDF named
# SI.pdf at initial submission (see template/rsi/aip-author-instructions).
# SI.tex compiles the content of paper/supplementary/*.md (which remain the
# editable sources of record) with S-numbered figures/tables and alt text.
si: SI.pdf
SI.pdf: SI.tex
	$(PDFLATEX) -interaction=nonstopmode SI.tex
	$(PDFLATEX) -interaction=nonstopmode SI.tex

clean:
	rm -f paper.pdf paper.aux paper.log paper.out paper.toc paper.bbl paper.blg paper.spl paperNotes.bib
	rm -f SI.pdf SI.aux SI.log SI.out SI.toc
	rm -f paper-draft.pdf paper-draft.aux paper-draft.log paper-draft.out paper-draft.bbl paper-draft.blg paper-draftNotes.bib
	rm -f real_person_paper.pdf real_person_paper.aux real_person_paper.log real_person_paper.out real_person_paper.bbl real_person_paper.blg real_person_paperNotes.bib
