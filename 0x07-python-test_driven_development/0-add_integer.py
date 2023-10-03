#!/usr/bin/python3

"""
Add two numbers
"""


def add_integer(a, b=98):
    """
    Adds two integers

    Args:
        a (int or float): first number
        b (int or float): second number. Defaults to 98.

    Raises:
        TypeError: number must be an integer

    Returns:
        - int: addition of a and b
    """

    if (not isinstance(a, int) and not isinstance(a, float)):
        raise TypeError("a must be an integer")
    if (not isinstance(b, int) and not isinstance(b, float)):
        raise TypeError("b must be an integer")

    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)

    return a + b
