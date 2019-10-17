#!/usr/bin/python3
"""
    Read n lines module
"""


def read_lines(filename="", nb_lines=0):
    """reads n lines of a text file and prints it to stdout

    Args:
        filename (str): file name or relative path
        nb_lines (int): lines to read
    """
    n_lines = 0

    with open(filename, encoding="utf-8") as fn:
        for line in fn:
            n_lines += 1

        if nb_lines <= 0 or nb_lines >= n_lines:
            read_data = fn.read()
        else:
            read_data = fn.read(nb_lines)

        for line in read_data:
            print(line, end="")
