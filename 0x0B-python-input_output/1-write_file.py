#!/usr/bin/python3
"""
Module
"""


def write_file(filename="", text=""):
    """
    writes a string to a text file (UTF8)

    Args:
        filename (str): Name of file
        text (str): String to be written to the file

    Returns:
        int: number of characters
    """
    with open(filename, 'w', encoding='utf-8') as file:
        chars = file.write(text)
    return chars
