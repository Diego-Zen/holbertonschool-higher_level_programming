#!/usr/bin/python3
import json
"""
    To JSON string module
"""


def to_json_string(my_obj):
    """returns the JSON representation of an object

    Args:
        my_obj (str): object

    Returns:
        json: representation of an object
    """
    return (json.dumps(my_obj))
