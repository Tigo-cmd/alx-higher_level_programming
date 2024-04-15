#!/usr/bin/python3
"""defines a inherited class checking module"""


def inherits_from(obj, a_class):
    """a function that returns True if the object is an instance of
     a class that inherited (directly or indirectly) from the specified class ; otherwise False.
    :param obj: object to be checked
    :param a_class:the class
    :return: True if meets requirements else False
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
