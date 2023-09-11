#!/usr/bin/python3
"""this module the list of available attributes and methods of an object"""


def lookup(obj):
    """this module the list of available attributes and methods of an object"""
    new_list = []
    for i in dir(obj):
        if i == '__init_subclass__':
            continue
        new_list.append(i)
    return new_list
