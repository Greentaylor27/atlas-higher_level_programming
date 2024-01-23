#!/usr/bin/python3
"""class for BaseGeometry"""


class BaseGeometry:
    """Methods for BaseGeometry"""
    def __init__(self):
            pass

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
        self.name = name
        self.value = value

class Rectangle(BaseGeometry):
    def __init__(self, width, height):
        self.__width = width
        self.__height = height
