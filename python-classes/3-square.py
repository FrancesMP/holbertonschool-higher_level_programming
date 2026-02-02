#!/usr/bin/python3
"""
Defines a Square class with size validation and area computation
"""


class Square:
    """
    Represents a square
    """
    def __init__(self, size=0):
        """
        Initializes a Square with a given size

        Args:
            size (int): The size of the square

        Raises:
            TypeError: If size is not an integer
            ValueError: If size is less than 0
        """
        if not isinstance(size, int):
            raise TypeError("Size must be an integer")
        if size < 0:
            raise ValueError("Size must be >= 0")

        self.__size = size

    def area(self):
        """
        Returns the current area of the square

        Return:
            int: the area (side * side)
        """
        return self.__size ** 2
