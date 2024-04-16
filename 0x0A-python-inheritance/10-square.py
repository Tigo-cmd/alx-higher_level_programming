#!/usr/bin/python3
"""defines a Square class module for functions"""
Rectangle = __import__(9-rectangle.py).Rectangle


class Square(Rectangle):
    """a rectangle class that inherits from Rectangle
     class
     """

    def __init__(self, size):
        """initializing function at first call
        Args:
            size: width of the square
        """
        super().__init__()
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """Return the area of the square."""
        return self.__size * self.__size
