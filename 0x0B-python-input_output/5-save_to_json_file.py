#!/usr/bin/python3
"""defines an object to text file using json module"""
import json


def save_to_json_file(my_obj, filename):
    """writes an object to atext file using a Json rep"""
    with open(filename, "w") as f:
        return json.dumps(my_obj, f)
