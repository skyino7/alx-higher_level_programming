#!/usr/bin/python3
"""
Write a function that prints the first x
elements of a list and only integers.
"""


def safe_print_list_integers(my_list=[], x=0):
    i = 0
    for item in range(x):
        try:
            if isinstance(my_list[item], int):
                print("{:d}".format(my_list[item]), end=' ')
                i += 1
        except (ValueError, TypeError):
            break
    print("")

    return i
