#!/usr/bin/python3
"""Square class module"""


class Square:
    """ an empty class Square that defines a square"""
    def __init__(self, size=0):
        """ constructor for Square method
            Private instance attribute: size
            Args:
                size (int) : private instance attribute
        """
        self.__size = size

    @property
    def size(self):
        """getter property for size attribute"""
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """returns the current square area
           Args:
               size: private instance attribute
        """
        return self.__size ** 2
