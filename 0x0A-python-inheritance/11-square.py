#!/usr/bin/python3

"""
Module
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Class

    Args:
        Rectangle (int): Rectangle
    """

    def __init__(self, size):
        """
        Args:
            size (int): size
        """
        super().integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """area"""
        return super().area()
