#!/usr/bin/python3
"""
Module Prints Objects
"""


def lookup(obj):
    """
    function that returns the list of available attributes
    and methods of an object:

    Args:
        obj (boject): prints Object

    Returns:
        list: list of available attributes
    """
    return dir(obj)
