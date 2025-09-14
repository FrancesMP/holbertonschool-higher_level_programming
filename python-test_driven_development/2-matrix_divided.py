#!/usr/bin/python3

"""
Module for matrix_divided function
"""


def matrix_divided(matrix, div):
    """
    matrix_divided : Divide a matrix by a number

    Args:
        matrix (list of list): matrix of input number
        div (int): divisor

    Raises:
        Check if the matrix is a matrix
        Check if each row of the matrix have the same size
        Check if div is a int
        Check if div = 0
    """

    list_len = []

    for item in matrix:
        if not type(item) is list:
            raise TypeError("matrix must be a matrix " +
                            "(list of lists) of integers/floats")

        list_len.append(len(item))

        for subitem in item:
            if not (type(subitem) is float or type(subitem) is int):
                raise TypeError("matrix must be a matrix " +
                                "(list of lists) of integers/floats")

    if len(set(list_len)) != 1:
        raise TypeError("Each row of the matrix must have the same size")

    if not (type(div) is float or type(div) is int):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    result_matrix = [item[:] for item in matrix]

    for item in result_matrix:
        for i in range(len(item)):
            item[i] = round(item[i] / div, 2)

    return (result_matrix)
