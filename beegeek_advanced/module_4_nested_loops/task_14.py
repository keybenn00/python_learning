n = int(input())
matrix = []

# Создаем матрицу(подсписки списков) из введеных значений
for _ in range(n):
    temp = [int(i) for i in input().split()]
    matrix.append(temp)

counter = 0

# В каждом подсписке матрицы проверяем каждое число на условие, если условие положительно увеличиваем счетчик, в конце проверки подсписка выводим счетчик и обнуляем его
for sublist in matrix:
    for num in sublist:
        if num > (sum(sublist) / len(sublist)):
            counter += 1
    print(counter, end = '\n')
    counter = 0