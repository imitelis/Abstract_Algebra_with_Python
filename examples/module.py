from structures import Module

# Example of a module operations:
def matrix_addition(matrix1, matrix2):
    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        raise ValueError("Matrices must be of the same size for addition")
    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix1[0])):
            row.append(matrix1[i][j] + matrix2[i][j])
        result.append(row)
    return result

def matrix_multiplication(matrix1, matrix2):
    if len(matrix1[0]) != len(matrix2):
        raise ValueError("Number of columns in the first matrix must be equal to the number of rows in the second matrix")
    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix2[0])):
            val = 0
            for k in range(len(matrix2)):
                val += matrix1[i][k] * matrix2[k][j]
            row.append(val)
        result.append(row)
    return result

def matrix_product(scalar, matrix):
    result = []
    for row in matrix:
        result_row = [scalar * element for element in row]
        result.append(result_row)
    return result

# Example usage:
basis = [[[1, 0], [0, 0]], [[0, 1], [0, 0]], [[0, 0], [1, 0]], [[0, 0], [0, 1]]]
module = Module(basis, matrix_addition, matrix_multiplication, matrix_product)

matrix1 = [[1, 2], [3, 4]]
matrix2 = [[2, 0], [1, 3]]

print(module.add(matrix1, matrix2))
print(module.multiply(matrix1, matrix2))
print(module.product(2, matrix2))