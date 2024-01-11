#!/usr/bin/python3
"""Defines a class called Square"""


class Square:
    """Attributes of an object known as Square"""
    def __init__(self, size=0):
        """Initailizes Attributes"""
        self.__size = size
        """Conditionals within the class"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """Method for finding the Area"""
        return (self.__size * self.__size)
