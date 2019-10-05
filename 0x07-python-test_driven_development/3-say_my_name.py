#!/usr/bin/python3
"""
    Say my name module
"""


def say_my_name(first_name, last_name=""):
    """ prints My name is <first name> <last name> """
    if type(first_name) is not str or type(last_name) is not str:
        raise TypeError("first_name must be a string or last_\
name must be a string")
    print("My name is {} {}".format(first_name, last_name))
