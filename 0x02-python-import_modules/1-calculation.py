#!/usr/bin/python3

from calculator_1 import add, sub, div, mul
if __name__ == "__main__":
    a = 5
    b = 10
    print("{} + {} = {}".format(a, b, add(a, b)))
    print("{} - {} = {}".format(a, b, sub(a, b)))
    print("{} / {} = {}".format(a, b, div(a, b)))
    print("{} * {} = {}".format(a, b, mul(a, b)))
