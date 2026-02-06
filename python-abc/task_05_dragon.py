#!/usr/bin/env python3

class SwimMixin:
    """Mixin class that provides swimming capability."""
    
    def swim(self):
        """Method to make the creature swim."""
        print("The creature swims!")


class FlyMixin:
    """Mixin class that provides flying capability."""
    
    def fly(self):
        """Method to make the creature fly."""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """Dragon class that inherits swimming and flying abilities from mixins."""
    
    def roar(self):
        """Dragon's unique ability to roar."""
        print("The dragon roars!")