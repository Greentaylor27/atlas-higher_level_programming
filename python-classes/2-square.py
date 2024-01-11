#!/usr/bin/python3
"""Define a class called Square"""


class Square:
    """Attributes of an object know as Square"""
    def __init__(self, size):
        """Conditionals within the class"""
        if not isinstance(size, str):
            raise TypeError("Size must be an integer")
        if size < 0:
            raise ValueError("Size must be >= 0")
        """Initalizes Attributes"""
        self.__size = size
