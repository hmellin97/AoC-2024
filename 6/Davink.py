def mark_visited(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == ".":
                matrix[i][j] = "X"
    return matrix

# Example matrix
matrix = [
    ['.', '.', '#', '.', '.'],
    ['#', '.', '#', '.', '#'],
    ['.', '#', '.', '.', '.'],
    ['#', '#', '#', '#', '#'],
]

marked_matrix = mark_visited(matrix)

for row in marked_matrix:
    print(row)