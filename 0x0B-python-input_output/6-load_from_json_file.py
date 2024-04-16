#!/usr/bin/python3
"""defines json manipulation module"""
import json


def load_from_json_file(filename):
    """creates an Object from a “JSON file
       obj: object
       filename: name of the file
    ”"""
    with open(filename, "r") as f:
        return json.load(f)
