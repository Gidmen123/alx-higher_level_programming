#!/usr/bin/python3
""" Defines a string-to-JSON function"""


import json


def to_json_string(my_obj):
    """
    Returns the JSON representation of an object as a string.

    Args:
        my_obj: The object to convert to JSON.

    Returns:
        A string representing the JSON data.

    """
    return json.dumps(my_obj)
