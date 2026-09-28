coords = list(input())
# Определяем положение ферзя по входным данным
i_ferz = 8 - int(coords[1]) # Формула применяется т.к. в шахматах идет отсчет от 8 а у нас от 0 (т.е. если i_ferz = 5, то чтобы найти i для матрицы надо 8 - 5 = 3)
j_ferz = ord(coords[0]) - 97 # Нам дается j_ferz в виде латиницы от a..h, чтобы перевести букву в число от 0..7 используем эту формулу

chessboard = [['.'] * 8 for _ in range(8)]

# Записываем в клетку, на положении ферзя, 'Q'
chessboard[i_ferz][j_ferz] = 'Q'

# Перебираем все клетки
for i in range(8):
    for j in range(8):
        # Находим вертикальные и горизонтальные ходы ферзя и меняем их на '*'
        if j == j_ferz and i != i_ferz or i == i_ferz and j != j_ferz:
            chessboard[i][j] = '*'
        # Находим  ходы ферзя на побочной диагонали и меняем их на '*',
        # условие неравенства нужно чтобы не заменить самого ферзя на '*'
        elif i + j == i_ferz + j_ferz and chessboard[i][j] != 'Q':
            chessboard[i][j] = '*'
        # Находим  ходы ферзя на главной диагонали и меняем их на '*'
        elif (i_ferz - i == j_ferz - j or i - i_ferz == j - j_ferz) and chessboard[i][j] != 'Q':
            chessboard[i][j] = '*'

for row in chessboard:
    print(*row)