#!/usr/bin/python3
"""
Module that wites an object to a text file using JSON
"""
import json


def save_to_json_file(my_obj, filename):
    """
    Function that writes an object to a text file using JSON representation

    Args:
        my_obj (object): object to be written to text file
        filename (string): File to be converted
    """
    with open(filename, mode="r") as x:
        return x.write(my_obj)
