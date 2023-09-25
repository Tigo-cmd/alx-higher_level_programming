#!/usr/bin/python3
"""This module prints <first name> <last name> passed in"""


def say_my_name(first_name, last_name=""):
    """
    this function prints the firstname and lastname passed
    Args:
        first_name: first name passed
        last_name: last name passed
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
