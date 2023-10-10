#!/usr/bin/python3
"""Module"""


def add_attr(obj, name, value):
    """
    adds a new attribute to an object

    Args:
        obj (object): obj
        name (str): name
        value (int): value

    Raises:
        TypeError: can't add new attribute
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    else:
        setattr(obj, name, value)
