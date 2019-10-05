#!/usr/bin/python3
"""
    Text identation module
"""


def text_indentation(text):
    """ prints a text with 2 new lines after each of ., ? and : """
    if type(text) is not str:
        raise TypeError("text must be a string")
    old = ""
    for i in text:
        if i == "." or i == "?" or i == ":":
            print(i, end="")
            print("\n")
        else:
            if (old == "." or old == "?" or old == ":") and i == " ":
                continue
            else:
                print(i, end="")
        old = i
