#!/usr/bin/python3

"""
Write a function that computes the square value
of all integers of a matrix.
"""


def square_matrix_simple(matrix=[]):
    res = []

    for row in matrix:
        row_res = []
        for elem in row:
            if isinstance(elem, int):
                row_res.append(elem ** 2)
            else:
                row_res.append(elem)
        res.append(row_res)
    return res
