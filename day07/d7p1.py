#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
from collections import deque

target = 'shiny gold bag'

def main():
    q = deque()
    adj = {} 
    count = 0
    with open('input', 'r') as file:
        data = [line.strip() for line in file.readlines()]
        for line in data:
            bags = re.findall('\w+\s\w+\sbag', line)
            print(bags)
            container = bags[0]
            if bags[1:].count(target) > 0 :
                q.append(container)
            adj[container] = bags[1:]

    return count

if __name__ == "__main__":
    c = main()
    print(c)
