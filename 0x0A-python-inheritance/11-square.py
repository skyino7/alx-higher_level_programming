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
        super().__init__(width=size, height=size)
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """area"""
        return self.__size ** 2
