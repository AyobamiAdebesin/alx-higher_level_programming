#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    square_mat = matrix
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            square_mat[i][j] = (matrix[i][j])**2
    return square_mat
