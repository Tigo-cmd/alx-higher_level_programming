#!/usr/bin/python3
"""an instance checking function module"""


def is_kind_of_class(obj, a_class):
    """
    checks if an object is an instance of, or if the objects is
    an instance of a class it inherited from, the specified class
    else, false
    :param obj: object to be checked
    :param a_class: the class tobe checked form
    :return: True if meets requirements else false
    """
    if not isinstance(obj, a_class):
        return False
    return True
