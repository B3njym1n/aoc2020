#!/usr/bin/env python
# -*- coding: utf-8 -*-

#  import pdb; pdb.set_trace()

def demo() -> int:
    data = [line.rstrip() for line in open('input', 'r').readlines()]
    width = len(data[0])
    height = len(data)
    x, y, trees = 0, 0, 0
    
    while y < height:
        #  breakpoint()
        if (data[y][x] == '#'):
            trees+=1
        x, y = (x + 3) % width, y + 1

    return trees

def f(i: int, j: int, data ) -> int:
    width = len(data[0])
    height = len(data)
    x, y, trees = 0, 0, 0
    
    while y < height:
        #  breakpoint()
        if (data[y][x] == '#'):
            trees+=1
        x, y = (x + i) % width, y + j

    return trees

if __name__ == "__main__":
    data = [line.rstrip() for line in open('input', 'r').readlines()]
    one = f(1, 1, data)
    three = f(3, 1, data)
    five = f(5, 1, data)
    seven = f(7, 1, data)
    vone = f(1, 2, data)
    print(one * three * five * seven * vone)
