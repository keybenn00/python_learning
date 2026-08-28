n = int(input())
matrix = []

# Создаем матрицу(подсписки списков) из введеных значений
for _ in range(n):
    temp = [int(num) for num in input().split()]
    matrix.append(temp)

counter = 0

# Если элемент матрицы на главной диагонали(элемент на главной диагонали если el[i][i]), то мы увеличиваем счетчик на этот элемент
for r in range(n):
    for c in range(n):
        if r == c:
            counter += matrix[r][c]

print(counter)