#!/usr/bin/python3
"""
Write a function that prints a
dictionary by ordered keys.
"""


def print_sorted_dictionary(a_dictionary):
    i = 0
    for key, value in sorted(a_dictionary.items()):
        i += 1
        res = str(key) + ": " + str(value)
        print(f"{res}")
