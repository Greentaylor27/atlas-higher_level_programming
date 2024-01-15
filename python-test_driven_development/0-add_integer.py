#!/usr/bin/python3
"""
Function that adds two integers or floats together and returns sum
"""


def add_integer(a, b=98):
    """
    Adds two numbers together and returns the Sum.
    Both numbers must be integers or float

    Args:
        a (int, float): first int/float to be used
        b (int, float): second int/float to be used

    Raises:
        TypeError: a is not an integer
        TypeError: b is not an integer

    Returns:
        int: Sum of two floats or ints
    """
    if isinstance(a, float):
        a = int(a)
    elif not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    else:
        pass
    if isinstance(b, float):
        b = int(b)
    elif not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    else:
        pass
    result = a + b
    return result
