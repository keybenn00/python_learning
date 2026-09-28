n = int(input())
matrix = [['-'] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
            matrix[i][j] = abs(j - i)

for row in matrix:
    print(*row)