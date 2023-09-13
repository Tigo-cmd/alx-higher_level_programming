#!/usr/bin/python3
"""this module returns an object (Python data structure)
represented by a JSON string
"""


import json


def from_json_string(my_str):
    """function  returns an object (Python data structure)
       represented by a JSON string
       Args:
           my_str: string to be converted to PDS
       Return:
          (Python data structure) represented by a JSON string
    """
    return json.loads(my_str)
