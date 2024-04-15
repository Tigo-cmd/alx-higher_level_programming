#!/usr/bin/python3
"""a class Module"""


class MyList(list):
    """a class that inherits form list
    Args:
        print_sorted(self): function that prints sorted list
    """
    def print_sorted(self):
        """prints the list, but sorted (ascending sort)"""
        print(sorted(self))
