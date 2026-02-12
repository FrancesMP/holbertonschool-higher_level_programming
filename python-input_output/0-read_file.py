#!/usr/bin/python3

"""
    Module to read file
"""


def read_file(filename=""):
    """
    Reads a text file (UTF8) and prints it to stdout.
    Uses the with statement for file handling.
    Does not handle file permission or file doesn't exist exceptions.

    Args:
    filename -- the name of the file to read (default is an empty string)
    """
    with open(filename, 'r', encoding='utf-8') as file:
        print(file.read(), end="")
