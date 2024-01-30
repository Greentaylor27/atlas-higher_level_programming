#!/usr/bin/python3
"""
Grandchild of base and child class to Rectangle
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Class attributes and methods for the class square"""
    def __init__(self, size, x=0, y=0, id=None):
        Rectangle.__init__(self, width=0, height=0, x=0, y=0)
        size = self.__height, self.__width

    def __str__(self):
        return ("[Square] ({}) {}/{} - {}".format(self.id, self.__x, self.__y, self.__size))
