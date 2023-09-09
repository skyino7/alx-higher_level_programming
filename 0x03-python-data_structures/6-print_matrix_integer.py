#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for mat in row:
            print("{}".format(mat), end=' ')
        print("")
