#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from sys import argv

def main(filename):
    with open(filename, 'r') as file:
        instrs = [l.strip() for l in file.readlines() ]
        base = 0
        accumulator = 0
        t = [False for i in range(len(instrs))]
        while True:
            if t[base] == False:
                t[base] = True
            else:
                print(base)
                break
            instr = instrs[base]
            op, operand = instr.split(' ')
            print(op, operand)
            if op == 'nop':
                base+=1
            elif op == 'acc':
                accumulator+= int(operand)
                base+=1
            elif op == 'jmp':
                base += int(operand)

        return accumulator


if __name__ == "__main__":
    filename = argv[1]
    c = main(filename)
    print(c)
