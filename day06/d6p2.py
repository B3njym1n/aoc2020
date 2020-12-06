#!/usr/bin/env python
# -*- coding: utf-8 -*-
from functools import reduce

def main():
    with open("input") as file:
        data = [blk.strip().split("\n") for blk in file.read().split("\n\n")]
        count = 0
        for group in data:
            print(group)
            r = reduce (lambda x, y: set(x) & set(y), group)
            print(len(r))
            count+= len(r)

        return count

if __name__ == "__main__":
    c = main()
    print(c)

