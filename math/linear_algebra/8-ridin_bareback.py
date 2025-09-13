#!/usr/bin/env python3
def mat_mul(mat1, mat2):
    """Multiply two 2D matrices. Return None if multiplication is not possible."""
    if len(mat1[0]) != len(mat2):
        return None
    result = []
    for i in range(len(mat1)):
        new_row = []
        for j in range(len(mat2[0])):
            sum_product = 0
            for k in range(len(mat1[0])):
                sum_product += mat1[i][k] * mat2[k][j]
            new_row.append(sum_product)
        result.append(new_row)
    return result
mat1 = [[1, 2],
        [3, 4],
        [5, 6]]
mat2 = [[1, 2, 3, 4],
        [5, 6, 7, 8]]
print(mat_mul(mat1, mat2))