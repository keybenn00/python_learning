n = int(input())
matrix = []

for _ in range(n):
    matrix.append([int(i) for i in input().split()])

matrix = matrix[::-1]

for row in matrix:
    print(*row)