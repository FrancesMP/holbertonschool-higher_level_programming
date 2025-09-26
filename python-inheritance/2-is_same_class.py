#!/usr/bin/python3

"""
    Module for is_same_class
"""


def is_same_class(obj, a_class):
    """
    is_same_class:
        Check if an object is extactly and instance
        of the specified class

    Args:
        obj (): object to check
        a_class (class): class to check

    Returns:
        boolean: True or false
    """
    if type(obj) is a_class:
        return (isinstance(obj, a_class))
    else:
        return False
