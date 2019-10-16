#!/usr/bin/python3
"""
    integer validator module
"""


class BaseGeometry():
    """ class base on base_geometry """

    def area(self):
        """raise an exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validator
        Args:
            name (string): name
            value (int): integer greater than 0

        Raises:
            TypeError: if value is not an integer
            ValueError: if value is less or equal to 0
        """
        if not isinstance (value, int):
            raise TypeError(name + " must be an integer")
        if value <= 0:
            raise ValueError(name + " must be greater than 0")
