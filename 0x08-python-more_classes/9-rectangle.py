#!/usr/bin/python3

"""
    Module
    Class: defines a rectangle
"""


class Rectangle:
    """
        width(int): int
        height(int): int

        number_of_instances(int) = int

    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Args: width(int) and height(int)
                number_of_instances(int + 1)

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
        Rectangle.number_of_instances += 1

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

    def __str__(self):
        """print the rectangle with the character #"""

        rectangle_str = ""

        if self.__width == 0 or self.__height == 0:
            return rectangle_str

        for i in range(self.__height):
            rectangle_str += str(self.print_symbol) * self.__width
            if i != self.__height - 1:
                rectangle_str += '\n'

        return rectangle_str

    def __repr__(self):
        """ return a string representation of the rectangle """
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """Deletes an instances of the rectangle"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        area_1 = rect_1.area()
        area_2 = rect_2.area()

        return rect_1 if area_1 >= area_2 else rect_2

    @classmethod
    def square(cls, size=0):
        return cls(width=size, height=size)
