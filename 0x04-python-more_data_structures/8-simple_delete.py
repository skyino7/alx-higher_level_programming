#!/usr/bin/python3

"""
Write a function that deletes
a key in a dictionary.
"""


def simple_delete(a_dictionary, key=""):

    a_dictionary.pop(key, None)
    return a_dictionary
