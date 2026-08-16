str_num = input().split()
list_of_unique = []

for el in str_num:
    if el not in list_of_unique:
        list_of_unique.append(el)

print(len(list_of_unique))