#!/usr/bin/python3
"""
    Pascal's triangle module
"""


def pascal_triangle(n):
    """returns a list of lists of integers representing the Pascal's triangle

    Args:
        n (int): numbers of lists

    Returns:
        list: list of lists
    """
    my_list = []
    if n <= 0:
        return my_list
