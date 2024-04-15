#!/usr/bin/python3
"""defines a Rectangle class module and functions"""


class Rectangle:
    """a rectangle class that inherits from BaseGeometry class
    """

    def __init__(self, width, height):
        """initializing function at first call
        Args:
            width: width of the rectangle
            height: height of the rectangle
        """
        super().__init__()
        self.__width = width
        self.__height = height
