#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix is None:
        return
    for row in matrix:
        for col in row:
            print(f"{col:d}", end=" ")
        print()
