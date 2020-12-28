#!/usr/bin/env python
# -*- coding: utf-8 -*-

def main():
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
                return 
            index += 1


if __name__ == "__main__":
    main()
