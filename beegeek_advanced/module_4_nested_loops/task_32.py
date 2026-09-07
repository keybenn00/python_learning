n_m = [int(i) for i in input().split()]
matrix = [['.'] * n_m[1] for _ in range(n_m[0])]

for i in range(n_m[0]):
    for j in range(n_m[1]):
        matrix[i][j] = (i + j) % n_m[1] + 1
        print(str(matrix[i][j]).ljust(3), end = ' ')
    print()