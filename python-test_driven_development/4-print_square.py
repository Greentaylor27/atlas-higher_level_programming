#!/usr/bin/python3
"""
Function that prints a literal square
"""


def print_square(size):
    """_summary_

    Args:
        size (int): intended integer for how big you want the square

    Raises:
        TypeError: size must be an integer
        TypeError: size must be >=0
        TypeError: size must be an integer
    """
    # Conditionals for function
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise TypeError("size must be >= 0")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    
    # Meat and potatoes of the code
    if size == 0:
        pass
    else:
        for x in range(size):
            for y in range(size):
                print("#", end="")
            print("")