#!/usr/bin/python3
"""
Write a function that returns a
set of common elements in two sets.
"""


def common_elements(set_1, set_2):
    res = [i for i in set_1 if i in set_2]
    return res
