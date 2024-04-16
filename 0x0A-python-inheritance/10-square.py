#!/usr/bin/python3
"""defines a Square class module for functions"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """a rectangle class that inherits from Rectangle
     class
     """

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
