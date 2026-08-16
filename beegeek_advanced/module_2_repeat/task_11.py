str_num = input().split()
str_num = [int(el) for el in str_num]

for i in range(len(str_num)):
    if i % 2 == 0:
        value = str_num.pop(i)
        str_num.insert(i + 1, value)

print(*str_num)