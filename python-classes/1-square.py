#!/usr/bin/python3
"""
Defines a square class with a private size attribute>
"""


class Square:
    """
    Represents a square
    """
    def __init__(self, size):
        """
        Initializes a square with a given size

        Args:
            size: The size of the square.
        """
        self.__size = size
