#!/usr/bin/python3
"""
Module
"""
import json


def from_json_string(my_str):
    """
    returns an object (Python data structure)
    represented by a JSON string

    Args:
        my_str (str): JSON string to be parsed

    Returns:
        object: Python data structure represented
        by a JSON string
    """
    return json.loads(my_str)
