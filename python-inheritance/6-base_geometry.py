#!/usr/bin/python3
"""class for BaseGeometry"""


class BaseGeometry:
    """Methods for BaseGeometry"""
    def __init__(self):
        pass
    def area(self):
        try:
            pass
        except NotImplementedError:
            raise Exception("area() if not implemented")
