#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    matrix_clone = []
    for i in matrix:
        matrix_clone.append(list(map((lambda x: x ** 2), i)))
    print(matrix_clone)
