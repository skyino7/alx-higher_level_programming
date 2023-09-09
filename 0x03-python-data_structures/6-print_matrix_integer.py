#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for mat in row:
            print("{:d}".format(mat), end=" ")
        print(f"")
