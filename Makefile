
.PHONY: all

all: README.md

README.md: *.md
	./make-index.py >$@
