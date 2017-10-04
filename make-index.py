#!/usr/bin/python

import glob

for filename in glob.glob("*.md"):
    if filename == 'README.md':
        continue
    with open(filename, 'r') as f:
        line = next(iter(f)).strip()
    print "* [%s](%s)" % (line, filename)
