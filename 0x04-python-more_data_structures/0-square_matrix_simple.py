#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    square_matrix = matrix
    for i in range(len(square_matrix)):
        square_matrix[i] = list(map(lambda x: x**2, square_matrix[i]) )
    return square_matrix
