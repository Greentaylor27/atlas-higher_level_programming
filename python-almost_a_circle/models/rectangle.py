#!/usr/bin/python3
"""
Child class (rectangle) from Base
"""
from models.base import Base


class Rectangle(Base):
    """Class Attributes and methods for the class Rectangle"""
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)

        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    """Getter and setters for attributes"""
    @property
    def width(self):
        """Getter for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Getter for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Getter for x"""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter for x"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Getter for y"""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter for y"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        Method that finds the area of a rectangle

        Returns:
            integer: Returns the area of a rectangle
        """
        return (self.__height * self.__width)

    def display(self):
        """
        Prints # in a rectangle
        """
        for x in range(self.__y):
            print()
        for y in range(self.__height):
            print(" " * self.__x + "#" * self.__width)

    def __str__(self):
        i = self.id
        x = self.__x
        y = self.__y
        h = self.__height
        w = self.__width
        print("[Rectangle] ({}) {}/{} - {}/{}".format(i, x, y, w, h))

    def update(self, *args, **kwargs):
        """
        Defines which arg goes to which attribute
        """
        arg_len = len(args)

        if arg_len >= 1:
            self.id = args[0]
        if arg_len >= 2:
            self.__width = args[1]
        if arg_len >= 3:
            self.__height = args[2]
        if arg_len >= 4:
            self.__x = args[3]
        if arg_len >= 5:
            self.__y = args[4]

        for key, value in kwargs.items():
            setattr(self, key, value)
