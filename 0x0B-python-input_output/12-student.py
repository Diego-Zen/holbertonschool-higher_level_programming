#!/usr/bin/python3
"""
    Student to JSON with filter
"""


class Student():
    """ defines a student """

    def __init__(self, first_name, last_name, age):
        """
        Args:
            first_name (str): first name student
            last_name (str): last name student
            age (int): age of student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ retrieves a dictionary representation of a student instance
        Args:
            attrs (list): atributes

        Returns:
            dict: dictionary representation
        """
        if attrs is None:
            return self.__dict__
        else:
            my_dict = self.__dict__
            new_dict = {}
            for attr in attrs:
                if attr in my_dict:
                    new = {attr: self.__dict__[attr]}
                    new_dict.update(new)
            return new_dict
