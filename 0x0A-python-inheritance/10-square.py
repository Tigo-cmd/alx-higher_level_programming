#!/usr/bin/python3
"""class Square that inherits from Rectangle"""

Square1 = __import__("9.rectangle").Rectangle


class Square(Square1):
    """class Square that inherits from Rectangle"""

    def __init__(self, size):
    """initializes a square"""
        super().__init__(size, size)
