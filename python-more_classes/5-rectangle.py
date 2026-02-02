#!/usr/bin/python3
"""
Defines a Rectangle class with width and height
"""


class Rectangle:
    """
    Represents a rectangle
    """
    def __init__(self, width=0, height=0):
        """
        Initialize a new Rectangle instance

        Args:
            width (int): Width of the rectangle (default is 0)
            height (int): Height of the rectangle (default is 0)
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Get the width of the rectangle

        Returns:
            int: Width of the rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Set the width of the rectangle

        Args:
            value (int): The new width

        Raises:
            TypeError: If value is not an integer
            ValueError: If value is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Get the height of the rectangle

        Returns:
            int: Height of the rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Set the height of the rectangle

        Args:
            value (int): The new height
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Compute and return the area of the rectangle

        Returns:
            int: Area of the rectangle
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Compute and return the perimeter of the rectangle

        Returns:
            int: Perimeter of the rectangle. If width or height is 0, returns 0
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width + self.__height) * 2

    def __str__(self):
        """
        Return a string representation of the rectangle using '#'

        Returns:
            str: Rectangle as a string of '#' characters
        """
        if self.__width == 0 or self.__height == 0:
            return ""

        return "\n".join("#" * self.__width for _ in range(self.__height))

    def __repr__(self):
        """
        Return an eval()-compatible string representation of the rectangle.

        Returns:
            str: String in the format Rectangle(width, height)
        """
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """
        Print a message when an instance of Rectangle is deleted
        """
        print("Bye rectangle...")
