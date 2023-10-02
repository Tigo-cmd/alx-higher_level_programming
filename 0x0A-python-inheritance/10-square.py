#!/usr/bin/python3
"""Defines a class Square that inherits a Rectangle"""
Square = __import__("9.rectangle").Rectangle


class Square(Square):
    """class Square that inherits a Rectangle"""

    def __init__(self, size):
    """initializes a square
       
       Args:
       size: size of the square
    """
        super().__init__(size, size)
