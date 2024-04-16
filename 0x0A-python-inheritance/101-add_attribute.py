#!/usr/bin/python3
"""this defines an attribute adder function"""


def add_attribute(a_class, name, value):
    """adds attribute to a class object
       Args:
           a_class = class object
           name = attribute of the class to be set
           value = param of the name attribute
    """
    if hasattr(a_class, '__dict__'):
        setattr(a_class, name, value)
    else:
        raise TypeError("can't add new attributes")
