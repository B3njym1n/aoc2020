#!/usr/bin/env python
# -*- coding: utf-8 -*-

import copy

def p1():
    with open('input', 'r') as input:
        tbl = [[c for c in row.strip()] for row in input.readlines()]
        changes = True
        new_tbl = make_tbl(tbl)
        while changes:
            new_tbl, changes = change(new_tbl)
            print(changes)
        print(count_occupied (new_tbl))

def change(tbl):
    rows = len(tbl)
    cols = len(tbl[0])
    changes = 0
    new_tbl = make_tbl(tbl)
    for row in range(0, rows):
        for col in range(0, cols):
            changes += flip(tbl, rows, cols, new_tbl, row, col)
    return new_tbl, changes

def make_tbl(tbl):
    return [[c for c in row] for row in tbl]

def flip(tbl, rows, cols, new_tbl, row, col):
    count_l = 0
    count_b = 0
    for y in range(row-1, row+2):
        for x in range(col-1, col+2):
            if ( y < rows and y > -1):
                if ( x < cols and x > -1):
                    if ( y == row and x == col):
                        pass
                    elif (tbl[y][x] == '.'):
                        pass ## skip
                    elif (tbl[y][x] == 'L'):
                        count_l += 1
                    elif (tbl[y][x] == '#'):
                        count_b += 1

    if (count_b > 3 and tbl[row][col] == '#'):
        new_tbl[row][col] = 'L'
        return 1
    if (count_b == 0 and tbl[row][col] == 'L'):
        new_tbl[row][col] = '#'
        return 1
    return 0
                
def count_occupied(tbl):
    return sum(sum(1 if c == '#' else 0 for c in row) for row in tbl)

if __name__ == "__main__":
    p1()
