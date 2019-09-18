#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix is not None:
        for i in matrix:
            length = len(i)
            x = 1
            for j in i:
                if x == length:
                    print("{:d}".format(j), end="")
                else:
                    print("{:d}".format(j), end=" ")
                x += 1
            print()
