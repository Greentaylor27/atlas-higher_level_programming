#!/usr/bin/python3
"""Define a class called Square"""


class Square:
    """Attributes of an object know as Square"""
    def __init__(self, size=0):
        """Initalizes Attributes"""
        self.__size = size
        """Conditionals within the class"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
