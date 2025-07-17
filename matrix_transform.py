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


# Mean by Row or Column:
def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
	if mode == "row":
		means = [sum(i)/len(i) for i in matrix]
	else:
		means = [[] for _ in range(len(matrix[0]))]
		for row_list in matrix:
			for j in range(len(means)):
				means[j].append(row_list[j])
		means = [sum(i)/len(i) for i in means]
	return means


# Eigenvalues of a Matrix:
def calculate_eigenvalues(matrix: list[list[float|int]]) -> list[float]:
	ad = matrix[0][0]+matrix[1][1]
	bc = (matrix[0][0]*matrix[1][1]) - (matrix[0][1]*matrix[1][0])
	l1 = (ad + ((ad)**2 - 4*(bc))**0.5) / 2
	l2 = (ad - ((ad)**2 - 4*(bc))**0.5) / 2
	eigenvalues = [l1, l2]
	return eigenvalues


# Matrix Transformation: T^−1 . A . S
import numpy as np
def transform_matrix(A: list[list[int|float]], T: list[list[int|float]], S: list[list[int|float]]) -> list[list[int|float]]:
	if np.isclose(np.linalg.det(T), 0) or np.isclose(np.linalg.det(S), 0):
		return -1
	A = np.array(A)
	T = np.array(T)
	S = np.array(S)
	T_inv = np.linalg.inv(T)
	T_inv_A = np.dot(T_inv, A)
	transformed_matrix = np.dot(T_inv_A, S)
	return transformed_matrix


# Calculate 2x2 Matrix Inverse:
def inverse_2x2(matrix: list[list[float]]) -> list[list[float]]:
	a, b, c, d = matrix[0][0], matrix[0][1], matrix[1][0], matrix[1][1]
	det = a*d - b*c
	if det == 0:
		return None
	mul = 1 / (a*d - b*c)
	a, b, c, d = a*mul, b*mul, c*mul, d*mul
	inverse = [[d, -b], [-c, a]]
	return inverse


# Multiply two matrices:
def matrixmul(a:list[list[int|float]],
              b:list[list[int|float]])-> list[list[int|float]]:
    if len(a[0]) != len(b):
        return -1
    c = []
    for i in a:
        temp = 0
        temp_list = []
        for j in range(len(b[0])):
            temp_list_in = []
            for num,k in enumerate(b):
                temp_list_in.append(i[num] * k[j])
            temp_list.append(sum(temp_list_in))
        c.append(temp_list)
    return(c)


# Calculate Covariance Matrix:
def calculate_covariance_matrix(vectors: list[list[float]]) -> list[list[float]]:
	num_features = len(vectors)
	cov_matrix = []
	for i in range(num_features):
		row = []
	return []

def mean(values):
    return sum(values) / len(values)

def covariance(x, y):
    x_mean = mean(x)
    y_mean = mean(y)
    return sum((xi - x_mean) * (yi - y_mean) for xi, yi in zip(x, y)) / (len(x) - 1)

def covariance_matrix(data):
    num_features = len(data)
    cov_matrix = []

    for i in range(num_features):
        row = []
        for j in range(num_features):
            cov = covariance(data[i], data[j])
            row.append(cov)
        cov_matrix.append(row)
    
    return cov_matrix
