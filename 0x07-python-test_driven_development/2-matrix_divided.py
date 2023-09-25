#!/usr/bin/python3
"""This module implements the divison of the elements of a matrix"""


def matrix_divided(matrix, div):
    """
    this function divides the elements of a matrix
    and returns a new matrix it declares two different lists,
    iterates through each rows of the matrix divides the element
    of each rows by div and appends to the list and finally appends
    to the main list
    :param matrix: list of lists to be divided elements(dividend)
    :param div: divisor
    :return: returns a new list wit the quotient
    """
    if len(matrix[0]) != len(matrix[1]):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int,float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    for i in matrix:
        for j in i:
            if not isinstance(j, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    result = [[round(i/div, 2) for i in row] for row in matrix]
    return result
