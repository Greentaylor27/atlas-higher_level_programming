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
        s = self.width
        return ("[Square] ({}) {}/{} - {}".format(i, x, y, s))

    @property
    def size(self):
        """Getter for size"""
        return self.width

    @size.setter
    def size(self, value):
        """Setter for size"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Assigns attribute to args"""
        arg_len = len(args)

        if arg_len >= 1:
            self.id = args[0]
        if arg_len >= 2:
            self.size = args[1]
        if arg_len >= 3:
            self.x = args[2]
        if arg_len >= 4:
            self.y = args[3]

        for key, value in kwargs.items():
            setattr(self, key, value)

    def to_dictionary(self):
        """
        Method that returns the dictionary representation of a Square
        """
        return {
            'id': self.id,
            'size': self.size,
            'x': self.x,
            'y': self.y
        }
