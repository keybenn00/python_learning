# тут нет list1 т.к в задаче программа сама подает на вход list1
maximum_number = 0

for li in list1:
    for el in li:
        if el > maximum_number:
            maximum_number = el

print(maximum_number)