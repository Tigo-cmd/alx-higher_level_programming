#!/usr/bin/python3
"""this module returns the JSON representation of an object (string)"""


import json


def to_json_string(my_obj):
    """function that returns the JSON representation of an object (string):
       Args:
           my_obj: string to be converted to JSON
       Return:
          JSON representation of an object (string):
    """
    return json.dumps(my_obj)
