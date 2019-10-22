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

        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def getWidth(self):
        return self.__width

    @getWidth.setter
    def setWidth(self, width):
        self.__width = width

    @property
    def getHeight(self):
        return self.__height

    @getHeight.setter
    def setHeight(self, height):
        self.__height = height

    @property
    def getX(self):
        return self.__x

    @getX.setter
    def setX(self, x):
        self.__x = x

    @property
    def getY(self):
        return self.__y

    @getY.setter
    def setY(self, y):
        self.__y = y
