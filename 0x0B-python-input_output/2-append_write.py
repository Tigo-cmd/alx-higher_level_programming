#!/usr/bin/python3
"""this module appends  a string to a text file (UTF8)
   and returns the number of characters added:
"""


def append_write(filename="", text=""):
    """function that appends a string to a text file (UTF8)
       and returns the number of characters added
       Args:
           filename: file to be appended and written to
           text: string to be appended to filename
       Return:
           no of characters added
    """
    with open(filename, 'a', encoding="utf-8") as file:
        main = file.write(text)
    return main
