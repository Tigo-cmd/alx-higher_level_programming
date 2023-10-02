#!/usr/bin/python3
"""Defines a Square class that inherits a Rectangle"""
Square = __import__("9.rectangle").Rectangle


class Square(Square):
    """implements the square class"""

    def __init__(self, size):
        """initializes a square
	       
	Args:
	size: size of the square
	"""
        super().__init__(size, size)

