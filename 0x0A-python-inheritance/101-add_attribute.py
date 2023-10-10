#!/usr/bin/python3
"""Module"""


def add_attr(obj, name, value):
    """
    adds a new attribute to an object

    Args:
        obj (object): _description_
        name (str): _description_
        value (int): _description_

    Raises:
        TypeError: _description_
    """
    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")
    else:
        setattr(obj, name, value)
