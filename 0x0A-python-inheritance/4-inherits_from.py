#!/usr/bin/python3
"""
    only sub class of module
"""


def inherits_from(obj, a_class):
    """if the object is an instance of a class that inherited from a class
    Args:
        obj (object): any object
        a_class (class): any class

    Returns:
        bool: True is is instance, otherwise False
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
