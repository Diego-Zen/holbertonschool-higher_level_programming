#!/usr/bin/python3
"""
    First rectangle module
"""
from models.base import Base


class Rectangle(Base):
    """rectangle class
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """constructor

        Args:
            width (int): rectangle width
            height (int): rectangle height
            x (int): x coordinate
            y (int): y coordinate
            id (int): identifier
        """

        if not isinstance(width, int):
            raise TypeError("width must be an integer")

        if not isinstance(height, int):
            raise TypeError("height must be an integer")

        if not isinstance(x, int):
            raise TypeError("x must be an integer")

        if not isinstance(y, int):
            raise TypeError("y must be an integer")

        if width <= 0:
            raise ValueError("width must be > 0")

        if height <= 0:
            raise ValueError("height must be > 0")

        if x < 0:
            raise ValueError("x must be >= 0")

        if y < 0:
            raise ValueError("y must be >= 0")

        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        if not isinstance(width, int):
            raise TypeError("width must be an integer")

        if width <= 0:
            raise ValueError("width must be > 0")

        self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if not isinstance(height, int):
            raise TypeError("height must be an integer")

        if height <= 0:
            raise ValueError("height must be > 0")

        self.__height = height

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        if not isinstance(x, int):
            raise TypeError("x must be an integer")

        if x < 0:
            raise ValueError("x must be >= 0")

        self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        if not isinstance(y, int):
            raise TypeError("y must be an integer")

        if y < 0:
            raise ValueError("y must be >= 0")

        self.__y = y