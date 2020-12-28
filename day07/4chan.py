#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

with open('input', 'r') as fh:
    contents = fh.read()

data = re.sub('( bags?|\.)', '', contents).splitlines()

G1 = {}
G2 = {}
for line in data:
    lhs, rhs = line.split(' contain ')
    if 'no other' in rhs:
        continue

    parts = rhs.split(', ')
    for label in parts:
        count, bag = label.split(' ', 1)
        count = int(count)
        s = G1.setdefault(bag, set())
        s.add(lhs)
        l = G2.setdefault(lhs, [])
        l.append((count, bag))

# part 1
seen = set()
accum = list(G1.get('shiny gold', ()))
n = 0
while accum:
    key = accum.pop()
    if key in seen:
        continue
    seen.add(key)
    n += 1
    for color in G1.get(key, ()):
        accum.append(color)

print(n)

# part 2
seen = set()
accum = [('shiny gold', 1)]
n = 0
while accum:
    key, multiple = accum.pop()
    for ct, bag in G2.get(key, ()):
        n += (ct * multiple)
        accum.append((bag, ct * multiple))

print(n)
