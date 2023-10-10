#!/usr/bin/python3
"""Module"""

import json


def load_from_json_file(filename):
    """
    creates an Object from a “JSON file”

    Args:
        filename (str): Name of file

    Returns:
        object: creates an Object from a “JSON file”
    """
    with open(filename, 'r') as file:
        return json.load(file)
