#!/usr/bin/env python3
"""
Just a small demo with abstract classes and inheritance.
We make animals, and each one knows how to make its own sound.
"""

from abc import ABC, abstractmethod


class Animal(ABC):
    """
    Abstract base class for all animals.
    Every animal must be able to make a sound.
    """

    @abstractmethod
    def sound(self):
        """Return the sound of the animal (must be implemented)."""
        pass


class Dog(Animal):
    """Dog class, inherits from Animal."""

    def sound(self):
        """Return the sound a dog makes."""
        return "Bark"


class Cat(Animal):
    """Cat class, inherits from Animal."""

    def sound(self):
        """Return the sound a cat makes."""
        return "Meow"
