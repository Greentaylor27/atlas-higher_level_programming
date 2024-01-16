#!/usr/bin/python3
"""
Function that divides a matrix
"""


def matrix_divided(matrix, div):
    if not isinstance(matrix, (int, float)):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    
    if div == 0:
        
    return (matrix / div)