#!/usr/bin/python3
"""
This module defines a class MyList that inherits from the built-in list.
It adds a public method to print the list in ascending sorted order.
"""


class MyList(list):
    """
    MyList class inherits from list and adds
    a method to print a sorted version of the list.
    """

    def print_sorted(self):
        """
        Prints the list in ascending sorted order without
        modifying the original list.
        """
        print(sorted(self))
