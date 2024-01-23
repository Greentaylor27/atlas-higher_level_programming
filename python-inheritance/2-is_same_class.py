#!/usr/bin/python3
"""Function that checks if two classes are the same"""


def is_same_class(obj, a_class):
    """Checks if two classes are the same instance

    Args:
        obj (class): First obj created
        a_class (class): Second obj created
    """
    return type(obj) is a_class
