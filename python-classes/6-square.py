#!/usr/bin/python3

"""
This module contains the definition of class 'Square'
"""


class Square:
    """
    Class to define a square
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        __init__ Construct the instance

        Args:
            size (int, optional): Size of the square. Defaults to 0.
            position (tuple, optional): Start position of the square.
                                        Defaults to (0, 0).

        Raises:
            TypeError: size must be an integer
            ValueError: size must be >= 0
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        self.position = position

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
            for emptyline in range(0, self.__position[1]):
                print("")
            for index1 in range(0, self.__size):
                for space in range(0, self.__position[0]):
                    print(" ", end="")
                for index2 in range(0, self.__size):
                    print("#", end="")
                print("")

    @property
    def position(self):
        """
        position Get the start position of the square by X, Y value

        Returns:
            tuple: coordinates of the square (X,Y)
        """
        return (self.__position)

    @position.setter
    def position(self, value):
        """
        position Define the start position of the square by X, Y value

        Args:
            value (tuple): coordinates of the square (X,Y)

        Raises:
            TypeError: position must be a tuple of 2 positive integers
        """
        error_msg = "position must be a tuple of 2 positive integers"
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError(error_msg)

        for number in value:
            if not isinstance(number, int):
                raise TypeError(error_msg)
            if number < 0:
                raise TypeError(error_msg)

        self.__position = value
