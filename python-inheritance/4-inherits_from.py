#!/usr/bin/python3
"""
This module provides a function to check
if an object inherits from a specified class.
"""


def inherits_from(obj, a_class):
    """
    Check if the object is an instance of a class
    that inherits (directly or indirectly) from a_class.

    Args:
        obj: The object to check.
        a_class: The class to compare with.

    Returns:
        bool: True if obj inherits from a_class,
        False otherwise.
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
