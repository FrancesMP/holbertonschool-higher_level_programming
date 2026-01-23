#!/usr/bin/python3
"""
Function that prints a text with 2 new lines after each of these
characters: '.', '?', ':'
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each '.', '?', or ':'

    Args:
        text (str): The text to print.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    end_chars = {'.', '?', ':'}
    line = ""

    for char in text:
        line += char
        if char in end_chars:
            print(line.strip())
            print()
            line = ""

    if line:  # print any remaining text
        print(line.strip())
