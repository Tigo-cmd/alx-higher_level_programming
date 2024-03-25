#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new = []
    for i in matrix:
        new.append([pow(i[j], 2) for j in range(3)])
    return new
