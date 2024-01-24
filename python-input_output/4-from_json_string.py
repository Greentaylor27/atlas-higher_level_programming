#!/usr/bin/python3
"""
Modules that converts JSON to Python
"""
import json


def from_json_string(my_str):
    """
    Function that converts JSON to python

    Args:
        my_str (string): String that is to be converted
    """
    return json.loads(my_str)
