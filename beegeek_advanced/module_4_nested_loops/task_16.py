n = int(input())
matrix = []

for _ in range(n):
    temp = [int(num) for num in input().split()]
    matrix.append(temp)

sum_up, sum_right, sum_bottom , sum_left = 0, 0, 0, 0

# Проверка элементов матрицы на соответствие четверям, сложение суммы четвертей(не учитывая диагоналей)
for i in range(n):
    for j in range(n):
        if i < j and i < n - 1 - j:
            sum_up += matrix[i][j]
        elif i < j and i > n - 1 - j:
            sum_right += matrix[i][j]
        elif i > j and i > n - 1 - j:
            sum_bottom += matrix[i][j]
        elif i > j and i < n - 1 - j:
            sum_left += matrix[i][j]

print(f'Верхняя четверть: {sum_up}')
print(f'Правая четверть: {sum_right}')
print(f'Нижняя четверть: {sum_bottom}')
print(f'Левая четверть: {sum_left}')
