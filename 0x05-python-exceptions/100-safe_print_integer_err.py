#!/usr/bin/python3

import sys

"""
Write a function that prints an integer.
"""


def safe_print_integer_err(value):
    try:
        if isinstance(value, int):
            print("{:d}".format(value))
            return True
        else:
            print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
            return False
    except (ValueError):
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return False
