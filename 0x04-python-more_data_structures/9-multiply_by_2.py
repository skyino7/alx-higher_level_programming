#!/usr/bin/python3
"""
Write a function that returns a new
dictionary with all values multiplied by 2
"""


def multiply_by_2(a_dictionary):
    new = {}

    for key, value in a_dictionary.items():
        new[key] = value * 2
    return new
