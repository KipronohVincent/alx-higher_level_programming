#!/usr/bin/python3
"""
    Module to find the max integer in a list

    Write a function that multiplies 2 matrices by using
    the module NumPy

    To install it: pip3 install numpy==1.15.0

    Prototype: def lazy_matrix_mul(m_a, m_b):
    Test cases should be the same as 100-matrix_mul
    but with new exception type/message
"""


import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """ multiply two matrix with numpy """
    return np.dot(m_a, m_b)
