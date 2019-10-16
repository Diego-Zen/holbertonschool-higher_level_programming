#!/usr/bin/python3
"""
    exact same object module
"""


def is_same_class(obj, a_class):
    """if the object is exactly an instance o a class

    Args:
        obj (object): any object
        a_class (class): any class

    Returns:
        bool: True if the object is an instance of a class or False otherwise
    """
    if type(obj) is a_class:
        return True
    else:
        return False
