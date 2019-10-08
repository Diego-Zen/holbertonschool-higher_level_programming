#!/usr/bin/python3
"""
    Divide a matrix module
"""


def matrix_divided(matrix, div):
    """ divides all elements of a matrix """
    matrix_clone = list()
    if matrix is None:
        raise TypeError("Matrix must be a matrix of integers/floats")
    if div is 0:
        raise ZeroDivisionError("division by zero")
    if len(matrix) > 1:
        if len(matrix[0]) != len(matrix[1]):
            raise TypeError("Each row of the matrix must have the same size")
    for i in matrix:
        matrix_clone.append(list(map((lambda x: test_case(x, div)), i)))
    return matrix_clone


def test_case(x, div):
    """ test type error """
    if type(x) is not int and type(x) is not float:
        raise TypeError("matrix must be a matrix (list of lists) of integers/\
floats")
    else:
        result = round(x / div, 2)
        return result
