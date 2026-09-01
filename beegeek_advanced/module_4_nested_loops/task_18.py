n, m = int(input()), int(input())
matrix = []

# Создаем матрицу на основе введенных данных
for i in range(n):
    temp = [int(el) for el in input().split()]
    matrix.append(temp)

# Находим максимальный элемент в матрице, запоминаем его (для сравнения) и его индекс (по условию задачи)
# В конце у максимума стоит - 1 для учтения 1 элемента матрицы в качестве максимального
maximum = matrix[0][0] - 1

for i in range(n):
    for j in range(m):
        if matrix[i][j] > maximum:
            maximum = matrix[i][j]
            index_max = []
            index_max.append(i)
            index_max.append(j)

print(*index_max)