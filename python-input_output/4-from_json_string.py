#!/usr/bin/python3

"""
Module: from_json_string.py

This module provides functionality to convert JSON strings into Python
objects. It includes one main function:
- from_json_string: Converts a JSON string to a Python object.

This is a custom module that wraps Python's json functionality for
specific use cases.
"""
import json


def from_json_string(my_str):

    """
    Convert a JSON string to a Python object.

    Args:
        my_str (str): The JSON string to convert.

    Returns:
        object: The Python object represented by the JSON string

    Raises:
        ValueError: If the JSON string is not valid
    """
    return json.loads(my_str)
