#!/usr/bin/python3
"""
Defines a Square class with a private size attribute,
getter, setter, and area computation.
"""


class Square:
    """
    Represents a square
    """
    def __init__(self, size=0):
        """
        Initializes a Square with a given size
        """
        self.size = size

    @property
    def size(self):
        """
        Initializes a Square with a given size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size of the square with validation

        Args:
            value (int): The new size of the square

        Raises:
            TypeError: If value is not an integer
            ValueError: If value is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        """
        Returns the current area of the square
        """
        return self.__size ** 2
