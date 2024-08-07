#!/usr/bin/python3
"""Square class module"""


class Square:
    """ an empty class Square that defines a square"""
    def __init__(self, size=0):
        """ constructor for Square method
            Private instance attribute: size
            Args:
                size: private instance attribute
            Instantiation with optional size: def __init__(self, size=0):
            size must be an integer, otherwise raise
            a TypeError exception with the message size must be an integer
            if size is less than 0, raise a ValueError
            exception with the message size must be >= 0
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """returns the current square area
           Args:
               size: private instance attribute
        """
        return self.__size ** 2
