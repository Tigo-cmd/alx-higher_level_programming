#!/usr/bin/python3
"""defines a Rectangle class module
   and functions
"""


class Rectangle:
    """a rectangle class that inherits class for 
    functionality
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

    def area(self):
        """Return the area of the rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """Return the print() and str() representation of a Rectangle."""
        string = "[" + str(self.__class__.__name__) + "] "
        string += str(self.__width) + "/" + str(self.__height)
        return string