n, m = [int(i) for i in input().split()]
matrix_A = [[int(i) for i in input().split()] for _ in range(n)]
input()
matrix_B = [[int(i) for i in input().split()] for _ in range(n)]
result_matrix = []
temp = []

for i in range(n):
    for j in range(m):
        num = matrix_A[i][j] + matrix_B[i][j]
        temp.append(num)
    result_matrix.append(temp)
    temp = []

for row in result_matrix:
    print(*row)