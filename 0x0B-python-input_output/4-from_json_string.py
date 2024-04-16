#!/usr/bin/python3
"""json manipulation fxn module"""
import json


def from_json_string(my_str):
    """
    handles an object (Python data structure) represented by a JSON string:
    :param my_str: jSON string
    :return: an object (Python data structure) represented by a JSON string:
    """
    return json.loads(my_str)
