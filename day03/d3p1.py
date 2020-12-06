#!/usr/bin/env python
# -*- coding: utf-8 -*-

#  import pdb; pdb.set_trace()

def main() -> int:
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

if __name__ == "__main__":
    trees = main()
    print(trees)
    #  fname = "input"
    #  with open(fname, 'r') as file:
    #      lines = file.readlines()
    #      for line in lines:
    #          print(line.rstrip())
