#!/usr/bin/python3
"""
Defines a Rectangle class with width and height
"""


class Rectangle:
    """
    Represents a rectangle, instance counting, and print symbol
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Initialize a new Rectangle instance

        Args:
            width (int): Width of the rectangle (default is 0)
            height (int): Height of the rectangle (default is 0)
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
            str: Rectangle drawn with `print_symbol` or
            empty string if width or height is 0
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        symbol = str(self.print_symbol) * self.__width

        return "\n".join([symbol for _ in range(self.__height)])

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
        and decrement the counter
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Return the rectangle with the bigger or equal area"""
        for i, rect in enumerate((rect_1, rect_2), start=1):
            if not isinstance(rect, Rectangle):
                raise TypeError(f"rect_{i} must be an instance of Rectangle")

        return rect_1 if rect_1.area() >= rect_2.area() else rect_2

    @classmethod
    def square(cls, size=0):
        """Return a new Rectangle instance with width == height == size."""
        return cls(size, size)
