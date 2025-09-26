#!/usr/bin/python3

"""
    Module for base_geometry
"""

Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """
    Square Class that inherit from Rectangle

    Args:
        Rectangle (obj): Obj rectangle
    """
    def __init__(self, size):
        """
        __init__ Constructor

        Args:
            size (int): size of the edge
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """
        area calculate the area

        Returns:
            int: area of the square
        """
        return super().area()
