#!/usr/bin/python3
"""defines a function that reads a text fil module"""


def read_file(filename=""):
    """
    reads a text file (UTF8) and prints to stdout
    :param filename: file to be read
    :return: nothing
    """
    with open(filename, encoding='utf-8') as tigo:
        """reads the files and automatically closes it"""
        print(tigo.read())