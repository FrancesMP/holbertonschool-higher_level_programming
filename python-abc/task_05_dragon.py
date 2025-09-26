#!/usr/bin/python3

"""
Mastering Mixins
"""


class SwimMixin:
    """
    SwimMixin : A mixin class for Swim
    """
    def swim(self):
        print("The creature swims!")


class FlyMixin:
    """
    FlyMixin : A mixin class for Fly
    """
    def fly(self):
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """
    Dragon that inherits brom both SwimMixin and FlyMixin
    """
    def roar(self):
        print("The dragon roars!")
