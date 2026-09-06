n = int(input())
matrix = []

for _ in range(n):
    matrix.append([int(i) for i in input().split()])

matrix = matrix[::-1]

for i in range(n):
    for j in range(n):
        print(matrix[j][i], end = ' ')
    print()