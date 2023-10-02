#!/usr/bin/python3
"""Defines a child square class: inherits from Rectangle"""
Square1 = __import__("9-rectangle").Rectangle


class Square(Square1):
    """Represents a square"""

    def __init__(self, size):
        """Initialisez a square

        Args:
        size (int): size of square
        """
        super().__init__(size, size)
