#!/usr/bin/python3
"""
Grandchild of base and child class to Rectangle
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Class attributes and methods for the class square"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        i = self.id
        x = self.x
        y = self.y
        s = self.size
        return ("[Square] ({}) {}/{} - {}".format(i, x, y, s))
