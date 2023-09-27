#!/usr/bin/python3
"""This is the base class all clases inherits frorm here"""


class Base:
    """This is the base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """this is the default constructor for the base class"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
