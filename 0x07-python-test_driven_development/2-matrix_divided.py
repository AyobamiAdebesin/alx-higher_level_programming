#!/usr/bin/python3
"""

This module contains a function that divides the numbers of a matrix

"""


def matrix_divided(matrix, div):
    """ Function that divides the integer/float numbers of a matrix

    Args:
        matrix: list of a lists of integers/floats
        div: number which divides the matrix

    Returns:
        A new matrix with the result of the division

    Raises:
        TypeError: If the elements of the matrix aren't lists
                   If the elemetns of the lists aren't integers/floats
                   If div is not an integer/float number
                   If the lists of the matrix don't have the same size

        ZeroDivisionError: If div is zero


    """

    err_msg_1 = "matrix must be a matrix (list of lists) of integers/floats"
    err_msg_2 = "Each row of the matrix must have the same size"
    err_msg_3 = "div must be a number"
    err_msg_4 = "division by zero"

    if not isinstance(matrix, list):
        raise TypeError(err_msg)

    for i in range(len(matrix)):
        if not isinstance(matrix[i], list):
            raise TypeError(err_msg)
        for j in range(matrix[i]):
            if not isinstance(matrix[i][j], int) and not isinstance (matrix[i][j], float):
                raise TypeError(err_msg)
    
    len_first_row = len(matrix[0])
    
    for i in range(1, len(matrix)):
        if len_first_row != 0 and len(matrix[i]) != len_first_row:
            raise TypeError(err_msg_2)
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError(err_msg_3)

    if div == 0:
        raise ZeroDivisionError(err_msg_4)

    new_matrix = matrix[:][:]
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            new_matrix[i][j] = round(matrix[i][j] / div, 2)
    return new_matrix
