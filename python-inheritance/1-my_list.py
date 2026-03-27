#!/usr/bin/python3
"""Task 1 : My List """
class MyList(list):
    """Create the class"""
    def print_sorted(self):
        """ Function that print a list of the instances of a given class """
        sort_list = sorted(self)
        print(sort_list)
        