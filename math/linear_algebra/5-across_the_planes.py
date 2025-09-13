#!/usr/bin/env python3
mat1 = [[1, 2], [3, 4]]
mat2 = [[5, 6], [7, 8]]
def add_matrices2D(mat1, mat2):
    if len(mat1) != len(mat2):
        return None
    result = []
    for row1, row2 in zip(mat1, mat2):
        if len(row1) != len(row2):
            return None
        result.append([a + b for a, b in zip(row1, row2)])
    return result
print(add_matrices2D(mat1, mat2))
print(mat1)
print(mat2)
print(add_matrices2D(mat1, [[1, 2, 3], [4, 5, 6]]))