# Build the HardwareX manuscript draft.
#
# Requirements: pandoc + a PDF engine. WeasyPrint is used by default (pure-Python,
# no LaTeX needed). Install with:
#   pip install weasyprint
#   sudo apt-get install -y pandoc
#
# Usage:
#   make pdf     # build paper.pdf
#   make html    # build paper.html
#   make clean

PANDOC ?= pandoc
SRC := paper.md

.PHONY: all pdf html clean
all: pdf

pdf: paper.pdf
paper.pdf: $(SRC)
	$(PANDOC) $(SRC) --pdf-engine=weasyprint --toc -o $@

html: paper.html
paper.html: $(SRC)
	$(PANDOC) $(SRC) --standalone --toc -o $@

clean:
	rm -f paper.pdf paper.html
