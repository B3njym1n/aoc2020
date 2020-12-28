#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import defaultdict
import sys

def p2():
    with open('input') as file:
        adapters = [int(e.strip()) for e in file.readlines()]
        adapters.sort()
        adapters.insert(0, 0)
        adapters.append(max(adapters) + 3)
        print(adapters)
        dp = defaultdict(int)
        dp[0] = 1
        for n in adapters:
            dp[n] += dp[n-1] + dp[n-2] + dp[n-3]

        return dp[max(dp)]
        

if __name__ == "__main__":
    print(p2())
