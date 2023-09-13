#!/usr/bin/python3
"""this module writes a string to a text file (UTF8)
   and returns the number of characters written:
"""


def write_file(filename="", text=""):
    """function that writes a string to a text file (UTF8)
       and returns the number of characters written
       Args:
           filename: file to be read and writing to
           text: string to be writing to filename
       Return:
           no of characters printed
    """
    with open(filename, 'w', encoding="utf-8") as file:
        main = file.write(text)
    return main
