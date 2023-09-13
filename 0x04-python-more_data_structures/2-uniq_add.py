#!/usr/bin/python3
"""
Write a function that adds all unique
integers in a list (only once for each integer).
"""


def uniq_add(my_list=[]):
    res = sum(list(set(my_list)))
    return res
