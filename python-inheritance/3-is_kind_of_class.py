#!/usr/bin/python3
"""
This module provides a function to check
if an object is an instance of a class or a subclass.
"""


def is_kind_of_class(obj, a_class):
    """
    Check if the object is an instance of the given class
    or a subclass of it.

    Args:
        obj: The object to check.
        a_class: The class to compare with.

    Returns:
        bool: True if obj is an instance of a_class
        or inherits from it, False otherwise.
    """
    if isinstance(obj, a_class):
        return True
    return False
