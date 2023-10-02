#!/usr/bin/python3
"""class Square that inherits from Rectangle"""
Rectangle = __import__("9.rectangle").Rectangle


class Square(Rectangle):
    """class Square that inherits from Rectangle"""

    def __init__(self, size):
    """init a square"""
        super().__init__(size, size)
