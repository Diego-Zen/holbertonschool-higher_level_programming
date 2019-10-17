#!/usr/bin/python3
"""
    Student to JSON
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

    def to_json(self):
        """ retrieves a dictionary representation of a student instance """
        return self.__dict__
