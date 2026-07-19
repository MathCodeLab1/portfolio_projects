import numpy as np

def add_matrices(A, B):
    return np.add(A, B)

def multiply_matrices(A, B):
    return np.matmul(A, B)

if __name__ == "__main__":
    A = np.array([[1, 2], [3, 4]])
    B = np.array([[5, 6], [7, 8]])

    print("Matrix A:\n", A)
    print("Matrix B:\n", B)
    print("A + B:\n", add_matrices(A, B))
    print("A x B:\n", multiply_matrices(A, B))