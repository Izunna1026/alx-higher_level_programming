#!/usr/bin/python3
"""This is to define a matrix division function"""


def matrix_divided(matrix, div):
    """This is to divide all elements of a matrix


    Args:
        matrix (list): A list of lists of ints or floats
        div (int/float): The divisor
    Raises:
        TypeError: if the matrix have rows of different sizes
        TypeError: if the matrix contains non-numbers
        TypeError: if div is not an int or float
        ZeroDivisionError: if div is 0
    Returns:
        The result of the division
    """
    if (not isinstance(matrix, list) or matrix == [] or 
            not all(isinstance(row, list) for row in matrix) or
            not all((isinstance(ele, int) or isinstance(ele, float))
                for ele in [num for row in matrix for num in row])):
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return ([list(map(lambda x: round(x / div, 2), row)) for row in matrix])
