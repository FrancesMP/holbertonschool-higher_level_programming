#!/usr/bin/python3
"""
This module defines a Square class
that inherits from Rectangle.
"""
Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    """
    A square defined by its size.
    """
    def __init__(self, size):
        """
        Initialize a square with validated size.

        Args:
            size (int): The size of the square sides.
        """
        self.__size = size
        self.integer_validator("size", size)
        super().__init__(size, size)
