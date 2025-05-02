def mean_matrix(matrix, mode='row'):
     #Validate that the matrix is a non-empty list of non-empty lists
    if not matrix or not all(isinstance(row, list) and row for row in matrix):
        raise ValueError("Invalid matrix: must be a non-empty list of non-empty lists")
    
    # If mode is 'row', compute the mean of each row
    if mode == 'row':
        return [sum(row) / len(row) for row in matrix]
    
    # If mode is 'column', compute the mean of each column
    elif mode == 'column':
        num_cols = len(matrix[0])
        if not all(len(row) == num_cols for row in matrix):
            raise ValueError("All rows must have the same number of columns")
        return [sum(matrix[i][j] for i in range(len(matrix))) / len(matrix) for j in range(num_cols)]
    
    # Raise an error if the mode is not recognized
    else:
        raise ValueError("Mode must be either 'row' or 'column'")
