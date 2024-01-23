#!/usr/bin/python3
"""
Module that opens and reads a file
"""


def read_file(filename=""):
    x = filename
    with open(x) as file:
        print(file.read())
