#!/usr/bin/python3

"""
Module of BaseGeometry
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    class
    """

    def __init__(self, width, height):
        """
        Args:
            width (int): width
            height (int): height
        """
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height
