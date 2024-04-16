#!/usr/bin/python3
"""defines a BaseGeometry class """


class BaseGeometry:
    """a class based on base geometry"""
    def __init__(self):
        """initialization function"""

    def area(self):
        """returns the area of the geometry"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates an integer
        Args:
            name: name of the value
            value: must be an integer
        """
        if type(value) != int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
