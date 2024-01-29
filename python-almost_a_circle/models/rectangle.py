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
    #Getter and setter for width
    def get_width(self):
        return self.__width
    def set_width(self, value):
        self.__width = value

    #Getter and setter for height
    def get_height(self):
        return self.__height
    def set_height(self, value):
        self.__height = value

    #Getter and setter for x
    def get_x(self):
        return self.__x
    def set_x(self, value):
        self.__x = value

    #Getter and setter for y
    def get_y(self):
        return self.__y
    def set_y(self, value):
        self.__y = value
