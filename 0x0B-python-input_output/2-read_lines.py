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
        if nb_lines <= 0:
            r_line = fn.read()
            print(r_line, end="")
        else:
            for line in fn:
                if n_lines < nb_lines:
                    print(line, end="")
                    n_lines += 1
                else:
                    break
