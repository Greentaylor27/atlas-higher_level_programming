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
    # Variable to be returned later
    result = int(a) + int(b)
    # Conditionals for the function to make sure
    # all inputs are ints/float
    if not isinstance(a, int):
        raise TypeError("a must be an integer")
    if not isinstance(b, int):
        raise TypeError("b must be an integer")
    if result == float('inf'):
        raise OverflowError("Float overflow occured")
    # If the function passes then it should return the sum
    return (result)
