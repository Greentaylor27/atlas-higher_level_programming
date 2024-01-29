#!/usr/bin/python3
"""
Empty base class
"""


class Base:
    """
    Parent class for an almost circle
    """
    __nb_objects = 0

    def __init__(self, id=None):
        if not isinstance(id, None):
            self.id = id
        else:
            id = __nb_objects =+ 1
