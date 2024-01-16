#!/usr/bin/python3
"""
Function that prints a literal square
"""
def print_square(size):
    def __init__(self, size=0):
        self.size = size
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise TypeError("Size must be >= 0")
        if isinstance(size, float) and size < 0:
            raise TypeError("size must be an integer")
        if size == 0:
            print("")
        else:
            for x in range(size):
                for y in range(size):
                    print("#", end="")