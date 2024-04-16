#!/usr/bin/python3
"""defines file appending function module"""


def append_write(filename="", text=""):
    """
    appends a string at the end of a text file
    :param filename:  text file to be appended to
    :param text: text to be appended
    :return: number of characters added
    """
    with open(filename, "a", encoding="utf-8" ) as f:
        return f.write(text)
