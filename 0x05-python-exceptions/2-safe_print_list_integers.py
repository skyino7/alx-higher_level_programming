#!/usr/bin/python3
"""
Write a function that prints the first x
elements of a list and only integers.
"""


def safe_print_list_integers(my_list=[], x=0):
    try:
        i = 0
        for item in my_list:
            if isinstance(item, int):
                print("{:d}".format(item), end=' ')
                i += 1
                if i == x:
                    break
        print()
        return i
    except TypeError:
        print("")
        return 0
