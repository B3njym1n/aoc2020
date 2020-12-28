#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re, collections

Sum, Ranges = 0, collections.defaultdict(set)
Search, Indexes = 1, collections.defaultdict(set)
Fields, Yours, Tickets = map(lambda x : x.split('\n'),
                             open('input', 'r').read().split('\n\n'))

Valid = [[int(x) for x in Yours[1].split(',')]]

# Read Ranges
for Key, *Line in map(re.compile('(?:^)[\w ]+|\d+.\d+').findall, Fields):
    for Pair in Line:
        A, B = map(int, Pair.split('-'))
        Ranges[Key] |= { *range(A, B+1) }

# Wtf Tickets
for Tickets in Tickets[1: -1]:
    for Number in (T := [*map(int, Tickets.split(','))]):
        for Key in Ranges:
            if Number in Ranges[Key]:
                break
        else:
            Sum += Number
            break
    else:
        Valid.append(T)

# Gold Search
for Key in Ranges:
    for I in range(len(Ranges)):
        V = {T[I] for T in Valid }
        if not V - Ranges[Key]:
            Indexes[I].add(Key)

# Reduce Fields
while len(S := sorted(Indexes, key = lambda k : len(Indexes[k]))):
    Value = Indexes[S[0]].pop()
    if 'departure' in Value:
        Search *= Valid[0][S[0]]
    for I in S[1:]:
        Indexes[I].remove(Value)
    del Indexes[S[0]]

# Results
print("Silver: " , Sum)
print("Gold: " , Search)
