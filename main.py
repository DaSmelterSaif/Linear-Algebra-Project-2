import numpy as np

# NAMES HERE (IT WON'T BE ON GITHUB LOL)

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

print("-------------------")
print(matrix, end="\n\n")

def computeEigenVector(A)-> np.ndarray:
    eigenvalues: list = [A[0][0], A[1][1], A[2][2]]
    tempMatrix: np.ndarray = np.zeros((3, 3))

    # When solving on a separate sheet, the eigenvectors
    # follow the following pattern:
    # s*[1 0 0]^T for a11
    # s*[(some number) 1 0]^T for a22
    # s*[(some number) (some number) 1]^T for a33
    # Calculating the already known values is redundant,
    # so I have kept it as is in the code.

    # Eigenvector for a11
    tempMatrix[0][0] = 1
    tempMatrix[1][0] = 0
    tempMatrix[2][0] = 0

    # Eigenvector for a22
    # -c12 / (c11 - c22)
    tempMatrix[0][1] = -A[0][1] / (A[0][0] - A[1][1])
    tempMatrix[1][1] = 1
    tempMatrix[2][1] = 0

    # Eigenvector for a33
    # (c23c12) / (c22 - c33)(c11 - c33) - c13/(c11 - c33)
    tempMatrix[0][2] = (A[1][2] * A[0][1]) / ((A[1][1] - A[2][2])*(A[0][0] - A[2][2]))
    tempMatrix [0][2] = tempMatrix[0][2] - A[0][2] / (A[0][0] - A[2][2])
    # -c23 / (c22 - c33)
    tempMatrix[1][2] = -A[1][2] / (A[1][1] - A[2][2])
    tempMatrix[2][2] = 1

    return tempMatrix

eigenVectors = computeEigenVector(matrix)

# ############ Output ############
for columns in range(3):
    print("Eigenvector for %d:" % (matrix[columns][columns]))
    print("s*(%.3f, %.3f, %.3f)^T\n" % (eigenVectors[0][columns],
            eigenVectors[1][columns], eigenVectors[2][columns]))
    