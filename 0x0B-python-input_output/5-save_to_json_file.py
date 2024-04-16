#!/usr/bin/python3
"""defines an object to text file using json module"""
import json


def save_to_json_file(my_obj, filename):
    """writes an object to a text file using a Json representation"""
    with open(filename, "w") as f:
        json.dump(my_obj, f)
