#!/usr/bin/python3
"""
Write a function that prints an integer with "{:d}".format().
"""


def safe_print_integer(value):
    try:
        print("{:d}".format(int(value)))
        print()
        return True
    except (ValueError, TypeError):
        return False
