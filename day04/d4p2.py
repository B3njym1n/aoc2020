#!/usr/bin/env python
# -*- coding: utf-8 -*-

def main(fname):
    with open(fname, 'r') as file:
        inputs = file.read().strip().split('\n\n')
        data = []
        count = 0
        for blk in inputs:
            keys = blk.replace("\n", " ").split(" ")
            data.append(dict(filter(None, map(lambda d : d.split(":"), keys))))

        for line in data:
            if not ("byr" in line and 1920 <= int(line["byr"]) <= 2002):
                continue
            if not ("iyr" in line and 2010 <= int(line["iyr"]) <= 2020):
                continue
            if not ("eyr" in line and 2020 <= int(line["eyr"]) <= 2030):
                continue
            if not ("hgt" in line):
                continue
            height = line["hgt"] 
            if not (height.endswith("cm") or height.endswith("in")): 
                continue 
            if height.endswith("cm") and not ( 150 <= int(height[:-2]) <= 193): 
                continue 
            if height.endswith("in") and not (59 <= int(height[:-2]) <= 76): 
                continue 
            if not ("hcl" in line and line["hcl"][0] == "#" and __import__("re").match("[a-f0-9]{6}", line["hcl"][1:])):
                continue 
            if not ("ecl" in line and line["ecl"] in ("amb", "blu", "brn", "gry", "grn", "hzl", "oth")): 
                continue 
            if not ("pid" in line and len(line["pid"]) == 9): 
                continue 
            try:
                int(line["pid"])
            except:
                continue
            count += 1
        
        return count

if __name__ == "__main__":
    fname = "input"
    print(main(fname))
