#!/usr/bin/python3
"""defines a base geometry class depending on 6-base_geometry"""


class BaseGeometry:
    """a base Geometry class"""

    def __init__(self):
        """initializing function at first call
        """

    def area(self):
        """returns the area of the geometry"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates an integer"""
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
