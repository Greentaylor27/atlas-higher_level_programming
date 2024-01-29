#!/usr/bin/python3
"""
Child class (rectangle) from Base
"""
from models.base import Base


class Rectangle(Base):
    """Class Attributes and methods for the class Rectangle"""
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    """Getter and setters for attributes"""
    @property
    def width(self):
        """Getter for width"""
        return self.__width
    @width.setter
    def set_width(self, value):
        """Setter for width"""
        self.__width = value

    @property
    def height(self):
        """Getter for height"""
        return self.__height
    @height.setter
    def set_height(self, value):
        """Setter for height"""
        self.__height = value

    @property
    def x(self):
        """Getter for x"""
        return self.__x
    @x.setter
    def set_x(self, value):
        """Setter for x"""
        self.__x = value

    @property
    def y(self):
        """Getter for y"""
        return self.__y
    @y.setter
    def set_y(self, value):
        """Setter for y"""
        self.__y = value
