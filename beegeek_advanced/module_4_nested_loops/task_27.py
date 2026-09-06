n = int(input())
matrix = [['.'] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if i + j + 1 == n:
            matrix[i][j] = 1
        elif i < n - 1 - j:
            matrix[i][j] = 0
        else:
            matrix[i][j] = 2
        print(matrix[i][j], end = ' ')
    print()

