#!/usr/bin/python3

"""

This is a module

Classes:
    Square: Square class that defines
    a square
"""


class Square:
    """
    Attributes:
        size (int): Private instance attribute

    Method:
        area (int): that returns the current square area
    """

    def __init__(self, size=0):
        """
        Args:
            size (int): Size of the Square

        Raises:
            TypeError: size must be an integer
            ValueError: size must be >= 0
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """
        Return:
            int: the current square area
        """
        return self.__size ** 2
