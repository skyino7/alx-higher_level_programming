#!/usr/bin/python3
"""Module"""


def append_after(filename="", search_string="", new_string=""):
    """
    inserts a line of text to a file,
    after each line containing a specific string
    """
    new = ""
    with open(filename, 'r') as file:
        for line in file:
            new += line
            if search_string in line:
                new += new_string

    with open(filename, 'w') as file:
        file.write(new)
