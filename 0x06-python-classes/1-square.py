#!/usr/bin/python3
"""Square Class module"""


class Square:
    """ an empty class Square that defines a square"""
    def __init__(self, size):
        """ constructor for Square method
            Private instance attribute: size
            Instantiation with size (no type/value verification)
        """
        self.__size = size
