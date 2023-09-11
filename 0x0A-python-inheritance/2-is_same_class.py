#!/usr/bin/python3
"""a function that returns True if the object is directly a class otherwise False."""


def is_same_class(obj, a_class):
    """returns True of false"""
    return type(obj) is a_class
