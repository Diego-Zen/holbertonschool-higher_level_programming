#!/usr/bin/python3
"""
    Append to a file module
"""


def append_write(filename="", text=""):
    """appends a string at the end of a text file

    Args:
        filename (str): file name
        text (str): text to append

    Returns:
        int: number of characters added
    """
    with open(filename, mode='a', encoding='utf-8') as fn:
        return (fn.write(text))
