#!/usr/bin/python3
"""
Defines a Square class with size validation,
area computation, and printing capability.
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
        Retrieves the size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size of the square with validation
        """
        if not isinstance(value, int):
            raise TypeError("Size must be an integer")
        if value < 0:
            raise ValueError("Size must be >= 0")

        self.__size = value

    def area(self):
        """
        Returns the current area of the square
        """
        return self.__size * self.__size

    def my_print(self):
        """
        Prints the square using the '#' character
        """
        if self.__size == 0:
            print()
            return

        for _ in range(self.__size):
            print("#" * self.__size)
