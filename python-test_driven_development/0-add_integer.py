#!/usr/bin/python3

"""
Module for basic calculation (add).
"""


def add_integer(a, b=98):
    """
    add_integer : Function that adds 2 integers

    Args:
        a (int): first integer
        b (int, optional): second integer. Defaults to 98.


    """

    if a == float('inf') or a == float('-inf'):
        raise OverflowError()

    if b == float('inf') or b == float('-inf'):
        raise OverflowError()

    if isinstance(a, float):
        a = int(a)

    if isinstance(b, float):
        b = int(b)

    if not isinstance(a, int):
        raise TypeError("a must be an integer")

    if not isinstance(b, int):
        raise TypeError("b must be an integer")

    result = a + b

    return result
