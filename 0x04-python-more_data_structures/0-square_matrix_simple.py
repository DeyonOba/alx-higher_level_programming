#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    return list(map(lambda x: list(map(lambda x: x**2, x)), matrix))


if __name__ == "__main__":
    my_list = [[1, 3], [3, 7]]

    print(square_matrix_simple(my_list))
