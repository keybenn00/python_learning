str_num = input().split()
last_num = str_num.pop(-1)
str_num.insert(0, last_num)

print(*str_num)