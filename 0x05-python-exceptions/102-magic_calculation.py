#!/usr/bin/python3

"""
Write the Python function def magic_calculation(a, b):
that does exactly the same as the following Python bytecode:
"""


def magic_calculation(a, b):
    result = 0

    for i in range(1, 3):
        try:
            if i > a:
                raise Exception('Too Far')
            else:
                result = result + (a ** b) / i
        except Exception:
            result = a + b

    return result
