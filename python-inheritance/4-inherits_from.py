#!/usr/bin/python3
"""Function that checks if a class is inherited from an object"""


def inherits_from(obj, a_class):
    """Checks if obj has been

    Args:
        obj (object): obj to check
        a_class (class): class to check from
    """
    return (issubclass(type(obj), a_class) and type(obj) is not a_class)
