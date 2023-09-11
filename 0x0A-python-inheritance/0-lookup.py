#!/usr/bin/python3
"""this module the list of available attributes and methods of an object"""


def lookup(obj):
    """
        Returns a list of available attributes and methods of an object
        Args:
            obj:  retrieve attributes and methods from here
        Returns:
            list: list of attribute and methods
        """
    new_list = []
    for i in dir(obj):
        new_list.append(i)
    return new_list
