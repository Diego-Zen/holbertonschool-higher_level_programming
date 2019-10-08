#!/usr/bin/python3
"""
   Real definition of a rectangle module
"""


class Rectangle:
    """ defines a rectangle """

    def __init__(self, width=0, height=0):
        """ innitialize the data """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """ retrieve width """
        return self.__width

    @width.setter
    def width(self, value):
        """ set value if is int and > 0, or raise error """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """ retrieve height """
        return self.__height

    @height.setter
    def height(self, value):
        """ set height if is int and > 0 or raise error """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
