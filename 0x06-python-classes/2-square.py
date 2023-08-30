#!/usr/bin/python3
"""This module defines a class Square"""


class Square:
    """An empty class that defines a square
    __init__: initializes the constructor
    """

    def __init__(self, size=0):
        """Defines an attribute and initializes the size attribute
        size: size of the square many things depend on it (area computation, etc.)
        """
        self.__size = size
        if not isinstance(size, int):
            raise TypeError("Size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
