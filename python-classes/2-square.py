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
