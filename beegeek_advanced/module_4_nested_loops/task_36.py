# Считываем строки и столбцы матрицы А
n, m = [int(i) for i in input().split()]
matrix_A = [[int(i) for i in input().split()] for _ in range(n)]
# Считываем пустой символ между двумя матрицами
input()
# Считываем строки и столбцы матрицы B
m, k = [int(i) for i in input().split()]
matrix_B = [[int(i) for i in input().split()] for _ in range(m)]

# Создаем итоговую матрицу в которую через цикл добавляем по строке
result_matrix = []
num = 0

# Перемножаем элементы строки матрицы A с элементами столбцов матрицы B, результат добавляем в матрицу temp.
# Как только переходим на следующую строку матрицы A, temp добавляем строкой в итоговую матрицу
for i in range(n):
    temp = []
    for h in range(k):
        for j in range(m):
            num += matrix_A[i][j] * matrix_B[j][h]
        temp.append(num)
        num = 0
    result_matrix.append(temp)

# Вывод итоговой матрицы построчно
for row in result_matrix:
    print(*row)