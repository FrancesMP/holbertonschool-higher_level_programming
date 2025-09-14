#!/usr/bin/python3

def square_matrix_simple(matrix=[]):

    new_matrix = []
    for row in matrix:
        new_matrix.append([element * element for element in row])
    return new_matrix
