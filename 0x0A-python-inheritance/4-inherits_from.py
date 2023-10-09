#!/usr/bin/python3

"""
Module
"""


def inherits_from(obj, a_class):
    """_summary_

    Args:
        obj (obj): object
        a_class (object): object

    Returns:
        bool: True if the object is an instance of a class
        that inherited (directly or indirectly) from the
        specified class ; otherwise False
    """
    return issubclass(type(obj), a_class)
