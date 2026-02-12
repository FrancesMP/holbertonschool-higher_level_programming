#!/usr/bin/python3

"""
Module to write a string to a text file and returns
the number of characters written.
"""


def write_file(filename="", text=""):
    """
    Writes a string to a text file (UTF8) and returns
    the number of characters written.
    Uses the with statement for file handling.
    Opens the file in write mode ('w'), overwriting
    existing content.

    Args:
        filename (str): The name of the file to write to
            (default is an empty string)
        text (str): The string to write to the file
            (default is an empty string)

    Returns:
        int: The number of characters written to the file
    """
    with open(filename, "w", encoding='utf-8') as filename:
        filename.write(text)
        return len(text)
