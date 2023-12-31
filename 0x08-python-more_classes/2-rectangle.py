#!/usr/bin/python3

"""
    Module
    Class: defines a rectangle
"""


class Rectangle:
    """
        width(int): int
        height(int): int

    """

    def __init__(self, width=0, height=0):
        """
        Args: width(int) and height(int)

        Raises:
            TypeError: must be an integer
            ValueError: must be >= 0
        """

        self.__width = 0
        self.__height = 0

        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")

        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")

        self.__width = width
        self.__height = height

    @property
    def width(self):
        """
        Width Property
        Returns: width attribute
        """
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Height Property
        Returns: height attribute
        """
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Area: Public Instance Method
        Returns: returns the rectangle area
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        perimeter: Public Instance Method
        Returns: eturns the rectangle perimeter
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)
