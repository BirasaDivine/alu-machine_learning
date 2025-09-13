#!/usr/bin/env python3
arr1 = [1, 2, 3, 4]
arr2 = [5, 6, 7, 8]
def add_arrays(arr1,arr2):
    if len(arr1) != len(arr2):
        return None
    return [a + b for a, b in zip(arr1, arr2)]
print(add_arrays(arr1, arr2))
print(arr1)
print(arr2)
print(add_arrays(arr1, [1, 2, 3]))