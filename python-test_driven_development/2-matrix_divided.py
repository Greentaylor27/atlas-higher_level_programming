#!/usr/bin/python3
"""
Function that divides a matrix
"""


def matrix_divided(matrix, div):
    """
    Function that divides an index in a matrix

    Args:
        matrix (list): List of ints or floats
        div (int, float): divisor

    Raises:
        TypeError: matrix must be a matrix (list of lists) of integers/floats
        TypeError: Each row of the matrix must have the same size
        TypeError: div must be a number
        ZeroDivisonError: divison by zero

    Returns:
        list: A matrix with new elements 
    """
    # Conditionals for error raising
    result = []
    if not isinstance(matrix, list):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    else:
        for row in matrix:
            if not all(isinstance(element, (int, float)) for element in row):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not isinstance(div, (float, int)):
        raise TypeError("div must be a number")
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    # Actual function
    for row in matrix:
        new_row = []
        for element in row:
            new_element = float(element / div)
            new_row.append(float(f'{new_element:.2f}'))
        result.append(new_row)
    return (result)