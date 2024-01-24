#!/usr/bin/python3
"""
Module to append a file
"""


def append_write(filename="", text=""):
    """
    Function that appends text to a file

    Args:
        filename (str, optional): File you want to append. Defaults to "".
        text (str, optional): text you want to add. Defaults to "".
    """

    with open(filename, mode="a") as x:
        return x.write(text)
