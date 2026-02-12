#!/usr/bin/python3

"""
    Module that creates an Object from a “JSON file”:
"""

import json


def load_from_json_file(filename):
    """
    load_from_json_file

    Args:
        filename (string): filename

    Returns:
        obj: python object load from a json file
    """
    with open(filename, "r", encoding="utf-8") as myfile:
        python_object = json.load(myfile)
        return python_object
