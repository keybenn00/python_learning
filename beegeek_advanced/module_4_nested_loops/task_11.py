seq_letters = [el for el in input().split()]
result = [[]]

for i in range(len(seq_letters)):
    for j in range(i, len(seq_letters)):
        result.append(seq_letters[i:j+1])

print(result)