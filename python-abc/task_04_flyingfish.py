#!/usr/bin/env python3
"""
FlyingFish example: exploring multiple inheritance in Python.
"""


class Fish:
    """Simple Fish class."""

    def swim(self):
        """Say that the fish is swimming."""
        print("The fish is swimming")

    def habitat(self):
        """Say where the fish lives."""
        print("The fish lives in water")


class Bird:
    """Simple Bird class."""

    def fly(self):
        """Say that the bird is flying."""
        print("The bird is flying")

    def habitat(self):
        """Say where the bird lives."""
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """
    FlyingFish inherits from both Fish and Bird.
    Shows multiple inheritance in action.
    """

    def swim(self):
        """Override swim for flying fish."""
        print("The flying fish is swimming!")

    def fly(self):
        """Override fly for flying fish."""
        print("The flying fish is soaring!")

    def habitat(self):
        """Override habitat for flying fish."""
        print("The flying fish lives both in water and the sky!")
