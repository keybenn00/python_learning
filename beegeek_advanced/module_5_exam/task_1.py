# Принимает список букв и кол-во индексов для последовательности/подсписков итогового списка
str_letters = input().split()
n = int(input())
# Создаем итоговый список и счетчик, который помогает определять индексы для каждого элемента списка букв
result_list = []
counter = 0

# Берем один индекс из диапозона индексов
for i in range(n):
    temp = []
    # Последовательно перебираем все элементы списка букв
    for el in range(len(str_letters)):
        # Если индекс элемента равен взятому i-индексу, то мы добавляем этот элемент в временный список
        if counter == i and counter == n - 1:
            temp.append(str_letters[el])
            counter = 0
        elif counter == i:
            temp.append(str_letters[el])
            counter += 1
        elif counter == n - 1:
            counter = 0
        else:
            counter += 1
    # Как только мы прошлись по всем элементам списка букв мы добавляем временный список в итоговый, 
    # а после берем новый i-индекс для которого делаем то же самое
    result_list.append(temp)
    counter = 0

print(result_list)