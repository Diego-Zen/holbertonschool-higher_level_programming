#!/usr/bin/python3
import json
from io import StringIO
"""
    From JSON string to object module
"""


def from_json_string(my_str):
    """returns an object represented by a JSON

    Args:
        my_str (str): JSON representation

    Returns:
        obj: object Python data structure
    """
    io = StringIO(my_str)
    return (json.load(io))
