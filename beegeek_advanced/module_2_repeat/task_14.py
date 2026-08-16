count_input = int(input())
list_mult = []
flag = False

for _ in range(count_input):
    num = int(input())
    list_mult.append(num)

condition_number = int(input())

for i in range(len(list_mult)):
    for j in range(i + 1, len(list_mult)):
        if list_mult[i] * list_mult[j] == condition_number:
            flag = True

if flag:
    print('ДА')
else:
    print('НЕТ')
