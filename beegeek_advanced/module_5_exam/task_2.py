# Принимает квадратную матрицу на вход
n = int(input())
matrix = [[int(i) for i in input().split()] for _ in range(n)]
# Создаем список содержащий числа, которые проходят по условию
list_of_positive_num = []

for i in range(n):
    for j in range(n):
        if (i + j + 1 == n) or (i > n - 1 - j):
            list_of_positive_num.append(matrix[i][j])

# Выводим максимум такого списка
print(max(list_of_positive_num))