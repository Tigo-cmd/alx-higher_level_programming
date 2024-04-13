#!/usr/bin/python3
"""This module implements the addition of two integers"""


def add_integer(a, b=98):
    """

    :param a: first parameter of the function
    :param b: second parameter of the function
    :return: returns the addition of the a and b
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    return a + b
