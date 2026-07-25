# Build the Review of Scientific Instruments manuscript.
#
# The manuscript (real_person_paper.tex) uses REVTeX 4.2 with the AIP
# substyles (`aip,rsi` document-class options) — the class behind the official
# AIP Publishing template that RSI recommends. The template files and the
# RSI/AIP author guidelines are mirrored in ./template/rsi/.
#
# This branch carries only the submitted manuscript and SI. The wider
# drafting workspace (paper.tex, the HardwareX archive, and the remaining
# build_*.py figure scripts with their source data) lives on PR #3's branch
# (copilot/vertical-cloud-labattempt-download-docs); see README.md.
#
# Requirements: a LaTeX engine with pdflatex and the revtex4-2 class
# (TeX Live: texlive-publishers; MiKTeX auto-installs).
#
# Usage:
#   make real    # build real_person_paper.pdf
#   make si      # build SI.pdf (the AIP-required separate supplementary-material PDF)
#   make figures # regenerate the figures whose inputs are committed on this branch
#   make clean   # remove the compiled PDFs and LaTeX aux files

PDFLATEX ?= pdflatex

.PHONY: all real si clean figures
all: real si

# Regenerate the figures whose inputs are committed on this branch.
# Not included: build_grooving_figure.py (needs docs/student-work/ from PR #3's
# branch) and the two schematic scripts make_ysz_stack_schematic.py /
# add_chamber_stand_schematic.py (need LibreOffice; run them directly).
figures:
	python3 build_power_figures_volts.py
	python3 build_crucible_combined_figure.py
	python3 build_ebsd_figure.py
	python3 build_microstructure_figure.py

real: real_person_paper.pdf
real_person_paper.pdf: real_person_paper.tex references.bib
	$(PDFLATEX) -interaction=nonstopmode real_person_paper.tex
	-bibtex real_person_paper
	$(PDFLATEX) -interaction=nonstopmode real_person_paper.tex
	$(PDFLATEX) -interaction=nonstopmode real_person_paper.tex

# Supplementary material: AIP requires SI as a single separate PDF named
# SI.pdf at initial submission (see template/rsi/aip-author-instructions).
si: SI.pdf
SI.pdf: SI.tex
	$(PDFLATEX) -interaction=nonstopmode SI.tex
	$(PDFLATEX) -interaction=nonstopmode SI.tex

clean:
	rm -f SI.pdf SI.aux SI.log SI.out SI.toc
	rm -f real_person_paper.pdf real_person_paper.aux real_person_paper.log real_person_paper.out real_person_paper.bbl real_person_paper.blg real_person_paperNotes.bib
