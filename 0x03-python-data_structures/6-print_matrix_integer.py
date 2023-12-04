#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        number = 0
        for col in row:
            number += 1
            print('{:d}'.format(col), end=(" " if number < len(row) else ""))
        print()
