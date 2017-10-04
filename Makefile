
.PHONY: all

all: README.md

README.md: *.md
	./make-index.py >$@

upload:
	~/systemperformanceanalysis/confluence-upload.py --markdown --space HOWTO --title 'How to use dwarfdump to read structure layouts' dwarfdump-struct.md --skiplines=2
