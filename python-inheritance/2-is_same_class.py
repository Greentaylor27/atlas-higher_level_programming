#!/usr/bin/python3
"""Function that checks if two classes are the same"""


def is_same_class(obj, a_class):
    """Checks if two classes are the same instance

    Args:
        obj (class): First obj created
        a_class (class): Second obj created
    """
    
    
    if id(obj) == id(a_class):
        return True
    else:
        return False
