#!/usr/bin/python3
"""rectangle class module"""


class Rectangle:
    """This class defines a rectangle"""

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
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """RETURNS the area of th rectangle"""
        return self.__height * self.__width

    def perimeter(self):
        """returns the perimeter of the rectangle"""
        if self.__height == 0 or self.__width == 0:
            return 0
        else:
            return 2 * (self.__width + self.__height)
