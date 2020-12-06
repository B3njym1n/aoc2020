#!/usr/bin/env python3
# -*- coding: utf-8 -*-

inputfile="input"

def count_(password: str, c: chr) -> int:
    return password.count(char)

#  with open(inputfile) as file:
#      inputs = file.readlines()
#      num_valid_psw = 0
#      for line in  inputs:
#          args = line.split(" ")
#          args[2] = args[2].replace("\n", "")
#          (l,h) = args[0].split("-")
#          (l, h) = (int(l), int(h))
#          char = list(args[1])[0]
#          print(l, h, char, args[2])
#
#      print(num_valid_psw)


def find_valid_password(inputfile: str) -> int:
    with open(inputfile, 'r') as file:
        inputs = file.readlines()

        num_valid_psw = 0
        for line in inputs:
            arguments = line.split(" ")
            password = arguments[2].replace("\n", "")
            (l, h) = arguments[0].split("-")
            (l, h) = (int(l), int(h))

            ch = arguments[1].replace(":", "")
            a = 1 if (password[l - 1] == ch) else 0
            b = 1 if (password[h - 1] == ch) else 0
            if (a ^ b):
                num_valid_psw += 1

        return num_valid_psw

if __name__ == "__main__":
    print(find_valid_password(inputfile))
