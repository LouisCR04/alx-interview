#!/usr/bin/python3
"""
0-pascal_triangle.py
Pascal's Triangle
"""


def pascal_triangle(n):
    """
    Returns a list of lists of integers representing Pascal’s triangle of n
    n: The number of rows
    return: List of lists of ints
    """

    if type(n) is not int:
        raise TypeError("n must be an integer")
    matrix = []
    if n <= 0:
        return matrix
    for i in range(n):
        arr = []
        for j in range(i+1):
            if j == 0:
                arr.append(1)
            elif j == i:
                arr.append(1)
            else:
                arr.append(matrix[i-1][j-1] + matrix[i-1][j])
        matrix.append(arr)
    return matrix
