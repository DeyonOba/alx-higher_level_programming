#!/usr/bin/python3

"""
Module contains function that divides all elements of ta matrix.

    - Prototype: def matrix_divided(matrix, div):
    - `matrix` must be a list of lists of integer and floats,
        otherwise raise a `TypeError` exception with the message
        "matrix must be a matrix (list of lists) of integers/ floats
    - Each row of the `matrix` must be of the same size, otherwise raise
        a `TypeError` exception with the message "Each row of the matrix must
        have the same size"
    - `div` must be a number (integer or float), otherwise raise a `TypeError`
        exception with the message "div must be a number".
    - `div` can't be equal to 0, otherwise raise a `ZereDivisionError`
        exception with the message "division by zero".
    - All elements of the matrix should be divided by `div`,
        rounded to 2 decimal places.
    - Returns a new matrix.
    - You are not allowed to import any module.
"""


def matrix_divided(matrix, div):
    """Divide a matrix of list of lists with a number.

    Parameters
    ----------
    matrix : list of list
        Matrix of list of lists of float and integers
    div : int or float
        Number used as divisor.

    Returns
    -------
    list
    """
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not isinstance(matrix, list):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats"
            )
    # Create a copy of the matrix
    matrix_cp = matrix.copy()
    row_size = 0
    for row_num, row in enumerate(matrix_cp):
        if not isinstance(row, list):
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats"
            )
        # Update variable `row_size` to current size of the first row in
        # the matrix
        if row_num == 0:
            row_size = len(row)
        # Any other row would be verified by variable `row_size`
        elif len(row) != row_size:
            raise TypeError("Each row of the matrix must have the same size")
        for idx, num in enumerate(row):
            if not isinstance(num, (int, float)):
                raise TypeError(
                    "matrix must be a matrix (list of lists)\
 of integers/floats"
                    )
            matrix_cp[row_num][idx] = round(num / div, 2)
    return matrix_cp
