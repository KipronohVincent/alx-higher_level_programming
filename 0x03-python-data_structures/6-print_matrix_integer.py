#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    """Print a matrix of integers."""
    for x in range(len(matrix)):
        for y in range(len(matrix[x])):
            print("{:d}".format(matrix[x][y]), end="")
            if y != (len(matrix[x]) - 1):
                print(" ", end="")

    print("")
