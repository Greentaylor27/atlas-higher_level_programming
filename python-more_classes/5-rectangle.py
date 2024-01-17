#!/usr/bin/python3
"""Class Rectangle"""


class Rectangle:
    """
    Attributes for Rectangle
    """
    def __init__(self, width=0, height=0):
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width

        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height

    @property
    def width(self):
        """Getter for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Height setter"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Method to find the area"""
        return (self.__height * self.__width)

    def perimeter(self):
        """Method for finding the perimeter"""
        pmeter = 2 * (self.__height + self.__width)
        if self.__height == 0 or self.__width == 0:
            pmeter = 0
        return pmeter

    def __str__(self):
        pcs = "\n".join(["#" * self.__width for _ in range(self.__height)])
        """Return a string representation of the rectangle"""
        if self.__height == 0 or self.__width == 0:
            return ""
        else:
            return pcs

    def __repr__(self):
        """Return a string that describes how to recreate the rectangle"""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """Prints a message when the rectangle is being destroyed."""
        print("Bye rectangle...")
