#!/usr/bin/python3
"""
    MyList module
"""


class MyList(list):
    """
    A class to represent a list
    """

    def print_sorted(self):
        """prints the list"""
        print(sorted(self))
