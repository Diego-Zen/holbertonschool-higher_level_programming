#!/usr/bin/python3
"""
    Write to a file module
"""


def write_file(filename="", text=""):
    """writes a string to a text file
    Args:
        filename (str): file name
        text (str): text to write

    Returns:
        int: number of characters written
    """
    with open(filename, mode='w', encoding='utf-8') as fn:
        return (fn.write(text))
