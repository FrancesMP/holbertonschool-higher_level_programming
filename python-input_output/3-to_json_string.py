#!/usr/bin/python3

import json

__doc__ = """
Module: to_json_string.py

This module provides a utility function to convert Python objects into JSON
string representations using Python's built-in json module. It includes one main function:
- to_json_string: Converts a Python object to a JSON string

This is a custom module that wraps Python's json functionality for specific use cases.
"""


def to_json_string(my_obj):
    """
    Convert a Python object to a JSON string representation.

    Args:
        my_obj: The Python object to convert to JSON
            representation.

    Returns:
        str: A JSON string representation of the object.

    Raises:
        TypeError: If the object cannot be serialized to JSON.
    """
    return json.dumps(my_obj)
