#!/usr/bin/python3
"""defines a Rectangle class module for functionality
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle:
    """a rectangle class that inherits from BaseGeometry class
       documentation errors alert
    """

    def __init__(self, width, height):
        """initializing function at first call of class
        Args:
            width: width of the rectangle
            height: height of the rectangle
        """
        super().__init__()
        self.integer_validator("width", width):
        self.__width = width
        self.integer_validator("height", height):
        self.__height = height
