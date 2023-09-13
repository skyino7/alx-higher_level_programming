#!/usr/bin/python3

"""
Write a function that returns a
key with the biggest integer value.
"""


def best_score(a_dictionary):
    best_key = None

    if a_dictionary:
        best_value = list(a_dictionary.values())[0]
        for key, value in a_dictionary.items():
            if value >= best_value:
                best_key = key
                best_value = value

    return best_key
