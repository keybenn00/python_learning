rows_cols = [int(i) for i in input().split()]
matrix = [['.'] * rows_cols[1] for _ in range(rows_cols[0])]

for i in range(rows_cols[0]):
    for j in range(rows_cols[1]):
        if j == 0:
            matrix[i][j] = i + 1
        else:
            matrix[i][j] = matrix[i][j - 1] + rows_cols[0]
        print(str(matrix[i][j]).ljust(3), end = ' ')
    print()