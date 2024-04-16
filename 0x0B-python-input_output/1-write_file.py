#!/usr/bin/python3
"""file writing function module"""


def write_file(filename="", text=""):
    """
     writes a string to a text file (UTF8) and return as thus
    :param filename: file to be written to
    :param text: the string to be written
    :return: the number of characters written
    """
    with open(filename, "w", encoding='utf-8') as f:
        f.write(text)
