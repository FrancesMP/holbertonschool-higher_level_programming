#!/usr/bin/python3
"""
    Module class to json
"""


def class_to_json(obj):
    """
    class_to_json

    Args:
        obj (obj): python object

    Returns:
        _dict_: dict format of the object
    """
    return obj.__dict__
