#!/usr/bin/python3
"""this module creates an Object from a “JSON file”:"""


import json


def load_from_json_file(filename):
    """this function  creates an Object from a “JSON file”:
       Args:
           filename: text file to be converted from to "JSON file"
       Return:
          nothing
    """
    with open(filename, 'r') as file:
        convert = json.loads(file.read())
    return convert
