#! /usr/bin/env python3
filename = "input"

try:
    file = open(filename)
    lines = file.readlines()
    res = []
    for line in lines:
        res.append(int(line.replace("\n", "")))

    res.sort()
    size = len(res)
    for i in range(size - 2):
        l, r = i + 1, size - 1
        while l < r:
            sum_ = res[i] + res[l] + res[r]
            if (sum_ < 2020):
                l+=1
            elif sum_ > 2020:
                r-=1
            else:
                print(res[i] * res[l] * res[r])
                l+=1
                r-=1

finally:
    file.close()
