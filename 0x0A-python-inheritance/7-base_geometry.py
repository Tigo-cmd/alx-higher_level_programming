#!/usr/bin/python3
"""defines a base geometry class"""


class BaseGeometry:
    """a base Geometry class"""

    def area(self):
        """returns the area of the geometry"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates an integer"""
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
