n = int(input())
matrix = []
flag = True

for _ in range(n):
    temp = [int(i) for i in input().split()]
    matrix.append(temp)

for r in range(n):
    for c in range(n):
        if r != c and matrix[r][c] != matrix[c][r]:
            flag = False
            break

if flag:
    print('YES')
else:
    print('NO')