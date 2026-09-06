n = int(input())
matrix = []

for _ in range(n):
    matrix.append([int(i) for i in input().split()])

for i in range(n):
    matrix[i][i], matrix[(n - 1) - i][i] = matrix[(n - 1) - i][i], matrix[i][i]

for row in matrix:
    print(*row)