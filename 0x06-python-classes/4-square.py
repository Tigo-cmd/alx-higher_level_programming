#!/usr/bin/python3
"""This module defines a class"""


class Square:
    """An empty class that defines a square
    __init__: initializes the constructor
    """

    def __init__(self, size=0):
        """Defines an attribute and initializes the size attribute
        size: size of the square many things depend on it (area computation, etc.)
        """
        self.__size = size

    @property
    def size(self):
        """Getter function for size this sets the size variable"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter function for Size which initializes the size to value"""
        if not isinstance(value, int):
            raise TypeError("Size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Public attribute that returns the current square area"""
        return self.__size ** 2
