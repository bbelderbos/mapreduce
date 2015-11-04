#!/usr/bin/env python
import sys

counts = {}

for line in sys.stdin:
    line = line.strip()
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0)+1

for k,v in counts.items():
    print "%s\t%s" % (k,v)
