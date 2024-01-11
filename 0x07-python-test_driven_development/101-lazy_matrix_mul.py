#!/usr/bin/python3
"""This is to define a matrix multiplication using Numpy"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """This sis to return the multiplication of 2 matrices

    Args:
        m_a (list of lists of ints/floats): The first matrix
        m_b (list of listd of ints/floats): The second matrix
    """

    return (np.matmul(m_a, m_b))
