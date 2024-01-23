#!/usr/bin/python3
"""Function that checks if a class is inherited from an object"""


def inhreits_from(obj, a_class):
    """Checks if obj has been 

    Args:
        obj (object): obj to check
        a_class (class): class to check from
    """
    return (issubclass(obj, a_class))
