#!/usr/bin/python3

"""
Write a function that replaces all
occurrences of an element by another in a new list.
"""


def search_replace(my_list, search, replace):
    new = my_list.copy()

    for i in range(len(new)):
        if new[i] == search:
            new[i] = replace
    return new
