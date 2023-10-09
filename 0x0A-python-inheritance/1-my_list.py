#!/usr/bin/python3

"""
Module
"""


class MyList(list):
    """
    class MyList that inherits from list

    Args:
        list (list): inherits from list
    """

    def print_sorted(self):
        """
        prints sorted list
        """
        sorted_list = sorted(self)
        print(sorted_list)
