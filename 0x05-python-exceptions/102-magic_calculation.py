#!/usr/bin/python3

"""
Write the Python function def magic_calculation(a, b):
that does exactly the same as the following Python bytecode:
"""


def magic_calculation(a, b):
    result = 0

    for i in range(1, 4):
        try:
            if i > a:
                raise Exception('Too Far')
            result = result + (a ** b) / i
        except:
            result = result + (a + b)

    return result
