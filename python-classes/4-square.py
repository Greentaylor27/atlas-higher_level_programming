#!/usr/bin/python3
"""Attributes of an object known as Square"""


class Square:
    """Attributes of an object know as Square"""
    def __init__(self, size=0):
        """Intializes Attributes"""
        self.__size = size
        """Conditionals with the class"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        
    def area(self):
        """Method for finding the area of this class"""
        return (self.__size * self.__size)
    
    @property
    def size(self):
        return self.__size 
    
    @size.setter
    def size(self, value):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        value = self.__size