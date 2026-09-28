n = int(input())
matrix = [[int(i) for i in input().split()] for _ in range(n)]
flag = True

# Проверка всех строк на содержание цифр от 1 до n
for i in range(n):
    values = [int(i) for i in range(1, n + 1)]
    for j in range(n):
        if matrix[i][j] in values:
            values.remove(matrix[i][j])
    if len(values) > 0:
        flag = False
        break

# Проверка всех столбцов на содержание цифр от 1 до n
for i in range(n):
    values = [int(i) for i in range(1, n + 1)]
    for j in range(n):
        if matrix[j][i] in values:
            values.remove(matrix[j][i])
    if len(values) > 0:
        flag = False
        break

if flag:
    print('YES')
else:
    print('NO')