import numpy as np

def vector_operations():
    v1 = np.array([1, 2, 3])
    v2 = np.array([4, 5, 6])
    
    dot = np.dot(v1, v2)
    norm_v1 = np.linalg.norm(v1)
    
    return {"dot_product": dot, "norm_v1": norm_v1}

def matrix_operations():
    A = np.array([[1, 2], [3, 4]])
    eigenvalues, eigenvectors = np.linalg.eig(A)
    
    return {"eigenvalues": eigenvalues, "eigenvectors": eigenvectors}
