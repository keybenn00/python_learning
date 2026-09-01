rows, cols = int(input()), int(input())

#Заполняем матрицу нулями
mult = [[0] * cols for _ in range(rows)]

# Делаем из нулей таблицу умножения
for r in range(rows):
    for c in range(cols):
        mult[r][c] = r * c
        print(str(mult[r][c]).ljust(3), end = ' ')
    print()