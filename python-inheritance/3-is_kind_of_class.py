#!/usr/bin/python3
"""Fuction that checks if an object is an instance of/inherits from obj"""


def is_kind_of_class(obj, a_class):
    """Checks if an object is an instance of/inherits from obj

    Args:
        obj (object): first object to compare
        a_class (object): second object to compare
    """
    return isinstance(obj, a_class)
