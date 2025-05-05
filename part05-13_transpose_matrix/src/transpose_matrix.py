# Write your solution here

def transpose(matrix: list):
    matrix_T = [item[:] for item in matrix]
    
    for r in range(len(matrix_T)):
        for c in range(len(matrix_T[r])):
            matrix[c][r] = matrix_T[r][c]


if __name__ == "__main__":
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(matrix)
    print(transpose(matrix))