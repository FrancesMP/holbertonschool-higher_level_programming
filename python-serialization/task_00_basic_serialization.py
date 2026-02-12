#!/usr/bin/python3

"""
    Module to serialize / deserialize
"""

import json


def serialize_and_save_to_file(data, filename):
    """
    serialize_and_save_to_file

    Args:
        data (dict): dictionnary of data
        filename (string): file name
    """
    with open(filename, "w") as myfile:
        json.dump(data, myfile, indent=4)


def load_and_deserialize(filename):
    """
    load_and_deserialize

    Args:
        filename (string): filename

    Returns:
        dict: dictionnary of data
    """
    with open(filename, "r") as myfile:
        data = json.load(myfile)
    return data
