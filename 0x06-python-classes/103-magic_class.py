#!/usr/bin/python3
import math


class MagicClass:
    """
    define a magic class
    """
    def __init__(self, radius=0):
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    """ Area """
    def area(self):
        return (self.__radius ** 2) * math.pi

    """ Circunference """
    def circunference(self):
        return (math.pi * 2) * self.__radius
