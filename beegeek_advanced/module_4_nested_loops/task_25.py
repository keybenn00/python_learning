n = int(input())
matrix = []
numbers = [num for num in range(1, n ** 2 + 1)]

for _ in range(n):
    matrix.append([int(i) for i in input().split()])

def is_numbers_correct(matrix):
    # Проверка на уникальность чисел и на 1 < число < n ** 2
    for i in range(n):
        for j in range(n):
            if matrix[i][j] in numbers:
                numbers.remove(matrix[i][j])

    if len(numbers) != 0:
        return False
    else:
        return True

def is_sum_correct(matrix):
    # Находим сумму первой строки, с ней сравниваем все остальные
    target = sum(matrix[0])

    # Проверка сумм строк
    for row in matrix:
        if sum(row) != target:
            return False

    # Проверка сумм столбцов
    for j in range(n):
        col_sum = 0
        for i in range(n):
            col_sum += matrix[i][j]
        if col_sum != target:
            return False

    # Проверка главной диагонали
    main_diag = sum(matrix[i][i] for i in range(n))
    if main_diag != target:
        return False

    # Проверка побочной диагонали
    side_diag = sum(matrix[i][n - 1 - i] for i in range(n))
    if side_diag != target:
        return False

    return True

if is_numbers_correct(matrix) and is_sum_correct(matrix):
    print('YES')
else:
    print('NO')