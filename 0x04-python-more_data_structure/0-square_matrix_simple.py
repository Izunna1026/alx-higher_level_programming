#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    sqr = []
    for x in matrix:
        for j in matrix:
            sqr.append(list(map(lambda x: x**2, j)))
        return (sqr)
