#!/usr/bin/python3
import json
"""
    Save object to a file module
"""


def save_to_json_file(my_obj, filename):
    """writes an object to a text file using a JSON representation

    Args:
        my_obj (obj): object
        filename (str): file name
    """
    with open(filename, mode='w', encoding='utf-8') as fn:
        fn.write(json.dumps(my_obj))
