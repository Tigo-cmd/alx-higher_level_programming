#!/usr/bin/python3
"""MyList class Module"""


class MyList(list):
    """a class that inherits form list"""
    def __init__(self):
        """this initislizes the object"""
        super().__init__()

    def print_sorted(self):
        """prints the list, but sorted (ascending sort)"""
        print(sorted(self))
