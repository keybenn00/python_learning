# Кол-во строк и столбцов на ввод
rows, cols = int(input()), int(input())
matrix = []
# Временный список для проверки условия на нужную длину
temp = []

for i in range(rows*cols):
    temp.append(input())
    if len(temp) == cols:
        matrix.append(temp)
        temp = []

for r in range(rows):
    for c in range(cols):
        print(matrix[r][c], end = ' ')
    print()

