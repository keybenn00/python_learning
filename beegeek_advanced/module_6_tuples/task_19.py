n = int(input())
class_list = []

for _ in range(n):
    str = input()
    class_list.append(str)

result_list = []

for i in range(len(class_list)):
    if int(class_list[i][-1]) >= 4:
        result_list.append(class_list[i])

for el in class_list:
    print(el, end = '\n')

print()

for el in result_list:
    print(el, end = '\n')