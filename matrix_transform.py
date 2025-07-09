# Write a Python function that transforms a given matrix A using the operation T^-1 AS, 
# where T and S are invertible matrices. The function should first validate if the 
# matrices T and S are invertible, and then perform the transformation. In cases where there is no solution return -1

import numpy as np

def transform_matrix(A, T, S):
    try:
        # Check if T and S are square matrices
        if T.shape[0] != T.shape[1] or S.shape[0] != S.shape[1]:
            return -1

        # Check if dimensions are compatible for the operation
        if T.shape[1] != A.shape[0] or A.shape[1] != S.shape[0]:
            return -1

        # Compute the inverses
        T_inv = np.linalg.inv(T)
        # Perform the transformation
        result = T_inv @ A @ S
        return result
    except np.linalg.LinAlgError:
        # Raised if T or S are not invertible
        return -1

# Matrix-Vector Dot Product:
def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
    if len(b) != len(a[0]):
        return -1
    else:
        dot_list = []
        for i in a:
            temp = 0
            for j in range(len(i)):
                temp += (i[j] * b[j])
            dot_list.append(temp)
        return dot_list

# Transpose of a matrix:
def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
	b = [[] for _ in range(len(a[0]))]
	for idx_i,i in enumerate(a):
		for j in range(len(b)):
			b[j].append(i[j])
	return b

# Reshape Matrix:
import numpy as np

def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
	a = [j for i in a for j in i]
	if (new_shape[0] * new_shape[1]) != len(a):
		return []
	reshaped_matrix = []
	idx = 0
	for i in range(new_shape[0]):
		temp_list = []
		for j in range(new_shape[1]):
			temp_list.append(a[idx])
			idx += 1
		reshaped_matrix.append(temp_list)
	return reshaped_matrix

