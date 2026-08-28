n = int(input())
matrix = []

for _ in range(n):
    temp = [int(i) for i in input().split()]
    matrix.append(temp)

# Берем за максимум первый элемент матрицы
maximum = matrix[0][0]

# Проходимся по всем элементам матрицы на условие, если истина и элемент больше максимума, то записываем его как максимум
for i in range(n):
    for j in range(n):
        if (i >= j) and matrix[i][j] > maximum:
            maximum = matrix[i][j]

print(maximum)
