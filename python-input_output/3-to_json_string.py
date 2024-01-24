#!/usr/bin/python3
"""
Module that returns the JSON representation of an onject
"""
import json


def to_json_string(my_obj):
    """
    Function that returns the JSON representation of an object

    Args:
        my_obj (object): Object you want the JSON representation of
    """
    return json.dumps(my_obj)
