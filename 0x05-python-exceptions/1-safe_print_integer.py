#!/usr/bin/python3
"""
Write a function that prints an integer with "{:d}".format().
"""


def safe_print_integer(value):
    try:
        if isinstance(value, int):
            print("{:d}".format(value))
            return True
        else:
            return False
    except ValueError:
        return False
