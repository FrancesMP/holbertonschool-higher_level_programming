#!/usr/bin/python3
"""
This module defines a base class for geometry objects.
"""


class BaseGeometry:
    """
    A base class for geometry with validation methods.
    """

    def area(self):
        """
        Raise an exception because the area method
        is not implemented yet.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validate that a value is an integer greater than 0.

        Args:
            name (str): The name of the variable.
            value (int): The value to validate.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is <= 0.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
