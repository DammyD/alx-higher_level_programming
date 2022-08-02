#!/usr/bin/python3
"""function"""


def pascal_triangle(n):
    """
    Creates a list of lists of integers representing the
    pascal triangle of a given integer.
    n: Levels of the triangle
    Args:
        - n: int
    """
    if (n <= 0):
        return ([])
    elif (n == 1):
        return ([1])
    elif (n == 2):
        return ([[1], [1, 1]])

    pascal = [[1], [1, 1]]

    for i in range(1, n - 1):
        new_list = []
        new_list.append(1)
        for j in range(1, len(paascal)):
            new_list.append(pascal[i][j - 1] + pascal[i][j])
        new_list.append(1)
        pascal.aappend(new_list)

    return (pascal)
