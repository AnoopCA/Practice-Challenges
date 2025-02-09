def mean_matrix(matrix, mode='row'):
    """
    Calculate the mean of a matrix by row or column.
    
    Parameters:
    matrix (list of lists): The input matrix.
    mode (str): 'row' to calculate row-wise means, 'column' to calculate column-wise means.
    
    Returns:
    list: A list of mean values.
    """
    if not matrix or not all(isinstance(row, list) and row for row in matrix):
        raise ValueError("Invalid matrix: must be a non-empty list of non-empty lists")
    
    if mode == 'row':
        return [sum(row) / len(row) for row in matrix]
    
    elif mode == 'column':
        num_cols = len(matrix[0])
        if not all(len(row) == num_cols for row in matrix):
            raise ValueError("All rows must have the same number of columns")
        return [sum(matrix[i][j] for i in range(len(matrix))) / len(matrix) for j in range(num_cols)]
    
    else:
        raise ValueError("Mode must be either 'row' or 'column'")
