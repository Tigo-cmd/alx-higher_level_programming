#!/usr/bin/python3
"""rectangle class module"""


class Rectangle:
    """This class defines a rectangle class"""

    def __init__(self, width=0, height=0):
        """ instance method
            Args:
                width: private instance attribute
                height: private instance attribute
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """getter method for width"""
        return self.__width

    @property
    def height(self):
        """getter property for rectangle height"""
        return self.__height

    @width.setter
    def width(self, value):
        """setter property for rectangle width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @height.setter
    def height(self, value):
        """setter property for rectangle height"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__height = value
