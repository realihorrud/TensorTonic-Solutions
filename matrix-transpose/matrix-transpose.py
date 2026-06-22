import numpy as np

def matrix_transpose(A):
    """
    Return the transpose of matrix A (swap rows and columns).
    """
    # input: [[1, 9, -2], [5, 8, 3]]
    # output: [[1, 5], [9, 8], [-2, 3]]
    flatten = []
    for r in A:
        for c in r:
            flatten.append(c)
    rows = len(flatten) // len(A) # 3
    cols = len(A) # 2
    transposed = np.zeros(shape=(rows, cols))
    for i in range(rows):
        for j in range(cols):
            transposed[i, j] = A[j][(i + rows) % rows]
    return transposed
            
            
