#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for i in range(0, len(matrix)):
        res = list(map(lambda x: x*x, matrix[i]))
        new_matrix.append(res)
    return new_matrix
