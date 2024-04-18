#!/usr/bin/python3
"""Defines a CLass Base.py"""


class Base:
    """Base class which handles all functionalities"""
    __nb_objects = 0

    def __init__(self, id=None):
        """initializing function at first call
            Args:
                id: an integer
        """
        if id is not None:
            self.id = id
        else:
            self.__nb_objects += 1
            self.id = self.__nb_objects
