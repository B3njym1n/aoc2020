#!/usr/bin/env python
# -*- coding: utf-8 -*-
from functools import reduce

def main():
    with open("input") as file:
        data = [blk.split("\n") for blk in file.read().split("\n\n")]
        print(data)
        count = 0
        for group in data:
            r = reduce(lambda x, y: set(x) | set(y), group)
            count += len(r)

        return count

if __name__ == "__main__":
    c = main()
    print(c)

