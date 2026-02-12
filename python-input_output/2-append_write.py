#!/usr/bin/python3

"""
Module to append a string to a text file and returns
the number of characters appended.
"""


def append_write(filename="", text=""):

    """
    Appends a string to a text file and returns
    the number of characters appended.

    Args:
        filename (str): The name of the file to append to
            (default is an empty string)
        text (str): The string to append to the file
            (default is an empty string)

    Returns:
        int: The number of characters appended to the file
    """

    with open(filename, "a", encoding='utf-8') as filename:
        filename.write(text)
        return len(text)