#!/usr/bin/python3

"""
Module: 5-save_to_json_file

This module provides a function to save a Python object to a JSON file.
It uses the standard json module for serialization and handles file
operations with proper resource management.
"""

import json


def save_to_json_file(my_obj, filename):
    """
    Serialize a Python object to a JSON file.

    Args:
        my_obj: The Python object to be serialized to JSON.
        filename (str): The name of the file where the JSON
            representation will be saved.

    Note:
        - The function will create the file if it doesn't exist.
        - If the file exists, it will be overwritten.
        - Uses UTF-8 encoding for the output file.

    Example:
        >>> save_to_json_file({"key": "value"}, "output.json")
    """
    with open(filename, "w", encoding='utf-8') as write:
        json.dump(my_obj, write)
