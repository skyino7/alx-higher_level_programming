#!/usr/bin/python3
"""
prints it to stdout:
"""


def read_file(filename=""):
    """
    Args:
        filename (str): reads a text file (UTF8).
    """
    with open(filename, 'r', encoding='utf-8') as file:
        text = file.read()
        print(text)
