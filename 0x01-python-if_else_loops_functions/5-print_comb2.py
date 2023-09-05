#!/usr/bin/python3

for num1 in range(100):
    if num1 < 99:
        print("{num:02d}".format(num=num1), end=", ")
    else:
        print("{num:02d}".format(num=num1))
