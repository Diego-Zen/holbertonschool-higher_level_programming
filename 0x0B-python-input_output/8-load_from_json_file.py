#!/usr/bin/python3
import json
from io import StringIO
"""
    Create object from a JSON file module
"""


def load_from_json_file(filename):
    """creates an object from a JSON file

    Args:
        filename (str): file name

    Returns:
        obj: object
    """
    with open(filename, encoding='utf-8') as fn:
        r_file = fn.read()
        io = StringIO(r_file)
        return (json.load(io))
