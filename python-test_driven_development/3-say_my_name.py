#!/usr/bin/python3
"""
Function that prints Who people are
"""


def say_my_name(first_name, last_name=""):
    """
    Prints a greeting to someone

    Args:
        first_name (str): A persons first name
        last_name (str, optional): A persons last name. Defaults to "".

    Raises:
        TypeError: first_name must be a string
        TypeError: last_name must be a string
    """
    # Conditionals for errors
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    # String cat and print
    full_name = first_name + " " + last_name
    print(full_name)
