#!/usr/bin/python3
"""
Module
"""


def is_same_class(obj, a_class):
    """

    Args:
        obj (obj): object
        a_class (obj): object

    Returns:
        bool: True if the object is exactly an instance
        of the specified class ; otherwise False
    """
    return type(obj) is a_class
