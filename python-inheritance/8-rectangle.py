#!/usr/bin/python3

"""
    Module for base_geometry
"""

BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """
    Rectangle Class to create a rectangle based on BaseGeometry

    Args:
        BaseGeometry (class): inheritance
    """
    def __init__(self, width, height):
        """
        __init__ Build the instance of the rectangle

        Args:
            width (any): width of the rectangle
            height (any): height of the rectangle
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
