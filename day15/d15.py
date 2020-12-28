#!/usr/bin/env python
# -*- coding: utf-8 -*-

input = [7, 14, 0, 17, 11, 1, 2]

def pi():
    his = dict([(x, n+1) for n, x in enumerate(input)])
    last = input[-1]
    for n in range(len(input), 30000001):
        x = n - his.get(last, n)
        his[last] = n
        if n in [2020, 3000000]:
            print(last)
        last = x

if __name__ == "__main__":
    pi()
