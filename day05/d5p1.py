#!/usr/bin/env python
# -*- coding: utf-8 -*-

def main(fname: str):
    with open(fname, 'r') as file:
        input = [line.strip() for line in file.readlines()]
        seats = []
        for code in input:
            print(code)
            row = 0
            col = 0
            low = 0
            hig = (1 << 7) - 1
            left = 0
            right = (1<<3) - 1
            for i in range(7):
                if i < 6:
                    if code[i] == 'F':
                        hig = (low + hig) // 2 
                    elif code[i] == 'B':
                        low = 1 + (low + hig) // 2
                else:
                    if code[i] == 'F':
                        row = low
                    elif code[i] == 'B':
                        row = hig

            print(row)

            for j in range(7, 10):
                if j < 9:
                    if code[j] == 'L':
                        right = (left + right) // 2 
                    elif code[j] == 'R':
                        left = 1 + (left + right) // 2
                else:
                    if code[j] == 'L':
                        col = left
                    elif code[j] == 'R':
                        col = right
            
            print(col)

            id = row * 8 + col
            print(id)
            seats.append(id)

    seats.sort(reverse=True)
    return seats[0]


if __name__ == "__main__":
    maxId = main("input")
    print(maxId)

