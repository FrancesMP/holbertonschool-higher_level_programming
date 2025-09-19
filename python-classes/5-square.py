#!/usr/bin/python3

"""
This module contains the definition of class 'Square'
"""


class Square:
    """
    Class to define a square
    """
    def __init__(self, size=0):
        """
        __init__ Construct the instance

        Args:
            size (int, optional): Size of the square. Defaults to 0.

        Raises:
            TypeError: size must be an integer
            ValueError: size must be >= 0
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        area Return the size (area) of the square

        Returns:
            int: size of the square
        """
        return (self.__size * self.__size)

    @property
    def size(self):
        """
        size Get the size of the square

        Returns:
            int: size of the square (edge length)
        """
        return (self.__size)

    @size.setter
    def size(self, value):
        """
        size Define the size of the square

        Args:
            value (int): Size of the square (edge length)

        Raises:
            TypeError: size must be an integer
            ValueError: size must be >= 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        """
        my_print Display the square (with # symbol)
        """
        if self.__size == 0:
            print("")
        else:
            for index in range(0, self.__size):
                for index in range(0, self.__size):
                    print("#", end="")
                print("")
