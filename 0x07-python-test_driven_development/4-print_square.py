#!/usr/bin/python3
"""This module prints a square with the character # """


def print_square(size):
    """
    This fn takes an integer and prints a square
    raises errors if any violations
    Args:
        size: size of the square
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    for row in range(size):
        print("#" * size)
