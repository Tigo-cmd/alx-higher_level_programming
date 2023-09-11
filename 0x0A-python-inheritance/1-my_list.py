#!/usr/bin/python3
""" a class MyList that inherits from list"""


class MyList(list):
    """returns the list in sorted order"""
    def print_sorted(self):
        """prints the sorted list"""
        print(sorted(self))
