#!/usr/bin/python3
""" Class Rectangle"""

BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """
    class Rectangle that inherits from BaseGeometry
    """
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """implements the area of the Rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """implements the prints description"""
        return f"[{self.__class__.__name__}] {self.__width}/{self.__height}"
