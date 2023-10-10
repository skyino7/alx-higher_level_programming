#!/usr/bin/python3
"""
Module
"""


def append_write(filename="", text=""):
    """
    appends a string at the end of a text file (UTF8)

    Args:
        filename (str): Name of file
        text (str): String to be appended to the file

    Returns:
        int: number of characters added
    """
    with open(filename, 'a', encoding='utf-8') as file:
        chars = file.write(text)
    return chars
