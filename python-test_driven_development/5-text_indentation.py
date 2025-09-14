#!/usr/bin/python3

"""
Module for print_square function
"""


def text_indentation(text):
    """
    prints a square with the character #.

    Args:
        size (int): size of the square

    """

    if type(text) is not str:
        raise TypeError("text must be a string")

    charac_list = (".", "?", ":")

    index = 0

    while index < len(text):
        print(text[index], end="")
        if text[index] in charac_list:
            print("\n")

            while text[index + 1] == " ":
                index += 1

        index += 1
