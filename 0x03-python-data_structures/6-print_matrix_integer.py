#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    """Print matrix of integers

    Args:
        matrix (list of list): List of list containing integer values
    """
    for row in matrix:
        n = len(row)

        for col in range(n):
            value = row[col]
            if col == n - 1:
                print("{:d}".format(value))
            else:
                print("{:d}".format(value), end=" ")


if __name__ == "__main__":
    matrix = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
            ]
    print_matrix_integer(matrix)
