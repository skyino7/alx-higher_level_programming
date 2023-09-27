"""
Magic class module
"""
import math


class _MagicClass:
    """
    Magic Class
    Attributes:
        radius (int): integer
    """

    def __init__(self, radius):
        """
        Args:
            radius (int): integer
            Raises: Typeerror: not an int
        """
        if not isinstance(radius, (int, float)):
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """
            float: area
        """
        return 2 ** self.__radius * math.pi

    def circumference(self):
        """
            float: circumference
        """
        return 2 * math.pi * self.__radius
