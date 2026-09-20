from copy import deepcopy

n = int(input())
matrix = [[int(i) for i in input().split()] for _ in range(n)]
m = int(input())

result_matrix = deepcopy(matrix)
num = 0

for _ in range(m - 1):
    new_matrix = []
    for i in range(n):
        temp = []
        for j in range(n):
            for k in range(n):
                num += result_matrix[i][k] * matrix[k][j]
            temp.append(num)             
            num = 0            
        new_matrix.append(temp)                                  
    result_matrix = deepcopy(new_matrix)

for row in result_matrix:
    print(*row)