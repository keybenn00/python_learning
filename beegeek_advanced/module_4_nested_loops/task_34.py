n, m = [int(i) for i in input().split()]
matrix = [[0] * m for _ in range(n)]

# Исходные границы которые поменяются во время цикла
top, bottom = 0, n - 1
left, right = 0, m - 1

# Исходные координаты которые поменяются во время цикла
i, j = 0, 0
current_direction = 'right'

# Цикл идущий по сторонам, обрезающий уже заполненые стороны
for num in range(1, (n * m) + 1):
    matrix[i][j] = num

    if current_direction == 'right':
        if j + 1 <= right:
            j += 1
        else:
            current_direction = 'down'
            top += 1
            i += 1
    elif current_direction == 'down':
        if i + 1 <= bottom:
            i += 1
        else:
            current_direction = 'left'
            right -= 1
            j -= 1
    elif current_direction == 'left':
        if j - 1 >= left:
            j -= 1
        else:
            current_direction = 'up'
            bottom -= 1
            i -= 1
    elif current_direction == 'up':
        if i - 1 >= top:
            i -= 1
        else:
            current_direction = 'right'
            left += 1
            j += 1

# Вывод
for i in range(n):
    for j in range(m):
        print(str(matrix[i][j]).ljust(3), end = ' ')
    print()