#!/usr/bin/python3
"""
Module that creates a file if it doesn't exsist\
Appends a file if it has already been created
"""


def write_file(filename="", text=""):
    """
    Function that overwrites a file if it already exsists\
    or creates a new file if there is none

    Args:
        filename (str, optional): File that you are tying to open.\
            Defaults to "".
        text (str, optional): What you want written down. Defaults to "".
    """
    x = filename
    with open(x, "w") as file:
        return file.write(text)
