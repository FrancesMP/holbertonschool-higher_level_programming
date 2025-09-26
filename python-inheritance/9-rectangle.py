#!/usr/bin/python3

"""
    Module for base_geometry
"""


class BaseGeometry():
    """
    BaseGeometry Improve base geometry with a public instance method
    """
    def area(self, width, height):
        """
        area pass

        Raises:
            Exception: area() is not implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        integer_validator Validate the "value" variable

        Args:
            name (string): Name of the value (always a string)
            value (int): Value

        Raises:
            TypeError: Must be an integer
            ValueError: Must be >= 0
        """
        self.name = name

        if type(value) is not int:
            raise TypeError(f"{self.name} must be an integer")

        self.value = value

        if value <= 0:
            raise ValueError(f"{self.name} must be greater than 0")


class Rectangle(BaseGeometry):
    """
    Rectangle Class Rectangle that inherits from BaseGeometry

    Args:
        BaseGeometry (object): parent object
    """
    def __init__(self, width, height):
        """
        __init__ constructor

        Args:
            width (int): width
            height (int): heigh
        """
        self.__width = width
        self.__height = height
        self.integer_validator("height", self.__height)
        self.integer_validator("height", self.__width)

    def area(self):
        """
        area calculate the area

        Returns:
            int: area of the rectangle (width * height)
        """
        return self.__width * self.__height

    def __str__(self):
        """
        __str__ method

        Returns:
            string: Description of the rectangle
        """
        result = "[Rectangle] " + str(self.__width) + "/" + str(self.__height)
        return (result)
