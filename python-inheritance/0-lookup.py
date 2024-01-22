#!/usr/bin/python3
"""Returns the available list of attributes and methods of an obj"""
def lookup(obj):
    """
    Function that returns the list of attributes and methods of an obj

    Args:
        obj: Then object you are looking up
    """
    return dir(obj)
