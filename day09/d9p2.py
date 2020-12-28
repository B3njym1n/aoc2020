#!/usr/bin/env python
# -*- coding: utf-8 -*-

def p1():
    with open('input', 'r') as file:
        data = [int(l.strip()) for l in file.readlines()]
        index = 25
        while index < len(data):
            num = data[index]
            prev = index - 25
            m = {}
            while prev < index:
                another = num - data[prev]
                if (m.get(data[prev])):
                    break
                else:
                    m[another] = data[prev] 
                prev += 1

            if (prev == index):
                print(index)
                print(data[index])
                return (index, data[index])
            index += 1

def p2():
    with open('input', 'r') as file:
        data = [int(l.strip()) for l in file.readlines()]
        index = 25
        target = 0
        while index < len(data):
            num = data[index]
            prev = index - 25
            m = {}
            while prev < index:
                another = num - data[prev]
                if (m.get(data[prev])):
                    break
                else:
                    m[another] = data[prev] 
                prev += 1

            if (prev == index):
                print(index)
                print(data[index])
                target = data[index]
                break
            index += 1
        
        i =  0
        flag = True
        
        while (flag and (i < len(data) - 1)):
            sum = 0
            j = i
            while (j < len(data)):
                sum += data[j]
                if sum < target:
                    j+=1
                elif sum > target:
                    break
                else:
                    rl = [x for x in data[i: j+1]]
                    rl.sort()
                    print(rl)
                    flag = False
                    print(rl[0] + rl[len(rl)-1])
                    break
            i += 1

if __name__ == "__main__":
    p2()
