#!/usr/bin/python3

"""
    Module with class MyList
"""


class MyList(list):
    """
    MyList class that inherit from list

    Args:
        list (list): list of int
    """
    def print_sorted(self):
        """
        print_sorted sort the list and display the result
        """
        sorted_list = sorted(self)
        print(sorted_list)
