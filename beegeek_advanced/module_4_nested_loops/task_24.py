n = 8
matrix = [['.'] * n for _ in range(n)]

cord = input()
num_column = ord(cord[0]) - ord('a')
num_row = int(cord[1])

for i in range(n):
    for j in range(n):
        if i == n - num_row and j == num_column:
            matrix[i][j] = 'N'
        elif (i == n - num_row + 2 or i == n - num_row - 2) and (j == num_column - 1 or j == num_column + 1):
            matrix[i][j] = '*'
        elif (j == num_column + 2 or j == num_column - 2) and (i == n - num_row - 1 or i == n - num_row + 1):
            matrix[i][j] = '*'
        print(matrix[i][j], end = ' ')
    print()