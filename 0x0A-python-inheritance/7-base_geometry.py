#!/usr/bin/python3

"""
Module of BaseGeometry
"""


class BaseGeometry(object):
    """
    Base Geometry Class
    """

    def area(self):
        """
        Area

        Raises:
            Exception: area() is not implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Public instance method: that validates value

        Args:
            name (string): name
            value (integer): value

        Raises:
            TypeError: must be an integer
            ValueError: must be greater than 0
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
