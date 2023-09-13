#!/usr/bin/python3
"""this module writes an Object to a text file, using a JSON representation"""


import json


def save_to_json_file(my_obj, filename):
    """this function writes an Object to a text file, using a JSON representation
       Args:
           my_obj: object to be used
           filename: text file to be written to
       Return:
          nothing
    """
    convert = json.dumps(my_obj)
    with open(filename, 'w') as file:
        file.write(convert)
