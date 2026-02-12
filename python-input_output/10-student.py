#!/usr/bin/python3

"""
class Student that defines a student
"""


class Student:
    """
     Class student defined by first name, last name and age
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        to_json Retrieve a dictionnary representation of a student instance

        Args:
            attrs (list, optional): list of wanted attributes.
            Defaults to None.

        Returns:
            dict: dict representation of a student istance
        """
        if attrs is None:
            result_dict = self.__dict__
        else:
            result_dict = {}
            for item in attrs:
                try:
                    result_dict[item] = self.__dict__[item]
                except KeyError:
                    next

        # reverse the dict to have the same result than in checker
        reverse_dict = {}
        for key in reversed(result_dict):
            reverse_dict[key] = result_dict[key]

        return reverse_dict
