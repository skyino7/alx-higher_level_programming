#!/usr/bin/python3
"""Module"""

import json


def save_to_json_file(my_obj, filename):
    """
    writes an Object to a text file, using a JSON representation

    Args:
        my_obj (boject): Object to be saved
        filename (str): Name of file
    """
    with open(filename, 'w') as file:
        file.write(json.dump(my_obj))
