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
        size (int): get size property and set size

        Raises:
            TypeError: if size is not int
            ValueError: if size is less than 0
        """
        return self.__size

    @size.setter
    def size(self, size):
        if type(size) == int:
            self.__size = size
        else:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
    """
    Area of a square

    Returns:
        the area of a square (size ** 2)
    """
    def area(self):
        return self.__size ** 2
