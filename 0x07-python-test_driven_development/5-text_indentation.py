#!/usr/bin/python3
"""This module adds indentation at specified characters"""


def text_indentation(text):
    """
    this function adds  2 new lines after each of these characters: ., ? and :
    Args:
        text: a string to checked for certain characters
    raises:
        TypeError: if text is not a string
    """
    marks = ['.', '?', ':']
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    j = 0
    while j < len(text) and text[j] == " ":
        j += 1
    while j < len(text):
        if text[j] in marks:
            print(text[j])
            print()
            j += 1
            while j < len(text) and text[j] == ' ':
                j += 1
        else:
            print(text[j], end='')
            j += 1
