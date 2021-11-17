#!/usr/bin/env python3

import re
import glob


multi_files = {'lldb-cheat-sheet.md', 'cmake-cheat-sheet.md'}


with open("README.md", "w") as out:
    out.write("\n")
    out.write("### general")
    out.write("\n")

    exclude = {'README.md'} | multi_files

    for filename in sorted(glob.glob("*.md")):
        if filename in exclude:
            continue
        with open(filename, 'r') as f:
            title = next(iter(f)).strip()
        out.write(f"* [{title}]({filename})\n")
    out.write("\n")

    for filename in multi_files:
        with open(filename, 'r') as f:
            title = next(iter(f)).strip()
            out.write(f"### {title}\n")

            anchor = None
            for line in f:
                if m := re.match(r'<a name="(.*)"', line):
                    anchor = m.group(1)
                    continue
                if m := re.match("### (.*)", line):
                    assert anchor is not None
                    title = m.group(1)
                    out.write(f"* [{title}]({filename}#{anchor})\n")
                anchor = None
        out.write("\n")
