#!/usr/bin/python3
"""
This module provides a function to list all attributes
and methods of a given object.
"""


def lookup(obj):
    """
    Return the list of attributes and methods of the object.

    Args:
        obj: The object to inspect.

    Returns:
        list: A list containing names of attributes and methods.
    """
    return dir(obj)
