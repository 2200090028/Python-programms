def transpose_matrix(matrix):
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
matrix = [
    [1, 2, 3],
    [4, 5, 6]
]
result = transpose_matrix(matrix)
print("Transposed matrix:", result)

