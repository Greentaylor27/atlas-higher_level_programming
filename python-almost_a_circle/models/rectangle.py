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

    def get_width(self):
        """Getter for width"""
        return self.__width
    def set_width(self, value):
        """Setter for width"""
        self.__width = value

    def get_height(self):
        """Getter for height"""
        return self.__height
    def set_height(self, value):
        """Setter for height"""
        self.__height = value

    def get_x(self):
        """Getter for x"""
        return self.__x
    def set_x(self, value):
        """Setter for x"""
        self.__x = value

    def get_y(self):
        """Getter for y"""
        return self.__y
    def set_y(self, value):
        """Setter for y"""
        self.__y = value
