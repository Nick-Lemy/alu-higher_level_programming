#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    result = []
    for row in matrix:
        name = []
        for i in row:
            name.append(i**2)
        result.append(name)
    return result
