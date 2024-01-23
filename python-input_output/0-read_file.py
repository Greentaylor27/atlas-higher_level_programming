#!/usr/bin/python3
"""
Module that opens and reads a file
"""


def read_file(filename=""):
    """
    Function that opens and reads a file

    Args:
        filename (str, optional): File name of the file you want open and read.\
            Defaults to "".
    """
    x = filename
    with open(x) as file:
        print(file.read(), end="")
