import numpy as np

def matrix_transpose(A):
    """
    Return the transpose of matrix A (swap rows and columns).
    """
    elems = 0
    for r in A:
        for c in r:
            elems += 1
    rows = elems // len(A)
    cols = len(A)
    transposed = np.zeros(shape=(rows, cols))
    for i in range(rows):
        for j in range(cols):
            transposed[i, j] = A[j][(i + rows) % rows]
    return transposed
            
            
