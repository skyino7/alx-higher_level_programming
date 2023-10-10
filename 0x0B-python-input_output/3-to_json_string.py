#!/usr/bin/python3

import json


def to_json_string(my_obj):
    """
    JSON representation of an object (string)

    Args:
        my_obj: Object converted to JSON

    Returns:
        str: JSON representation of an object
    """
    return json.dumps(my_obj)
