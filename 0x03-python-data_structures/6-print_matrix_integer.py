#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix is None:
        for x in range(len(matrix)):
            for y in range(len(matrix[x])):
                print("{:d}".format(matrix[x][y]), end="")
            print()
