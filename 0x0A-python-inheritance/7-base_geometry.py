#!/usr/bin/python3
"""class BaseGeometry."""


class BaseGeometry:
    """implements the base geometry"""
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates integers and raises Exception if failed """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater then 0")
