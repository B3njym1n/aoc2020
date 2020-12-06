#!/usr/bin/env python
# -*- coding: utf-8 -*-

def main(fname):
    with open(fname, 'r') as file:
        inputs = file.read().strip().split('\n\n')
        count = 0
        for w in inputs:
            if "byr" in w and "iyr" in w and "eyr" in w and "hgt" in w and "hcl" in w and "ecl" in w and "pid" in w:
                count+=1

        return count

if __name__ == "__main__":
    fname = "input"
    print(main(fname))
