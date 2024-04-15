#!/usr/bin/python3
"""defines an instance checking function"""


def is_same_class(obj, a_class):
    """
    a function that returns True if the object is exactly
    an instance of the specified class ; otherwise False.
    :param obj: object to be checked
    :param a_class: a class
    :return: True if object is an instance else false
    """
    if type(obj) != a_class:
        return False
    return True
