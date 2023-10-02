#!/usr/bin/python3
"""defines a Class Square that inherits from Rectangle"""
Square = __import__("9.rectangle").Rectangle


class Square(Square):
    """class Square that inherits from Rectangle"""

    def __init__(self, size):
    """initializes a square
       
       Args:
       size: size of the square
    """
        super().__init__(size, size)
