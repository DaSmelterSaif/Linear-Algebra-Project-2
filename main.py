import numpy as np

# A 3x3 array with zeros.
matrix: np.ndarray = np.zeros((3, 3))

# ############ Input ############
print("Enter the 6 constants for the upper triangular matrix")
print("[[a11 a12 a13]")
print(" [0   a22 a23]")
print(" [0   0   a33]]:")
print("-------------------")

for i in range(3):
    matrix[0][i] = float(input(f"a1{i+1}: "))

for i in range(1, 3):
    matrix[1][i] = float(input(f"a2{i+1}: "))

matrix[2][2] = float(input("a33: "))

print(matrix)

def computeEigenVector(A)-> np.ndarray:
    eigenvalues: list = [A[0][0], A[1][1], A[2][2]]
    tempMatrix: np.ndarray = A.copy()

    # for value in eigenvalues:
    #     pass

    # Eigenvalues[0]
    value = eigenvalues[0]
    tempMatrix[0][0] = 0
    tempMatrix[1][1] = tempMatrix[1][1] - value
    tempMatrix[2][2] = tempMatrix[2][2] - value
    # TODO - Add the rest of the code to compute the eigenvector.
    # TODO - Automate using the for loop.

    return tempMatrix

print(computeEigenVector(matrix))