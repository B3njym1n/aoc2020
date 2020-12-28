#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

def p1():
    with open('input', 'r') as file:
        input = file.read();
        fields, yours, nearby, = input.split("\n\n")
        fieldRanges = [re.findall("\d+\-\d+", l)  for l in fields.strip().split('\n')]
        tickets = [[d for d in l.split(',')] for l in nearby.strip().split('\n')]
        sum = 0
        for ticket in tickets[1:]:
            for value in ticket:
                if not validate_v1(value, fieldRanges):
                    sum += int(value)

        print(sum)

def validate_v1(value, fieldRanges):
    for field in fieldRanges:
        for frange in field:
            low, high = frange.split('-')
            if int(low) <= int(value) <= int(high):
                return True

    return False 

def p2():
    with open('input', 'r') as file:
        input = file.read();
        fields, yours, nearby, = input.split("\n\n")
        fieldRanges = [re.findall("\d+\-\d+", l)  for l in fields.strip().split('\n')]
        fieldNames = [l.split(':')[0] for l in fields.strip().split('\n')]
        tickets = [[d for d in l.split(',')] for l in nearby.strip().split('\n')]
        tickets = tickets[1:]
        validTickets = []
        for ticket in tickets:
            for value in ticket:
                if not validate_v1(value, fieldRanges):
                    break
            validTickets.append(ticket)
        
        print(fieldNames)
        for idx in range(len(fieldNames)):
            for t in validTickets:
                pass

if __name__ == "__main__":
    p1()
