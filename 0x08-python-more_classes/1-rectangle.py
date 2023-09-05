#!/usr/bin/python3
"""This module defines rectangle class"""


class Rectangle:
    """This class defines a Rectangle and it's properties
       Args:
            __width: private attribute
            __height: private property for the rectangle
    """

    def __init__(self, width=0, height=0):
        """initial constructor function for the rectangle class"""
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Getter property of the width"""
        return self.__width

    @width.setter
    def width(self, param):
        """setter property for the width which checks"""
        if not isinstance(param, int):
            raise TypeError("width must be an integer")
        elif param < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = param

    @property
    def height(self):
        """Getter property of the height"""
        return self.__height

    @height.setter
    def height(self, param):
        """setter property for the height which checks"""
        if not isinstance(param, int):
            raise TypeError("height must be an integer")
        elif param < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = param
