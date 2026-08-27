seq_letters = [el for el in input().split()]
result_list = []
list_repeat = []

for i in range(len(seq_letters) - 1):
    if seq_letters[i] == seq_letters[i + 1]:
        list_repeat.append(seq_letters[i])
    else:
        if not list_repeat:
            result_list.append([seq_letters[i]])
        else:
            list_repeat.append(seq_letters[i])
            result_list.append(list_repeat)
            list_repeat = []

if list_repeat:
    list_repeat.append(seq_letters[-1])
    result_list.append(list_repeat)
else:
    result_list.append([seq_letters[-1]])

print(result_list)