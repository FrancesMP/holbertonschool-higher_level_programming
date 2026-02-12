#!/usr/bin/python3
"""
    Student to Json

Returns:
    dict: retrieves a dictionary representation of a Student instance (
"""


class Student:
    """
     class Student
    """
    def __init__(self, first_name, last_name, age):
        """
        __init__

        Args:
            first_name (string): first name
            last_name (string): last name
            age (int): age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        to_json

        Returns:
            dict: retrieves a dictionary representation of a Student instance (
        """
        return self.__dict__
