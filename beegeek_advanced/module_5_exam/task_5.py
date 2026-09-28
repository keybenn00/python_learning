n = int(input())
matrix = [[int(i) for i in input().split()] for _ in range(n)]
flag = True

for i in range(n):
    for j in range(n):
        if matrix[i][j] != matrix[n - 1 - j][n - 1 - i]:
            flag = False
            break


if flag:
    print('YES')
else:
    print('NO')