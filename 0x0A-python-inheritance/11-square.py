#!/usr/bin/python3
"""this module inherits for the rectangle module"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """a rectangle class that inherits from Rectangle"""

    def __init__(self, size):
        """initializing function at first call
        Args:
            size: width of the square
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Return the area of the square."""
        return self.__size * self.__size
    
    def __str__(self):
        """Return the print() and str() representation of a Square class."""
        string = "[" + str(self.__class__.__name__) + "] "
        string += str(self.__size) + "/" + str(self.__size)
        return string
