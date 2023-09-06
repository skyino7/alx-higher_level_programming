#!/usr/bin/python3

for val in range(122, 96, -1):
    if val % 2 != 0:
        val -= 32
    print("{:s}".format(chr(val)), end="")
