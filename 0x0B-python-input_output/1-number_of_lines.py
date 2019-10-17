#!/usr/bin/python3
"""
    NUmber of lines module
"""


def number_of_lines(filename=""):
    """number of lines of a text file

    Args:
        filename (string): file name or relative path

    Returns:
        int: number of lines
    """
    n_lines = 0

    with open(filename, encoding="utf-8") as fn:
        for line in fn:
            n_lines += 1

    return n_lines
