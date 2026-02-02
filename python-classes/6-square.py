#!/usr/bin/python3
"""
Defines a Square class with size and position.

This module provides a Square class that allows size validation,
position handling, area computation, and formatted printing.
"""


class Square:
    """
    Represents a square.

    Attributes:
        __size (int): Size of the square.
        __position (tuple): Position of the square (x, y)
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        Initialize a new Square instance.

        Args:
            size (int): The size of the square (default is 0).
            position (tuple): A tuple of two positive integers representing
                              the position of the square (default is (0, 0))
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """
        Get the size of the square

        Returns:
            int: The size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Set the size of the square.

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

    @property
    def position(self):
        """
        Get the position of the square

        Returns:
            tuple: The position of the square (x, y)
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Set the position of the square

        Args:
            value (tuple): A tuple of two positive integers

        Raises:
            TypeError: If value is not a tuple of two positive integers
        """
        if (
            not isinstance(value, tuple) or
            len(value) != 2 or
            not all(isinstance(i, int) and i >= 0 for i in value)
        ):

            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Compute and return the area of the square

        Returns:
            int: The area of the square
        """
        return self.__size ** 2

    def my_print(self):
        """
        Print the square using the '#' character

        The square is printed respecting the position attribute
        If size is 0, an empty line is printed
        """
        if self.__size == 0:
            print()
            return
        for _ in range(self.__position[1]):
            print()

        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
