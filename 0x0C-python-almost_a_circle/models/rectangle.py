#!/usr/bin/python3
"""
Module Doc
"""
from models.base import Base


class Rectangle(Base):
    """
    Rectangle class Doc
    inherits from Base
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Class constructor Doc
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
        Getter for width Doc
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter for width Doc
        """
        self.val_int(value, "width")
        self.validate_positive(value, "width")
        self.__width = value

    @property
    def height(self):
        """
        Getter for height Doc
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter for height Doc
        """
        self.val_int(value, "height")
        self.validate_positive(value, "height")
        self.__height = value

    @property
    def x(self):
        """
        Getter for x Doc
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        x Doc
        """
        self.val_int(value, "x")
        self.val_non(value, "x")
        self.__x = value

    @property
    def y(self):
        """
        Getter for y Doc
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        y Doc
        """
        self.val_int(value, "y")
        self.val_non(value, "y")
        self.__y = value

    def val_int(self, value, attribute_name):
        """
        Validate integer Doc
        """
        if not isinstance(value, int):
            raise TypeError(f"{attribute_name} must be an integer")

    def validate_positive(self, value, attribute_name):
        """
        Validate positive Doc
        """
        if value <= 0:
            raise ValueError(f"{attribute_name} must be > 0")

    def val_non(self, value, attribute_name):
        """
        Validate non-negative Doc
        """
        if value < 0:
            raise ValueError(f"{attribute_name} must be >= 0")

    def area(self):
        """
        Area Doc
        """
        return self.width * self.height

    def display(self):
        """
        Print the Rectangle character #
        """
        for _ in range(self.height):
            print("#" * self.width)

    def __str__(self):
        """
        __str__ Doc
        """
        restr = "[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}"
        return restr.format(self.id, self.x, self.y, self.width, self.height)

    def to_dictionary(self):
        """
        to_dict Doc
        """
        return {
            'x': self.x,
            'y': self.y,
            'id': self.id,
            'height': self.height,
            'width': self.width
        }

    def update(self, *args, **kwargs):
        """
        Update Doc
        """
        if args:
            attributes = ['id', 'width', 'height', 'x', 'y']
            for i in range(len(args)):
                setattr(self, attributes[i], args[i])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)
