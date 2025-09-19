#!/usr/bin/python3

"""
This module contains the definition of class 'Rectangle'
"""


class Rectangle:
    """
     Rectangle : class to define a rectangle by width and height

    Returns:
        Rectangle: A new instance of the Rectangle class
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        __init__ Constructor to build the instance_

        Args:
            width (int, optional): Rectangle width. Defaults to 0.
            height (int, optional): Rectangle high. Defaults to 0.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """
        width Get the width of the rectangle

        Returns:
            int: size of the rectangle (width length)
        """
        return (self.__width)

    @width.setter
    def width(self, value):
        """
        width Define the width of the rectangle

        Args:
            value (int): size of the rectangle (width length)

        Raises:
            TypeError: width must be an integer
            ValueError: width must be >= 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        height Get the height of the rectangle

        Returns:
            int: size of the rectangle (height length)
        """
        return (self.__height)

    @height.setter
    def height(self, value):
        """
        height Define the height of the rectangle

        Args:
            value (int): size of the rectangle (height length)

        Raises:
            TypeError: height must be an integer
            ValueError: height must be >= 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        area Get the area of the rectangle

        Returns:
            int: area of the rectangle
        """
        return (self.__height * self.__width)

    def perimeter(self):
        """
        perimeter Get the perimeter of the rectangle

        Returns:
            int: perimeter of the rectangle
        """

        if self.__height == 0 or self.__width == 0:
            perimeter = 0
        else:
            perimeter = (self.__height * 2) + (self.__width * 2)

        return (perimeter)

    def __str__(self):
        """
        __str__ Returns a human-readable representation of the rectangle.
                Loop through each row and column to construct
                the ASCII output
                Adds a newline (\n) at the end of each row
                except for the last one.
        Returns:
            result: 'Sentence' composed by # and \n
        """
        result = ""
        if self.__height == 0 or self.__width == 0:
            return result
        else:
            for item_y in range(0, self.__height):
                for item_x in range(0, self.__width):
                    result = result + str(self.print_symbol)
                if item_y != (self.__height - 1):
                    result = result + "\n"
            return result

    def __repr__(self):
        """
        __repr__: Return a string representation of the rectangle object
                allowing to be recreated using eval()

        Returns:
            str: A string in the format "Rectangle(width, height)"
        """
        return (f"Rectangle({self.width}, {self.__height})")

    def __del__(self):
        """
        __del__ Method called when a Rectangle instance is deleted
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        bigger_or_equal Compare two rectangle object and
                        return the bigger (area based)

        Args:
            rect_1 (Rectangle): First instance of Rectangle
            rect_2 (Rectangle): Second instance of Rectangle

        Raises:
            TypeError: rect_1 must be an instance of Rectangle
            TypeError: rect_2 must be an instance of Rectangle

        Returns:
            Rectangle: The biggest rectangle (area based)
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        return cls(size, size)
