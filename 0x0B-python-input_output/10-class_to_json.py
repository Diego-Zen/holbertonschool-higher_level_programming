#!/usr/bin/python3
"""
    Class to JSON module
"""


def class_to_json(obj):
    """returns the dictionary description fpr JSON serialization of an object

    Args:
        obj (obj): instance of a class

    Returns:
        dict: dictionary description
    """
    return obj.__dict__
