#!/usr/bin/python3
"""Function that returns the available list of attributes and methods of an object"""
def lookup(obj):
    """
    Function that returns the list of attributes and methods of an obj

    Args:
        obj: Then object you are looking up
    """
    return dir(obj)
