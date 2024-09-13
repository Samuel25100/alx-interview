#!/usr/bin/python3
"""function: rotate_2d_matrix"""


def rotate_2d_matrix(matrix):
    """rotate the matrix 90 degree clockwise by in-place edit"""
    n = len(matrix)
    for x in range(0, int(n / 2)):
        for y in range(x, n-x-1):
            temp = matrix[y][n-1-x]
            matrix[y][n-1-x] = matrix[x][y]
            matrix[x][y] = matrix[n-1-y][x]
            matrix[n-1-y][x] = matrix[n-1-x][n-1-y]
            matrix[n-1-x][n-1-y] = temp
