# -*- coding: utf-8 -*
import sys
with open("inverted_index.txt") as f:
    lines = f.readlines()

print(lines)

for line in lines:
    if line.startswith(sys.argv[1]):
    # if line.find(sys.argv[1]) >= 0:
        print(line[:-1])
