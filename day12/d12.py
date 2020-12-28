#!/usr/bin/env python
# -*- coding: utf-8 -*-

def p1(ins):
    x, y = 0, 0
    dir = 0;
    for w in ins:
        c, d = w[0], int(w[1:])
        if c == 'E':
            x += d
        elif c == 'N':
            y += d
        elif c == 'W':
            x -= d
        elif c == 'S':
            y -= d
        elif c == 'L':
            dir += d
        elif c == 'R':
            dir -= d
        elif c == 'F':
            if (dir % 360 == 0):
                x += d
            elif (dir % 360 == 90):
                y += d
            elif (dir % 360 == 180):
                x -= d
            elif (dir % 360 == 270):
                y -= d

    print(x, y)
    print(abs(x) + abs(y))

def p2(ins):
    x, y = 0, 0
    vec = [10, 1]
    for w in ins:
        c, d = w[0], int(w[1:])
        if c == 'E':
            vec[0] += d
        elif c == 'N':
            vec[1] += d
        elif c == 'W':
            vec[0] -= d
        elif c == 'S':
            vec[1] -= d
        elif c == 'L':
            if d == 90:
                vec[0], vec[1] = -vec[1], vec[0]
            elif d == 180:
                vec[0], vec[1] = -vec[0], -vec[1]
            elif d == 270:
                vec[0], vec[1] = vec[1], -vec[0]
        elif c == 'R':
            if d == 90:
                vec[0], vec[1] = vec[1], -vec[0]
            elif d == 180:
                vec[0], vec[1] = -vec[0], -vec[1]
            elif d == 270:
                vec[0], vec[1] = -vec[1], vec[0]
        elif c == 'F':
            x, y = x + vec[0] * d, y + vec[1]*d

    print(x, y)
    print(abs(x) + abs(y))

if __name__ == "__main__":
    with open('input') as file:
        ins = [i.strip() for i in file.readlines()]
        p1(ins)
        p2(ins)
