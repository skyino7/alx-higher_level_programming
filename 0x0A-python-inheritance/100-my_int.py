#!/usr/bin/python3

"""
Module
"""


class MyInt(int):
    """Class MyInt"""

    def __eq__(self, other):
        """rebel"""
        return self.real != other

    def __ne__(self, other):
        """rebel"""
        return self.real == other
