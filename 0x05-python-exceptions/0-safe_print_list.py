#!/usr/bin/python3
"""
Write a function that prints x elements of a list.
"""


def safe_print_list(my_list=[], x=0):
    try:
        i = 0
        for item in my_list:
            if i < x:
                print(f"{my_list[i]}", end="")
                i += 1
        print()
    except IndexError:
        print('Error: The input is not in the list')

    return i
