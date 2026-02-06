#!/usr/bin/python3
"""
This module provides a function to check
if an object is exactly an instance of a given class.
"""


def is_same_class(obj, a_class):
    """
    Check if the object is exactly an instance of the given class.

    Args:
        obj: The object to check.
        a_class: The class to compare with.

    Returns:
        bool: True if obj is exactly an instance of a_class, False otherwise.
    """
    if type(obj) == a_class:
        return True
    return False
