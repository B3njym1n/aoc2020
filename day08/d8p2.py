#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from sys import argv

def main(filename):
    with open(filename, 'r') as file:
        instrs = [l.strip().split(' ') for l in file.readlines() ]
        base = 0
        jmps = [x for x in range(len(instrs)) if instrs[x][0] == 'jmp']
        for jmp in jmps:
            acc = 0
            ip = 0
            visisted = []
            while ip < len(instrs):
                if ip in visisted:
                    break
                op = instrs[ip]
                visisted.append(ip)
                if ip == jmp:
                    ip += 1
                    continue
                if op[0] == 'acc':
                    if op[1][0] == '+':
                        acc += int(op[1][1:])
                    else:
                        acc -= int(op[1][1:])
                    ip += 1
                if op[0] == 'jmp':
                    if op[1][0] == '+':
                        ip += int(op[1][1:])
                    else:
                        ip -= int(op[1][1:])
                if op[0] == 'nop':
                    ip += 1
            if ip == len(instrs):
                return acc

if __name__ == "__main__":
    filename = argv[1]
    c = main(filename)
    print(c)
