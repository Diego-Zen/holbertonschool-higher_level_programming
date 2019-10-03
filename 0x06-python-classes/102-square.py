#!/usr/bin/python3


class Square:
    """
    Defines a square
    Args:
        size (int): size of a square

    Raises:
        TypeError: if size is not int
        ValueError: if size is less than 0
    """
    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        """
        value (int, float): get size property and set size

        Raises:
            TypeError: if size is not int
            ValueError: if size is less than 0
        """
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int and type(value) is not float:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
    """
    Area of a square

    Returns:
        the area of a square (size ** 2)
    """
    def area(self):
        return self.__size ** 2

    """
    Rich comparision operators
    """
    def __it__(self, other):
        return self.__size < other.__size
    def __le__(self, other):
        return self.__size <= other.__size
    def __eq__(self, other):
        return self.__size == other.__size
    def __ne__(self, other):
        return self.__size != other.__size
    def __gt__(self, other):
        return self.__size > other.__size
    def __ge__(self, other):
        return self.__size >= other.__size
