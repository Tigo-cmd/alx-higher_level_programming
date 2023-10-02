#!/usr/bin/python3
"""Defines a square class that inherits from Rectangle"""
Square = __import__("9-rectangle").Rectangle


class Square(Square):
    """implements  a square"""

    def __init__(self, size):
        """Initialisez a square

        Args:
        size: size of square
        """
        super().__init__(size, size)
