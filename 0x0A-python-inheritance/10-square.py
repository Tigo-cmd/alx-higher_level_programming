#!/usr/bin/python3
"""defines a Square class module"""


class Square(Rectangle):
    """a rectangle class that inherits from Rectangle class"""

    def __init__(self, size):
        """initializing function at first call
        Args:
            size: width of the square
        """
        super().__init__()
        self.__size = size

    def area(self):
        """Return the area of the square."""
        return self.__size * self.__size