#!/usr/bin/env python
# -*- coding: utf-8 -*-

def p1():
    with open('input','r') as f:
        time = int(f.readline().rstrip())
        ids = [int(c) for c in f.readline().rstrip().split(',') if c != 'x']
        dtimes = [(id - time % id) for id in ids]
        print(dtimes)

def p2():
    with open('input','r') as f:
        f.readline()
        ids = [c for c in f.readline().rstrip().split(',') ]
        time = 0
        time_jump = 1
        for offset, busid in enumerate(ids):
            if busid != 'x':
                print(offset, int(busid))
                while (time + offset) % int(busid) != 0:
                    time += time_jump
                time_jump = time_jump * int(busid) 
        
        print(time)


if __name__ == '__main__':
    #  p1()
    p2()
