#!/usr/bin/env python3
# -*- coding: utf-8 -*-

inputfile="input"

def count_(password: str, c: chr) -> int:
    return password.count(char)

with open(inputfile) as file:
    inputs = file.readlines()
    num_valid_psw = 0
    for line in  inputs:
        args = line.split(" ")
        args[2] = args[2].replace("\n", "")
        (l,h) = args[0].split("-")
        (l, h) = (int(l), int(h))
        char = list(args[1])[0]
        print(l, h, char, args[2])
        c = count_(args[2], char)
        print(c)
        if ( c <= h and c >= l):
            num_valid_psw+=1
        
    print(num_valid_psw)
