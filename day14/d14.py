#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
from functools import reduce
import itertools

def p1():
    with open('input', 'r') as file:
        inputs = [l.strip() for l in file.readlines()]

    mem = {} 
    mask = ''
    for i in inputs:
        if 'mask' in i:
            print(i[7:])
            mask = i[7:]
        else:
            address, value = re.findall('\d+', i)
            b = bin(int(value))[2:]
            b = b.zfill(36)
            print(b)
            l = list(b)
            for i, c in enumerate(mask):
                if c == 'X':
                    l[i] = b[i]
                    continue
                elif c == '1':
                    l[i] = '1'
                elif c == '0':
                    l[i] = '0'

            newb = reduce(lambda a, b: a + b, l)
            print(newb)
            newb = int(newb, 2)
            mem[address] = newb

    sum = 0
    for p in mem:
        sum += mem[p] 

    print('sum is %d' %  sum)

def p2():
    with open('input', 'r') as file:
        inputs = [l.strip() for l in file.readlines()]

    mem = {} 
    mask = ''
    for i in inputs:
        if 'mask' in i:
            mask = i[7:]
        else:
            address, value = re.findall('\d+', i)
            a = bin(int(address))[2:]
            a = a.zfill(36)
            l = list(a)
            for i, c in enumerate(mask):
                if c == 'X':
                    l[i] = 'X' 
                elif c == '1':
                    l[i] = '1'
                elif c == '0':
                    continue

            newa = reduce(lambda a, b: a + b, l)
            print(newa)
            results = []
            floats = newa.count("X")
            combos = list(itertools.product([0, 1], repeat=floats))
            for combo in combos:
                temp = newa
                for bit in combo:
                    temp = temp.replace('X', str(bit), 1)
                results.append(temp)
            for addr in results:
                mem[addr] = int(value)


    sum = 0
    for p in mem:
        sum += mem[p]

    print('sum is %d' %  sum)

if __name__ == '__main__':
    p1()
    p2()
