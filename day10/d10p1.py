#!/usr/bin/env python
# -*- coding: utf-8 -*-

def p1():
    with open('input') as file:
        adapters = [int(e.strip()) for e in file.readlines()]
        adapters.sort()
        print(adapters)
        i, j = 0 ,1
        oneJoltDiff = 0
        threeJoltDiff = 0
        while j < len(adapters):
            difference = adapters[j] - adapters[i]
            if difference == 1:
                oneJoltDiff += 1
            elif difference == 3:
                threeJoltDiff += 1
            i += 1
            j += 1

        print((oneJoltDiff + 1) * (threeJoltDiff + 1))


if __name__ == "__main__":
    p1()
