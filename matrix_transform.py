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
