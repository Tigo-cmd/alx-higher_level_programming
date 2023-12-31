#!/usr/bin/python3
"""this module read a text file"""


def read_file(filename=""):
    """this reads and prints to stdout the contents of the file
       Args:
           filename: file to be read and printed
    """
    with open(filename, encoding='utf-8') as file:
        for line in file:
            print(line, end='')
