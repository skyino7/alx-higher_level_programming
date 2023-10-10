#!/usr/bin/python3
"""
prints it to stdout:
"""


def read_file(filename=""):
    """
    Args:
        filename (str): reads a text file (UTF8).
    """
    with open(filename, encoding='utf-8') as file:
        for text in file:
            print(text, end="")
