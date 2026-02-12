#!/usr/bin/python3

"""
    Returns a list of lists of integers representing the Pascals triangle of n:
"""


def pascal_triangle(n):
    """
    pascal_triangle

    Build the next row of Pascal's triangle
    1. Start with 1
    2. Compute values as the sum of adjacent elements in current_list
    3. End with 1
    4. Update current_list and append new_list to pascal_list

    Args:
        n (int): iteration on pascal triangle

    Returns:
        list: list of lists of integers
    """

    # Define variable
    pascal_list = []
    current_list = []
    new_list = []

    # Check sepcial case
    if n <= 0:
        return pascal_list

    # Loop on triangle, (two first case are special case)
    for index in range(n):
        if index == 0:
            pascal_list.append([1])

        elif index == 1:
            pascal_list.append([1, 1])
            current_list.extend([1, 1])

        else:
            new_list = []
            new_list.append(1)

            for sub_index in range(len(current_list) - 1):
                value = current_list[sub_index] + current_list[sub_index+1]

                new_list.append(value)

            new_list.append(1)
            current_list = new_list
            pascal_list.append(new_list)

    return pascal_list
