#!/usr/bin/python3
"""
Module that loads from a JSON to txt file
"""
import json


def load_from_json_file(filename):
    """
    Function that loads a JSON file to text

    Args:
        filename (string): file you are trying to open
    """
    with open(filename) as x:
        data = x.read()
        return json.loads(data)
