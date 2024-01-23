#!/usr/bin/python3
"""class for BaseGeometry"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """
    Class to define A rectangle

    inhertiance: BaseGeometry

    Args:
        BaseGeometry (Class): Parent class

    Attributes:
        height (int): Height of rectangle
        width (int): Width of rectangle
    """
    def __init__(self, width, height):
        super().__init__()
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
