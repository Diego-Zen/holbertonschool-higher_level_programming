#!/usr/bin/python3
"""
    same class or inherit from module
"""


def is_kind_of_class(obj, a_class):
    """if the object is an instance of

    Args:
        obj (object): any object
        a_class (class): any class

    Returns:
        bool: True if the object is an instance of, otherwise False
    """
    return isinstance(obj, a_class)
