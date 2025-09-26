#!/usr/bin/python3
"""
This module defines a custom list class.
"""


class MyList(list):
    """
    A custom list class that extends the built-in list.
    """

    def print_sorted(self):
        """
        Print the list elements in sorted order.
        """
        print(sorted(self))
