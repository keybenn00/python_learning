n, m = int(input()), int(input())
matrix = []

for _ in range(n):
    temp = [int(i) for i in input().split()]
    matrix.append(temp)

# Принимаем номера столбцов для обмена
list_swap = [int(i) for i in input().split()]

for r in range(n):
    for c in range(m):
        # Меняем местами первый и второй указанные столбцы
        if c == list_swap[0]:
            matrix[r][c], matrix[r][list_swap[1]] = matrix[r][list_swap[1]], matrix[r][c]

# Выводим матрицу
for r in range(n):
    for c in range(m):
        print(matrix[r][c], end = ' ')
    print()