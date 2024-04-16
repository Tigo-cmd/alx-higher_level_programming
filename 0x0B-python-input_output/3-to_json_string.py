#!/usr/bin/python3
"""json manipulation function module"""
import json


def to_json_string(my_obj):
    """
    handles JSON representation of an object(string)
    :param my_obj: str to be converted to json
    :return: converted object as JSON
    """
    return json.dumps(my_obj)
