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
        position (int): Private instance attribute

    Methods:
        area: returns the current square area
        my_print: prints in stdout the square in the character #
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Args:
            size (int): Size of the Square
            position (int): Position of the square
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """
        Getter method for the size property

        Returns:
            value of the size attribute
        """
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("szie must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """
        Getter method for the position property

        Returns:
            value of the position attribute
        """
        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple) or len(value) != 2 or not all(isinstance(x, int) and x >= 0 for x in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """
        Return:
            int: the current square area
        """
        return self.__size ** 2

    def my_print(self):
        """
        Method prints in stdout the square with the character #
        """
        if self.__size == 0:
            print()
        else:
            for i in range(self.__position[1]):
                print()
            for j in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
