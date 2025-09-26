#!/usr/bin/python3

"""
Abstract animal class and its subclasses
"""

from abc import ABC, abstractmethod


class Animal(ABC):
    """
    Animal Parent class to generate animal subclass

    Args:
        ABC (_type_): Abstract
    """
    @abstractmethod
    def sound(self):
        """
        sound Empty (build the abstract)
        """
        pass


class Dog(Animal):
    """
    Dog Class for Dog object

    Args:
        Animal (object): inherit from Animal
    """
    def sound(self):
        """
        sound Function to know the sound of the animal

        Returns:
            string: Bark
        """
        return ("Bark")


class Cat(Animal):
    """
    Cat Class for Cat object

    Args:
        Animal (object): inherit from Animal
    """
    def sound(self):
        """
        sound Function to know the sound of the animal

        Returns:
            string: Meow
        """
        return ("Meow")
