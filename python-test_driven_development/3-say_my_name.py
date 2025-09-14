#!/usr/bin/python3

"""
Module for say_my_name function
"""


def say_my_name(first_name, last_name=""):
    """
    say_my_name Function that prints

    Args:
        first_name (_type_): _description_
        last_name (str, optional): _description_. Defaults to "".

    Raises:
        TypeError: _description_
        TypeError: _description_
    """

    if type(first_name) is not str:
        raise TypeError("first_name must be a string")

    if type(last_name) is not str:
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
