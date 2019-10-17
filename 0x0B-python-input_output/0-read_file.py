#!/usr/bin/python3
"""
    Read file module
"""


def read_file(filename=""):
    """reads a text file and prints it to stdout

    Args:
        filename (string): file name
    """
    with open(filename, encoding="utf-8") as fn:
        for line in fn:
            print(line, end="")
