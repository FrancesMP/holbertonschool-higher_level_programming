#!/usr/bin/env python3
"""
Quick example with abstract classes for shapes.
We define a generic shape, then make Circle and Rectangle.
Each one can calculate its area and perimeter.
"""

import math
from abc import ABC, abstractmethod


class Shape(ABC):
    """
    Abstract base class for all shapes.
    Every shape must be able to give area and perimeter.
    """

    @abstractmethod
    def area(self):
        """Return the area of the shape."""
        pass

    @abstractmethod
    def perimeter(self):
        """Return the perimeter of the shape."""
        pass


class Circle(Shape):
    """Circle shape, defined by its radius."""

    def __init__(self, radius):
        """Create a circle with a given radius."""
        self.radius = radius

    def area(self):
        """Return the area of the circle."""
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        """Return the perimeter (circumference) of the circle."""
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """Rectangle shape, defined by width and height."""

    def __init__(self, width, height):
        """Create a rectangle with width and height."""
        self.width = width
        self.height = height

    def area(self):
        """Return the area of the rectangle."""
        return self.width * self.height

    def perimeter(self):
        """Return the perimeter of the rectangle."""
        return 2 * (self.width + self.height)


def shape_info(shape):
    """
    Print out the area and perimeter of any shape.
    Works with any object that implements Shape.
    """
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")
